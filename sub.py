def numb():
  a=int(input('Please enter a number--->>>'))

  for i in range(2,21):
    if not (a%i):
      print(f'The number{a} divisible by is {i}without a remainder') 
  return    
numb()     
