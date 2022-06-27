def palindrome(word):
  word=word.replace(' ','')
  word=word.lower()
  inverted_word=word[::-1]
  return word==inverted_word


def run():
  word = input('write a word ')
  is_palindrome = palindrome(word)
  if is_palindrome:
    print('Is palindrome')
  else:
    print('Is not palindrome')

if __name__ == '__main__':
  run()
