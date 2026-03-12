# -------------------------------------------------------------
# URL Shortener Backend Simulation
# This program simulates the backend logic of a URL shortening
# service similar to Bitly. It generates short codes for long
# URLs and stores a mapping between the short code and the
# original URL. Users can shorten URLs and retrieve the
# original link using the generated short code.
# -------------------------------------------------------------

import random
import string

url_database = {}

BASE_URL = "http://short.ly/"


def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits
    short_code = ''.join(random.choice(characters) for _ in range(length))
    return short_code


def shorten_url():

    long_url = input("Enter the long URL: ")

    short_code = generate_short_code()

    url_database[short_code] = long_url

    short_url = BASE_URL + short_code

    print("\nShort URL created successfully!")
    print("Short URL:", short_url, "\n")


def retrieve_url():

    code = input("Enter short code: ")

    if code in url_database:
        print("Original URL:", url_database[code], "\n")
    else:
        print("Short URL not found.\n")


def display_database():

    print("\n========== URL DATABASE ==========")

    if not url_database:
        print("No URLs stored.")
    else:
        for code, url in url_database.items():
            print(f"{BASE_URL}{code}  -->  {url}")

    print("==================================\n")


def main():

    while True:

        print("========= URL SHORTENER =========")
        print("1. Shorten URL")
        print("2. Retrieve Original URL")
        print("3. View Stored URLs")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            shorten_url()

        elif choice == "2":
            retrieve_url()

        elif choice == "3":
            display_database()

        elif choice == "4":
            print("Exiting URL Shortener...")
            break

        else:
            print("Invalid option.\n")


main()