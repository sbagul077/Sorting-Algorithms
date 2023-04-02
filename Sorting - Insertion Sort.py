# Insertion Sort
# Time Complexity: O(n^2).
# Space Complexity: O(1)
class Solution:
    def insertion_Sort(self, nums):
        n = len(nums)
        for i in range(n):
            cursor = nums[i]  # puttiing storing current element in a variable
            pos = i  # curr position of the cursor

            # we'll keep comparing the current element until pos is 0 and previous element is smaller than the current one
            while pos > 0 and nums[pos - 1] > cursor:
                nums[pos] = nums[pos - 1]
                pos -= 1
            # Final swap
            nums[pos] = cursor

        return nums


nums = [2, 8, 1, 3, 6, 7, 5, 4]

if __name__ == "__main__":
    obj = Solution()
    print("Before Sorting: {}".format(nums))
    print("After Sorting:  {}".format(obj.insertion_Sort(nums)))
