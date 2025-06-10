"""
Two pointers
Basic patterns
type 01: Opposite direciton (Start & End):

Used when the array is sorted and you're searching for a pair or comparing symmetric values.

"""

# left = 0
# right = len(arr) - 1

# while left < right:
#     #perform check or operations
#     if arr[left] + arr[right] == target:
#         return [left, right]
#     elif arr[left] + arr[right] < target:
#         left += 1
#     else:
#         right -= 1



"""
Type 02: Same direction (left -> right)

Used for problems like removing duplicates, moving zeroes, or maintaining a window.
"""

# slow = 0

# for fast in range(len(arr)):
#     if is_valid(arr[fast]): #is_valid() is a filtering condition and a placeholder, it could be arr[fast] != 0 or arr[fast] != target
#         arr[slow] = arr[fast]
#         slow += 1


"""
Example Question 01: Two Sum 2: Input array is sorted
"""


def twoSum(numbers, target):
    left, right = 0, len(numbers) - 1

    while left < right:
        curr_sum = numbers[left] + numbers[right]
        if curr_sum == target:
            return [left + 1, right + 1] # array is defined to start from 1 (1-indexed)
        elif curr_sum < target:
            left += 1
        else:
            right -= 1


"""
Example Question 02: 3Sum
"""

def threeSum(nums):
    nums.sort()
    res = []
    n = len(nums)

    for i in range(n - 2):
        #skip duplicate 'i'
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        target = -nums[i]
        left, right = i + 1, n - 1

        while left < right:
            curr_sum = nums[left] + nums[right]
            if curr_sum == target:
                res.append([nums[i], nums[left], nums[right]])

                #skip duplicate left/right
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1

            elif curr_sum < target:
                left += 1
            else:
                right -= 1

    return res







if __name__ == "__main__":
    numbers = [1, 2, 4, 6, 8]
    target = 8
    print(twoSum(numbers, target))

    print(threeSum([0, 3, 6, 7, -3, 1, 4, -2, 2]))