# Prettified Stopwatch
# Expand the stopwatch project from this chapter so that it uses the rjust() and ljust() string methods to “prettify” the output.

# Instead of output such as this:

# Lap #1: 3.56 (3.56)
# Lap #2: 8.63 (5.07)
# Lap #3: 17.68 (9.05)
# Lap #4: 19.11 (1.43)

# . . . the output will look like this:

# Lap # 1:   3.56 (  3.56)
# Lap # 2:   8.63 (  5.07)
# Lap # 3:  17.68 (  9.05)
# Lap # 4:  19.11 (  1.43)


import time,pyperclip
print('Press ENTER to begin. Afterward, press ENTER to "click" the stopwatch. Press Ctrl-C to quit.')

input()
print('Stopwatch has started')

start_time=time.time()
last_time=start_time

lapNo=1
saved_laps=[]

try:
    while True:
        input()
        lap_time=round(time.time()-last_time,2)
        totalTime=round(time.time() - start_time,2)
        #print('LAp #%s: %s (%s)' %(lapNo,totalTime,lap_time),end='')
        
        #format
        format_lapNo= 'Lap # %s:' %lapNo
        format_time=str(totalTime).rjust(5)
        format_lap=str(lap_time).rjust(5)
        formatted=format_lapNo + format_time + ' ( ' + format_lap + ' ) '
        print(formatted)#,end=' ')
        lapNo+=1
        last_time=time.time()
        saved_laps.append(formatted)

except KeyboardInterrupt:
    print('stopwatch stopped\n Done')
    pyperclip.copy('\n'.join(saved_laps))
