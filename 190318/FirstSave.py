Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("Hello Python!")
Hello Python!
>>> print("결과값은",9*18,"입니다.")
결과값은 162 입니다.
>>> print("Hello Python!"*100)
Hello Python!Hello Python!Hello Python!Hello Python!Hello Python!Hello Python!Hello Python!Hello Python!Hello Python!Hello Python!Hello Python!Hello Python!Hello Python!Hello Python!Hello Python!Hello Python!Hello Python!Hello Python!Hello Python!Hello Python!Hello Python!Hello Python!Hello Python!Hello Python!Hello Python!Hello Python!Hello Python!Hello Python!Hello Python!Hello Python!Hello Python!Hello Python!Hello Python!Hello Python!Hello Python!Hello Python!Hello Python!Hello Python!Hello Python!Hello Python!Hello Python!Hello Python!Hello Python!Hello Python!Hello Python!Hello Python!Hello Python!Hello Python!Hello Python!Hello Python!Hello Python!Hello Python!Hello Python!Hello Python!Hello Python!Hello Python!Hello Python!Hello Python!Hello Python!Hello Python!Hello Python!Hello Python!Hello Python!Hello Python!Hello Python!Hello Python!Hello Python!Hello Python!Hello Python!Hello Python!Hello Python!Hello Python!Hello Python!Hello Python!Hello Python!Hello Python!Hello Python!Hello Python!Hello Python!Hello Python!Hello Python!Hello Python!Hello Python!Hello Python!Hello Python!Hello Python!Hello Python!Hello Python!Hello Python!Hello Python!Hello Python!Hello Python!Hello Python!Hello Python!Hello Python!Hello Python!Hello Python!Hello Python!Hello Python!Hello Python!
>>> import turtle
>>> t=turtle.pen()
>>> t.forward(120)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    t.forward(120)
AttributeError: 'dict' object has no attribute 'forward'
>>> t.forward(100)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    t.forward(100)
AttributeError: 'dict' object has no attribute 'forward'
>>> import turtle
>>> t=turtle.Pen()
>>> t.forward(100)
>>> t.right(90)
>>> t.forward(100)
>>> t.left(90)
>>> t.left(90)
>>> t.left(90)
>>> t.forward(100)
>>> t.forward(10)
>>> t.back(5)
>>> t.forward(15)
>>> t.right(90)
>>> t.forward(100)
>>> 
