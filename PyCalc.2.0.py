from appJar import gui

# create the GUI & set a title
app = gui("PyCalc 2.0")

'''
Function specified for button clicks
with it's each specific functions
'''
class FirstInit:
    def __init__(self):
        self.num1 = self.num2 = 0
        self.opr = None
        self.resArray = []

calc = FirstInit()

def clicked(widgets):

    if widgets == 'AC':
        calc.num1 = calc.num2 = 0
        calc.opr = None
        app.setEntry("Result", "", callFunction = False)

    if widgets == '1' or widgets == '2' or widgets == '3' or widgets == '4' or widgets == '5' or widgets == '6' or widgets == '7' or widgets == '8' or widgets == '9' or widgets == '0':
        if app.getEntry("Result") == None:
            app.setEntry("Result", widgets, callFunction = False)

        elif calc.opr == None:
            strNum = str(app.getEntry("Result")) + str(widgets)
            calc.num1 = int(strNum)
            app.setEntry("Result", calc.num1, callFunction = False)
            
        else:
            if app.getEntry("Result") == '+' or app.getEntry("Result") == '-' or app.getEntry("Result") == 'x' or app.getEntry("Result") == '/':
                 app.clearEntry("Result", callFunction = False) 
            strNum = str(app.getEntry("Result")) + str(widgets)
            calc.num2 = int(strNum)
            app.setEntry("Result", calc.num2, callFunction = False)
    
    if widgets == '+' or widgets == '-' or widgets == 'x' or widgets == '/':
        calc.opr = widgets
        app.clearEntry("Result", callFunction = False)
        app.setEntry("Result", calc.opr, callFunction = False)

    # if widgets == '.':


    if widgets == '=':
        if calc.opr == '+':
            result = calc.num1 + calc.num2
        if calc.opr == '-':
            result = calc.num1 + calc.num2
        if calc.opr == 'x':
            result = calc.num1 * calc.num2
        if calc.opr == '/':
            result = float(calc.num1) / float(calc.num2)

        app.clearEntry("Result", callFunction = False)
        app.setEntry("Result", result, callFunction = False)

'''
Calculator Entries and Buttons
with Row and Column Layouts
'''
app.addEntry("Result", 0, 0, colspan = 4)
app.disableEntry("Result")

buttonMC = app.addButton("MC", clicked, 1, 0)
buttonMR = app.addButton("MR", clicked, 1, 1)
buttonMAdd = app.addButton("M+", clicked, 1, 2)
buttonMDel = app.addButton("M-", clicked, 1, 3)

buttonAC = app.addButton("AC", clicked, 2, 0)
buttonPercent = app.addButton("%", clicked, 2, 1)
buttonDiv = app.addButton("/", clicked, 2, 2)
buttonMult = app.addButton("x", clicked, 2, 3)

button7 = app.addButton("7", clicked, 3, 0)
button8 = app.addButton("8", clicked, 3, 1)
button9 = app.addButton("9", clicked, 3, 2)
buttonSubtract = app.addButton("-", clicked, 3, 3)

button4 = app.addButton("4", clicked, 4, 0)
button5 = app.addButton("5", clicked, 4, 1)
button6 = app.addButton("6", clicked, 4, 2)
buttonPlus = app.addButton("+", clicked, 4, 3)

button1 = app.addButton("1", clicked, 5, 0)
button2 = app.addButton("2", clicked, 5, 1)
button3 = app.addButton("3", clicked, 5, 2)
buttonEquals = app.addButton("=", clicked, 5, 3, rowspan = 2)

buttonDot = app.addButton(".", clicked, 6, 0)
button0 = app.addButton("0", clicked, 6, 1)
buttonConvertPN = app.addButton("+/-", clicked, 6, 2)

'''
Set the widths across all the buttons
'''
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

# start the GUI
app.go()