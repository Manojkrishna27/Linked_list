class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
def search_element_ddl(head,key):
    temp=head
    while temp:
        if temp.data==key: # take temp for reuse compare to target if found true
            return True
        temp=temp.next
    return False # else false
head=Node(10)
head.next=Node(15)
head.next.prev=head
head.next.next=Node(20)
head.next.next.prev=head.next
head.next.next.next=Node(30)
head.next.next.next.prev=head.next.next
print(search_element_ddl(head,20)) # true
print(search_element_ddl(head,2)) # false