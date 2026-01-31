import string
def analyze_text(text):
    # Your solution here
    bucket = dict()
    answer = dict()
    # 1. Split the text into words and normalize them
    # (make lowercase and remove punctuation)
    words = text.translate(str.maketrans('', '', string.punctuation)).lower().split(" ")
    # 2. Count the occurrences of each word
    for i in words:
        if i in bucket:
            bucket[i] += 1
        else:
            bucket[i] = 1
    
    # 3. Find the number of unique words
    count = 0
    for key, value in bucket.items():
        count += 1 
    answer["unique_count"] = count
    # 4. Identify repeated words (appearing more than once)
    repeated_words = []
    for key, value in bucket.items():
        if bucket[key] >= 2:
            repeated_words.append(key)
    answer["repeated_words"] = list(set(repeated_words))
    # 5. Find palindrome words
    palindromes = []
    for key, value in bucket.items():
        palindrome = True
        j = len(key) - 1
        for i in range(0,len(key)//2):
            if key[i] != key[j] and i != j:
                palindrome = False
                continue
            j -= 1
        if(palindrome):
            palindromes.append(key)
    answer["palindromes"] = palindromes
        
    # 6. Return the results in a dictionary with sorted lists
    return answer
   
   
   
    pass
