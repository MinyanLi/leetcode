
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        s = {}
        ans = []
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    s[list1[i]] = i + j   # s append {common item: index sum}
        for i in s:
            if s[i] == s[min(s, key=s.get)]:  # s.get() is getting value from dict /  dict.get(key, default = None)
                ans.append(i)

        return ans
      
'''
>>> d = {320: 1, 321: 0, 322: 3}
>>> min(d, key=d.get)
321
'''
