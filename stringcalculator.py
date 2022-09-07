def test():
    #empty string
    assert(add("")==0),"Empty String doesn't return 0"
    
    #1 Number
    assert(add("1")==1),"String \"1\" doesn't return 1"
    assert(add("2")==2)
    
    #2 numbers
    assert(add("1,2")==3)
    assert(add("2,3")==5)
    
    #3 numbers
    assert(add("1,2,3")==6)
    assert(add("2,3,6")==11)
    
    #4 numbers
    assert(add("1,2,3,4")==10)
    assert(add("1,4,5,6")==16)
    
    #Handle New Lines
    assert(add("1\n2")==3)
    assert(add("3\n4")==7)
    
    #Handle Different Delimiters(1 )
    assert(add("//;\n1;2;3")==6)
    assert(add("//-\n1-2-3")==6)
    
    #Handle Different Delimiters(multiple chars)
    assert(add("//---\n1---2---3")==6)
    assert(add("//-!;o-\n1-!;o-2-!;o-3")==6)
    
    #
    
    print("PASSED ALL TESTS")
    
def add(numbersString):
    if len(numbersString)==0:
        return 0
    elif len(numbersString)==1:
        return int(numbersString)
    elif numbersString[0]=="/":
        result=0
        delim=""
        lines=numbersString.split("\n")
        for char in range(2,len(lines[0])): 
            delim=delim+lines[0][char]
        numbers=lines[1].split(delim)
        return multipleNumbers(numbers)
    
    else:
        result=0
        delim=","
        if numbersString[1] != ",":
            delim="\n"
        numbers= numbersString.split(delim)
        # for num in numbers:
        #     result += int(num)
        return multipleNumbers(numbers)
    
def multipleNumbers(numbers):
    result=0
    #numbers=numbersString.split(delim)
    for num in numbers:
        result += int(num)
    return result 
    
test()