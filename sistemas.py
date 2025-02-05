#Solucionador de sistemas
from fractions import Fraction
print("CALC de sistemas cramer\n ax+by=k1\n cx+dy=k2")
a = float(input("Digite A:"))
b = float(input("Digite B:"))
k1 = float(input("Digite k1:"))
c = float(input("Digite C:"))
d = float(input("Digite D:"))
k2 = float(input("Digite k2:"))

if a * d - b * c != 0:
    x = (k1*d - k2*b)/(a*d - b*c)
    y = (k2*a - k1*c)/(a*d - b*c)
    xf = Fraction(x).limit_denominator(10)
    yf = Fraction(y).limit_denominator(10)
    print("{},{}\n{},{}".format(x,y,xf,yf))
 
