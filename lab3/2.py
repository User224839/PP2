def has_33(nums):
    return any(nums[i] == nums[i+1] == 3 for i in range(len(nums)-1))

def spy_game(nums):
    code = [0, 0, 7]
    for num in nums:
        if num == code[0]:
            code.pop(0)
        if not code:
            return True
    return False

def sphere_volume(radius):
    return (4/3) * 3.141592653589793 * (radius ** 3)