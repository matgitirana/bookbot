import sys
from stats import *

def get_book_text(filepath: str):
  with open(filepath) as f:
    file_contents = f.read()
    
    return file_contents
  
def main():
  if len(sys.argv) < 2:
    print('Usage: python3 main.py <path_to_book>')
    sys.exit(1)

  path_to_book = sys.argv[1]

  book_text = get_book_text(f'./{path_to_book}')

  num_words = get_num_words(book_text)

  character_counts = get_character_counts(book_text)

  sorted_counts = sort_character_counts(character_counts)

  print('============ BOOKBOT ============')
  print(f'Analyzing book found at {path_to_book}...')

  print('----------- Word Count ----------')
  print(f'Found {num_words} total words')

  print('--------- Character Count -------')
  for c in sorted_counts:
    if c['char'].isalpha():
      print(f'{c['char']}: {c['num']}')

main()