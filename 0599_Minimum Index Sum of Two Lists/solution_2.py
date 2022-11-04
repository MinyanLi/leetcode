class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        
        dic1 = {}
        idxSum = []
        
        
        for i in range(len(list1)):
            dic1[list1[i]] = i      # dic1 = {item in list1 : index}
        
        
        for i in range(len(list2)):
            target = list2[i]       # target = items in list2
            if target in dic1:      # if items in list2 exsists in dic1 which already contains all the items in list1
                idxSum.append([target, i+dic1[target]])    # idxSum =[[common item1, index sum1],[common item2, index sum2]...]
        
        idxSum.sort(key=itemgetter(1))  #idxSum sort by index sum
        result = [idxSum[0][0]]      # result = item with min index sum
        
        for i in range(1, len(idxSum)):
            if idxSum[i][1] == idxSum[0][1]:  # for items in idxSum, if index sum = min index sum
                result.append(idxSum[i][0])
            else:
                break
        return result
