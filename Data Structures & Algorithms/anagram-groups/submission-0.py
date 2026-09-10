class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res: list[list[str]] = []
        groups = defaultdict(list)

        for st in strs:
            ss = "".join(sorted(st))
            groups[ss].append(st)

        for group in groups.values():
            res.append(group)

        return res