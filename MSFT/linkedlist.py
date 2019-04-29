class Node: 
    
    # Constructor to initialize the node object 
    def __init__(self, data): 
        self.data = data 
        self.next = None
        
     # Constructor to initialize the linked list    
class LinkedList:
    def __init__(self):
        self.head = None
        
    #Traversing the list
    def traverse(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next
    
    #Reversing the list        
    def reverse(self):
      prev = None
      curr = self.head
      while curr:
        next = curr.next

        curr.next = prev
        prev = curr
        curr = next
      self.head = prev
    
    #removing duplicates
    def remove_dups(self):
        unique = []
        node = self.head
        prev = None
        
        while node:
            if node.data not in unique:
                unique.append(node.data)
                prev = node
                node = node.next
            else:
                node = node.next
                prev = node
        return unique

    def isPalindrome(self):
        node = self.head
        fast = node
        slow = node

        prev = None

        while fast and fast.next:
            fast = fast.next.next

            next = node.next   #the reversal
            node.next = prev
            prev = node
            node = next

        if fast:
            slow = slow.next
        else:
            slow = node

        while prev:
            if (prev.data == slow.data):
                slow = slow.next
                prev = prev.next
            else:
                return False
        return True
   
           
#Instantiating the LinkedList            
llist = LinkedList()    
 
node1 = Node(10)  
node2 = Node(10)
node3 = Node(20)
node4 = Node(50)
node5 = Node(10)

llist.head =  node1
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

llist.traverse()
print(" ")
llist.reverse()
llist.traverse()

print(llist.isPalindrome())

#print(llist.remove_dups())
