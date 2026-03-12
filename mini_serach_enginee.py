# Mini Search Engine using Python
# This program allows users to search keywords within a collection of documents.
# It builds an inverted index to map words to the documents containing them.
# The search engine then returns documents that match the user's query.
# This project demonstrates basic information retrieval and text processing concepts.
import re

# -------------------------
# Sample Documents
# -------------------------

documents = {
    1: "Python is a popular programming language",
    2: "JavaScript is widely used for web development",
    3: "Python is used in data science and machine learning",
    4: "Search engines help find information on the internet",
    5: "Machine learning and artificial intelligence are future technologies"
}

# -------------------------
# Build Inverted Index
# -------------------------

def build_index(docs):
    index = {}

    for doc_id, text in docs.items():
        words = re.findall(r'\w+', text.lower())

        for word in words:
            if word not in index:
                index[word] = set()

            index[word].add(doc_id)

    return index


# -------------------------
# Search Function
# -------------------------

def search(query, index, docs):

    words = re.findall(r'\w+', query.lower())

    results = set()

    for word in words:
        if word in index:
            if not results:
                results = index[word].copy()
            else:
                results &= index[word]

    return results


# -------------------------
# Main Program
# -------------------------

def main():

    index = build_index(documents)

    print("\nMini Search Engine")
    print("-------------------")

    query = input("Enter search keyword: ")

    results = search(query, index, documents)

    if results:
        print("\nSearch Results:\n")
        for doc_id in results:
            print(f"Document {doc_id}: {documents[doc_id]}")
    else:
        print("\nNo results found.")


if __name__ == "__main__":
    main()