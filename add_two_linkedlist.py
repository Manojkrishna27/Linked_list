class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def add_two_number(l1,l2):
    dummy=Node(0)

    temp=dummy
    carry=0

    while l1 or l2 or carry:

        val1=l1.data if l1 else 0
        val2=l2.data if l2 else 0

        total= val1+val2+carry

        carry=total//10

        digits=total%10

        temp.next=Node(digits)

        temp=temp.next

        if l1:
            l1=l1.next
        if l2:
            l2=l2.next

    return dummy.next

l1=Node(2)
l1.next=Node(2)
l1.next.next=Node(4)

l2=Node(5)
l2.next=Node(6)
l2.next.next=Node(1)
result=add_two_number(l1,l2)
temp=result
while temp:
    print(temp.data,end="->")
    temp=temp.next
print("Null")
