def calculate_lengths(words):
    # Use map() with a lambda function to calculate the length of each word
    word_lengths = map(lambda x : len(x), words)
    
    # Return the list of word lengths
    return list(word_lengths)
