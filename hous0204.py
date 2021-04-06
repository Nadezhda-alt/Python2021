time = int(input("Введите секунды"))
if time > 3600: #в одном часе секунд
    hour = time//3600
else:
    time < 0
    hour = 00
#minute = hour - (time//60) #в одной минуте секунд
minute = (time - (hour*3600))//60
if minute < 1:
    minute = 0
x = time // 60
secund = time - (x*60)

print(hour,"часов", minute, "минут", secund, "секунд")
