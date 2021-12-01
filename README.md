## >>> ▶️Python Execution⚙️ <<<
This project is about how a python file is executed. 

---
<pre>
	    compiling
Python-Code --------> CPython-Byte-Code

In Detail:
                 compiling
Python-Code -> AST -> CPython-Byte-Code
</pre>

The Interpreter compiles the Python-Source-Code in a Byte-Code and executes this Byte-Code line by line. The standard interpreter is called CPython.<br>
The compile-step consists of the building of the AST (abstract syntax tree) and the compiling of the AST.<br>
The AST is the Python-Code in a tree-structure.<br>
For a better understanding and a practical use, see the [ast_example.ipynb](./ast_example.ipynb).<br>
<br>
The CPython-Byte-Code can be reading and used for analysis with the dis module (disassemble).<br>
For a short look see the [dis_example.ipynb](./dis_example.ipynb).

---

Here is my [presentation](https://prezi.com/view/auF8RoiBnLPW4IlwHwg0/).

---
### Quellen

- https://pypi.org/project/showast/

- https://www.javatpoint.com/python-ast-module

- https://www.journaldev.com/19243/python-ast-abstract-syntax-tree

- https://kamneemaran45.medium.com/python-ast-5789a1b60300

- https://pybit.es/articles/ast-intro/

- https://greentreesnakes.readthedocs.io/en/latest/tofrom.html

- https://www.mattlayman.com/blog/2018/decipher-python-ast/

- https://tenthousandmeters.com/blog/python-behind-the-scenes-1-how-the-cpython-vm-works/

- https://tenthousandmeters.com/blog/python-behind-the-scenes-6-how-python-object-system-works/

- https://medium.com/analytics-vidhya/no-jargon-behind-the-scenes-of-python-852eb6949b90

- https://youtu.be/9bFvpOFyClI

- https://youtu.be/URNdRl97q_0

- https://youtu.be/arxWaw-E8QQ

- https://youtu.be/QgL6Ace9aJM

- https://youtu.be/VsjJfaUdFO8

- https://youtu.be/_OlNOKg3PpY

- https://youtu.be/AisW8ZhqUuc

- https://youtu.be/-ZPg5lJCln8

- https://tenthousandmeters.com/blog/python-behind-the-scenes-1-how-the-cpython-vm-works/

- https://www.geeksforgeeks.org/understanding-the-execution-of-python-program/

- https://www.geeksforgeeks.org/internal-working-of-python/

- https://www.youtube.com/watch?v=NcaMLIUpjbY

- https://www.youtube.com/watch?v=PJ16cdc0YKM

- https://www.programiz.com/python-programming/methods/built-in/compile

- https://av.tib.eu/media/44977

- https://opensource.com/article/18/4/introduction-python-bytecode

- https://towardsdatascience.com/understanding-python-bytecode-e7edaae8734d

---
