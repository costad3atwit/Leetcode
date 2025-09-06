#Problem num.232
class MyQueue(object):

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack1.append(x)

        

    def pop(self):
        """
        :rtype: int
        """
        self.peek()
        return self.stack2.pop()



    def peek(self):
        """
        :rtype: int
        """
        if self.empty():
            return None
        elif len(self.stack2)!= 0:
            return self.stack2[-1]
        else:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.stack2[-1]
        
        

    def empty(self):
        """
        :rtype: bool
        """
        return (len(self.stack1) == 0) and (len(self.stack2) == 0)
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
