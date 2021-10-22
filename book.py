def e_bokk():

  savat=[]

  while True:
    books=input("Kitob nomini kiriting -->>> ")
    savat.append(books)
    c = input('Yana kitob xarid qilasizmi ? (Y/N)')
    if c == 'N':
      print('Xaridingiz uchun tashakkur!')
      break 
e_bokk()