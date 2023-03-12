class Node:
    def __init__(self,val=0):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.count = 0
        
    def addFirst(self, val):
        node = Node(val)
        node.next = self.first
        self.first = node
        if self.count == 0:
            self.last = node
        self.count += 1
    
    def addLast(self, val):
        node = Node(val)
        self.last.next = node
        self.last = node
        if not self.first:
            self.first = node
        self.count += 1
    
    def removeFirst(self):
        if not self.first:
            return
        if self.first == self.last:
            self.first = self.last = None
            return
        
        temp = self.first.next
        self.first.next = None
        self.first = temp
        self.count -= 1
    
    def removeLast(self):
        if not self.first:
            return
        
        if self.first == self.last:
            self.first = self.last = None
            return
        
        prev = self.getPrevious(self.last)
        self.last = prev
        self.last.next = None
        self.count -= 1
    
    def getPrevious(self,node):
        cur = self.first
        while cur.next:
            if cur.next == node:
                return cur
            cur = cur.next
        return None
    
    def contains(self,val):
        return self.indexOf(val) != -1
    
    def indexOf(self,val):
        if not self.first:
            return -1
        
        idx = 0
        cur = self.first
        while cur:
            if cur.val == val:
                return idx
            cur = cur.next
            idx += 1
        
        return -1
    
    def size(self):
        return self.count
        
    def toArray(self):
        res = []
        cur = self.first
        while cur:
            res.append(cur.val)
            cur = cur.next
        
        return res
    
    def reverse(self):
        if not self.first:
            return
        prev = self.first
        cur = self.first.next
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
            
        self.last = self.first
        self.last.next = None
        self.first = prev
        
    def print(self):
        cur = self.first
        while cur:
            print(cur.val)
            cur = cur.next

ll = LinkedList()
print(ll.toArray())
ll.reverse()
print(ll.toArray())