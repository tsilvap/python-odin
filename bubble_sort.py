def bubble_sort(nums):
    """Sort a list of numbers using Bubble Sort."""
    sorted_nums = nums.copy()

    len_nums = len(nums)
    for i in range(0, len_nums):
        for j in range(0, len_nums - i - 1):
            if sorted_nums[j] > sorted_nums[j + 1]:
                temp = sorted_nums[j + 1]
                sorted_nums[j + 1] = sorted_nums[j]
                sorted_nums[j] = temp

    return sorted_nums


def bubble_sort_by(elems, comp):
    """Sort list of elements using Bubble Sort and custom comparison.

    :param elems: List of elements to be sorted
    :param comp: Function to be used to compare elements
    :return sorted_elems: List of elements, sorted using the custom
    comparison function
    """
    sorted_elems = elems.copy()

    len_elems = len(elems)
    for i in range(0, len_elems):
        for j in range(0, len_elems - i - 1):
            if comp(sorted_elems[j], sorted_elems[j + 1]):
                temp = sorted_elems[j + 1]
                sorted_elems[j + 1] = sorted_elems[j]
                sorted_elems[j] = temp

    return sorted_elems
