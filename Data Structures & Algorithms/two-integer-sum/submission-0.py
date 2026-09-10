class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mymap = defaultdict(int)

        for i in range(len(nums)):
            num = nums[i]

            diff = target - num
            if diff in mymap:
                return [mymap[diff], i]
            else:
                mymap[num] = i
        
        return [-1, -1]