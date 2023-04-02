# Bubble Sort
# Time Complexity: O(n^2)
# Space Complexity: O(1)

class Solution:
    def bubbleSort(self, arr):

        n = len(arr)
        swapped = True

        i = -1

        while swapped:
            swapped = False
            i += 1

            for j in range(1, n - i):
                if arr[j - 1] > arr[j]:
                    self.swap(arr, j - 1, j)
                    swapped = True

        return arr

    def swap(self, arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp


arr = [6, 5, 3, 1, 4, 8, 2, 7]
if __name__ == "__main__":
    obj = Solution()
    print(obj.bubbleSort(arr))
