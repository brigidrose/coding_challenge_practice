#ADD TO ZERO (easier)

nums = [1, 2, 4, -2]
n = 5

def add_to_zero(nums, n):
    """Given list of ints, return True if any two nums sum to 0."""
    i = 0
    j = 0
    sums = []

    while i < len(nums):
        j = i + 1
        while j < len(nums):
            if nums[i] + nums[j] == n:
                sums.append(nums[i], nums[j])
                print sums
        j += 1
    i += 1

 
    return sums