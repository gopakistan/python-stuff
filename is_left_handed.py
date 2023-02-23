def is_left_handed(pips):
    
    def swap(items1, x, items2, y):
        if items1 == items2:
            returnTwo = False
        else:
            returnTwo = True
        temp = items1[x]
        items1[x] = items2[y]
        items2[y] = temp
        if returnTwo:
            return items1, items2
        else: 
            return items1

    def rotate(top, bottom, first, second):
        #2 3 -> 4 2
        #4 5 -> 5 3

        #1 2 -> 4 1
        #4 3 -> 3 2

        #top[1]     top[2]
        #bottom[1]  bottom[2]
        temp = top[first]
        top[first] = bottom[first]
        bottom[first] = bottom[second]
        bottom[second] = top[second]
        top[second] = temp
        return top, bottom

    def getBottom(items):
        items2 = []
        for x in items:
            items2.append(7-x)
        swap(items2, 1, items2, 2)
        return items2

    def flip(top, bottom):
        temp = top
        top = bottom
        bottom = temp
        return (top, bottom)

    def shift(items):
        items.append(items[0])
        for x in range(len(items) - 1):
            items[x] = items[x+1]
        return items[:3]

    #1. fill in top and bottom
    #2. if 1 is in bottom, flip them
        #2.1 swap bottom 1, 2
    #3. keep shifting so that #1 is right-most
        #3.1 getBottom() when done
    #4. if top = [1, 2, 3] -> return True
        #4.1 else: rotate
        #4.2 repeat rotating 3 times
        # return False

    #1
    canSee = []
    canNotSee = []
    for x in pips:
        canSee.append(x)        
    canNotSee = getBottom(canSee)

    #2
    if 1 in canNotSee:
        stack = flip(canSee, canNotSee)
        canSee = stack[0]
        canNotSee = stack[1]

    #3
    if canSee[0] != 1:
        while canSee[0] != 1:
            canSee = shift(canSee)
        canNotSee = getBottom(canSee)

    #4
    for i in range(4):
        if canSee == [1, 2, 3]:
            return True
        else: 
            canSee = rotate(canSee, getBottom(canSee), 1, 2)[0]
    return False
