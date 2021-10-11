import time
import threading

def long_task():
  for i in range(5):
    time.sleep(1)
    print("working: %s" % i)

print("Start");
threads = []
for i in range(5):
  t = threading.Thread(target=long_task) # multi threading
  threads.append(t)

for t in threads:
  t.start()
  print("thread started")

for t in threads:
  print("thread joined")
  t.join()

print("End")


