class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

def delete_tail(head):
    if head is None:
        return None
    if head.next is None:
        return None
    temp=head

    while temp.next:
        temp=temp.next

    temp.prev.next=None # disconnect
    return head
def printlist(head):
    temp=head
    while temp!=None:
        print(temp.data,end="->")
        temp=temp.next
    print("Null")
head=Node(1)
head.next=Node(2)
head.next.prev=head
head.next.next=Node(3)
head.next.next.prev=head.next
head.next.next.next=Node(4)
head.next.next.next.prev=head.next.next
printlist(head) # original 
printlist(delete_tail(head)) # after deleting