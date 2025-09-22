import random

# The interpreter acts as a simple calculator
# + - * / and () are allowed
print(50-5*6+(4/2));
a = 231 #type int
b = 1.623 #type float
# Division always returns a float
print(17/3);
# To do floor division and get an integer result you can use the // operator
print(17//3);
# To calculate the remaider you can use %
print(17%3);
print((17/3)*(17//3)+(17%3));
# To calculate powers you can use **
print(5**2);
# The = sign is used to assign (or define) a value to a variable
c = "carota" #type str
print (c+"23ac59");
# The last printed expression is assigned to the variable _
# round(value, number of decimals)
ab = round(a/b,2);
print(ab);
print("\'Is it?\' they said");
s = "First line.\nSecond line."
print(s);
print(r"C:\some\name");
print("""\

Usage: thingy [OPTIONS]

     -h                        Display this usage message

     -H hostname               Hostname to connect to

""")


print("Py""thon")

print(10*"a"+"no")
count = len(c+"23ac59");
print(count);

davide = ("Idk what is going on here"
          "I'm looking at the wrogn stuff!")

print(davide)

bashar = "pappero"
print(bashar[0] + bashar[-1]+ bashar[-2] + "c" + bashar[-1] + "d" + "i" + bashar[-1])

sessoPazzo = "capucapu"
print(sessoPazzo[:2] + sessoPazzo[0] + sessoPazzo[4:6]) #cacca???

print(len(sessoPazzo))

paradoxFaCacare = [0, 2, 4, 6, 8, 10]
print(paradoxFaCacare[1]+paradoxFaCacare[4])

paradoxFaCacare[1] = 658
print(paradoxFaCacare[1]+paradoxFaCacare[4])

paradoxFaCacare.append(ab)
paradoxFaCacare.append(ab/2)
print(paradoxFaCacare)

paradoxFaCacare[2:4] = (9009,2314,7854)
print(paradoxFaCacare)
paradoxFaCacare[:] = []
print(len(paradoxFaCacare))

basharIsShittingMe = ["por", "cod", "kane"]
pacchettoNonScopa = ["è", "vero"]
patrzioSiLamenta = ["true", "false", "true"]
davideSiFaICazziDiBashar = ["sesso","commedia","divina"]
cavoli= [basharIsShittingMe, pacchettoNonScopa, patrzioSiLamenta, davideSiFaICazziDiBashar]
print(cavoli)
print(cavoli[0][1])
cavoli[:] = []
print(cavoli)

#####################################

a = random.randint(1, 6)
b = random.randint(1, 6)
c = random.randint(1, 6)
if (a+b+c) <= 10 :
     print("hai fallito il tiro")
else :
     print("hai avuto successo")
#is this a dice?

###################

i = 144*144
print('Il valore di i +', i)

a, b = 0, 1
while a < 1000:
     print(a, end=',') #the keyword argument end can be used to avoid the newline after the output, or end the output with a different string:
     a,b = b, a+b

cacoa = -2**3
print(cacoa)