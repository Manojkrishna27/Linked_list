class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def insert_at_head(head,value):

    new_node=Node(value)

    new_node.next=head

    head=new_node

    return head
    
def printlist(head):
    temp=head
    while temp!=None:
        print(temp.data,end="->")
        temp=temp.next
    print("NULL")
  
head=Node(10)
head.next=Node(15)
head.next.next=Node(20)

head=insert_at_head(head,5)

printlist(head)