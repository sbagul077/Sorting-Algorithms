# Quick Sort
# Time Complexity: Average O(nlogn). worst O(n^2)
# Space Complexity: O(logn)
class Solution:
    def partition(self, array, begin, end):
        pivot_idx = begin

        for i in range(begin + 1, end + 1):
            if array[i] <= array[begin]:
                pivot_idx += 1
                array[i], array[pivot_idx] = array[pivot_idx], array[i]
        array[pivot_idx], array[begin] = array[begin], array[pivot_idx]
        return pivot_idx

    def quick_sort_recursion(self, array, begin, end):
        if begin >= end:
            return

        pivot_idx = self.partition(array, begin, end)
        self.quick_sort_recursion(array, begin, pivot_idx - 1)
        self.quick_sort_recursion(array, pivot_idx + 1, end)

    def quick_sort(self, array, begin=0, end=None):
        if end is None:
            end = len(array) - 1

        self.quick_sort_recursion(array, begin, end)
        return array


arr = [5, 2, 4, 6, 1, 3, 7]
if __name__ == "__main__":
    obj = Solution()
    print("Before Sorting :- {}".format(arr))
    print(" After Sorting :- {}".format(obj.quick_sort(arr, 0, None)))
