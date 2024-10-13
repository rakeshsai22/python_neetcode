from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        seen = set()
        for str in strs:
            if str not in seen:
                sub_list = [s for s in strs if sorted(s) == sorted(str)]
                result.append(sub_list)
                seen.update(sub_list)
        return result

sol_instance = Solution()
print(sol_instance.groupAnagrams(["eat", "bat", "tea", "tan", "nat"]))