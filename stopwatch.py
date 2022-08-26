# This is what the program does:
# Find the current time by calling time.time() and store it as a timestamp at the start of the program, as well as at the start of each lap.
# Keep a lap counter and increment it every time the user presses ENTER.
# Calculate the elapsed time by subtracting timestamps.
# Handle the KeyboardInterrupt exception so the user can press CTRL-C to quit.

import time
print('Press ENTER to begin. Afterward, press ENTER to "click" the stopwatch. Press Ctrl-C to quit.')

input()
print('Stopwatch has started')

start_time=time.time()
last_time=start_time

lapNo=1

try:
    while True:
        input()
        lap_time=round(time.time()-last_time,2)
        totalTime=round(time.time() - start_time,2)
        print('LAp #%s: %s (%s)' %(lapNo,totalTime,lap_time),end='')
        lapNo+=1
        last_time=time.time()

except KeyboardInterrupt:
    print('stopwatch stopped\n Done')
