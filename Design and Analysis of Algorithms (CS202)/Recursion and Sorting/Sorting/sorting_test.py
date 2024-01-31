import sorting
import time

import random

list1 = [random.randint(0, 100) for _ in range(100)]
list2 = [random.randint(0, 10000) for _ in range(10000)]
list3 = [random.randint(0, 1000000) for _ in range(1000000)]

start_time = time.time()
answer_sorting.insertion_sort(list1.copy())
print("--- %s seconds spent by insertion sort on list1 ---" % (time.time() - start_time))
start_time = time.time()
answer_sorting.merge_sort(list1.copy())
print("--- %s seconds spent by merge sort for list1 ---" % (time.time() - start_time))

start_time = time.time()
answer_sorting.insertion_sort(list2.copy())
print("--- %s seconds spent by insertion sort on list2 ---" % (time.time() - start_time))
start_time = time.time()
answer_sorting.merge_sort(list2.copy())
print("--- %s seconds spent by merge sort for list2 ---" % (time.time() - start_time))

start_time = time.time()
answer_sorting.insertion_sort(list3.copy())
print("--- %s seconds spent by insertion sort on list3 ---" % (time.time() - start_time))
start_time = time.time()
answer_sorting.merge_sort(list3.copy())
print("--- %s seconds spent by merge sort for list3 ---" % (time.time() - start_time))
