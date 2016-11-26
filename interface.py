from exp_evalv import evalv_exp

print("""Hello, Welcome to PyCalc v1.01\n
Available operators: + - * / ^ ( )
Available symbols: e, pi
To plot a function, start with function notation 'f(x)='
and use the variable 'x' """)

while True:

    sequence = input("\nEnter an equation or expression: ")
    try:
        print(evalv_exp(sequence))
    except OverflowError as e:
        print("OverflowError: result too large!")
    except SyntaxError as e:
        print("SyntaxError:", e)
    except ZeroDivisionError as e:
        print("ZeroDivisionError: you can't divide by zero!")
    except Exception as e:
        print("Unexpected error:", e)