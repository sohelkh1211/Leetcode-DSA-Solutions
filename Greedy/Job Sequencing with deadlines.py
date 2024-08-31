def jobScheduling(jobs, profits, deadlines):
  # Put every inputs in single array
  inputs = [(job, profit, deadline) for job,profit,deadline in zip(jobs, profits, deadlines)]
  # Sort inputs array based on profit
  inputs.sort(key=lambda x:x[1], reverse = True)
  # print(inputs)
  
  max_deadline = max(deadlines)
  # Slots to assign jobs
  slots = {(x, x+1):'' for x in range(max_deadline)}
  max_profit = 0 
  
  for job, profit, deadline in inputs:
    # Assign a job to a slot in descending order. E.g: If deadline is 3 then first check if slot (2,3) is vacant or not. If it is then {(2,3): 'J1'} otherwise check for previous slot i.e (1,2) till (1,0)
    for d in range(deadline, 0, -1):
      if slots[(d-1, d)] == '':
        slots[(d-1, d)] = job
        max_profit += profit
        break
  return slots, max_profit
  
jobs = ['J1', 'J2', 'J3', 'J4', 'J5']
profits = [100, 19, 27, 25, 15]
deadlines = [2, 1, 2, 1, 3]
slots, max_profit = jobScheduling(jobs, profits, deadlines)
print("Job sequence: ", end = " ")
for job in slots.values():
  print(job, end = " ")
print("\nMax profit: ", max_profit)