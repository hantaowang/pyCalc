from exp_evalv import evalv_exp
print("""Hello, Welcome to PyCalc v1.01\n
Enter in a mathematical expression to calculate
Available operators: + - * / ^ ( )
Available symbols: e, pi""")

while True:
    sequence = input("\nEnter an expression: ")
    try:
        print(evalv_exp(sequence))
    except Exception as e:
        print("Error:", e)