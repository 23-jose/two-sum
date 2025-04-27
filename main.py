from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:

    temp = target
    # YOUR ANSWER
    for i in range(len(nums)):
        temp2 = temp - nums[i]
        if temp2 in nums[i+1:]: 
            j = nums.index(temp2, i+1)
            return [i, j]
        temp = target
    
    return []