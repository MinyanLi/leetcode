class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
      
        l1 = 0
        l2 = 0
        res = {}

        for i in list1:
            if i in list2:    # common item in list1 and list2
                l2 = list2.index(i)     # l2 = index of item in list2
                if l2 + l1 in res.values():  # if index sum already exists in res = {}
                    res[i] = l1 + l2      # res append {common item i : index sum}
                else:
                    if not len(res):   # if res is empty
                        res[i] = l1 + l2  # res append {common item i : index sum}
                    else:
                        for value , index in res.items():
                            if index > l2+l1:    # if original index sum in res > new index sum
                                res.clear()      # clear res
                                res[i] = l1 + l2 # and add the new common item and new index sum
                                break
                            else:
                                continue
            else:
                pass
            l1 += 1    # next round is the next item in list1
        return list(res.keys())
        
                
                
