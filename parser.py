def G():
    lex()
    print("G -> E")
    E()
    if(next_token == "$" and not error):
        print("success")
    else:
        print("failure: unconsumed input: ", unconsumed_input())

def E():
    global error
    if error:
        return
    print("E -> T R")
    T()
    R()

def T():
    global error
    if error:
        return
    print("T -> F S")
    F()
    S()

def R():
    global error
    if error:
        return
    if next_token == "+":
        print("R -> + T R")
        lex()
        T()
        R()
    elif next_token == "-":
        print("R -> - T R")
        lex()
        T()
        R()
    else:
        print("R -> e")

def F():
    global error
    if error:
        return
    if next_token == "(":
        print("F -> (E)")
        lex()
        E()
        if next_token == ")":
            lex()
        else:
            error = True
            print("error: unexptected token ", next_token)
            print("unconsumed_input: ", unconsumed_input())
            return
    elif next_token == '0' or next_token == '1' or next_token == '2' or next_token == '3' or next_token == '4' or next_token == '5'or next_token == '6' or next_token == '7' or next_token == '8' or next_token == '9':
        print("F -> N")
        N()
    else:
        error = True
        print("error: unexptected token ", next_token)
        print("unconsumed_input: ", unconsumed_input())
        return

def S():
    global error
    if error == True:
        return
    if next_token == "*":
        print("S -> * F S")
        lex()
        F()
        S()
    elif next_token == "/":
        print("S -> / F S")
        lex()
        F()
        S()
    else:
        print("S -> e")

def N():
    global error
    if error:
        return
    if next_token == '0' or next_token == '1' or next_token == '2' or next_token == '3' or next_token == '4' or next_token == '5'or next_token == '6' or next_token == '7' or next_token == '8' or next_token == '9':
        print("N -> "+str(next_token))
        lex()
    else:
        error = True
        print("error: unexptected token ", next_token)
        print("unconsumed_input: ", unconsumed_input())
        return

def lex():
    char = myfile.read(1)
    if (char !='\n' and char != ' '):
        global next_token
        next_token = char
        pop_char()
        print(char)
    else:
        lex()
            
#Return unconsumed String        
def unconsumed_input():
    return ''.join(character_list)

#Pops the first charcater fromn the list        
def pop_char():
    character_list.pop(0)


error = False
next_token = ""

file_list = ["D:/lab3/f1.txt","D:/lab3/f2.txt",
                 "D:/lab3/f3.txt","D:/lab3/f4.txt",
                 "D:/lab3/f5.txt","D:/lab3/f6.txt",
                 "D:/lab3/f7.txt","D:/lab3/f8.txt",
                 "D:/lab3/f9.txt","D:/lab3/f10.txt"]

for file in file_list:
    myfile = open(file,"r")
    character_list = [ch for ch in open(file).read() if ch != '\n' if ch != ' ']
    G()
    print()

