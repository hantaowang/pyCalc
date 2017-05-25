# pyCalc
A simple graphing calculator built on Python

Visit [hantaowang.me/pycalc](http://hantaowang.me/pycalc) to learn more.

#### Try it Out
To run pycalc, you must have [python3](https://www.python.org/download/releases/3.0/) installed along with a command line interpreter such as Terminal or Gitbash. If you are running MacOS, you already have both preinstalled. Download the files and run `python3 interface.py` to begin. 

Alternativetly, use the embedded python shell to on [hantaowang.me/pycalc](http://hantaowang.me/pycalc). However, due to the limitations of the shell, pyCalc runs noticabely slower and functions resulting in complex numbers may not evaluate.

Try expressions such as `5(4)^2+3` and equations such as `f(x)=x^2` or `f(x)=(9-x^2)^0.5`. To clear the graph, enter `clear`.

#### What is pyCalc
For first side project, I was inspired by a class project I did in CS 61A, the [Scheme Interpreter](https://github.com/hantaowang/schemeinterpreter), to create my own interactive interpreter. I also wanted to incorporate various computer science principles I had learened in class. Thus I created pyCalc, an interpreter that computes mathematical expressions and draw functions, much like a graphing calculator can.

pyCalc can evalualte expressions and plot equations on a `[-10,10]x[-10,10]` graph. It also adheres to the orders of operations and size of the graph can be changed in the source code. pyCalc works by using a Read-Evalv-Print Loop (REPL). The Read phase recursively breaks down, or parses, user input into significant bits called tokens, which it assembles into a Tree object based on the order of operations. The Evalv phases traverses each level of the tree and evaluates the nodes from the bottom up. The final solution is then either printed, or graphed.

<img src="https://raw.githubusercontent.com/hantaowang/hantaowang.github.io/master/assets/img/repl.png" /img>

#### More like this
This project was built by Hantao (Will) Wang.
Find out more about me on my [website](hantaowang.me)!
