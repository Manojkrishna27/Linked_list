class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
def insert_at_pos(head,pos,value):
    new_node=Node(value)
# if position at one connect 
    if pos==1:
        if head:
             head.prev=new_node
             new_node.next=head

        return new_node
    # else diffrent position traverse first
    temp=head
    count=1
    while temp and count < pos-1:
        temp=temp.next
        count+=1
    # if temp none return head
    if temp is None:
        return head
    # insert the node
    new_node.next=temp.next
    new_node.prev=temp
 # fix to previous node if temp.next exist
    if temp.next:
        temp.next.prev=new_node
# else temp.next will be new_node
    temp.next=new_node

    return head

def printlist(head):
    temp=head
    while temp!=None:
        print(temp.data,end="->")
        temp=temp.next
    print("NULL")
head=Node(1)
head.next=Node(2)
head.next.prev=head
head.next.next=Node(3)
head.next.next.prev=head.next
head.next.next.next=Node(4)
head.next.next.prev=head.next.next

head=insert_at_pos(head,3,5)
printlist(head)

    

        