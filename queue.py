class Queue(object):
    def __init__(self):
        self.contents=[]
    def push(self,x):
        self.contents.append(x)
        return x
    def pop(self):
        return self.contents.pop(0)
    def isempty(self):
        return len(self.contents)==0
