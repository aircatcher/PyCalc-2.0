from appJar import gui

'''
Create the GUI & set a title
'''
app = gui("PyCalc 2.0")

'''
Start the Initialization on program launch
'''
class FirstInit:
    def __init__(self):
        self.num1 = self.num2 = 0
        self.temp = 0
        self.memory = 0
        self.result = 0
        self.opr = None
        self.percent = None
        self.resArray = []

        app.setSize(210, 225)
        app.setResizable(canResize = False)
        app.setBg("#6A6A6A")
        app.setFont(size = 12, family = "Arial Black", weight = "normal")

calc = FirstInit()
calc.memory = float(calc.memory)

'''
Function specified for button clicks
with it's each specific functions
'''
def clicked(widgets):
    # Clear everything, not including the history*
    # *TODO: History for storing previous results in a storage window
    if widgets == 'AC':
        calc.num1 = calc.num2 = 0
        calc.temp = 0
        calc.result = 0
        calc.opr = None
        calc.percent = None
        app.setEntry("Result", "", callFunction = False)

    # If number 0 to 9 are pressed
    if widgets == '1' or widgets == '2' or widgets == '3' or widgets == '4' or widgets == '5' or widgets == '6' or widgets == '7' or widgets == '8' or widgets == '9' or widgets == '0':
        if app.getEntry("Result") == None:
            app.setEntry("Result", widgets, callFunction = False)

        elif calc.opr == None and calc.temp == 0:
            strNum = str(app.getEntry("Result")) + str(widgets)
            calc.num1 = int(strNum)
            app.setEntry("Result", calc.num1, callFunction = False)

        elif calc.opr == None and calc.temp != 0:
            app.setEntry("Result", calc.temp, callFunction = False)
        
        elif calc.opr != None and calc.temp != 0 and calc.percent != None:
            app.setEntry("Result", widgets, callFunction = False)
            calc.num2 = widgets

        elif app.getEntry("Result") == '+' or app.getEntry("Result") == '-' or app.getEntry("Result") == 'x' or app.getEntry("Result") == '/':
            app.clearEntry("Result", callFunction = False)
            strNum = str(app.getEntry("Result")) + str(widgets)
            calc.num2 = int(strNum)
            app.setEntry("Result", calc.num2, callFunction = False)
    
    # If operators +, -, *, / are pressed
    if widgets == '+' or widgets == '-' or widgets == 'x' or widgets == '/':
        calc.opr = widgets
        app.clearEntry("Result", callFunction = False)
        app.setEntry("Result", calc.opr, callFunction = False)
    
    if widgets == '%':
        if calc.percent == None:
            calc.percent = widgets
            if calc.opr == None and calc.temp == 0:
                num1 = 0
            elif calc.opr != None and calc.temp == 0:
                num2 = num2 / 100
                calc.result = num2
            elif calc.opr != None and calc.temp != 0:
                calc.temp = float(calc.temp) / 100
                calc.result = calc.temp

            app.clearEntry("Result", callFunction = False)
            app.setEntry("Result", calc.result, callFunction = False)

    # If dot (.) is pressed
    # if widgets == '.':

    if widgets == 'M+':
        if app.getEntry("Result"):
            calc.memory += float(app.getEntry("Result"))
    if widgets == 'M=':
        if app.getEntry("Result"):
            calc.memory -= app.getEntry("Result")

    if calc.memory == 0:
        app.disableButton("MC")
        app.disableButton("MR")
    else:
        app.enableButton("MC")
        app.enableButton("MR")
        if widgets == 'MC':
            calc.memory = 0
            app.disableButton("MC")
            app.disableButton("MR")
        if widgets == 'MR':
            app.setEntry("Result", calc.memory, callFunction = False)

    # If equal (=) is pressed
    if widgets == '=':
        # Check if there is result from previous calculation
        if calc.temp == 0 and calc.percent == None:
            if calc.opr == '+':
                calc.result = calc.num1 + float(calc.num2)
            if calc.opr == '-':
                calc.result = calc.num1 - float(calc.num2)
            if calc.opr == 'x':
                calc.result = calc.num1 * float(calc.num2)
            if calc.opr == '/':
                calc.result = float(calc.num1) / float(calc.num2)
        # If so, then use it as a replacement for num1
        elif calc.temp != 0 and calc.percent == None:
            if calc.opr == '+':
                calc.result = calc.temp + float(calc.num2)
            if calc.opr == '-':
                calc.result = calc.temp - float(calc.num2)
            if calc.opr == 'x':
                calc.result = calc.temp * float(calc.num2)
            if calc.opr == '/':
                calc.result = float(calc.temp) / float(calc.num2)
        elif calc.temp != 0 and calc.percent != None:
            calc.result = float(calc.temp) + float(calc.num2)
            calc.temp = 0
            calc.percent = None
        
        if calc.result != None:
            calc.temp = calc.result

        app.clearEntry("Result", callFunction = False)
        app.setEntry("Result", calc.temp, callFunction = False)

