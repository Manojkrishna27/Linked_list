class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
def count_node(head):
    temp=head
    count=0
    while temp!=None:
        print(temp.data,end="->")
        temp=temp.next
        count+=1
    print("NULL")
    return count
head=Node(10)
head.next=Node(15)
head.next.prev=head
head.next.next=Node(20)
head.next.next.prev=head.next
head.next.next.next=Node(25)
head.next.next.next.prev=head.next.next

print(count_node(head))
