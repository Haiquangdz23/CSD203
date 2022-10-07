import random
from timeit import default_timer as timer
def bubble_sort(lst):
    """
    Bubble sort function
    :param lst: lst of unsorted integers
    """

    # Traverse through all list elements
    for i in range(len(lst)):

        # Last i elements are already in place
        for j in range(len(lst) - i - 1):

            # Traverse the list from 0 to size of lst - i - 1
            # Swap if the element found is greater than the next element
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

def heapify(nums, heap_size, root_index):
    # Assume the index of the largest element is the root index
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    # If the left child of the root is a valid index, and the element is greater
    # than the current largest element, then update the largest element
    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child

    # Do the same for the right child of the root
    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child

    # If the largest element is no longer the root element, swap them
    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]
        # Heapify the new root element to ensure it's the largest
        heapify(nums, heap_size, largest)

def heap_sort(nums):
    n = len(nums)

    # Create a Max Heap from the list
    # The 2nd argument of range means we stop at the element before -1 i.e.
    # the first element of the list.
    # The 3rd argument of range means we iterate backwards, reducing the count
    # of i by 1
    for i in range(n, -1, -1):
        heapify(nums, n, i)

    # Move the root of the max heap to the end of
    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)

def insertion_sort(lst):
    """
    Insertion sort function
    :param lst: lst of unsorted integers
    """

    # Traverse through 1 to len(lst)
    for i in range(1, len(lst)):

        key = lst[i]

        # Move elements of lst greater than key, to one position ahead
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key

def merge(left_list, right_list):
    sorted_list = []
    left_list_index = right_list_index = 0

    # We use the list lengths often, so its handy to make variables
    left_list_length, right_list_length = len(left_list), len(right_list)

    for _ in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:
            # We check which value from the start of each list is smaller
            # If the item at the beginning of the left list is smaller, add it
            # to the sorted list
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            # If the item at the beginning of the right list is smaller, add it
            # to the sorted list
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1

        # If we've reached the end of the of the left list, add the elements
        # from the right list
        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        # If we've reached the end of the of the right list, add the elements
        # from the left list
        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1

    return sorted_list

def merge_sort(nums):
    # If the list is a single element, return it
    if len(nums) <= 1:
        return nums

    # Use floor division to get midpoint, indices must be integers
    mid = len(nums) // 2

    # Sort and merge each half
    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])

    # Merge the sorted lists into a new one
    return merge(left_list, right_list)

def partition(nums, low, high):
    # We select the middle element to be the pivot. Some implementations select
    # the first element or the last element. Sometimes the median value becomes
    # the pivot, or a random one. There are many more strategies that can be
    # chosen or created.
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1

        j -= 1
        while nums[j] > pivot:
            j -= 1

        if i >= j:
            return j

        # If an element at i (on the left of the pivot) is larger than the
        # element at j (on right right of the pivot), then swap them
        nums[i], nums[j] = nums[j], nums[i]

def quick_sort(nums):
    # Create a helper function that will be called recursively
    def _quick_sort(items, low, high):
        if low < high:
            # This is the index after the pivot, where our lists are split
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums) - 1)

def selection_sort(lst):
    """
    Selection sort function
    :param lst: List of integers
    """

    # Traverse through all lst elements
    for i in range(len(lst)):
        # Find the minimum element in unsorted lst
        min_index = i
        for j in range(i + 1, len(lst)):
            if lst[min_index] > lst[j]:
                min_index = j

        # Swap the found minimum element with the first element
        lst[i], lst[min_index] = lst[min_index], lst[i]


# Driver code to test above
if __name__ == '__main__':
   # Generate an array of 10000 random float numbers and compare processing (sorting) time of above function
    k = {}
    # Bubble_sort
    lst = [random.uniform(0,100) for _ in range(10000)]
    print('Sorting...')
    start = timer()
    bubble_sort(lst)
    stop = timer()
    print('Sorting time (bubble sort):', stop - start,'\n')
    k['Bubble_s']= stop - start
    
    # Heap_sort
    nums = [random.uniform(0,100) for _ in range(10000)]
    print('Sorting...')
    start = timer()
    heap_sort(nums)
    stop = timer()
    print('Sorting time (heap sort):', stop - start,'\n')
    k['Heap_s']=stop - start
    
    # Insertion_sort
    lst = [random.uniform(0,100) for _ in range(10000)]
    print('Sorting...')
    start = timer()
    insertion_sort(lst)
    stop = timer()
    print('Sorting time (insertion sort):', stop - start,'\n')
    k['Insertion_s']=stop - start
    
    # Merge_sort
    nums = [random.uniform(0,100) for _ in range(10000)]
    print('Sorting...')
    start = timer()
    merge_sort(nums)
    stop = timer()
    print('Sorting time (merge sort):', stop - start,'\n')
    k['Merge_s']=stop - start
    
    # Quick_sort
    nums = [random.uniform(0,100) for _ in range(10000)]
    print('Sorting...')
    start = timer()
    quick_sort(nums)
    stop = timer()
    print('Sorting time (quick sort):', stop - start,'\n')
    k['Quick_s']=stop - start
    
    # Selection_sort
    lst = [random.uniform(0,100) for _ in range(10000)]
    print('Sorting...')
    start = timer()
    selection_sort(lst)
    stop = timer()
    print('Sorting time (selection sort):', stop - start,'\n')
    k['Selection_s']=stop - start
    
    
    print(sorted(k.items(), key = lambda x : x[1]))