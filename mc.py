a = int(input('enter your highest 10th mark : '))
b = int(input('enter your 2nd highest 10th mark : '))
c = int(input('enter your 3rd highest 10th mark : '))
x = (a + b + c)/6

print('10th avg :',x)
y = x + 30
print('Enter your 11th marks without adding practical marks:')
d = int(input('Tamil : '))
e = int(input('English : '))
f = int(input('Maths :'))
g = int(input('Biology :'))
h = int(input('Physics :'))
i = int(input('Chemistry :'))
tam = y + (d/90)*20
eng = y + (e/90)*20
mat = y + (f/90)*20
bio = y + (g/70)*20
phy = y + (h/70)*20
che = y + (i/70)*20


print('12th mark:')
print('Tamil:',tam)
print('English:',eng)
print('Maths:',mat)
print('Biology:',bio)
print('Physics:',phy)
print('Chemistry:',che)

print('TOTAL:',tam+eng+mat+bio+phy+che)
print('Eng cut off :',mat+((phy+che)/2))

print('Thank you for using mc!')

# Made by Harish G
