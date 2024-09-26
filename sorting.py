  
def bubble(unsortedList):
    
    print("START")
    
    currentPosition = 0
    holder = 0
    sorted = False
    while not sorted:
        for i in range(0, len(unsortedList) - 1, 1):
            #Iterate one Index
            if unsortedList[i] > unsortedList[i + 1]:
                #Swap the two elements
                holder = unsortedList[i]
                unsortedList[i] = unsortedList[i + 1]
                unsortedList[i + 1] = holder
                    
            #Check if Sorted
        canContinue = True
            
        print("CHECKING IF SORTED")
        print(len(unsortedList))
        for i in range(0, len(unsortedList) - 1, 1):
            if unsortedList[i] > unsortedList[i + 1]:
                canContinue = False
        if canContinue:
            sorted = True
    return unsortedList
              