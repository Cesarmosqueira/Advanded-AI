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
    makespan=0

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
        self.makespan = makespan
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


# TODO
def reproduce_reps(reps, size):
    return reps


print("JSSP with genetic algorithms")
random.seed(datetime.now())


size = 200 # population
population = []

for i in range(size):
    jssp = JSSP()
    jssp.load_data(jobs, n, m)
    jssp.set_reps(jssp.random_sample())
    jssp.calc_makespan()
    population += [jssp]



epochs = 100
for i in range(epochs):
    print(f"Epoch #{i}")
    population = sorted(population, key=lambda x: x.makespan)
    makespans = [p.makespan for p in population]
    top = population[5:]
    new_population = reproduce_reps([p.reps for p in top], size)
    # telemetry
    # updates

# shows 

# TODO: check RS to fill missing parts













