from heapq_max import *
from typing import List


def second_highest_element(given_list: List[int]):
    heap_max = []
    for element in given_list:
        heappush_max(heap_max, element)
    return heap_max[1]


print(second_highest_element([1,3, 6, 8, 9, 2, 5]))
