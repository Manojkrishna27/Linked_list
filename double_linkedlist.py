class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

def insert_at_head(head,value):
    new_node=Node(value)

    if head is None:
        return new_node
    
    new_node.next=head
    head.prev=new_node

    return new_node

def printlist(head):
    temp=head
    while temp!=None:
        print(temp.data,end="->")
        temp=temp.next
    print("Null")
head=None

head=insert_at_head(head,2)
head=insert_at_head(head,3)
head=insert_at_head(head,4)
head=insert_at_head(head,5)
printlist(head)




