class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        HashMap={}
        for i in strs:
            temp=''.join(sorted(i))
            if temp in HashMap:
                HashMap[temp].append(i)
            else:
                HashMap[temp]=[i]
        return HashMap.values()