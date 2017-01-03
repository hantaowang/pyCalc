# pyCalc
A simple graphing calculator built on Python

Visit [hantaowang.me/pycalc](hantaowang.me/pycalc) to learn more

####Try it Out
To run pycalc, you must have [python3](https://www.python.org/download/releases/3.0/) installed along with a command line shell. Download the files and run `python3 interface.py` to begin. 

Alternativetly, use the embedded python shell to on [hantaowang.me/pycalc](hantaowang.me/pycalc). However, due to the limitations of the shell, pyCalc runs noticabely slower and functions resulting in complex numbers may not evaluate.

Try expressions such as `5(4)^2+3` and equations such as `f(x)=x^2` or `f(x)=(9-x^2)^0.5`. To clear the graph, enter `clear`.

####What is pyCalc
As my first side project, I wanted to create a program that computes mathematical expressions and draw functions, much like a graphing calculator can. I was inspired by a class project I did in CS 61A, the [Scheme Interpreter](https://github.com/hantaowang/schemeinterpreter), and wanted to create my own interpreter independetly. I also wanted to incorporate various computer science principles I had learened. 

pyCalc can evalualte expressions and plot equations on a [-10,10]x[-10,10] graph. It also adheres to the orders of operations. 
