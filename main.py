from stats import *

def get_book_text(filepath: str):
  with open(filepath) as f:
    file_contents = f.read()
    
    return file_contents
  
def main():
  book_text = get_book_text('./books/frankenstein.txt')

  num_words = get_num_words(book_text)

  character_counts = get_character_counts(book_text)

  print(f'Found {num_words} total words')
  print(character_counts)

main()