class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def find_cycle(head):
    slow=head
    fast=head

    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next

        if slow==fast:
            break
    else:
        return None
    slow=head
    while slow!=fast:
        slow=slow.next
        fast=fast.next
    return slow

    
# create list
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)

# create cycle (50 → 30)
head.next.next.next.next.next = head.next.next

node = find_cycle(head)

if node:
    print("Cycle starts at:", node.data)
else:
    print("No cycle")