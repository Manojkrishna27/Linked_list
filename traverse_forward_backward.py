class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
def forward(head):
    temp=head
    while temp!=None:
        print(temp.data,end="->")
        temp=temp.next
    print("NULL")
def backward(head):
    temp=head
    # traverse
    while temp.next:
        temp=temp.next
    # go to prev by printing
    while temp!=None:
        print(temp.data,end="->")
        temp=temp.prev
    print("NULL")
head=Node(10)
head.next=Node(20)
head.next.prev=head
head.next.next=Node(30)
head.next.next.prev=head.next
forward(head)
backward(head)