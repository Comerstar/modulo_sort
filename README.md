
# Modulo Sort

Modulo sort is a sorting algorithm based on a misunderstanding of radix sort.

To run this application, run `python3 modulo_sort.py`. The interface expects users to input the list of integers they wish to sort in the order they appear in the list. Alternatively, the defined function `modulo_sort(comp, lst)` can be called in code, where `lst` is the list of positive integers (including zero) to be sorted. The list will be sorted in ascending order. A list with negative numbers may never finish being sorted.

## Algorithm

Modulo sort performs counting sort on the list repeatedly, like radix sort. But instead of sorting it on each digit of the number, it performs counting sort on the value of the digit mod i, where i is an increasing base. It terminates once the list is completely sorted.

## Time Complexity

The time complexity of modulo sort is highly dependent on the numbers being sorted. If the two numbers have the exact same value mod some number for many numbers, then they cannot be sorted for a very long term. The upper bound is `mn`, where `m` is the largest number in the list, and `n` is the number of items.
