class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def reverse(head):
    prev=None
    curr=head
    if head is None:
        return head
    while curr:
        next_node=curr.next
        curr.next=prev
        prev=curr
        curr=next_node
    return prev
def palindrome(head):
    # middile element logic
    slow=head
    fast=head

    while fast.next:
        slow=slow.next
        fast=fast.next.next
    second_half=reverse(slow) # reverse second part

    first_half=head
    # palindrome logic
    
    while second_half:
        if first_half.data!=second_half.data:
            return False
        first_half=first_half.next
        second_half=second_half.next
    
    return True
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(2)
head.next.next.next.next = Node(1)

print(palindrome(head))
        
        