class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def reverse_linked_list(head):
     prev=None
     curr=head
     while curr:
         next_node=curr.next
         curr.next=prev
         prev=curr
         curr=next_node
     return prev 
def printlist(head):
    temp=head
    while temp!=None:
        print(temp.data,end="->")
        temp=temp.next
    print("Null")

head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
head.next.next.next=Node(40)
printlist(head)
printlist(reverse_linked_list(head))