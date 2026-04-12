class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

def delete_head(head):
    if head is None:
        return None
    if head.next is None:
        return None
    
    head=head.next # change head to head.next (1 to 2)
    head.prev=None # and now head will be 2 you need to connect to None

    return head
def printlist(head):
    temp=head
    while temp!=None:
        print(temp.data,end="->")
        temp=temp.next
    print("Null")

head=Node(1)
head.next=Node(2)
head.next.next=Node(3)
head.next.next.next=Node(4)
printlist(delete_head(head))
