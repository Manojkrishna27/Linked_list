class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
# two pointer method is used here (fast and slow)
def middle_element(head):
    slow=head
    fast=head

    # fast will be always one step ahead than slow if slow=2 then fast will be
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
        
    return slow.data

head=Node(1)
head.next=Node(2)
head.next.next=Node(3)
head.next.next.next=Node(4)
head.next.next.next.next=Node(5)
temp=head
while temp!=None:
    print(temp.data,end="->")
    temp=temp.next
print("NULL")

print("the middle element is",middle_element(head))