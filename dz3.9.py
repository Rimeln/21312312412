def area(a,b):
 if a<=0 or b<=0:
  raise ValueError("Сторона должна быть больше нуля")
 else:
  print("Площадь равна:",a*b,"Периметр равен:",(a+b)*2)

try:
 area(2,4)
except ValueError as e:
 print("Ошибка:", e)