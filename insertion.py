# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Function to insert at head
def insert_at_head(head, x):
    new_node = Node(x)
    new_node.next = head
    return new_node


# Function to create linked list from Python list
def create_linked_list(arr):
    head = None
    for i in reversed(arr):   # reverse to maintain order
        head = insert_at_head(head, i)
    return head


# Function to print linked list
def print_list(head):
    curr = head
    while curr:
        print(curr.data, end=" -> ")
        curr = curr.next
    print("None")


# ------------------ TEST CASES ------------------

# Example 1
arr = [1, 2, 3]
X = 7

head = create_linked_list(arr)
head = insert_at_head(head, X)

print("Output:")
print_list(head)


# Example 2 (Empty list)
arr2 = []
X2 = 7

head2 = create_linked_list(arr2)
head2 = insert_at_head(head2, X2)

print("\nOutput for empty list:")
print_list(head2)