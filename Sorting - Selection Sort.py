# Selection Sort
# Time Complexity: O(n^2)
# Space Complexity: O(1)
class Solution:
    def selectionSort(self, arr):
        for i in range(len(arr)):
            self.min = i
            for j in range(i + 1, len(arr)):
                # Select the smallest value
                if arr[j] < arr[self.min]:
                    self.min = j
            # Place it at the front of the
            # sorted end of the array
            self.swap(arr, self.min, i)

        return arr

    def swap(self, arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp


arr = [5, 2, 4, 6, 1, 3, 7]
if __name__ == "__main__":
    obj = Solution()
    print(obj.selectionSort(arr))


