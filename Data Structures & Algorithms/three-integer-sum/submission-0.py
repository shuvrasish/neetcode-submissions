class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        target = 0
        s = set()

        res = []
        for i in range(n - 2):
            hs = defaultdict(int)
            for j in range(i + 1, n):
                diff = target - (nums[i] + nums[j])
                if diff in hs:
                    s.add(
                        tuple(sorted([nums[i], nums[hs[diff]], nums[j]]))
                    )
                else:
                    hs[nums[j]] = j
        

        for tup in s:
            res.append([tup[0], tup[1], tup[2]])
        return res
