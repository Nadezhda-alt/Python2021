number = int(input("Введите процент от 1 - 20"))
if number == 1:
    name = "процент"
elif number <= 4:
    name = "процента"
else:
    name = "процентов"
print(number, name)
