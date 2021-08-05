import time

seconds = 5
count=0
while True:
    time.sleep(time.time() % seconds)
    count=count+1
    print(count)

    if count > 4 :
        break
    




