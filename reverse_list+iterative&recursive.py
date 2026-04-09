class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def insert_at_tail(head,value):
    newnode=Node(value)
    if head is None:
        return newnode

    temp=head
    
    while temp.next:
        temp=temp.next
    temp.next=newnode
    return head

def interative_reverse(head):
    prev=None
    curr=head
    while curr:
        new_node=curr.next
        curr.next=prev
        prev=curr
        curr=new_node
    return prev
def recursive_reverse(head):
    if head is None or head.next is None:
        return head
    new_head=recursive_reverse(head.next)

    head.next.next=head
    head.next=None
    return new_head

   
def printlist(head):
    temp=head
    while temp:
        print(temp.data,end="->")
        temp=temp.next
    print("None")

head=None
for i in range(1,7):
    head=insert_at_tail(head,i)
printlist(head)

head=interative_reverse(head)
printlist(head)

head=recursive_reverse(head)
printlist(head)