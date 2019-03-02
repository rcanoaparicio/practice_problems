"""
    The area of a circle is defined as πr^2.
    Estimate π to 3 decimal places using a Monte Carlo method.
    Hint: The basic equation of a circle is x^2 + y^2 = r^2.
"""
import random
import math
import time


def monte_carlo_method():
    total_times = 0
    times_inside = 0
    pi_value = 0
    while str(pi_value)[:5] != "3.141":
        if math.sqrt(math.pow(random.uniform(0, 1), 2) + math.pow(random.uniform(0, 1),2)) <= 1:
            times_inside += 1
        total_times += 1
        pi_value = 4*times_inside/total_times
    return pi_value

def monte_carlo_method_v2():
    total_times = 0
    times_inside = 0
    pi_value = 0
    i = 0
    j = 0
    while i < 1:
        while j < 1:
            if math.sqrt(i*i + j*j) <= 1:
                times_inside += 1
            total_times += 1
            pi_value = 4*times_inside/total_times
            j += 0.01
        i += 0.01
    print(pi_value)
    while str(pi_value)[:5] != "3.141":
        if math.sqrt(math.pow(random.uniform(0, 1), 2) + math.pow(random.uniform(0, 1),2)) <= 1:
            times_inside += 1
        total_times += 1
        pi_value = 4*times_inside/total_times
    return pi_value


for j in range(100):
    monte_carlo_method_v2()
print("herro")
total_time = 0
for i in range(1, 5):
    start = time.time()
    for j in range(100):
        monte_carlo_method()
    total_time += (time.time()-start)
    print(time.time()-start)
    print("curr total",total_time/(i*100))
print("TOTAL TIME v1:", total_time/500)

total_time = 0
for i in range(1, 5):
    start = time.time()
    for j in range(100):
        monte_carlo_method_v2()
    total_time += (time.time()-start)
    print(time.time()-start)
    print("curr total",total_time/(i*100))
print("TOTAL TIME v2:", total_time/500)
