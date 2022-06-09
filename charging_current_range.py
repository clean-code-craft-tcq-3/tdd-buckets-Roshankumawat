
def checkDifference(number1, number2):
   return number2-number1
    
def checkRange(inputArray):
    reading=1
    inputArray.sort()
    first_number1= inputArray[0]
    for index in range(0, len(inputArray)-1):
        first_number= inputArray[index]
        next_number= inputArray[index+1]
        if (checkDifference(first_number,next_number) ==0 or checkDifference(first_number,next_number)==1):
            reading=reading+1
        else:
            return (first_number1,first_number, reading )
