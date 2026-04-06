class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def detect_cycle(head):
    slow=head
    fast=head

    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next

        if slow==fast:            # fast and slow if equals it will be true
            return True
    return False

head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
head.next.next.next=Node(40)
head.next.next.next.next=head.next  # creating cycle
print(detect_cycle(head))
temp=head
count=0
while temp!=None and count<5:
    print(temp.data,end="->")
    temp=temp.next
    count+=1
print("Null")    