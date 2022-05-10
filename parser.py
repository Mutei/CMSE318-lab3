error = False
next_token = ""

def lex():
    for i in range(1,7):
        fname = "f"+str(i)+".txt"
        my_file = open(fname,"r")
        for line in my_file:
            for character in line:
                if character == " ":
                    continue
                next_token = character
                return next_token

def unconsumed_input():
    pass

def N():
    global error
    if error:
        return
    if next_token >= 0 and next_token <= 9:
        print("N -> "+str(next_token))
        lex()
    else:
        error = True
        print("error: unexptected token ", next_token)
        print("unconsumed_input ", unconsumed_input())
        return

def F():
    print(next_token)
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
            print("unconsumed_input ", unconsumed_input())
            return
    elif next_token >= 0 and next_token <= 9:
        print("F -> N")
        N()
    else:
        error = True
        print("error: unexptected token ", next_token)
        print("unconsumed_input ", unconsumed_input())
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

def E():
    global error
    if error:
        return
    print("E -> T R")
    T()
    R()

def G():
    lex()
    print("G -> E")
    E()

G()