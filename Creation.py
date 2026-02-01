class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

node1=Node(10)

node2=Node(15)


node3=Node(20)

node1.next=node2
node2.next=node3
node3.next=None

head=node1
temp=head

while temp is not None:
    print(temp.data,end="->")
    temp=temp.next
print("NULL")
