class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
    
def delete_at_pos(head,pos):
    if head is None:
        return head
    # delete head
    if pos==1:
        if head.next:
            head.next.prev=None
        return head.next
    count=1
    temp=head
    # reach position
    while temp and count <pos:
        temp=temp.next
        count+=1
    if temp is None:
        return head
    # connect previous node
    if temp.prev:
        temp.prev.next=temp.next
    # connect next node
    if temp.next:
        temp.next.prev=temp.prev
    return head
def printlist(head):
    temp=head
    while temp!=None:
        print(temp.data,end="->")
        temp=temp.next
    print("Null")

head=None
head=Node(1)
head.next=Node(2)
head.next.prev=head
head.next.next=Node(3)
head.next.next.prev=head.next
head.next.next.next=Node(4)
head.next.next.next.prev=head.next.next
printlist(head)
delete_at_pos(head,2)
printlist(head)