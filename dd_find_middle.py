class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
def find_middle(head):
    slow=head
    fast=head
    # use fast and slow pointer method for finding middle element
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
    return slow.data
def printlist(head):
    temp=head
    while temp!=None:
        print(temp.data,end="->")
        temp=temp.next
    print("Null")
head=Node(10)
head.next=Node(20)
head.next.prev=head
head.next.next=Node(30)
head.next.next.prev=head.next
head.next.next.next=Node(40)
head.next.next.next.prev=head.next.next
head.next.next.next.next=Node(50)
head.next.next.next.next.prev=head.next.next.next
print(find_middle(head))