class Stack:

    def __init__(self,size:int) -> None:
        self.size = size
        self.board = [0] * size
        self.curidx = -1 
    
    def push(self,num):
        if self.curidx + 1 >= len(self.board):
            print("overflow stack!")
            exit(1)

        self.curidx += 1
        self.board[self.curidx] = int(num)

    def set(self,idx:int,num):
        self.board[idx] = int(num)

    def get(self,idx:int):
        return self.board[idx]

    def pop(self):
        if self.curidx < 0:
            print("stack is empty!")
            exit(1)

        num = self.get(self.curidx)
        self.curidx -= 1
        return num

    def popn(self,size):
        nums = []
        if self.curidx + 1 < size:
            print("stack size not enouf size")
            exit(1)

        for _ in range(0,size):
            nums.append(self.pop())
        
        return nums

    def print(self):
        sub = []
        for i in range(0,self.curidx+1):
           sub.append(self.board[i]) 
        
        print(sub)
