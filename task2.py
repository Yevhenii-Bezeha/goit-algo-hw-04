import heapq

def merge_k_lists(arr):

    min_heap = []

    for i, lst in enumerate(arr):
        if lst:
            heapq.heappush(min_heap, (lst[0], i, 0))

    result = []

    while min_heap:
        val, list_idx, elem_idx = heapq.heappop(min_heap)
        result.append(val)

        if elem_idx + 1 < len(arr[list_idx]):
            next_val = arr[list_idx][elem_idx + 1]
            heapq.heappush(min_heap, (next_val, list_idx, elem_idx + 1))

    return result

test_list = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(test_list)
print("Sorted list", merged_list)
