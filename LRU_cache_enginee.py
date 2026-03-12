class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # dictionary
        self.head = Node(0, 0)  # dummy head
        self.tail = Node(0, 0)  # dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head

    # Remove node from linked list
    def remove(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    # Insert node right after head (Most Recently Used)
    def insert(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        node = Node(key, value)
        self.insert(node)
        self.cache[key] = node

        if len(self.cache) > self.capacity:
            # remove LRU from tail
            lru = self.tail.prev
            self.remove(lru)
            del self.cache[lru.key]

    # Display current cache state (for better understanding)
    def display(self):
        current = self.head.next
        print("Cache state (Most Recent → Least Recent): ", end="")
        while current != self.tail:
            print(f"[{current.key}:{current.value}] ", end="")
            current = current.next
        print()


# ================= MAIN PROGRAM =================

if __name__ == "__main__":
    capacity = int(input("Enter Cache Capacity: "))
    lru = LRUCache(capacity)

    while True:
        print("\n----- LRU Cache Menu -----")
        print("1. Put (Insert Key, Value)")
        print("2. Get (Retrieve Value by Key)")
        print("3. Display Cache")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            key = int(input("Enter key: "))
            value = int(input("Enter value: "))
            lru.put(key, value)
            print("Key inserted successfully!")
            lru.display()

        elif choice == 2:
            key = int(input("Enter key: "))
            result = lru.get(key)
            if result == -1:
                print("Key not found!")
            else:
                print("Value:", result)
            lru.display()

        elif choice == 3:
            lru.display()

        elif choice == 4:
            print("Exiting program...")
            break

        else:
            print("Invalid choice! Try again.")