class Solution:
  def minCostII(self, costs: list[list[int]]) -> int:
    prevIndex = -1  
    prevMin1 = 0  
    prevMin2 = 0  

    for cost in costs: 
      index = -1
      min1 = math.inf
      min2 = math.inf
      for i, cst in enumerate(cost):   
        theCost = cst + (prevMin2 if i == prevIndex else prevMin1)
        if theCost < min1:
          index = i
          min2 = min1
          min1 = theCost
        elif theCost < min2:  
          min2 = theCost

      prevIndex = index
      prevMin1 = min1
      prevMin2 = min2

    return prevMin1