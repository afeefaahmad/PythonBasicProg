#gfg 
    def findUnion(self, a, b):

        unionSet = set(a+b)
        return len(unionSet)
      
**********************************************************
#Without using set
  def findUnion(self, a, b):
        # code here
        combinedList = a+b
        distinctList = []
        for element in combinedList:
            if element not in distinctList:
                distinctList.append(element)
                
        return len(distinctList)

************************************************************
#Without TLE

