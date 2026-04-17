class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
def delete_node(node):

    # connect to prev
    if node.prev:
        node.prev.next=node.next
    # connect node next to node's prev
    if node.next:
        node.next.prev=node.prev
    return node
def printlist(head):
    temp=head
    while temp!=None:
        print(temp.data,end="->")
        temp=temp.next
    print("NULL")
head=Node(10)
head.next=Node(20)
head.next.prev=head
head.next.next=Node(25)
head.next.next.prev=head.next
head.next.next.next=Node(30)
head.next.next.next.prev=head.next.next
delete_node(head.next.next) # 25
temp=head
while temp!=None:
    print(temp.data,end="->")
    temp=temp.next
print("NULL")