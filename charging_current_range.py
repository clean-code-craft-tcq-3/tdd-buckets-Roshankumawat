newArray=[]
def isConsecutive(number1, number2):
    difference = number2 - number1
    return (difference == 0 or difference == 1)
def getRangeDetails(inputArray):
    newArray=[]
    inputArray.sort()
    reading=1
    range_first_number=inputArray[0]
    range_end_number= inputArray[0]

    for index in range(0, len(inputArray)-1):
        if(isConsecutive(inputArray[index],inputArray[index+1])):
            reading+=1
            range_end_number=inputArray[index+1]
                    
        else:
            newRangeArray=(range_first_number, range_end_number, reading)
            newArray.append(newRangeArray)
            reading=1
            range_first_number=inputArray[index+1]
            range_end_number=inputArray[index+1]

    newRangeArray=(range_first_number, range_end_number, reading)
    newArray.append(newRangeArray)
    return newArray



