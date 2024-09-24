class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #sort the strings
        strMap={}
        finalList=[]
        unpairedWords=[]
        for x in strs:
            sortedStr=''.join(sorted(x))
            if sortedStr in strMap:
               
                strMap[sortedStr].append(x)
                print('im in')
                print(strMap[sortedStr])
            else:
                strMap[sortedStr]=[x]
                print('not in')
                print(strMap[sortedStr])
       
        finalList=list(strMap.values())
        return finalList