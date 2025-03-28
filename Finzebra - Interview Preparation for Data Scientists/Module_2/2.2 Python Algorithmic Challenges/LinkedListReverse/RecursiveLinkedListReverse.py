# Function to reverse the linked list recursively
def reverse_linked_list_recursive(head):
    # Base case: if the list is empty or has only one node
    if not head or not head.next:
        return head

    # Reverse the rest of the list
    reversed_list = reverse_linked_list_recursive(head.next)

    # Move the current node to the end
    head.next.next = head
    head.next = None

    return reversed_list

# Example usage
head = ListNode(1)  # Create the linked list: 1 -> 2 -> 3
head.next = ListNode(2)
head.next.next = ListNode(3)

# Reverse the linked list
reversed_head = reverse_linked_list_recursive(head)

# Print the reversed linked list
while reversed_head:
    print(reversed_head.val, end=" ")  # Output: 3 2 1
    reversed_head = reversed_head.next