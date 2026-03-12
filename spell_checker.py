# -------------------------------------------------------------
# Professional Spell Checker and Auto-Correct System
# This program checks a sentence for spelling mistakes.
# It compares each word with a dictionary and finds the
# closest match using Python's difflib module.
# Misspelled words are corrected and a formatted report
# is displayed along with the corrected sentence.
# -------------------------------------------------------------

import difflib
import string

# Dictionary of valid words
DICTIONARY = [
    "i","am","a","btech","student","love","learning","python",
    "programming","computer","science","developer","algorithm",
    "network","database","software","engineering","analysis",
    "system","application","security","internet","cloud",
    "data","machine","technology"
]

# ---------------------------------------
# Spell checking and correction function
# ---------------------------------------
def correct_sentence(sentence):

    words = sentence.split()
    corrected_words = []
    corrections = []

    for word in words:

        clean_word = word.lower().strip(string.punctuation)

        # If word is correct
        if clean_word in DICTIONARY:
            corrected_words.append(clean_word)

        # If word is wrong
        else:
            suggestion = difflib.get_close_matches(clean_word, DICTIONARY, n=1, cutoff=0.6)

            if suggestion:
                corrected_words.append(suggestion[0])
                corrections.append((clean_word, suggestion[0]))
            else:
                corrected_words.append(clean_word)

    corrected_sentence = " ".join(corrected_words)

    return corrected_sentence, corrections


# ---------------------------------------
# Display professional report
# ---------------------------------------
def display_report(original, corrected, corrections):

    print("\n========== SPELL CHECK REPORT ==========")

    print("\nOriginal Sentence  :", original)

    if corrections:
        print("\nCorrections Made:")
        for wrong, right in corrections:
            print(f"  {wrong}  →  {right}")
    else:
        print("\nNo spelling mistakes found.")

    print("\nCorrected Sentence :", corrected)

    print("\n========================================")


# ---------------------------------------
# Main Program
# ---------------------------------------
def main():

    print("=========== PROFESSIONAL SPELL CHECKER ===========")

    sentence = input("\nEnter a sentence to check: ")

    corrected_sentence, corrections = correct_sentence(sentence)

    display_report(sentence, corrected_sentence, corrections)


if __name__ == "__main__":
    main()