def get_num_words(text: str):
  words = text.split()
  return len(words)

def get_character_counts(text: str):
  result = {}

  for c in text:
    char = c.lower()
    result.setdefault(char, 0)
    result[char] += 1

  return result