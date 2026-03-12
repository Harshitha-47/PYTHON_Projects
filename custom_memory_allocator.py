
# Custom Memory Allocator Simulation
# This program simulates a basic memory allocation system.
# It demonstrates how memory blocks are allocated and freed
# using a simple First-Fit allocation strategy.
# Users can request memory, release memory, and view the
# current memory state. This project demonstrates concepts
# used in operating system memory management.


MEMORY_SIZE = 100
memory = [{"start":0,"size":MEMORY_SIZE,"free":True}]


def display_memory():

    print("\n========== MEMORY STATE ==========")

    for block in memory:
        status = "Free" if block["free"] else "Allocated"
        print(f"Start: {block['start']} | Size: {block['size']} | Status: {status}")

    print("==================================\n")


def allocate_memory(size):

    for block in memory:

        if block["free"] and block["size"] >= size:

            start = block["start"]

            remaining = block["size"] - size

            block["size"] = size
            block["free"] = False

            if remaining > 0:
                new_block = {
                    "start": start + size,
                    "size": remaining,
                    "free": True
                }

                memory.insert(memory.index(block) + 1, new_block)

            print(f"Memory allocated at address {start}\n")
            return

    print("Memory allocation failed. Not enough space.\n")


def free_memory(address):

    for block in memory:

        if block["start"] == address and not block["free"]:

            block["free"] = True
            print("Memory freed successfully.\n")
            return

    print("Invalid memory address.\n")


def main():

    while True:

        print("========= MEMORY ALLOCATOR =========")
        print("1. Allocate Memory")
        print("2. Free Memory")
        print("3. Display Memory")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            size = int(input("Enter memory size to allocate: "))
            allocate_memory(size)

        elif choice == "2":
            addr = int(input("Enter start address to free: "))
            free_memory(addr)

        elif choice == "3":
            display_memory()

        elif choice == "4":
            print("Exiting Memory Allocator...")
            break

        else:
            print("Invalid option.\n")


main()