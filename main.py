f = open("words.txt", "r")

words = f.read().splitlines()

f.close()

def filter_n_letter_words(words, n):
    """Filter the list of words to only include those with exactly 5 letters."""
    return [word for word in words if len(word) == n]


def filter_words_with_only_alphabets(words):
    """Filter the list of words to only include those that contain only alphabetic characters."""
    return [word for word in words if word.isalpha()]


def to_lowercase(words):
    """Convert all words in the list to lowercase."""
    return [word.lower() for word in words]

words = filter_n_letter_words(words, 5)
words = filter_words_with_only_alphabets(words)
words = to_lowercase(words)

def get_answer(pattern, wordle, limit=10):
  # store no. of occurance as well
  global words

  def word_to_dictionary(word):
      """Convert a word to a dictionary with letters as keys and their counts as values."""
      return {char: word.count(char) for char in set(word)}


  answer = {}
  for p in pattern:
    if p in answer:
        continue
    for word in words:
        letters = word_to_dictionary(wordle)
        if len(word) != len(p):
            continue
        match = True
        for i, char in enumerate(p):
            if char == "#":
                if word[i] not in letters or letters.get(word[i], 0) == 0:
                    match = False
                    break
                else:
                    letters[word[i]] -= 1
            elif char == ".":
                if word[i] in letters:
                    match = False
                    break
        if match:
            answer[p] = answer.get(p, []) + [word]
            if len(answer[p]) >= limit:
                break

  # print("Answer:")
  # for p, words in answer.items():
  #     print(f"{p}: {', '.join(words)}") 
  # print(f"Total patterns found: {len(answer)}")
  return answer

