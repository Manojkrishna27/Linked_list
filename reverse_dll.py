class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

def reverse_dll(head):
    temp=None
    curr=head
    while curr:
        # swap 
        temp=curr.prev 
        curr.prev=curr.next
        curr.next=temp

        curr=curr.prev
    if temp:
        head=temp.prev
    return head
def printlist(head):
    temp=head
    while temp!=None:
        print(temp.data,end="->")
        temp=temp.next
    print("NULL")
head=Node(10)
head.next=Node(15)
head.next.prev=head
head.next.next=Node(20)
head.next.next.prev=head.next
head.next.next.next=Node(25)
head.next.next.next.prev=head.next.next
printlist(head)

printlist(reverse_dll(head))

