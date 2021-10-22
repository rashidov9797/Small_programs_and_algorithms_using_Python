from pywebio.input import  input, FLOAT
from pywebio.output import put_text
from  math import  pi


def round():
  """A web application that calculates the radius of a circle"""
  r = input('Enter the radius of the circle-->>>',type=FLOAT)
  yuza = pi*(r**2)
  per = 2*pi*r 
  put_text(f"Radius circl {yuza}, perimeter{per} ")
round()  