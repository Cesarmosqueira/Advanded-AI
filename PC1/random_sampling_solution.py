import numpy as np
import random
import matplotlib.pyplot as plt
from datetime import datetime

# static data from the problem

with open('demo') as f:
    n, m = [int(x) for x in f.readline().split()]
    jobs = np.zeros((n, m, 2), dtype=int)
    i = 0
    for line in f:
        jobs[i] = np.array([int(x) for x in line.split()]).reshape(m, 2)
        i += 1

class JSSP:
    n=0
    m=0

    def load_data(self, jobs, n, m):
        self.jobs = jobs
        self.n = n
        self.m = m

    def set_reps(self, rep_):
        self.rep = rep_


    def calc_makespan(self, v=False):
        mstart = np.zeros((self.m), dtype=int)
        jend = np.zeros((self.m), dtype=int)
        idxs = np.zeros((self.n), dtype=int)
        makespan = 0
        for e in self.rep:
            i = idxs[e]
            idxs[e] += 1
            midx = self.jobs[e, i, 0]
            time = self.jobs[e, i, 1]
            if v:
                print(f"Job {e} task {i} to machine {midx} starting at {mstart[midx]} duration {time}")
            mstart[midx] = max(mstart[midx], jend[e]) + time
            jend[e] = mstart[midx]
            if mstart[midx] > makespan:
                makespan = mstart[midx]
        return makespan

    def random_sample(self):
        # gen m instances for each number between 0 and n (copilot did NOT wrote this)
        l = [x%self.n for x in range(self.n*self.m)]
        random.shuffle(l)
        return l


    def plot_graph(self, makespan):
        mstart = np.zeros((self.m), dtype=int)
        jend = np.zeros((self.m), dtype=int)
        idxs = np.zeros((self.n), dtype=int)
        schedule = np.zeros((self.m*10, makespan))

        for e in self.rep:
            i = idxs[e]
            idxs[e] += 1
            midx = self.jobs[e, i, 0]
            time = self.jobs[e, i, 1]
            mstart[midx] = max(mstart[midx], jend[e])
            schedule[midx*10:(midx+1)*10, mstart[midx]:mstart[midx] + time] = e+1
            mstart[midx] += time
            jend[e] = mstart[midx]

        plt.imshow(schedule)
        plt.show()

print("JSSP with random sampling")

model = JSSP()
model.load_data(jobs, n, m)

makespans = []
best_makespan = float('inf')
best_sample = []
best_index = 0

epochs = 100
for i in range(epochs):
    sample = model.random_sample()
    model.set_reps(sample)

    makespan = model.calc_makespan()
    if makespan <= best_makespan:
        best_makespan = makespan
        best_sample = sample.copy()
        best_index = i

    makespans += [makespan]
    

random.seed(datetime.now())

print(" == Best random sample == ")
model.set_reps(best_sample)
print(" Best makespan:", best_makespan)
plt.title("Best solution")
model.plot_graph(best_makespan)


plt.title("Random samples")

plt.annotate("Best Makespan", (best_index+1, best_makespan))
plt.scatter(best_index, best_makespan)
plt.plot(makespans, c='r', label="Random samples")

plt.xlabel("Epoch (random sample)")
plt.ylabel("Makespan")
plt.legend()
plt.show()

