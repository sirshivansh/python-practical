class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp=temp.next
            temp.next = new_node
        print(f"{data} added to Linked List.")
    def delete(self):
        if not self.head:
            print("Linked List is Empty.")
        else:
            removed = self.head.data
            self.head = self.head.next
            print(f"Removed {removed} from Linked List")
    def display(self):
        if not self.head:
            print("Linked List is empty.")
        else:
            temp= self.head
            print("Linked List Elements :", end ="")
            while temp:
                print(temp.data, end= " -> ")
                temp=temp.next
            print("None")

# Menu Driven Program
def menu():
    linked_list = LinkedList()
    stack = []
    queue = []

    while True:
        print("\nMenu : ")
        print("1. Linked List - Insert Element")
        print("2. Linked List - Delete Element")
        print("3. Linked List - Display Element")
        print("4. Stack - Push Element")
        print("5. Stack - Pop Element")
        print("6. Stack - Display Element")
        print("7. Queue - Enqueue Element")
        print("8. Queue - Dequeue Element")
        print("9. Queue - Display Element")
        print("10. Exit")

        choice = int(input("Enter your choice : "))
        
        if choice == 1:
            data = input("Enter your data to insert in Linked List: ")
            linked_list.insert(data)
        elif choice == 2:
            linked_list.delete()
        elif choice == 3:
            linked_list.display()
        elif choice == 4:
            data = input("Enter data to push onto stack : ")
            stack.append(data)
        elif choice == 5:
            if stack:
                removed = stack.pop()
                print(f"Popped {removed} from the stack.")
            else:
                print("Stack is Empty.")
        elif choice == 6:
            print("Stack Elements:", stack[::-1] if stack else "Stack is empty.")
        elif choice == 7:
            data = input("Enter data inn Queue: ")
            queue.append(data)
            print(f"{data} enqueued into Queue.")
        elif choice == 8:
            if queue:
                removed = queue.pop(0)
                print(f"Dequeued {removed} from Queue.")
            else:
                print("Queue is Empty.")
        elif choice == 9:
            print("Queue Elements: ", queue if queue else "Queue is Empty.")
        elif choice ==10:
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again!")

#Running the Program
if __name__ == "__main__":
    menu()