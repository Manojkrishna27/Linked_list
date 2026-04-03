class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def insert_at_tail(head,value):
    new_node=Node(value)

    if head is None:
        return new_node
    
    temp=head
    while temp.next:
        temp=temp.next

    temp.next=new_node

    return head

head=Node(10)
head.next=Node(15)
head.next.next=Node(20)
head.next.next.next=Node(25)

head=insert_at_tail(head,30)

temp=head
while temp!=None:
    print(temp.data,end="->")
    temp=temp.next
print("NULL")
