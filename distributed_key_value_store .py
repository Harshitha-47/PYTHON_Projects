# Distributed Key-Value Store Simulation
# This program simulates a distributed key-value database
# system where data is stored across multiple nodes.
# Users can store, retrieve, and view key-value pairs.
# This demonstrates basic concepts used in distributed
# storage systems such as Redis and Dynamo-style databases.
import hashlib

# Simulated distributed nodes
nodes = {
    "Node1": {},
    "Node2": {},
    "Node3": {}
}


def get_node(key):
    """
    Determine which node stores the key
    using a hash function
    """
    node_list = list(nodes.keys())

    hash_value = int(hashlib.md5(key.encode()).hexdigest(), 16)

    index = hash_value % len(node_list)

    return node_list[index]


def put():
    key = input("Enter key: ")
    value = input("Enter value: ")

    node = get_node(key)

    nodes[node][key] = value

    print(f"\nData stored in {node}\n")


def get():
    key = input("Enter key to retrieve: ")

    node = get_node(key)

    if key in nodes[node]:
        print(f"\nValue: {nodes[node][key]} (from {node})\n")
    else:
        print("Key not found.\n")


def display():
    print("\n========== DISTRIBUTED STORE ==========")

    for node, data in nodes.items():

        print(f"\n{node}:")

        if not data:
            print("  No data stored")

        for key, value in data.items():
            print(f"  {key} -> {value}")

    print("\n=======================================\n")


def main():

    while True:

        print("====== DISTRIBUTED KEY VALUE STORE ======")
        print("1. Put (Store Data)")
        print("2. Get (Retrieve Data)")
        print("3. View All Nodes")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            put()

        elif choice == "2":
            get()

        elif choice == "3":
            display()

        elif choice == "4":
            print("Exiting system...")
            break

        else:
            print("Invalid choice.\n")


main()