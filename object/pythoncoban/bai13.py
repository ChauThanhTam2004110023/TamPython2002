###@@@ chu vi v diện tích
import math
xA = float(input("xA: "))
yA = float(input("yA: "))
xB = float(input("xB: "))
yB = float(input("yB: "))
xC = float(input("xC: "))
yC = float(input("yC: "))

ab = math.sqrt((xB-xA) ** 2 + (yB-yA) ** 2)
bc = math.sqrt((xC-xB) ** 2 + (yC-yB) ** 2)
ac = math.sqrt((xC-xA) ** 2 + (yC-yA) ** 2)

##kiểm tra
if(ab+bc > ac) and (ab+ac > bc) and (bc+ac > ab):
    cv= ab+ac+bc
    print("Chu vi: ", cv)
    ##Diện tích
    p = cv/2
    s = math.sqrt(p*(p-ab) * (p-bc) * (p-ac))
    print("Diện tích: ", s)
else:
    print("Không tạo thành tam giác")