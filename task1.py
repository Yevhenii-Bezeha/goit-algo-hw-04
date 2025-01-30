import random
import timeit

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr


def benchmark_sorting_algorithms():
    sizes = [100, 1000, 10000]
    results = []

    for size in sizes:
        data = [random.randint(0, size) for _ in range(size)]

        insertion_time = timeit.timeit(lambda: insertion_sort(data.copy()), number=1)
        merge_time = timeit.timeit(lambda: merge_sort(data.copy()), number=1)
        timsort_time = timeit.timeit(lambda: sorted(data.copy()), number=1)

        results.append((size, insertion_time, merge_time, timsort_time))

    print("Size\tInsertion Sort\tMerge Sort\tTimsort")
    for size, insertion_time, merge_time, timsort_time in results:
        print(f"{size}\t{insertion_time:.6f}\t{merge_time:.6f}\t{timsort_time:.6f}")

if __name__ == "__main__":
    benchmark_sorting_algorithms()
