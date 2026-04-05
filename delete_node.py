class Node:

    def __init__(self,data):
        self.data=data
        self.next=None

def delete_node(head,pos):

    if pos==0:
        return head.next
    
    temp=head
    for i in range(pos-1):
        if temp is None or temp.next is None:
            return head
        temp =temp.next

    temp.next=temp.next.next   # deletion ==skipping

    return head

head=Node(1)
head.next=Node(2)
head.next.next=Node(3)
head.next.next.next=Node(4)
head.next.next.next.next=Node(5)
temp=head                         # printing before deletion
while temp!=None:
    print(temp.data,end="->")
    temp=temp.next
print("NULL")

head=delete_node(head,3)
temp=head                       # printing after deletion
while temp!=None:
    print(temp.data,end="->")
    temp=temp.next
print("NULL")