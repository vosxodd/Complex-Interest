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
    for j in range(1, 13):
        if i == 1 and j == 1:
            print("|    ", j, "    | ", "%.2f"%(capital), "    |   ", "%.2f"%(capital*percent/100), "   | ", "%.2f"%(capital + capital*percent/100), " |")
        elif 1<=j<=9:
            capital += investment + float("%.2f"%(capital*percent/100))
            print("|    ", j, "    | ", "%.2f"%(capital), "    |   ", "%.2f"%(capital*percent/100), "   | ", "%.2f"%(capital + capital*percent/100), "  |")
        elif j>9:
            capital += investment + capital*percent/100
            print("|   ", j, "    | ", "%.2f"%(capital), "    |   ", "%.2f"%(capital*percent/100), "   | ", "%.2f"%(capital + capital*percent/100), "  |")



