def isMonotonic(ar):
  isNonDecreasing = True
  isNonIncreasing = True
  for i in range(1,len(ar)):
    if ar[i]<ar[i-1] :
      isNonDecreasing = False
    if ar[i]>ar[i-1]:
      isNonIncreasing = False
      
  return isNonDecreasing or isNonIncreasing
