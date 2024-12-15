class Queue :
    Top = -1
    def __init__(self,value):
        self.value = value
        self.Array = [0] * self.value

    def Push(self, item):
        if self.Top != self.value-1: # Checking Stack is Full
            self.Array[self.Top+1] = item
            self.Top += 1
            return self.Array
        else :
            return "Stack is full!"


    def Pop(self):
        if self.Top != -1 : # Checking Stack is Empty
            self.Array[self.Top] = 0
            self.Top -= 1
            return self.Array
        else :
            return "Queue is Empty!"

    def Peek(self):
        return self.Array[0]




#-----------------------------------------------------------------------------------------------------------------------

size = int(input())

q = Queue(size)

print("\n")

print(q.Push(100),"\n")
print(q.Push(200),"\n")
print(q.Push(300),"\n")

print(q.Peek())

print(q.Push(400),"\n")
print(q.Push(500),"\n")


print(q.Pop(),"\n")
print(q.Pop(),"\n")
print(q.Pop(),"\n")
print(q.Pop(),"\n")
print(q.Pop(),"\n")
