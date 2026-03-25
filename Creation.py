"""A Linked List is a way to store data like a chain 
Instead of storing data side by side (like an array),
data is stored in separate boxes, and each box knows where the next box is."""
class Node:
    def __init__(self,data): # using constructor we are making DATA and next reference 
        self.data=data
        self.next=None

node1=Node(10) # step 1 we have to set data

node2=Node(15)


node3=Node(20)

node1.next=node2 # step 2 we have to make link to next to each of the nodes
node2.next=node3
node3.next=None  # last node always NONE

head=node1 # and then step 3 make the head as start
temp=head  # Use temp for reuse the code

while temp is not None:  
    print(temp.data,end="->")
    temp=temp.next
print("NULL")
