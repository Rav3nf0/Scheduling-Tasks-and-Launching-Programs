import time, subprocess

timeleft=3
while timeleft >0:
    print(timeleft ,end=' ')
    time.sleep(1)
    timeleft-=1

subprocess.Popen(['start','C:\\Users\\AADARSH\\Downloads\\breach-alarm.wav'],shell=True)