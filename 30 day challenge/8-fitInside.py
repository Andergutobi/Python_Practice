#__Complete a program in order to determine if a box fits in another box.

class box:
    length = 0
    width = 0
    height = 0
    
    #this method will check if the length, width & height, and then it will output which dimension is the longest.
    def getLongestSide(self):
        self.max = self.length
        if self.width > self.max:
            self.max = self.width
        if self.height > self.max:
            self.max = self.height
        return self.max
    #this method should output which dimension is yhe shortest.
    def getShortestSide(self):
        self.min = self.length
        if self.width < self.min:
            self.min = self.width
        if self.height < self.min:
            self.min = self.height
        return self.min
box1 = box()
dimensions = input("Enter box1's dimensions. ex. 1 2 3 :  ").split()
box1.length = int(dimensions[0])
box1.width = int(dimensions[1])
box1.height = int(dimensions[2])

box2 = box()
dimensions = input("Enter box2's dimensions. ex. 1 2 3 :  ").split()
box2.length = int(dimensions[0])
box2.width = int(dimensions[1])
box2.height = int(dimensions[2])

def canFitBox1InBox2(box1, box2):
    if box1.getLongestSide() < box2.getLongestSide() and box1.getShortestSide() < box2.getShortestSide():
        return True
    elif box1.getLongestSide() >= box2.getLongestSide() and box1.getShortestSide() >= box2.getShortestSide():
        return False
    else:
        return False
    
if canFitBox1InBox2(box1, box2) == True:
    print("Yes, Box1 Fits in!")
else:
    print('No, Box1 wont fit in Box2.')
    
    
        
        