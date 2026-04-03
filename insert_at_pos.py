class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def insert_at_pos(head,value,pos):
    new_node=Node(value)

    if pos==0:
        new_node.next=head
        return new_node
    
    temp=head # temp traversal
    for i in range(pos-1):
        if temp is None:
            return head
        
        temp=temp.next

    new_node.next=temp.next  # connect new to next
    temp.next=new_node      # then previous to new

    return head

head=Node(5)
head.next=Node(15)
head.next.next=Node(20)
head.next.next.next=Node(25)

head=insert_at_pos(head,10,1)
temp=head
while temp!=None:
    print(temp.data,end="->")
    temp=temp.next
print("NULL")
        

