# Merge Sort
# Time Complexity: O(n^2).
# Space Complexity: O(1)
class Solution:
    def merge_Sort(self, nums):
        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2
        left = self.merge_Sort(nums[: mid])
        # print(left, "Left", nums)
        right = self.merge_Sort(nums[mid:])
        # print(right, "Right", nums)

        return self.merge(left, right, nums.copy())

    def merge(self, left, right, merged):
        left_cursor = 0
        right_cursor = 0
        # print(left, right, merged)
        # print(merged)
        while left_cursor < len(left) and right_cursor < len(right):
            # sort each one and place it in the result
            if left[left_cursor] <= right[right_cursor]:
                merged[left_cursor + right_cursor] = left[left_cursor]
                left_cursor += 1
            else:
                merged[left_cursor + right_cursor] = right[right_cursor]
                right_cursor += 1
        # print(merged, "before")
        for left_cursor in range(left_cursor, len(left)):
            merged[left_cursor + right_cursor] = left[left_cursor]
        # print(merged, "after")
        for right_cursor in range(right_cursor, len(right)):
            # print(right[right_cursor])
            merged[left_cursor + right_cursor] = right[right_cursor]
        # print(merged)
        return merged


# nums = [2, 8, 1, 3, 6, 7, 5, 4]
nums = [6, 5, 3, 1, 8, 7, 2, 4]
if __name__ == "__main__":
    obj = Solution()
    print("Before Sorting: {}".format(nums))
    print("After Sorting:  {}".format(obj.merge_Sort(nums)))
