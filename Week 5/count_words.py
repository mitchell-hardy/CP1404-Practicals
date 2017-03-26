"""
Program to count the amount of words in a string and return
the occurrence of each to the user.
"""
__author__ = 'Mitch Hardy'


def count_words():
    """
    Determine qty of each word in user_sentence.
    Only adds keys to dictionary if not already within.
    Print Dictionary with sorted and aligned formatting.
    """
    user_sentence = input(str("Please enter a sentence: ")).lower().split()
    sentence_dict = {}
    for word in user_sentence:
        word_count = user_sentence.count(word)
        if word not in sentence_dict:
            sentence_dict[word] = word_count
    longest_word = max(len(word) for word in user_sentence)
    for key, value in sorted(sentence_dict.items()):
        print("{:{}} : {}".format(key, longest_word, value))

count_words()
