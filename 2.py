import turtle

def f(len, gl):
    if gl == 0:
        turtle.fd(len)
    else:
        f(len//3, gl-1)
        turtle.left(60)
        f(len//3, gl-1)
        turtle.right(120)
        f(len//3, gl-1)
        turtle.left(60)
        f(len//3, gl-1)

turtle.shape("turtle")

for i in range(3):
    f(200, 3)
    turtle.right(120)

turtle.done()
