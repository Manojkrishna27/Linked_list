class Node:

    def __init__(self,data):
        self.data=data
        self.next=None

def find_nth_node(head,n):

    slow=head
    fast=head

    # move fast to n
    for i in range(n):
        if fast is None:
            return None
        fast=fast.next

    while fast:
        slow=slow.next
        fast=fast.next

    return slow
head=Node(5)
head.next=Node(10)
head.next.next=Node(15)
head.next.next.next=Node(20)
head.next.next.next.next=Node(25)
temp=head
while temp!=None:
    print(temp.data,end="->")
    temp=temp.next
print("NULL")
head=find_nth_node(head,2)
print("The node",head.data,"was Found")

