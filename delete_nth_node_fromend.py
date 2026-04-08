class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def Delete_nth_Node(head,n):
    # use dummy for handling edge case
    dummy=Node(0)
    dummy.next=head

    slow=dummy
    fast=dummy

    for i in range(n+1):
        if fast is None:
            return head
        fast=fast.next

    while fast:
        fast=fast.next
        slow=slow.next

    slow.next=slow.next.next #actual deletion
    return dummy.next

def printlist(head):
    temp=head
    while temp!=None:
        print(temp.data,end="->")
        temp=temp.next
    print("Null")



head=Node(5)
head.next=Node(10)
head.next.next=Node(15)
head.next.next.next=Node(20)
head.next.next.next.next=Node(25)
# before
printlist(head)
head=Delete_nth_Node(head,2)
# after
printlist(head)