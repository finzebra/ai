# Define the ListNode class
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val  # Value of the node
        self.next = next  # Pointer to the next node

# Function to reverse the linked list iteratively
def reverse_linked_list(head):
    prev = None  # Initialize prev to None
    current = head  # Start with the head of the linked list
    while current:
        next_node = current.next  # Store the next node
        current.next = prev  # Reverse the pointer of the current node
        prev = current  # Move prev to the current node
        current = next_node  # Move current to the next node
    return prev  # Return the new head of the reversed linked list

# Example usage
head = ListNode(1)  # Create the linked list: 1 -> 2 -> 3
head.next = ListNode(2)
head.next.next = ListNode(3)

# Reverse the linked list
reversed_head = reverse_linked_list(head)

# Print the reversed linked list
while reversed_head:
    print(reversed_head.val, end=" ")  # Output: 3 2 1
    reversed_head = reversed_head.next