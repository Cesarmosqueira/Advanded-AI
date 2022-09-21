
import sys
import random

# JSSP



VERBOSE = True if len(sys.argv) == 2 and sys.argv[1] == 'v' else False

def get_delay(gantt):
    # naive technique
    delay = 0
    completion_day = 0
    for duration, due_date in gantt:
        completion_day += duration
        delay_n = completion_day - due_date
        delay += 0 if delay_n <= 0 else delay_n

    return delay


durations = [6,4,5,2, 8]
due_dates = [8,4,12, 19, 15]

# knowledge base: https://www.geeksforgeeks.org/genetic-algorithms/
#
# initialization of the indices: Random indices
# until convergence: (fitness stops to improve)
#  - fitness: total delay (minimize)
#  - crossover: slice the indices and randomly generate the rest
#  - mutation: some of the crossover should probably muatate
#  - calculate fitness of new indices

indices_size = 15
indices = []
for i in range(indices_size):
    ind = list(range(len(durations)))
    random.shuffle(ind)
    indices += [ind]
    
gantt = list(zip(durations, due_dates))

def build_gen(gantt, indices):
    new_gantt = [[] for _ in range(len(indices))]
    for i, ind in enumerate(indices):
        new_gantt[i] = gantt[ind]
    return new_gantt

population = []
for i in indices:
    population += [build_gen(gantt, i)]

epochs = 10

# utility func
def randomize_with_size(array, size):
    res = []
    for i in range(size):
        res += [array[i % len(array)]]
    random.shuffle(res)
    return res

delays = []
best_population = []
min_delay = float('inf')
for epoch in range(epochs):
    print(f"Epoch #{epoch}: ", end="")
    avg = 0
    delays = []
    for i, p in enumerate(population):
        d_i = get_delay(p)
        
        # update best population
        if d_i < min_delay:
            min_delay = d_i
            best_population = p.copy()

        avg += d_i
        delays += [[i, d_i]]
    avg /= len(population)
    print(f"avg: {avg}")

    top_indices = sorted(delays, key=lambda x: x[1])[:5]
    top = []
    for ind in top_indices:
        top += [population[ind[0]]]
    
    crossover_point = int(len(top[0]) * 0.7)
    
    if VERBOSE:
        print("Top 5")
        for t in top:
            print(t)
        print()

        print("Crossovered")

    # crossover
    crossovered = []
    for t in  randomize_with_size(top, indices_size):
        rest = t[crossover_point:].copy()
        random.shuffle(rest)
        
        crossovered += [t[:crossover_point] + rest]

        if VERBOSE:
            print(crossovered)

    # mutation (Not today canadios)

    # update population
    population = crossovered

