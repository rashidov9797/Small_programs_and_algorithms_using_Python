def fibonachi(a_son):
  """Fibonachi ketma-ketligi"""
  sonlar = []

  for i in range(a_son):
    if i==0 or i==1:
      sonlar.append(1)
    else:
      sonlar.append(sonlar[i-1] + sonlar[i-2])  
  return sonlar 

print(fibonachi(10))




