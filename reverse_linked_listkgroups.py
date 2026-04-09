# this is very important problem use python tutor for understanding visually
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def reverse_by_k_groups(head,k):
    temp=head
    count=0

    while temp and count<k:
        temp=temp.next
        count+=1
    if count<k:
        return head
    prev=None
    curr=head
    next_node=None
    count=0

    while curr and count<k:
        next_node=curr.next
        curr.next=prev
        prev=curr
        curr=next_node
        count+=1
    
    if next_node:
        head.next=reverse_by_k_groups(next_node,k)


    return prev

def insert_at_tail(head,value):
    new_node=Node(value)
    if head is None:
        return new_node
    temp=head
    while temp.next:
        temp=temp.next

    temp.next=new_node
    return head

def printlist(head):
    temp=head
    while temp:
        print(temp.data,end="->")
        temp=temp.next
    print("NULL")

head=None
for i in range(1,7):
    head=insert_at_tail(head,i)
printlist(head)

head=reverse_by_k_groups(head,2)
printlist(head)