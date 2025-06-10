"""
Two pointers
Basic patterns
type01: Opposite direciton (Start & End):

Used when the array is sorted and you're searching for a pair or comparing symmetric values.

"""

left = 0
right = len(arr) - 1

while left < right:
    #perform check or operations
    if arr[left] + arr[right] == target:
        return [left, right]
    elif arr[left] + arr[right] < target:
        left += 1
    else:
        right -= 1



"""
Type02: Same direction (left -> right)

Used for problems like removing duplicates, moving zeroes, or maintaining a window.
"""

`
