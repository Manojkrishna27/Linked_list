class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

def insert_at_tail(head,value):
    new_node=Node(value)

    temp=head
    if head is None:
        return new_node
    
    while temp.next:
        temp=temp.next
    temp.next=new_node
    new_node.prev=temp

    return head
def printlist(head):
    temp=head
    
    while temp!=None:
        print(temp.data,end="->")
        temp=temp.next
    print("Null")
head=None
head=insert_at_tail(head,1)
head=insert_at_tail(head,2)
head=insert_at_tail(head,3)
head=insert_at_tail(head,4)
printlist(head)
