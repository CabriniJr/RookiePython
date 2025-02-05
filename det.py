#Calculadora de determinante de matrizes 3x3 by Luigi
print("\nCalculadora de determinante de matrizes 3x3\n\nDigite os valores dos elementos \n")

#Elementos
a10 = 0
a11 = int(input("a11: "))
print("{}  {}  {}\n{}  {}  {}\n{}  {}  {}\n".format(a11,0,0,0,0,0,0,0,0))   
a12 = int(input("a12: "))
print("{}  {}  {}\n{}  {}  {}\n{}  {}  {}\n".format(a11,a12,0,0,0,0,0,0,0)) 
a13 = int(input("a13: "))
print("{}  {}  {}\n{}  {}  {}\n{}  {}  {}\n".format(a11,a12,a13,0,0,0,0,0,0))
a21 = int(input("a21: "))
print("{}  {}  {}\n{}  {}  {}\n{}  {}  {}\n".format(a11,a12,a13,a21,0,0,0,0,0))
a22 = int(input("a22: "))
print("{}  {}  {}\n{}  {}  {}\n{}  {}  {}\n".format(a11,a12,a13,a21,a22,0,0,0,0))
a23 = int(input("a23: "))
print("{}  {}  {}\n{}  {}  {}\n{}  {}  {}\n".format(a11,a12,a13,a21,a22,a23,0,0,0))
a31 = int(input("a31: "))
print("{}  {}  {}\n{}  {}  {}\n{}  {}  {}\n".format(a11,a12,a13,a21,a22,a23,a31,0,0))
a32 = int(input("a32: "))
print("{}  {}  {}\n{}  {}  {}\n{}  {}  {}\n".format(a11,a12,a13,a21,a22,a23,a31,a32,0))
a33 = int(input("a33: "))
print("{}  {}  {}\n{}  {}  {}\n{}  {}  {}\n".format(a11,a12,a13,a21,a22,a23,a31,a32,a33))
det1 = (a11*a22*a33)+(a12*a23*a31)+(a21*a32*a13)
det2 = (a13*a22*a31)+(a12*a21*a33)+(a23*a32*a11)
det = det1 - det2
print("\n Determinante: ",det)