years=int(input("Срок размещения капитала (лет):"))
capital=float(input("Начальный капитал ($):"))
percent=float(input("Процентная ставка (%/мес.):"))
investment=float(input("Инвестиционные вливания ($/мес.):"))
for i in range (1,years+1):
    print(i,"год")
    print("-"*46)
    print("|         |   основа   | сумма %   |          |")
    print("| месяц   | инвестиций | за месяц  | капитал  |")
    print("-----------------------------------------------")
    for j in range (1,13):
          if i==1 and j==1:
              print("|    ",j,"    | ",capital,"    |   ",round(capital*percent/100,2),"   | ",capital+round(capital*percent/100),"  |")
          else:
              capital+=investment+round(capital*percent/100)
              print("|    ",j,"    | ",(capital),"    |   ",round(capital*percent/100,2),"   | ",capital+round(capital*percent/100),"  |")
              