'''
Calculator Entries and Buttons
with Row and Column Layouts
'''
class Layout:
    # First Row
    def row1():
        app.addEntry("Result", 0, 0, colspan = 4)
        app.disableEntry("Result")

    # Second Row
    def row2():
        buttonMC = app.addButton("MC", clicked, 1, 0)
        buttonMR = app.addButton("MR", clicked, 1, 1)
        buttonMAdd = app.addButton("M+", clicked, 1, 2)
        buttonMDel = app.addButton("M-", clicked, 1, 3)

    # Third Row
    def row3():
        buttonAC = app.addButton("AC", clicked, 2, 0)
        buttonPercent = app.addButton("%", clicked, 2, 1)
        buttonDiv = app.addButton("/", clicked, 2, 2)
        buttonMult = app.addButton("x", clicked, 2, 3)

    # Fourth Row
    def row4():
        button7 = app.addButton("7", clicked, 3, 0)
        button8 = app.addButton("8", clicked, 3, 1)
        button9 = app.addButton("9", clicked, 3, 2)
        buttonSubtract = app.addButton("-", clicked, 3, 3)

    # Fifth Row
    def row5():
        button4 = app.addButton("4", clicked, 4, 0)
        button5 = app.addButton("5", clicked, 4, 1)
        button6 = app.addButton("6", clicked, 4, 2)
        buttonPlus = app.addButton("+", clicked, 4, 3)

    # Sixth Row
    def row6():
        button1 = app.addButton("1", clicked, 5, 0)
        button2 = app.addButton("2", clicked, 5, 1)
        button3 = app.addButton("3", clicked, 5, 2)
        buttonEquals = app.addButton("=", clicked, 5, 3, rowspan = 2)

    # Seventh Row
    def row7():
        buttonDot = app.addButton(".", clicked, 6, 0)
        button0 = app.addButton("0", clicked, 6, 1)
        buttonConvertPN = app.addButton("+/-", clicked, 6, 2)

    row1()
    row2()
    row3()
    row4()
    row5()
    row6()
    row7()

    if calc.memory == 0:
        app.disableButton("MC")
        app.disableButton("MR")

layout = Layout()

'''
Set the widths across all the buttons
'''
class Width():
    app.setButtonWidth("MC", 4)
    app.setButtonWidth("MR", 4)
    app.setButtonWidth("M+", 4)
    app.setButtonWidth("M-", 4)

    app.setButtonWidth("AC", 4)
    app.setButtonWidth("%", 4)
    app.setButtonWidth("/", 4)
    app.setButtonWidth("x", 4)

    app.setButtonWidth("7", 4)
    app.setButtonWidth("8", 4)
    app.setButtonWidth("9", 4)
    app.setButtonWidth("-", 4)

    app.setButtonWidth("4", 4)
    app.setButtonWidth("5", 4)
    app.setButtonWidth("6", 4)
    app.setButtonWidth("+", 4)

    app.setButtonWidth("1", 4)
    app.setButtonWidth("2", 4)
    app.setButtonWidth("3", 4)
    app.setButtonWidth("=", 4)

    app.setButtonWidth(".", 4)
    app.setButtonWidth("0", 4)
    app.setButtonWidth("+/-", 4)

width = Width()

# '''
# Set the font styles for non numerical buttons
# '''
# class SpecialButtonStyles():
#     app.setFont(weight = "bold")

# sbStyles = SpecialButtonStyles()

'''
Start the GUI
'''
app.go()