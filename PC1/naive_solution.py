import random

# JSSP

def get_delay(gantt):
    # naive technique
    delay = 0
    completion_day = 0
    for duration, due_date in gantt:
        completion_day += duration
        delay_n = completion_day - due_date
        delay += 0 if delay_n <= 0 else delay_n
        print(f"Delay_N: {delay_n}, Delay_T: {delay}")
    print(delay)



durations = [6,4,5]
due_dates = [8,4,12]

# Naive method:
#   - Do the tasks due date wise. 
#   - In some cases this method minimizes the total delay.


gantt = sorted(list(zip(durations, due_dates)), key=lambda x: x[1])

get_delay(gantt)





