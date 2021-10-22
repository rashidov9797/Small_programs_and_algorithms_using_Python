
def even_or_odd(a):
  """A function that determines whether an even or odd number"""
  if a%2 == 0:
    return f'{a} is an even number'
  else:
    return f'The number {a} is not an even number'  
print(even_or_odd(90))    