"""
CTEC 121
<Stephen Guild>
<Mod 4 Lab>
<assignment/lab description
"""

""" IPO template
Input(s): list/description
Process: description of what function does
Output: return value and description
"""
from graphics import *

def main():
    '''
    win=GraphWin("Title", 600, 300)

    p=Point(100,100)
    x=p.getX()
    y=p.getY()
    print("x and y",x,y)

    input()
    '''

    '''
    win=GraphWin("My Squares",600,600)
    p1=Point(50,50)
    p2=Point(100,100)
    r1=Rectangle(p1,p2)
    r1.draw(win)

    r2=Rectangle(Point(200,200),Point(250,250))
    r2.draw(win)

    input()
    '''

    win=GraphWin("shapes",400,400)
    center=Point(200,200)
    circ=Circle(center,60)
    circ.setFill('red')
    circ.draw(win)
    label=Text(center,"Red Circle")
    label.draw(win)
    rect=Rectangle(Point(60,60),Point(140,140))
    rect.draw(win)
    line=Line(Point(40,60), Point(360,330))
    line.draw(win)
    oval=Oval(Point(40,300),Point(360,399))
    oval.draw(win)

    input()

main()    