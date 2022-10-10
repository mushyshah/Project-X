

list1 = [11,3,22,52,1,24,0]
# list2 = [5,22,12,85,312,7,9]
sumValue = 22

# Challenge
# Return the values and indicies of the array elements 
# that sum up to the sumValue
for countX,x in enumerate(list1):
    # print(f"{index},{x}")
    for countY,y in enumerate(list1):
        result = x + y
        if (result == sumValue) and countX != countY :
            print(f"{countX},{x}  -  {countY},{y} - {result}") 
            print(str(countX)+","+str(x)+" - "+str(countY)+","+str(y)+" - "+str(result))
            print("%s,%s - %s,%s - %s" % (countX, x, countY, y, result))