high=0
weight=0
g=0.0
Vx0=0.0
x0=0.0
while 1:
    try:
        high=float(input("Введите высоту: "))
        if high<=0:
            raise MyException(Exception)
    except Exception:
       print("Некорректный ввод, повторите ввод")
    else:
        x0=high
        break
while 1:
    try:
        weight=float(input("Введите массу: "))
        if weight<=0:
            raise MyException(Exception)
    except Exception:
        print("Некорректный ввод, повторите ввод")
    else:
        break
while 1:
    try:
        Point=int(input("Выберите местоположение:\n   1 - Экватор\n   2 - Полюс\n"))
        if Point<1 or Point>2:
            raise MyException(Exception)
        elif Point==1:
            g=9.78
        else:
            g=9.832
    except Exception:
         print("Некорректный ввод, повторите ввод")
    else:
        accelerationX=-g
        break
while 1:
    try:
        Vx0=float(input("Введите начальную скорость: "))
        if Vx0<0:
            raise MyException(Exception)
    except:
        print("Некорректный ввод")
    else:
        Vx0*=-1
        break
while 1:
    try:
        t0=int(input("Введите начальное время: "))
        if t0<0:
            raise MyException(Exception)
    except:
        print("Некорректный ввод")
    else:
        break
x1=x0
deltaT=0
print("\n")
while x1>0:
    t1=t0+deltaT
    V1=Vx0+accelerationX*deltaT
    x1=x0+V1*deltaT
    print("Высота - {:.3f}\nСкорость - {:.3f}\nВремя - {}\n\n".format(x1,V1,t1))
    deltaT+=1
