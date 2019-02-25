"""
    Implement a job scheduler which takes in a function f and an integer n,
    and calls f after n milliseconds.
"""
import time
import threading

def task():
    print("Doing a task")

def helper(f, n):
    time.sleep(n/1000)
    f()

def scheduler(f, n):
    t = threading.Thread(target=helper, args=(f,n,))
    t.start()

print("start")
for i in range(10):
    scheduler(task, 1000*i)
print("end")
