from algorithms.heap import HeapSort
from algorithms.radix import RadixSort
from timeit import default_timer as timer
from timeit import time
import random

''' 
The ideal sorting algorithm would have the following properties:

Stable: Equal keys aren’t reordered.
Operates in place, requiring O(1) extra space.
Worst-case O(n·lg(n)) key comparisons.
Worst-case O(n) swaps.
Adaptive: Speeds up to O(n) when data is nearly sorted or when there are few unique keys.

There is no algorithm that has all of these properties, and so the choice of 
sorting algorithm depends on the application.
'''

times = {'first': [], 'second': []}
sizes = [10, 100, 1000]
samples = 2

for size in sizes:
    tot = 0.0
    for _ in range(samples):
        lst = RadixSort(size)
        t0 = timer()
        lst.sort()
        t1 = timer()
        tot += (t1-t0)
    times['first'].append(float(tot/samples))

    tot = 0.0
    for _ in range(samples):
        lst = HeapSort(size)
        t0 = timer()
        lst.sort()
        t1 = timer()
        tot += (t1-t0)
    times['second'].append(float(tot/samples))
    
print("\n\tn\tALGORITHM 1.\tALGORITHM 2.")
print("\t___","_"*30)

for row,size in enumerate(sizes):
    print("\t%d \t%f \t%0f "%(size, times['first'][row], times['second'][row]))
