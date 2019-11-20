class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Dic = {}
        for i in range(len(nums)):
            num = nums[i]
            pair = target - num
            if pair in Dic:
                return [Dic[pair],i]
            Dic[num] = i
        return None
