'''
Some turtle functions you can use to make your shapes


forward(<distance>) - This function takes a positive or negative number and
will move the turtle forward.

back(<distance>) - This function takes a positive or negative numbers and
it will move the turtle back.

right(<angle>) - This function takes a number that represents
angle in degrees. It will turn the turtle to  its right

left(<angle>) - This functions takes an number that represents
 an angle in degrees. It will turn the turtle to its left.

pencolor(<color>) - This functions takes a string that represents a color. The
turtle's pen will draw in that color. The possible color values can be found
at https://www.tcl.tk/man/tcl8.4/TkCmd/colors.htm

penup() - This function takes no parameters. When called it will
lift the turtle's pen up, the turtle will not draw when moved.

pendown() - This function takes no parameters. When called it will put the
turtle's pen down. It will draw when moved.

speed(<number>) - This function takes a number. It determines how fast the
turtle moves around the screen. Strangely enough if you want it to go as
fast as possible you have to pass it 0 as a parameter.

goto(<x>, <y>) - This function takes two numbers, a position along the x-axis
and a position along the y-axis. It will move the turtle to that position.

fillcolor(<color>) - This function takes a string that represents a color. The
color will be used to fill shape the turtle has made. In order to get the turtle
to fill the shape you have to use the begin_fill() function before the turtle
starts drawing the shape and the end_fill() function after it finishes for the
shape to be filled in.

begin_fill() - This function takes no parameters. It is put before the turtle
draws a shape that you want filled in.

end_fill() - This function takes no parameters. It is put after the turtle has
finished drawing a shape that you want filled in.

dot(<size>, <color>) - This function takes two parameters. The first is a
positive number that represents the diameter of the dot to be drawn by the
turtle. The second is a string that represents the color the dot should be.


BONUS:

circle(<radius>, <extent>, <steps>) - This function takes three parameters.
However you only have to put in the first one. The <radius> parameter is the
necessary parameter, it is a number that represents the radius of the circle.
The <extent> is optional. It represents an angle saying how much of the circle
should be drawn, if you don't put in anything for <extent> it will draw the whole
circle. If you put in 180, it will draw a half circle. The third parameter
<steps> is a number that represents how many steps the turtle should take to
draw the circle. Try setting <steps> as 5 to see what happens.


'''




from turtle import *

# START WRITING YOUR CODE HERE

penup()
goto(-300,0)

def square(c):
	for i in range(4):
		pendown()
		color(c)
		forward(50)
		right(90)
		penup()
	back (60)
def door(s):
	forward(30)
	for h in range(4):
		pendown()
		color("black")
		forward(20)
		right(90)
		penup()
	forward(30)

def window(x):
	forward(30)
	for k in range(4):
		pendown()
		color("white")
		forward(10)
		right(90)
		penup()
	forward(30)

def windows(r):
	forward(30)
	for w in range(4):
		pendown()
		color("white")
		forward(10)
		right(90)
		penup()
	forward(30)

def triangle(d):
	forward(60)
	for j in range(3):
		pendown()
		color(d)
		forward(50)
		left(120)
		penup()
	forward(60)

for o in range(3):
	begin_fill()
	square("red")
	end_fill()
	
	begin_fill()
	triangle("orange")
	end_fill()
	
	begin_fill()
	square ("purple")
	end_fill()
	
	begin_fill()
	triangle("magenta")
	end_fill()
	
	begin_fill()
	square("blue")
	end_fill()
	
	begin_fill()
	triangle("green")
	end_fill()
	
goto(-315, -30)
for z in range(9):
	#begin_fill()
	door("black")
	#end_fill()

goto(-320, -10)
for y in range (9):
	#begin_fill()
	#fill_color("white")
	window("white")
	#window()
	#end_fill()

goto(-300, -10)
for e in range(9):
	#begin_fill()
	#fill_color("white")
	windows("white")
	#window()
	#end_fill()
	
penup()
goto(-250, 250)
dot(75,"yellow")
goto(300,300)
input()



