#Q1
x=7
y=20
print(x+y)
print(x/y)
print(x-y)
print(x*y)
#Q2
Even=list(range(0,102,2))
print(Even)
print(Even[0:10])
print(len(Even))
Even.append(2024)
print(Even)
#Q3
z=Even[-1]
if z%5==0:
    print("Divisible")
else:
    print("Not Divisible")
#Q4
for i in range(6):
    print(i)
#Q5
import turtle
turtle.bgcolor("white")
turtle.pensize(5)
turtle.pencolor("red")
for i in range(5):
    turtle.forward(50)
    turtle.left(72)
turtle.done()
#Q6
def pythtest(a,b,c):
    result = a**2+b**2==c**2
    return result
print(pythtest(3,4,5))
#Q7 add a colon on the while statement + indent
#Q8
import matplotlib.pyplot as plt
p=[23,45,34,56,53]
q=[1,2,24,75,76]
plt.plot(p,q,color="red",marker="o",markerfacecolor="red")
plt.xlim(20,60)
plt.ylim(0,80)
plt.show()




