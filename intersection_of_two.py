class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def intersection_of_list(head1,head2):
    p1=head1
    p2=head2

    while p1!=p2: # this check the memory address
        p1=p1.next if p1 else head2 # if not in p1 move to second list
        p2=p2.next if p2 else head1  # if not p2 move to first list

    return p1


head1=Node(10)
head1.next=Node(15)
head1.next.next=Node(20)
head1.next.next.next=Node(25)
head2=Node(10)
head2.next=head1.next # here is  the intersection
node=intersection_of_list(head1,head2)
if node:
    print("intersection at",node.data)
else:
    print("No intersection")