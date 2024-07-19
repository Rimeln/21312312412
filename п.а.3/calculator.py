from function import MathFunctions

a=int(input("Введите первое число:"))
b=int(input("Введите второе число:"))
func=input("Введите знак операции(+,-,*,/):")
if func=="+":
    res = MathFunctions.add(a,b)
elif func=="-":
    res = MathFunctions.sub(a,b)
elif func=="*":
    res = MathFunctions.mul(a,b)
elif func=="/":
    res = MathFunctions.div(a,b)
else:
    print("Неправильный выбор знака")
print(res)