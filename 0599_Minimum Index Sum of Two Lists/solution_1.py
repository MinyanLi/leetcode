# joint list1 and list2 as list3
# addup the index and put it into list index_sum
# find out the min index sum
# put item with min index sum into list list_min_index

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        
        list3 = []
        index_sum = []
        list_min_index = []

        for i in list1:
            for j in list2:
                if i == j:
                    list3.append(i) 
                    index_sum.append(list1.index(i) + list2.index(j))

        common = dict(zip(list3, index_sum))

        common = dict(sorted(common.items(), key=lambda item: item[1]))

        min_sum = list(common.values())[0]

        for i,j in common.items():
            if j == min_sum:
                list_min_index.append(i)
                
        return list_min_index
        
