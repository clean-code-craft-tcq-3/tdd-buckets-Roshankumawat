newArray=[]
def checkDifference(number1, number2):
   difference = number2 - number1
   return (difference == 0 or difference == 1)

def getRangeDetails(inputArray):
    itr= 0
    newArray=[]
    inputArray.sort()
    reading=1
    range_first_number=inputArray[0]
    range_end_number= inputArray[0]
    

    
    for index in range(0, len(inputArray)-1):
        if(isConsecutive(inputArray[index],inputArray[index+1])):#and index<len(inputArray)-1
            reading+=1
            range_end_number=inputArray[index+1]
           
        else:
           newArray.append(range_first_number)
           newArray.append(range_end_number)
           reading=1
           range_first_number=inputArray[index+1]
           range_end_number=inputArray[index+1]

        newRangeArray=(range_first_number, range_end_number, reading)
        newArray.append(newRangeArray)
       
    return reading 
