# Social Network Friend Graph using Python
# This program simulates a simple social networking system using a graph.
# Each user is represented as a node and friendships are edges between users.
# Users can be added, friendships can be created, and mutual friends can be found.
# This project demonstrates graph data structures and adjacency lists in Python.
# Social Network Friend Graph using Python
# This program simulates a simple social networking system using a graph.
# Each user is represented as a node and friendships are edges between users.
# Users can be added, friendships can be created, and mutual friends can be found.
# This project demonstrates graph data structures and adjacency lists in Python.

social_graph = {}


# -----------------------------
# Add User
# -----------------------------
def add_user(user):
    if user not in social_graph:
        social_graph[user] = []
        print(f"{user} added to the network.")
    else:
        print("User already exists.")


# -----------------------------
# Add Friendship
# -----------------------------
def add_friend(user1, user2):

    if user1 not in social_graph:
        add_user(user1)

    if user2 not in social_graph:
        add_user(user2)

    if user2 not in social_graph[user1]:
        social_graph[user1].append(user2)
        social_graph[user2].append(user1)
        print(f"{user1} and {user2} are now friends.")
    else:
        print("Friendship already exists.")


# -----------------------------
# Show Friends
# -----------------------------
def show_friends(user):

    if user in social_graph:
        friends = social_graph[user]

        if friends:
            print(f"Friends of {user}: {', '.join(friends)}")
        else:
            print(f"{user} has no friends yet.")

    else:
        print("User not found.")


# -----------------------------
# Mutual Friends
# -----------------------------
def mutual_friends(user1, user2):

    if user1 in social_graph and user2 in social_graph:

        mutual = set(social_graph[user1]) & set(social_graph[user2])

        if mutual:
            print("Mutual Friends:", ", ".join(mutual))
        else:
            print("No mutual friends.")

    else:
        print("User not found.")


# -----------------------------
# Display Network
# -----------------------------
def display_network():

    print("\nSocial Network Graph\n")

    for user in social_graph:
        print(f"{user} -> {social_graph[user]}")


# -----------------------------
# Main Menu
# -----------------------------
def main():

    while True:

        print("\n===== Social Network Menu =====")
        print("1. Add User")
        print("2. Add Friendship")
        print("3. Show Friends")
        print("4. Mutual Friends")
        print("5. Display Network")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            user = input("Enter username: ")
            add_user(user)

        elif choice == "2":
            u1 = input("Enter first user: ")
            u2 = input("Enter second user: ")
            add_friend(u1, u2)

        elif choice == "3":
            user = input("Enter username: ")
            show_friends(user)

        elif choice == "4":
            u1 = input("Enter first user: ")
            u2 = input("Enter second user: ")
            mutual_friends(u1, u2)

        elif choice == "5":
            display_network()

        elif choice == "6":
            print("Exiting program...")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()