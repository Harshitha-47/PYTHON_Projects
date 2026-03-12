class AutoComplete:
    def __init__(self):
        # Dictionary to store words with frequency
        self.word_freq = {}

    # Insert word with frequency
    def insert(self, word, freq=1):
        if word in self.word_freq:
            self.word_freq[word] += freq
        else:
            self.word_freq[word] = freq

    # Return top-k suggestions based on prefix
    def suggest(self, prefix, k):
        # Filter words matching prefix
        matches = []

        for word in self.word_freq:
            if word.startswith(prefix):
                matches.append((word, self.word_freq[word]))

        # Sort by frequency (highest first)
        matches.sort(key=lambda x: x[1], reverse=True)

        # Return only top-k words
        return [word for word, freq in matches[:k]]

    # Real-time update when user selects a word
    def update_frequency(self, word):
        if word in self.word_freq:
            self.word_freq[word] += 1


# ---------------- MAIN PROGRAM ---------------- #

ac = AutoComplete()

# Insert initial words
ac.insert("python", 5)
ac.insert("pyramid", 2)
ac.insert("pycharm", 3)
ac.insert("java", 4)
ac.insert("javascript", 6)

# Take prefix input
prefix = input("Enter prefix: ")
k = int(input("Enter number of suggestions (k): "))

# Get top-k suggestions
suggestions = ac.suggest(prefix, k)

print("Top Suggestions:", suggestions)

# Simulate user selecting a word
if suggestions:
    selected = suggestions[0]
    print("User selected:", selected)
    ac.update_frequency(selected)

    print("Updated Frequency:", ac.word_freq[selected])