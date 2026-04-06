class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
def reverse(head):

    prev=None
    curr=head

    while curr:
        next_node=curr.next # store next
        curr.next=prev    # reveser link
        prev=curr           # this will move previous 
        curr=next_node       # this will move curr

    return prev

head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
head.next.next.next=Node(40)
head=reverse(head)
temp=head
while temp!=None:
    print(temp.data,end="->")
    temp=temp.next
print("Null")