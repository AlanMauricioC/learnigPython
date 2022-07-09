def run():
  number = int(input('Give me a number'))
  if is_prime(number):
    print('Is prime number ')
  else:
    print('Is not a prime number ')
  
def is_prime(number):
  if number<=1:
    return False

  for i in range(2,number):
    if number%i==0:
      return False
  return True
    
if __name__ == '__main__':
  run()
