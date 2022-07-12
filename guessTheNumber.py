import random 

def run():
 random_num=random.randint(1,100); 
 selected_num=int(input('choose a number between 1 and 100'))
 while selected_num!=random_num:
   print(random_num)
   if selected_num>random_num:
     print('Too high :c')
   else:
     print('Too low :c')
   selected_num=int(input('Choose another number'))
 print('You win!')

if __name__ == '__main__':
  run()
