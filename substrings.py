def substrings(word, dictionary):
    """Return occurrences of substrings of dictionary in word.

    :param word: A string to be analyzed
    :param dictionary: A list of substrings of word
    :return occurrences: A dictionary where each key is a substring
    of word that's in dictionary, and each value is the number of
    occurrences of that substring in word.
    """
    word = word.lower()
    occurrences_temp = {substr: 0 for substr in dictionary}

    for substr in dictionary:
        for i in range(0, len(word)):
            if word[i:i + len(substr)] == substr:
                occurrences_temp[substr] += 1

    occurrences = {}
    for substr in occurrences_temp:
        if occurrences_temp[substr] > 0:
            occurrences[substr] = occurrences_temp[substr]

    return occurrences
