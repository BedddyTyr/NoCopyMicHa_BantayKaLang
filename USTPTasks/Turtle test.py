import turtle

pen = turtle.Turtle()
pen.shape("turtle")
pen.pensize(3)

pen.color(str(input("Enter color (you can use hex code): ")))
pen.begin_fill()
pen.circle(radius=eval(input("Input the BIGness of the shape: ")), steps=eval(input("Input how many sides it has: ")))
pen.end_fill()

pen.hideturtle()

turtle.done()
