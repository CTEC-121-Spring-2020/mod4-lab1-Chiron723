#convert.py
#ipo or program discipline

from graphics import *

def main():
    #create a window object
    win=GraphWin("Celcius Converter", 400,300)

    #create objects
    celciusTempString="Celcius Temperature:      "
    fahrenheitTempString="Fahrenheit Temperature:"

    #create Text boxes
    Text(Point(150,50),celciusTempString).draw(win)
    Text(Point(150,250),fahrenheitTempString).draw(win)

    #create center box
    Rectangle(Point(125,100),Point(275,200)).draw(win)

    #create Button text
    buttonText=Text(Point(200,150),"Convert it")
    buttonText.draw(win)

    #create input and output fields
    inputCelciusField=Entry(Point(300,50),5)
    inputCelciusField.setText("0.0")
    inputCelciusField.draw(win)

    outputFahrenheitField=Text(Point(300,250),"")
    outputFahrenheitField.draw(win)

    win.getMouse()

    CelciusTemperature=float(inputCelciusField.getText())
    fahrenheit=9.0/5.0*CelciusTemperature+32

    #Display Results
    outputFahrenheitField.setText(round(fahrenheit,2))

    buttonText.setText("Quit")

    win.getMouse()

main()