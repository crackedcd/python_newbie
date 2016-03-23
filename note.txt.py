object:
    int     1234
    long    35L
    float   3.1415
    bool    True False
    str     'spam' "guido's" """n lines"""
    list    [1, [2, 'three'], 4]
    dict    {'food', 'spam', 'taste', 'yum'}
    tuple   (1, 'spam', 4, 'U')

a + b
a - b
a * b
a / b
a % b
-a
+a
a ** b
a < b
a <= b
a > b
a >= b
a == b
a != b
a or b
a and b
not a

>>> "Python mola"[1:4]
'yth'
>>> "Python mola".find("mola")
7
>>> "Python mola".replace("Python", "PHP no")
'PHP no mola'
>>> "Python mola".split(" ")
['Python', 'mola']
>>> " ".join(["Python", "mola"])
'Python mola'

>>> nums = [1, 2, 3]
>>> nums[0]
1
>>> 2 in nums
True
>>> nums.append(4)
>>> nums
[1, 2, 3, 4]
>>> len(nums)
4

>>> user = {'nick': 'cc', 'age': 28}
>>> user.keys()
['nick', 'age']
>>> user.values()
['cc', 28]
>>> user['age']
28
>>> user.get('age', 50)
28
>>> user.get('age_not_exits', 50)
50
>>> user.update({'nick': 'yy', 'age': 28})
>>> user
{'nick': 'yy', 'age': 28}

>>> "%s is like a %s" % ("Life", "boat")
'Life is like a boat'
>>> t = "%(str1)s is like a %(str2)s"
>>> v = {"str1": "Life", "str2": "boat"}
>>> t % v
'Life is like a boat'

>>> int(1.3)
1
>>> int(1.9)
1
>>> float(1 + 2)
3.0
>>> str(1 + 2)
'3'
>>> int(1.1 + 2.3)
3
>>> int(1.1 + 2.2)
3
>>> str(1.1 + 2.2)
'3.3'
>>> float(1.1 + 2.2)
3.3000000000000003

>>> len("Python mola")
11
>>> len([1, 2, 3, 4])
4

>>> type(True)
<type 'bool'>
>>> type("Python Mola")
<type 'str'>

>>> range(5)
[0, 1, 2, 3, 4]
>>> range(5, 10)
[5, 6, 7, 8, 9]
>>> range(1, 10, 2)
[1, 3, 5, 7, 9]

>>> sum([1, 2, 3, 4, 5])
15

>>> a = [1, 2, 3]
>>> b = [4, 5, 6]
>>> zip(a, b)
[(1, 4), (2, 5), (3, 6)]

>>> sorted([5, 1, 3, 2, 4])
[1, 2, 3, 4, 5]

>>> round(3.1415926, 2)
3.14
>>> round(3.1415926, 3)
3.142

>>> int_list = [1, 2, 3, 4, 5]
>>> int_list
[1, 2, 3, 4, 5]
>>> str_list = map(str, int_list)
>>> str_list
['1', '2', '3', '4', '5']
>>> reduce((lambda x, y: x + y), int_list)
15
>>> reduce((lambda x, y: x + y), str_list)
'12345'

>>> dir([1, 2, 3])
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__delslice__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getslice__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__setslice__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> help([1, 2, 3])
Help on list object:

class list(object)
 |  list() -> new empty list
 ...
 ...
 ...


def my_first_function(p1, p2):
    return "Hello, World!"

class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def hello(self):
        return 'My name is %s' % self.name

s = Student("cc", 28)


Dir1/
    __init__.py
    dir_a/
        __init__.py
        a.py
        b.py
    dir_b/
        __init__.py
        c.py
        d.py
    dir_c/
        __init__.py
        e.py
        f.py

from Dir1.dir_b import d
D()
from Dir1 import dir_c
dir_c.e.E()


count = 0
while count < 5:
    print "Number %i" % count
    count += 1

for i in range(4):
    print "Number %i" % count

try:
    result = 3 / 0
except:
    print "Division by Zero"


web_step1:
    HTML
    CGI
web_step2:
    PHP
    ASP
    JSP
web_step3:
    Rails
    Yii
    Yaf
    Django

>>> import django

Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    import django
ImportError: No module named django

D:\Program Files\Python\Python27>python.exe -m pip install django --default-timeout=3600


MVC
Models      数据存取
Views       展示什么、如何展示
Controller  输入访问

Django:
    urls.py -> views.py -> models.py 
       ^          |
       |          v
       ------- *.html 

urls.py: 什么样的url调用什么样的视图
views.py: 函数指明请求的业务层逻辑
    view函数接受HttpRequest请求对象，内部处理后返回HttpResponse对象







浮点数可用科学计数法 1.23x10^9就是1.23e9，0.000012可以写成1.2e-5

字符串可以用单引号或双引号，无区别。
三引号可换行。

\用于转义
r在字符串引号前表示字符串内所有\不表示转义，例如r'\t'实际是'\\t'

布尔可以用and or not关键字计算

空值是None

文件开头加上：
# -*- coding: utf-8 -*-
使得python解释器可以用utf-8编码读取

格式化输出：
'Hi, %s, you have $%d.' % ('Michael', 1000000)
%d整数
%f浮点数
%s字符串
%x十六进制整数
%%表示%

list列表：可变元素的有序集合
classmates = ['Michael', 'Bob', 'Tracy']
追加元素
classmates.append('Adam')
插入元素
classmates.insert(1, 'Jack')
删除元素
classmates.pop()    classmates.pop(1)

tuple元组：不可变元素的有序集合
classmates = ('Michael', 'Bob', 'Tracy')
空tuple
t = ()
1个元素的tuple
t = (1,)

dict字典：k-v存储
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
插入元素
d['Adam'] = 67
删除元素
d.pop('Bob')
一个key只能对应一个value，判断key是否存在
'Thomas' in d    或者    d.get('Thomas')

set集合：自动过滤重复key的k-v存储
s = set([1, 2, 3])
添加元素（重复的会自动过滤）
s.add(4)
删除元素
s.remove(4)
set可用于进行数学的交集并集计算
>>> s1 = set([1, 2, 3])
>>> s2 = set([2, 3, 4])
>>> s1 & s2
set([2, 3])
>>> s1 | s2
set([1, 2, 3, 4])


数据类型转换为整型，使用int()函数

多个变量可以一起赋值
>>> a, b, c, d = 0, 1, 2.2, '3'
>>> print a, b, c, d
0 1 2.2 3

赋值操作可以为函数取别名
>>> a = abs
>>> a(-1)
1

用def定义函数，用return返回
>>> def haha(x, y):
	print "x : %s, y : %s" % (x, y)
>>> haha('hello', 'world')
x : hello, y : world
若不写return，则默认返回为return None，return None也可简写成return

空函数（空语句）使用pass作为占位符

数据类型检查isinstance()
>>> isinstance(1, int)
True
>>> isinstance(1, str)
False
>>> isinstance(1, (int, str))
True

函数可以同时返回多个值，其实返回是一个tuple

函数可以使用默认参数，必选参数在前，默认参数在后

函数定义时默认参数值就会被计算出来，下次调用时会记录，所以默认参数必须指向不变对象，或设置为None并在函数内判断是否为None
错误的例子：
>>> def app_end(L = []):
    L.append('END')
    return L
>>> app_end()
['END']
>>> app_end()
['END', 'END']
>>> app_end()
['END', 'END', 'END']
正确的例子：
>>> def app_end(L = None):
    if L is None:
        L = []
    L.append('END')
    return L
>>> app_end()
['END']
>>> app_end()
['END']
>>> app_end()
['END']

可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))
可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple

关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})
关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict

使用*args和**kw是Python的习惯写法

使用[a:b:c]进行切片，代表从a开始取元素（缺省为0），取到第b个（但不包括b[这里要算上第0个开始], 缺省为len(list)），每隔c个取一个（缺省为0）
tuple和字符串也可以切片，结果的类型仍然不变

创建0-99的数列:
>>> L = range(100)
前10个数：
>>> L[:10]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
后10个数：
>>> L[-10:]
[90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
后10个数的顺序不能倒：
>>> L[-1:-10]
[]
前10个数，每两个取一个：
>>> L[:10:2]
[0, 2, 4, 6, 8]
所有数，每5个取一个：
>>> L[::5]
[0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
>>> 

遍历list或者tuple的过程叫做迭代（iteration）
>>> d = {'a': 1, 'b': 2, 'c': 3}
>>> for key in d:
        print key
a
c
b
dict的存储不是按照list的方式顺序排列！所以结果的顺序可能不一样！

字符串也是可迭代的：
>>> for ch in 'ABC':
        print ch
A
B
C

可通过collections模块的Iterable类型判断对象是否可迭代
from collections import Iterable
>>> isinstance('abc', Iterable)
True
>>> isinstance([1,2,3], Iterable)
True
>>> isinstance(123, Iterable)
False

默认迭代的是key，
若要迭代value，使用for value in d.itervalues()
若要迭代k - v，使用for k, v in d.iteritems()
enumerate可把list变成索引-元素对，实现下标循环：
>>> for i, value in enumerate(['A', 'B', 'C']):
        print i, value
0 A
1 B
2 C

列表生成式 list comprehension
[]

生成 list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> range(1, 11)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

生成 list [1x1, 2x2, 3x3, ..., 10x10]
使用循环
>>> L = []
>>> for x in range(1, 11):
...     L.append(x * x)
... 
>>> L
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
>>> 
或直接使用range生成列表
>>> [x * x for x in range(1, 11)]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

range可以加上判断：
>>> [x * x for x in range(1, 11) if x % 2 == 0]
[4, 16, 36, 64, 100]

range可以使用两层循环：
>>> [m + n for m in 'ABC' for n in 'XYZ']
['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']

利用列表生成式列出目录下所有文件和目录：
>>> import os
>>> [d for d in os.listdir('.')]
['DLLs', 'Doc', 'include', 'Lib', 'libs', 'LICENSE.txt', 'NEWS.txt', 'python.exe', 'pythonw.exe', 'README.txt', 'Scripts', 'tcl', 'Tools', 'w9xpopen.exe']

利用列表生成式使用两个变量来生成list：
>>> d = {'x': 'A', 'y': 'B', 'z': 'C' }
>>> [k + '=' + v for k, v in d.iteritems()]
['y=B', 'x=A', 'z=C']

利用列表生成式处理list元素：
>>> L = ['Hello', 'World', 'IBM', 'Apple']
>>> [s.lower() for s in L]
['hello', 'world', 'ibm', 'apple']
>>> [s.upper() for s in L]
['HELLO', 'WORLD', 'IBM', 'APPLE']
加上判断：
>>> L = ['Hello', 'World', 18, 'Apple', None]
>>> [s.lower() for s in L if isinstance(s, str)]
['hello', 'world', 'apple']

列表容量有限，占用大量存储空间，如果有一定的算法，但不需创建完整list，边循环边计算，则可使用生成器 Generator
将列表生成式的[]改成()，则就是生成器
>>> L = [x * x for x in range(10)]
>>> L
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> G = (x * x for x in range(10))
>>> G
<generator object <genexpr> at 0x01AC2300>

generator对象的元素会在每一次需要的时候才计算，可使用next()方法打印：
>>> G.next()
0
>>> G.next()
1
>>> G.next()
4
>>> G.next()
9
>>> G.next()
16
>>> G.next()
25
......
>>> g.next()
81
>>> g.next()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration

因为generator生成器也是可迭代的，所以也可使用for来循环：
>>> G = (x * x for x in range(10))
>>> for n in G:
	print n
0
1
4
9
16
25
36
49
64
81

!!! yield !!!
yield是一个表达式，包含了yield的函数，就是一个generator
>>> def h():
	print 'haha'
	yield 1
	print 'heihei'
	yield 2
	print 'xixi'

## 得到一个generator
>>> h()
<generator object h at 0x01BFE760>

## 用next()方法调用后，h()开始执行，直到遇到yield 1，输出结果'haha'
>>> a = h()
>>> a = h()
>>> a.next()
haha
1

## 再次使用next()方法，会继续找函数内下一个yield表达式>>> a.next()
>>> a.next()
heihei
2

## 再次next()，由于没有下一个yield了，抛出异常
>>> a.next()
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    a.next()
StopIteration

即，通过yield使函数变成一个"边计算边执行"的generator，再用next()可以"单步"执行：
>>> def h():
	print 1
	yield
	print 2
	yield
	
>>> a = h()
>>> a.next()
1
>>> a.next()
2
>>> a.next()

Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    a.next()
StopIteration

若需要向yield传递值，可使用send(msg)方法，实际上next()方法就是send(None)

>>> def h():
	print 'haha'
	a = yield 1
	print a
	b = yield 2
	print b

## 第一次调用的时候，无法传递msg的值，因为这时还没有yield可以接收msg的内容，会报错
>>> a = h()
>>> a.send('test1')
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    a.send('test1')
TypeError: can not send non-None value to a just-started generator

>>> a.send(None)
haha
1

## 因为上面已经执行了一次send(None)，相当于是一次next()，所以yield 1已经过了，yield 2可以接收msg的内容：
>>> a.send('test2')
test2
2
## 相当于是print b的时候，print了yield 2，因为yield接收了send的'test2'字符串，所以print出test2 2


一个整体generator使用yield的例子：
>>> def h():
	print 'start'
	a = yield '第一个yield生效' # 这里是第一个中断，无法赋值
	print a
	b = yield ' ↑ 这是send()过来的参数' # 可以使用send(msg)把msg传过来了
	print b
	
>>> a = h()
>>> print a.send(None)
start
第一个yield生效
>>> print a.send('传递的msg参数')
传递的msg参数
 ↑ 这是send()过来的参数
>>> 

用yield把函数变成generator生成器来实现一个斐波那契数列吧：
>>> def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
        
>>> for n in fib(6):
	print n
	
1
1
2
3
5
8
>>> 

变量可以指向函数：
>>> abs
<built-in function abs>
>>> f = abs
>>> f
<built-in function abs>
>>> f(-1)
1
即，f是一个变量，它指向一个可以计算绝对值的函数abs。
推论，对于abs()求绝对值函数而言，函数名abs就是一个变量，它指向一个可以计算绝对值的函数。
高阶函数，就是让函数的参数能够接收别的函数。函数式编程就是指这种高度抽象的编程范式。
>>> def add(x, y, f):
	return f(x) + f(y)
>>> add(-1, 1, abs)
2


!!! MapReduce !!!

map()函数接收两个参数，一个是函数，一个是序列，map()将传入的函数依次作用到序列的每个元素
例如要将一个list [1, 2, 3, 4, 5, 6, 7, 8, 9] 全部乘方：
>>> def f(x):
	return x ** 2
>>> L = [1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> map(f, L)
[1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> 

    
reduce()函数接收两个参数，一个是函数，一个是序列，函数必须能接收两个参数，reduce()将结果继续和序列的下一个元素做累积计算
例如要将一个list [1, 2, 3, 4, 5, 6, 7, 8, 9] 全部求和：
>>> def add(x, y):
	return x + y

>>> reduce(add, [1, 3, 5, 7, 9])
25

综合map()和reduce()，一个例子把str转成int：

# 将两字节的str拆分成高位x和低位y，x * 10 + y转成int
def f(x, y):
    return x * 10 + y

# 这时如果用f()函数去reduce一个list，则会挨个将list的元素乘以10，加上下一个元素，再把结果乘以10，加上再下一个元素
'''
即是：
1 * 10 + 2 = 12
12 * 10 + 3 = 123
123 * 10 + 4 = 1234
'''
reduce(f, [1, 2, 3, 4])

# 构造list，使0-9这10个数字分别有字符和数字的对应，即{str : int}
def char2num(s):
    L = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return L[s]

# 这时map(char2num, '13579')，就会将'13579'里的元素挨个执行char2num，也即是将13579挨个转成了int
# 再进行reduce
reduce(f, map(char2num, '1357924680'))

将这些小功能合并起来，其实就可以实现一个str2int函数：
>>> def str2int(s):
        def f(x, y):
            return x * 10 + y
        def char2num(s):
            return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
        return reduce(f, map(char2num, s))

>>> S = '1234567890'
>>> I = str2int(S)
>>> S, I
('1234567890', 1234567890)
>>> 

再来两个例子：
利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']

[root@1 ~/scripts]# cat 1.python 
#!/usr/bin/env python
# coding: utf-8
## 获取用户输入，并格式化成第一位大写，后续小写

from pprint import pprint

def getUserInput():
    userInput = None
    userInputList = []
    while True:
        userInput = raw_input()     # 获取用户输入
        userInputList.append(userInput)     # 可多次输入，拼成List
        if userInput == 'END':      # 输入END时停止
            userInputList.pop()
            break
    return userInputList

def strFormat(s):
    return s[0:1].upper() + s[1:len(s)].lower()     # 第一位取大写，后续位取小写，再字符串拼接

def mapInputList(inputList):
    return map(strFormat, inputList)

pprint(mapInputList(getUserInput()))

[root@1 ~/scripts]# python 1.python
haha
XIXI
hEIhEI
END
['Haha', 'Xixi', 'Heihei']
[root@test1 ~/scripts]# 


sum()函数可以接受一个list并求和，编写一个prod()函数，可以接受一个list并利用reduce()求积
[root@1 ~/scripts]# cat 2.python       
#!/usr/bin/env python
# coding: utf-8
## 利用reduce()求List的积

from pprint import pprint

def prod():
    L = input()     # 用input，因为raw_input()会自动转成字符串，但这里是不完美的，因为输入字符串需要手工输入单引号'，否则会报出语法错误。我还不会try catch，就先这样吧
    if isinstance(L, list):
        return multiReduce(L)
    else:
        return 'Input must be a LIST.'

def multiReduce(L):
    return reduce(multi, L)

def multi(x, y):
    return x * y

result = prod()
pprint(result)
[root@1 ~/scripts]# python 2.python 
[1, 2, 3, 4, 5]
120
[root@1 ~/scripts]# 


filter()用于过滤序列
filter()接收一个函数和一个序列，和map()不同的是，map会把函数依次作用于每个元素，最后取return的结果，但filter()会根据return的值是True或False来决定保留或丢弃元素
例如：
>>> def f(s):
	if s == 'haha':
		return True
	else:
		return False

	
>>> filter(f, ['haha', 'xixi', 'heihei'])
['haha']

# 删除偶数：
>>> def is_odd(n):
	return n % 2 == 1
>>> filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])
[1, 5, 9, 15]

# 删除序列中的空字符串：
# lstrip(rm)会删除字符串左边开始能在rm中匹配到的所有字符，直到不匹配为止
# rstrip(rm)会删除字符串右边开始能在rm中匹配到的所有字符，直到不匹配为止
# strip(rm)会删除字符串两边开始能在rm中匹配到的所有字符，直到不匹配为止
>>> S = '1232233234123223323'
>>> S.lstrip('123')
'4123223323'
>>> S.rstrip('123')
'1232233234'
>>> S.strip('123')
'4'
>>> def not_empty(s):
	return s and s.strip()      
>>> filter(not_empty, ['A', '', 'B', None, 'C', '  '])
['A', 'B', 'C']
>>> 

排序函数sorted()也是一个高阶函数，默认能对数字的list进行从小到大的排序，或对字符串的ascii大小进行排序：
>>> sorted([36, 5, 12, 9, 21])
[5, 9, 12, 21, 36]
>>> sorted(['bob', 'about', 'Zoo', 'Credit'])
['Credit', 'Zoo', 'about', 'bob']

如果要实现字符串倒序，就需要自己实现一个倒序的比较函数，传递给sorted()这个高阶函数，sorted()函数会按自实现的这个比较的return来排序：
>>> def desc_cmp(x, y):
	if x < y:
		return 1
	else:
		return -1
>>> sorted([36, 5, 12, 9, 21], desc_cmp)
[36, 21, 12, 9, 5]

如果要实现忽略大小写的字符串排序，就需要自己实现先把字符串变为全部小写的、再比较的函数，再传递结果给sorted()高阶函数，sorted()会按自实现函数的return结果排序：
>>> def ignore_case_cmp(x, y):
	if x.upper() < y.upper():
		return -1
	else:
		return 1
>>> sorted(['bob', 'about', 'Zoo', 'Credit'], ignore_case_cmp)
['about', 'bob', 'Credit', 'Zoo']


闭包closure：
高阶函数可以将函数作为返回值返回
在一个内部函数里，对在外部函数的变量进行引用，那么内部函数就是一个闭包
例如求和函数
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax
>>> calc_sum(1, 2, 3, 4)
10

再定义一个返回求和函数的函数lazy_sum：
def lazy_sum(*args):
    def calc_sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return calc_sum

调用lazy_sum()时，返回的并非求和的结果而是求和的函数
>>> f = lazy_sum(1, 2, 3, 4)
>>> f
<function calc_sum at 0x01BAC130>
调用函数f时，才真正计算求和的结果
>>> f()
10

利用闭包，可以实现将某变量当成"函数配置"的功能，以此对函数进行加工处理，生成一个"功能增强版"的函数：
$ python closure.py
outter number is: 100
inner number is: 20
120
[yuchao@test1 ~/scripts]$ cat closure.py 
#!/usr/bin/env python
# coding: utf-8

def plusOutter(outterNum):
    print "outter number is:", str(outterNum)

    # this is a CLOSURE function
    def plusInner(innerNum):
        print "inner number is:", str(innerNum)
        return innerNum + outterNum

    # return the CLOSURE function, not the calc result
    return plusInner

v1 = plusOutter(100)

print v1(20)
[yuchao@test1 ~/scripts]$ python closure.py
outter number is: 100
inner number is: 20
120

闭包重要的一点是，闭包的返回函数并不会立即执行，而是直到调用时才会执行



匿名函数lambda：
lambda可以用来定义一个匿名函数，因为没有函数名，所以不会有函数名冲突
lambda使用"lambda 参数: 表达式"来定义，例如
f(x) = x^2，可以用匿名函数表达成lambda x: x * x
偶数数列，可以用你们函数表达成map(lambda x: x * 2, range(1, 10))


    
时间模块datetime：
日期    datetime.date
时间    datetime.time
日期时间    datetime.datetime
时间间隔    datetime.timedelta
时区    datetime.tzinfo

class datetime.date(year, month, day)
date.max、date.min：date对象所能表示的最大、最小日期；
date.resolution：date对象表示日期的最小单位。这里是天；
date.today()：返回一个表示当前本地日期的date对象；
date.fromtimestamp(timestamp)：根据给定的时间戳，返回一个date对象；
date.weekday()：返回weekday，如果是星期一，返回0；如果是星期2，返回1，以此类推；
data.isoweekday()：返回weekday，如果是星期一，返回1；如果是星期2，返回2，以此类推；
date.isocalendar()：返回格式如(year，month，day)的元组；
date.isoformat()：返回格式如'YYYY-MM-DD'的字符串；
date.strftime(fmt)：自定义格式化字符串("%Y-%m-%d %H:%M:%S")
time.hour、time.minute、time.second、time.microsecond：时、分、秒、微秒；
time.tzinfo：时区信息；
time.isoformat()：返回型如"HH:MM:SS"格式的字符串表示；
time.strftime(fmt)：返回自定义格式化字符串("%Y-%m-%d %H:%M:%S")
datetime.utcfromtimestamp(timestamp)：根据时间戮创建一个datetime对象；
datetime.combine(date, time)：根据date和time，创建一个datetime对象；
datetime.strptime(date_string, format)：将格式字符串转换为datetime对象；
datetime.strftime(fmt)：自定义格式化字符串("%Y-%m-%d %H:%M:%S")
%a 星期的简写。如 星期三为Web
%A 星期的全写。如 星期三为Wednesday
%b 月份的简写。如4月份为Apr
%B月份的全写。如4月份为April 
%c:  日期时间的字符串表示。（如： 04/07/10 10:43:39）
%d:  日在这个月中的天数（是这个月的第几天）
%f:  微秒（范围[0,999999]）
%H:  小时（24小时制，[0, 23]）
%I:  小时（12小时制，[0, 11]）
%j:  日在年中的天数 [001,366]（是当年的第几天）
%m:  月份（[01,12]）
%M:  分钟（[00,59]）
%p:  AM或者PM
%S:  秒（范围为[00,61]，为什么不是[00, 59]，参考python手册~_~）
%U:  周在当年的周数当年的第几周），星期天作为周的第一天
%w:  今天在这周的天数，范围为[0, 6]，6表示星期天
%W:  周在当年的周数（是当年的第几周），星期一作为周的第一天
%x:  日期字符串（如：04/07/10）
%X:  时间字符串（如：10:43:39）
%y:  2个数字表示的年份
%Y:  4个数字表示的年份
%z:  与utc时间的间隔 （如果是本地时间，返回空字符串）
%Z:  时区名称（如果是本地时间，返回空字符串）
%%:  %% => %
>>> today = datetime.date.today()
>>> yesterday = today - datetime.timedelta(days=1)
>>> tomorrow = today + datetime.timedelta(days=1)
>>> today
datetime.date(2015, 3, 23)
>>> yesterday
datetime.date(2015, 3, 22)
>>> tomorrow
datetime.date(2015, 3, 24)
>>> n = datetime.datetime.now()
>>> nn = n - datetime.timedelta(minutes=5)
>>> nnn = n + datetime.timedelta(hours=5)
>>> n.strftime("%Y-%m-%d %H:%M:%S")
'2015-03-23 17:37:38'
>>> nn.strftime("%Y-%m-%d %H:%M:%S")
'2015-03-23 17:32:38'
>>> nnn.strftime("%Y-%m-%d %H:%M:%S")
'2015-03-23 22:37:38'
    


装饰器：
因为函数就是对象，对象可以赋值，所以可以通过赋值的变量调用函数：
>>> def now():
	print datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	
>>> now()
2015-03-23 17:42:11
>>> f = now
>>> f()
2015-03-23 17:42:25

通过装饰器Decorator，我们可以增强now()函数的功能，但不修改now()函数的定义，
实现一个log函数打印函数名，通过函数对象的__name__属性可以取到函数名：
def log(func):
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper

>>> now = log(now)
>>> now()
call now():
2015-03-23 18:05:46
>>> 
这里非常复杂，我没有完全看懂，我的理解是：
由于log()是一个decorator，返回一个函数，所以，原来的now()函数仍然存在
此时若执行log(now)，表示执行了log，且把now作为func参数传入，执行了wrapper
同时，再将该函数log(now)执行的返回赋值给now，则同名的now变量指向了log(now)，于是调用新的now——即now()——将执行函数log(now)，即在log()函数中返回的wrapper()函数。因此，会先print func的函数名，再通过func(*args, **kw)来执行原本的now()。
但，因为这里执行的新的now实际是通过wrapper执行了旧的now，因此now的函数名被改变了：
>>> now.__name__
'wrapper'
因此，需要在wrapper内部修改wrapper的函数名，例如：
wrapper.__name__ = func.__name__
同样，python内置的functools.wraps可以达到这个功能，@functools.wraps(func)

python可以使用@符号作为装饰器decorator的修饰
参考https://www.python.org/dev/peps/pep-0318/
@dec2
@dec1
def func(arg1, arg2, ...):
    pass
相当于：
def func(arg1, arg2, ...):
    pass
func = dec2(dec1(func))

因此，刚才的now = log(now)，可以改为在原始的now()前修饰log(func)，即：
@log
def now():
    ...

因此，最终完成的装饰器是：
[yuchao@test1 ~/scripts]$ cat logNow.py 
#!/usr/bin/env python
# coding: utf-8

import datetime, functools

# log函数的参数是一个函数名
def log(func):
    # 闭包wrapper函数接受可变参数args和关键字参数kw
    @functools.wraps(func)
    def wrapper(*args, **kw):
        # 通过__name__属性取出函数名
        print 'call %s():' % func.__name__
        # 执行了原始函数并返回，因为参数是*args和**kw，因此wrapper()函数可以接受任意参数的调用
        return func(*args, **kw)
    return wrapper

@log
def now():
    print datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

now()
print 'function now()\'s name is :', now.__name__
[yuchao@test1 ~/scripts]$ python logNow.py 
call now():
2015-03-23 18:26:48
function now()'s name is : now


随机数和随机字符串
import random
import string

#随机整数：
print random.randint(1,50)

#随机选取0到100间的偶数：
print random.randrange(0, 101, 2)

#随机浮点数：
print random.random()
print random.uniform(1, 10)

#随机字符：
print random.choice('abcdefghijklmnopqrstuvwxyz!@#$%^&*()')

#多个字符中选取特定数量的字符：
print random.sample('zyxwvutsrqponmlkjihgfedcba', 5)

#多个字符中选取特定数量的字符组成新字符串：
string.join(random.sample(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'], 10)).replace(' ', '')

#随机选取字符串：
print random.choice(['剪刀', '石头', '布'])

#打乱排序
items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print random.shuffle(items)



正则：
re.match    从字符串的开始匹配一个模式，若开始就不匹配，则直接返回None
            re.match(pattern, string, flags)
            第一个参数是正则表达式，如果匹配成功，则返回一个Match，否则返回一个None；regex贪婪匹配，regex?非贪婪匹配
            第二个参数表示要匹配的字符串；
            第三个参数是标识位，re.M多行模式，re.S点任意匹配模式

re.search   找到第一个匹配就返回，若开始不匹配，就直到找到匹配为止            
            re.search(pattern, string, flags)

re.sub      替换匹配的表达式
            re.sub(pattern, repl, string, count)

re.findall  获取所有匹配的字符串

re.compile  将正则表达式编译成一个正则表达式对象，可提高效率


#!/usr/bin/env python
# coding: utf-8

import re

mobileNum = '18611112222'

mHideObj = re.match(r'^(\d{3})(\d{4})(\d{4})$', mobileNum) 

print 'python regexp is :', '\'^(\d{3})(\d{4})(\d{4})$\''

print "element 0 (the Full String) :", mHideObj.group(0)
print "element 1 :", mHideObj.group(1)
print "element 2 :", mHideObj.group(2)
print "element 3 :", mHideObj.group(3)

mHideStr = "".join([mHideObj.group(1), '****', mHideObj.group(3)])

print "regexp result is :", mHideStr


python使用"未来的功能"
__future__ 模块
例如：
在Python 2.7的代码中直接使用Python 3.x的除法
>>> 10 / 3
3.3333333333333335
>>> 10.0 / 3
3.3333333333333335
>>> from __future__ import division
>>> print '10 / 3 =', 10 / 3
10 / 3 = 3.33333333333
>>> print '10.0 / 3 =', 10.0 / 3
10.0 / 3 = 3.33333333333
>>> print '10 // 3 =', 10 // 3
10 // 3 = 3



面向对象编程
采用面向对象的程序设计思想，我们首选思考的不是程序的执行流程，而是数据类型应该被视为一个对象，这个对象拥有属性。
首先必须创建出这个对应的对象，然后，给对象发消息，让对象自己把自己的数据打印出来。
数据封装、继承和多态是面向对象的三大特点。


在Python中，定义类是通过class关键字，类名通常是大写开头的单词。
(object)表示该类是从哪个类继承下来的：
class Student(object):
    pass

创建实例是通过类名+()实现的：
bart = Student()

可以自由地给一个实例变量绑定属性，比如，给实例bart绑定一个name属性：
>>> bart.name = 'Bart Simpson'
>>> bart.name
'Bart Simpson'

通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属性绑上去：
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

__init__方法的第一个参数永远是self，表示创建的实例本身，因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。

>>> bart = Student('Bart Simpson', 59)
>>> bart.name
'Bart Simpson'
>>> bart.score
59

面向对象编程的一个重要特点就是数据封装。
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def print_score(self):
        print '%s: %s' % (self.name, self.score)

>>> bart.print_score()
Bart Simpson: 59


实例的变量名如果以双下划线__开头，就变成了一个私有变量（private）
class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score
    def print_score(self):
        print '%s: %s' % (self.__name, self.__score)

这样的变量，外部是无法访问的，需要给Student类增加get_name和get_score方法

同时双下划线开头和结尾的，是特殊变量，能够直接访问，不是private，要避免使用这样的变量名。

判断对象类型，使用type()函数或isinstance()函数
>>> type(123)
<type 'int'>
>>> type('str')
<type 'str'>
>>> type(None)
<type 'NoneType'>

>>> import types
>>> type('abc')==types.StringType
True
>>> type(u'abc')==types.UnicodeType
True
>>> type([])==types.ListType
True
>>> type(str)==types.TypeType
True

>>> type(int)==type(str)==types.TypeType
True

>>> isinstance('a', str)
True
>>> isinstance(u'a', unicode)
True
>>> isinstance('a', unicode)
False

>>> isinstance('a', (str, unicode))
True
>>> isinstance(u'a', (str, unicode))
True

>>> isinstance(u'a', basestring)
True

使用dir()函数获得一个对象的所有属性和方法
也可以在自己的对象中定义dir()可以看到的方法
>>> class MyObject(object):
...     def __len__(self):
...         return 100
...
>>> obj = MyObject()
>>> len(obj)
100

getattr()、setattr()以及hasattr()可以直接操作一个对象的状态
>>> hasattr(obj, 'x') # 有属性'x'吗？
True
>>> obj.x
9
>>> hasattr(obj, 'y') # 有属性'y'吗？
False
>>> setattr(obj, 'y', 19) # 设置一个属性'y'
>>> hasattr(obj, 'y') # 有属性'y'吗？
True
>>> getattr(obj, 'y') # 获取属性'y'
19
>>> obj.y # 获取属性'y'
19

传入一个default参数，如果属性不存在，就返回默认值：
>>> getattr(obj, 'z', 404) # 获取属性'z'，如果不存在，返回默认值404
404

>>> hasattr(obj, 'power') # 有属性'power'吗？
True
>>> getattr(obj, 'power') # 获取属性'power'
<bound method MyObject.power of <__main__.MyObject object at 0x108ca35d0>>
>>> fn = getattr(obj, 'power') # 获取属性'power'并赋值到变量fn
>>> fn # fn指向obj.power
<bound method MyObject.power of <__main__.MyObject object at 0x108ca35d0>>
>>> fn() # 调用fn()与调用obj.power()是一样的
81


使用@property装饰器可以把方法变成属性调用形式：
把一个getter方法变成属性，只需要加上@property，
然后对类定义一个setter方法@[property].setter，
只定义getter方法，不定义setter方法就是一个只读属性。
例如：
[yuchao@test1 ~/scripts/test]$ cat score.py
#!/usr/bin/env python
# coding: utf-8

class Student(object):

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self.__score = value

    @property
    def ifPass(self):
        if not isinstance(self.__score, int):
            raise ValueError('score must be an integer!')
        if self.__score < 0 or self.__score > 100:
            raise ValueError('score must between 0 ~ 100!')
        if self.__score > 59:
            return 'pass', self.__score
        if self.__score < 60:
            return 'not pass', self.__score

s = Student()
s.score = 90
print s.score
print s.ifPass

s.score = 30
print s.score
print s.ifPass

[yuchao@test1 ~/scripts/test]$ python score.py 
90
('pass', 90)
30
('not pass', 30)


多重继承Mixin
class 动物()
class 哺乳类(动物)
class 鸟类(动物)
class 能飞类(动物)
class 能跑类(动物)
class 蝙蝠(哺乳类, 能飞类)
class 狗(哺乳类, 能跑类)
class 鸽子(鸟类, 能飞类)
class 鸵鸟(鸟类, 能跑类)


__str__
__str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串
class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name=%s)' % self.name
    __repr__ = __str__

__iter__
方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的next()方法拿到循环的下一个值
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def next(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100000: # 退出循环的条件
            raise StopIteration();
        return self.a # 返回下一个值

__getitem__
按照下标取出元素
class Fib(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a
若要实现切片，__getitem__()传入的参数可能是一个int，也可能是一个切片对象slice，所以要做判断：
class Fib(object):
    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L
>>> f = Fib()
>>> f[0:5]
[1, 1, 2, 3, 5]
>>> f[:10]
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

__getattr__
动态返回一个属性
[yuchao@test1 ~/scripts/test]$ cat score.py 
#!/usr/bin/env python
# coding: utf-8

class Student(object):
    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, attr):
        if attr == 'score':
            return 99
        if attr == 'getage':
            return lambda: 25
        return 80

s = Student()
print s.name
print s.score
print s.getage()
print s.haha

这个类中并没有score属性，当实例尝试去调用不存在的score属性时，解释器会尝试调用__getattr__(self, 'score')，这样就可以返回score的值
也可以使用lambda函数来直接返回函数，调用方式变成s.function()
[yuchao@test1 ~/scripts/test]$ python score.py 
Michael
99
25
80

__call__
对实例进行调用
[yuchao@test1 ~/scripts/test]$ cat name.py 
#!/usr/bin/env python
# coding: utf-8

class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)

s = Student('cc')
print s
s()
[yuchao@test1 ~/scripts/test]$ python name.py 
<__main__.Student object at 0x2ba57b4b8e90>
My name is cc.


type()函数可以查看一个类型或变量的类型
[yuchao@test1 ~/scripts/test]$ cat h.py
#!/usr/bin/env python
# coding: utf-8
class Hello(object):
    def hello(self, name='world'):
        print('Hello, %s.' % name)

[yuchao@test1 ~/scripts/test]$ cat go.py 
#!/usr/bin/env python
# coding: utf-8
from h import Hello
h = Hello()
h.hello()
print(type(Hello))
print(type(h))

[yuchao@test1 ~/scripts/test]$ python go.py 
Hello, world.
<type 'type'>
<class 'h.Hello'>

Hello是一个class，它的类型就是type，而h是一个实例，它的类型就是class Hello
通过type()可以动态创建类，例如：
def fn(self, name='world'): # 先定义函数
    print('Hello, %s.' % name)
Hello = type('Hello', (object,), dict(hello=fn)) # 创建Hello class
与上面的class Hello(obj)等价

type()函数依次传入3个参数：
1. class的名称；
2. 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
3. class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。


错误和异常处理
格式：
try:
    print 'try...'
    r = 10 / int('a')
    print 'result:', r
except ValueError, e:
    print 'ValueError:', e
except ZeroDivisionError, e:
    print 'ZeroDivisionError:', e
else:
    print 'no error!'
finally:
    print 'finally...'
print 'END'
错误可以跨越多个调用的层次被捕获

用assert替代print进行调试：
[yuchao@test1 ~/scripts/test]$ cat err.py 
#!/usr/bin/env python
# coding: utf-8
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n
def main():
    foo('0')
main()
执行时可以用python -O err.py抑制assert的输出

用logging可以不抛出错误，并且输出到文件：
[yuchao@test1 ~/scripts/test]$ cat log.py 
#!/usr/bin/env python
# coding: utf-8
import logging
logging.basicConfig(level=logging.DEBUG)  ## debug, info, warning, error
s = '0'
n = int(s)
logging.info('n = %d' % n)
print 10 / n

[yuchao@test1 ~/scripts/test]$ python log.py 
INFO:root:n = 0
Traceback (most recent call last):
  File "log.py", line 10, in <module>
    print 10 / n
ZeroDivisionError: integer division or modulo by zero

使用pdb调试：
python -m pdb err.py
l           打印代码执行到的步骤
p 变量      打印变量的值
n           下一步
如果不在执行时指定python -m pdb，也可以在代码中某处添加pdb.set_trace()，代码指定到此处会自动暂停进入pdb，使用c继续执行


文件读写
f = open('File.txt', 'r')
f.close
'r'：只读（缺省。如果文件不存在，则抛出错误）
'w'：只写（如果文件不存在，则自动创建文件）
'a'：附加到文件末尾
'r+'：读写
'rb'：二进制读

也可以使用codecs直接读成某种编码：
import codecs
with codecs.open('/Users/michael/gbk.txt', 'r', 'utf-8') as f:
    f.read() # u'\u6d4b\u8bd5'


操作文件和目录
import os
# 操作系统名字
os.name
os.uname()
# 系统环境变量, dict
os.environ
# 获取具体的环境变量值, 即取environ dict的对象
os.getenv()
# 查看当前目录的绝对路径:
os.path.abspath('.')
# 创建目录，因为mkdir是绝对路径，所以需要先拼出绝对路径，使用os.path.join可以正确处理不同操作系统的路径分隔符/和\
mydir = os.path.join('/home/yuchao', 'testdir')
os.mkdir(mydir)
os.rmdir(mydir)
# 拆分路径也是类似，需要通过os.path.split()处理不同的路径分隔符，第一部分是路径，第二部分是相对的最后级别的目录或文件
>>> s = os.path.split('home/yuchao/testdir/file.txt')
>>> print s
('home/yuchao/testdir', 'file.txt')
# 取得文件后缀名
os.path.splitext('/home/yuchao/testdir/file.txt')
# 重命名
os.rename('test.txt', 'test.py')
# 删除文件
os.remove('test.py')

python.os原本是不支持复制文件操作的，需要引用shutil模块
import shutil
shutil.copyfile()

例子：
列出当前目录的目录：
[x for x in os.listdir('.') if os.path.isdir(x)]
列出当前目录下的所有.py文件
[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']

例子，find . -type f -name "*xxx*"

[yuchao@test1 ~/scripts/test]$ tree .
.
|-- 1
|   |-- test1
|   |-- test2
|   |-- test3
|   |-- tst1
|   |-- tst2
|   `-- tst3
|-- 2
|   `-- test2
|-- 3
|-- file.py
`-- test.txt

3 directories, 9 files
[yuchao@test1 ~/scripts/test]$ find . -type f -name "*test*"
./test.txt
./1/test1
./1/test2
./1/test3
./2/test2


序列化
变量从内存中变成可存储或传输的过程称为序列化，python中称为pickling
变量内容从序列化的对象重新读到内存里称为反序列化，python中称为unpickling

cPickle | pickle
两个模块功能一样，cPickle是c写的，效率高，pickle是python写的，效率低
try:
    import cPickle as pickle
except ImportError:
    import pickle

# pickle.dumps()方法把任意对象序列化成一个str
d = dict(name='Bob', age=20, score=88)
pickle.dumps(d)
# 写到文件
f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()
# 读文件，反序列化
f = open('dump.txt', 'rb')
d = pickle.load(f)
f.close()
d


python的json序列化
json类型        python类型
{}              dict
[]              list
"string"	    'str' 或 u'unicode'
1234.56	        int 或 float
true/false	    True/False
null	        None

# json.loads方法能把json转换成python内置数据结构，json.dumps反之
import json
json.dumps(json.loads(jsondata))
# dummps()方法把python对象写到str，dump()方法可以直接把JSON写入一个file-like Object
# loads()方法把JSON的字符串反序列化，load()方法从file-like Object中读取字符串并反序列化
>>> import json
>>> d = dict(name='Bob', age=20, score=88)
>>> json.dumps(d)
'{"age": 20, "score": 88, "name": "Bob"}'
>>> json_str = '{"age": 20, "score": 88, "name": "Bob"}'
>>> json.loads(json_str)
{u'age': 20, u'score': 88, u'name': u'Bob'}

# python的dict对象可以直接转换成json的{}，但一般使用class对象定义类，再进行json序列化
# 即是先定义类，类里实现方法将实例转换成dict，再序列化成json
[yuchao@test1 ~/scripts/test]$ cat pickling.py       
#!/usr/bin/env python
# coding: utf-8
import json
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
s = Student('Bob', 20, 88)
def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }
print(json.dumps(s, default=student2dict))
[yuchao@test1 ~/scripts/test]$ python pickling.py 
{"age": 20, "score": 88, "name": "Bob"}



多进程 multiprocessing
fork()系统调用会返回两次，在子进程永远返回0，在父进程返回子进程的id，子进程通过getppid()获取父进程的id

[yuchao@test1 ~/scripts/test]$ cat multiprocessing.py 
#!/usr/bin/env python
# coding: utf-8
# multiprocessing.py
import os
# 现在还是一个进程，打印当前进程的pid
print 'Process (%s) start...' % os.getpid()
# 现在也还是一个进程
pid = os.fork()
# 到这里变成了两个进程，父进程fork()了一个子进程，两个进程分别执行
# 父进程和子进程都会分别执行下面的代码
# fork()在子进程的返回值是0，所以子进程的执行会进入 pid == 0 的分支
if pid == 0:
    print 'I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid())
# fork()在父进程的返回值是子进程的pid，所以父进程的执行会进入else
else:
    print 'I (%s) just created a child process (%s).' % (os.getpid(), pid)
# 这里来验证一下确实是执行了两次（分别在父进程和子进程各一次）
print 'processing executed.'

[yuchao@test1 ~/scripts/test]$ python multiprocessing.py
Process (341) start...
I am child process (342) and my parent is 341.
processing executed.
I (341) just created a child process (342).
processing executed.

multiprocessing模块提供了一个Process子模块来代表一个进程对象，创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例，用start()方法启动
# 启动一个子进程并等待其结束
[yuchao@test1 ~/scripts/test]$ cat process.py 
#!/usr/bin/env python
# coding: utf-8
from multiprocessing import Process
import os
def run_proc(name):
    print 'Run child process %s (%s)...' % (name, os.getpid())
if __name__=='__main__':
    print 'Parent process %s.' % os.getpid()
    p = Process(target=run_proc, args=('test',))
    print 'Process will start.'
    p.start()
    # join()方法可以等待子进程结束后再继续往下运行，用于进程同步
    p.join()
    print 'Process end.'
[yuchao@test1 ~/scripts/test]$ python process.py 
Parent process 18896.
Process will start.
Run child process test (18897)...
Process end.

# 使用multiprocessing模块的Pool类，通过进程池批量创建子进程
[yuchao@test1 ~/scripts/test]$ cat pool.py 
#!/usr/bin/env python
# coding: utf-8
from multiprocessing import Pool
import os, time, random
def long_time_task(name):
    print 'Run task %s (%s)...' % (name, os.getpid())
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print 'Task %s runs %0.2f seconds.' % (name, (end - start))
if __name__ == '__main__':
    print 'Parent process %s.' % os.getpid()
    # Pool()的参数可以设定同时跑几个进程
    p = Pool()
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print 'Waiting for all subprocesses done...'
    # 在join()之前，必须先调用close()，在close()之后就不能继续添加新的Process了
    p.close()
    # 用Pool对象调用的join()方法会等待所有子进程执行完毕
    p.join()
    print 'All subprocesses done.'
[yuchao@test1 ~/scripts/test]$ python pool.py 
Parent process 19564.
Waiting for all subprocesses done...
Run task 0 (19565)...
Run task 1 (19566)...
Task 0 runs 0.89 seconds.
Run task 2 (19565)...
Task 2 runs 0.14 seconds.
Run task 3 (19565)...
Task 1 runs 2.40 seconds.
Run task 4 (19566)...
Task 3 runs 1.62 seconds.
Task 4 runs 1.38 seconds.
All subprocesses done.

multiprocessing的Queue、Pipes等可以用于进程通信
# 以Queue为例，在父进程中创建两个子进程，一个往Queue里写数据，一个从Queue里读数据
[yuchao@test1 ~/scripts/test]$ cat queue.py    
#!/usr/bin/env python
# coding: utf-8
from multiprocessing import Process, Queue
import os, time, random
# 写数据进程执行的代码:
def write(q):
    for value in ['A', 'B', 'C']:
        print 'Put %s to queue...' % value
        q.put(value)
        time.sleep(random.random())
# 读数据进程执行的代码:
def read(q):
    while True:
        value = q.get(True)
        print 'Get %s from queue.' % value
if __name__=='__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()
[yuchao@test1 ~/scripts/test]$ python queue.py
Put A to queue...
Get A from queue.
Put B to queue...
Get B from queue.
Put C to queue...
Get C from queue.


多线程 threading
# 启动一个线程就是把一个函数传入并创建Thread实例，然后调用start()开始执行
# current_thread()函数返回当前线程的实例
[root@test1 ~/scripts/test]# cat th.py      
#!/usr/bin/env python
# coding: utf-8
import time, threading
# 新线程执行的代码:
def loop():
    print 'thread %s is running...' % threading.current_thread().name
    n = 0
    while n < 5:
        n = n + 1
        print 'thread %s >>> %s' % (threading.current_thread().name, n)
        time.sleep(1)
    print 'thread %s ended.' % threading.current_thread().name

print 'thread %s is running...' % threading.current_thread().name
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print 'thread %s ended.' % threading.current_thread().name
[root@test1 ~/scripts/test]# python th.py
thread MainThread is running...
thread LoopThread is running...
thread LoopThread >>> 1
thread LoopThread >>> 2
thread LoopThread >>> 3
thread LoopThread >>> 4
thread LoopThread >>> 5
thread LoopThread ended.
thread MainThread ended.

多线程和多进程最大的不同在于，多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响，而多线程中，所有变量都由所有线程共享，所以，任何一个变量都可以被任何一个线程修改，因此，线程之间共享数据最大的危险在于多个线程同时改一个变量
# 线程锁
balance = 0
lock = threading.Lock()
def run_thread(n):
    for i in range(100000):
        # 先要获取锁:
        lock.acquire()
        try:
            # 修改:
            change_it(n)
        finally:
            # 修改完了释放锁:
            lock.release()

Python解释器执行代码存在Global Interpreter Lock -- GIL锁
线程执行前，必须先获得GIL锁，每执行100条字节码，解释器就自动释放GIL锁，让别的线程有机会执行。GIL全局锁实际上把所有线程的执行代码都给上了锁，因此多线程在Python中只能交替执行，即使100个线程跑在100核CPU上，也只能用到1个核。
因此，Python的多线程不能实现多核任务，只能通过多进程实现多核任务。

multiprocessing的managers模块可以将多进程分布到多台机器上，无需了解网络通信的细节
[root@test1 ~/scripts/test]# cat taskmanager.py       
#!/usr/bin/env python
# coding: utf-8
import random, time, Queue
from multiprocessing.managers import BaseManager
# 发送任务的队列:
task_queue = Queue.Queue()
# 接收结果的队列:
result_queue = Queue.Queue()
# 从BaseManager继承的QueueManager:
class QueueManager(BaseManager):
    pass
# 把两个Queue都注册到网络上, callable参数关联了Queue对象:
QueueManager.register('get_task_queue', callable=lambda: task_queue)
QueueManager.register('get_result_queue', callable=lambda: result_queue)
# 绑定端口5000, 设置验证码'abc':
manager = QueueManager(address=('', 5000), authkey='abc')
# 启动Queue:
manager.start()
# 获得通过网络访问的Queue对象:
task = manager.get_task_queue()
result = manager.get_result_queue()
# 放几个任务进去:
for i in range(10):
    n = random.randint(0, 10000)
    print('Put task %d...' % n)
    task.put(n)
# 从result队列读取结果:
print('Try get results...')
for i in range(10):
    r = result.get(timeout=60)
    print('Result: %s' % r)
# 关闭:
manager.shutdown()
[root@test1 ~/scripts/test]# cat taskworker.py       
#!/usr/bin/env python
# coding: utf-8

import time, sys, Queue
from multiprocessing.managers import BaseManager

# 创建类似的QueueManager:
class QueueManager(BaseManager):
    pass

# 由于这个QueueManager只从网络上获取Queue，所以注册时只提供名字:
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

# 连接到服务器，也就是运行taskmanager.py的机器:
server_addr = '127.0.0.1'
print('Connect to server %s...' % server_addr)
# 端口和验证码注意保持与taskmanager.py设置的完全一致:
m = QueueManager(address=(server_addr, 5000), authkey='abc')
# 从网络连接:
m.connect()
# 获取Queue的对象:
task = m.get_task_queue()
result = m.get_result_queue()
# 从task队列取任务,并把结果写入result队列:
for i in range(10):
    try:
        n = task.get(timeout=1)
        print('run task %d * %d...' % (n, n))
        r = '%d * %d = %d' % (n, n, n*n)
        time.sleep(1)
        result.put(r)
    except Queue.Empty:
        print('task queue is empty.')
# 处理结束:
print('worker exit.')
[root@test1 ~/scripts/test]# python taskmanager.py 
Put task 9959...
Put task 3200...
Put task 9188...
Put task 9585...
Put task 2819...
Put task 5450...
Put task 4497...
Put task 6639...
Put task 9636...
Put task 4583...
Try get results...
Result: 9959 * 9959 = 99181681
Result: 3200 * 3200 = 10240000
Result: 9188 * 9188 = 84419344
Result: 9585 * 9585 = 91872225
Result: 2819 * 2819 = 7946761
Result: 5450 * 5450 = 29702500
Result: 4497 * 4497 = 20223009
Result: 6639 * 6639 = 44076321
Result: 9636 * 9636 = 92852496
Result: 4583 * 4583 = 21003889
[root@test1 ~/scripts/test]# python taskworker.py 
Connect to server 127.0.0.1...
run task 9959 * 9959...
run task 3200 * 3200...
run task 9188 * 9188...
run task 9585 * 9585...
run task 2819 * 2819...
run task 5450 * 5450...
run task 4497 * 4497...
run task 6639 * 6639...
run task 9636 * 9636...
run task 4583 * 4583...
worker exit.


collections是python内建的集合模块

namedtuple生成带名称的tuple
>>> from collections import namedtuple
>>> Point = namedtuple('Point', ['x', 'y'])
>>> p = Point(1, 2)
>>> p.x
1
>>> p.y
2

deque是队列和栈
>>> from collections import deque
>>> q = deque(['a', 'b', 'c'])
>>> q.append('x')
>>> q.appendleft('y')
>>> q
deque(['y', 'a', 'b', 'c', 'x'])

defaultdict是可以在key不存在时返回默认值的dict
>>> from collections import defaultdict
>>> dd = defaultdict(lambda: 'N/A')
>>> dd['key1'] = 'abc'
>>> dd['key1'] # key1存在
'abc'
>>> dd['key2'] # key2不存在，返回默认值
'N/A'

OrderedDict是key有序的dict
>>> od = OrderedDict()
>>> od['z'] = 1
>>> od['y'] = 2
>>> od['x'] = 3
>>> od.keys() # 按照插入的Key的顺序返回
['z', 'y', 'x']

Counter是简单的计数器
>>> from collections import Counter
>>> c = Counter()
>>> for ch in 'programming':
...     c[ch] = c[ch] + 1
...
>>> c
Counter({'g': 2, 'm': 2, 'r': 2, 'a': 1, 'i': 1, 'o': 1, 'n': 1, 'p': 1})


# base64编码
>>> import base64
>>> base64.b64encode('binary\x00string')
'YmluYXJ5AHN0cmluZw=='
>>> base64.b64decode('YmluYXJ5AHN0cmluZw==')
'binary\x00string'

# "url安全"的base64编码(把+和/分别变成-和_)
>>> base64.b64encode('i\xb7\x1d\xfb\xef\xff')
'abcd++//'
>>> base64.urlsafe_b64encode('i\xb7\x1d\xfb\xef\xff')
'abcd--__'
>>> base64.urlsafe_b64decode('abcd--__')
'i\xb7\x1d\xfb\xef\xff'

# 因为base64会用=补全字节数，但在url和cookie中=有歧义，所以很多base64编码还会去掉=符号，解码需要自己实现
#!/usr/bin/env python
# coding: utf-8
import base64
def safe_b64decode(str):
    # base64编码长度永远是4的倍数
    b64Len = 4
    for equalCount in range(0, b64Len - (len(str) % b64Len)):
        str = ''.join([str, '='])
    return base64.b64decode(str)

s = 'YWJjZA=='
ss = 'YWJjZA'
print base64.b64decode(s)
print safe_b64decode(ss)
[root@test1 ~/scripts/test]# python b.py    
abcd
abcd


struct模块处理str和其他二进制数据类型的转换
struct的pack函数把任意数据类型变成字符串
>>> # >表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数。
>>> import struct
>>> struct.pack('>I', 10240099)
'\x00\x9c@c'
unpack把str变成相应的数据类型
>>> #后面的str依次变为 I：4字节无符号整数 和 H：2字节无符号整数
>>> struct.unpack('>IH', '\xf0\xf0\xf0\xf0\x80\x80')
(4042322160, 32896)


摘要算法hash
# f()对任意长度的数据data计算出固定长度的摘要digest
# 摘要算法不可逆
digest = f(data)

[yuchao@galileo1 ~/scripts/test]$ cat hash.py 
#!/usr/bin/env python
# coding: utf-8
# md5摘要，还可选用其他方法

import hashlib

# 获得hash摘要
md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?')
print md5.hexdigest()

# 可多次update，最终结果和单次一致
md5_multi = hashlib.md5()
md5_multi.update('how to use md5 ')
md5_multi.update('in python hashlib?')
print md5_multi.hexdigest()

[yuchao@galileo1 ~/scripts/test]$ python hash.py 
d26a53750bc40b38b65a520292f69306
d26a53750bc40b38b65a520292f69306


itertools迭代器
itertools模块提供的全部是处理迭代功能的函数，它们的返回值不是list，而是迭代对象，只有用for循环迭代的时候才真正计算

count(p,q) 返回p, p+q, p+2*q, ....
cycle(p)  返回 p[0], p[1],...p[last],p[0],p[1]......
repeat(p, n) 返回 p...p (n times)
chain(p,q..) 把几个参数连接起来
compress(data, selectors)   compress('ABCDEF', [1,0,1,0,1,1]) --> A C E F   
dropwhile(pred, seq)    dropwhile(lambda x: x<5, [1,4,6,4,1]) --> 6 4 1
groupby()
>>> for n, v in itertools.groupby('aaabbbb ccc aaaaa'):
	print n, list(v)
a ['a', 'a', 'a']
b ['b', 'b', 'b', 'b']
  [' ']
c ['c', 'c', 'c']
  [' ']
a ['a', 'a', 'a', 'a', 'a']
ifilter(pred, seq)      ifilter(lambda x: x%2, range(10)) --> 1 3 5 7 9
ifilterfalse(pred, seq)  ifilterfalse(lambda x: x%2, range(10)) --> 0 2 4 6 8
islice(seq, start, stop, step)     islice('ABCDEFG', 2, None) --> C D E F G
imap(fun, p, q)                    imap(pow, (2,3,10), (5,2,3)) --> 32 9 1000
starmap(fun, seq)                  starmap(pow, [(2,5), (3,2), (10,3)]) --> 32 9 1000
tee(it, n)  将迭代器it复制n份
takewhile(pred, seq)               takewhile(lambda x: x<5, [1,4,6,4,1]) --> 1 4
izip(p,q,...)                      izip('ABCD', 'xy') --> Ax By
izip_longest(p,q,...)              izip_longest('ABCD', 'xy', fillvalue='-') --> Ax ByC- D-
product(p,q,...)                    笛卡尔积
permutations(seq, r)              permutations('ABCD', 2) -->AB AC AD BA BC BD CA CB CD DA DB DC 
combination(seq, r)                          combinations('ABCD', 2) -->AB AC AD BC BD CD
combinations_with_replacement(seq, r)    combinations_with_replacement('ABCD', 2) -->AA AB AC AD BB BC BD CC CD DD



HTMLParser 解析 HTML 内容
from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print('<%s>' % tag)

    def handle_endtag(self, tag):
        print('</%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('<%s/>' % tag)

    def handle_data(self, data):
        print('data')

    def handle_comment(self, data):
        print('<!-- -->')

    def handle_entityref(self, name):
        print('&%s;' % name)

    def handle_charref(self, name):
        print('&#%s;' % name)

parser = MyHTMLParser()
parser.feed('<html><head></head><body><p>Some <a href=\"#\">html</a> tutorial...<br>END</p></body></html>')


PIL图形处理Python Imaging Library

# 缩放图片
import Image
# 打开一个jpg图像文件，注意路径要改成你自己的:
im = Image.open('/Users/michael/test.jpg')
# 获得图像尺寸:
w, h = im.size
# 缩放到50%:
im.thumbnail((w//2, h//2))
# 把缩放后的图像用jpeg格式保存:
im.save('/Users/michael/thumbnail.jpg', 'jpeg')

# 模糊效果
import Image, ImageFilter
im = Image.open('/Users/michael/test.jpg')
im2 = im.filter(ImageFilter.BLUR)
im2.save('/Users/michael/blur.jpg', 'jpeg')

# 生成验证码
import Image, ImageDraw, ImageFont, ImageFilter
import random
# 随机字母:
def rndChar():
    return chr(random.randint(65, 90))
# 随机颜色1:
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))
# 随机颜色2:
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))
# 240 x 60:
width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
# 创建Font对象:
font = ImageFont.truetype('Arial.ttf', 36)
# 创建Draw对象:
draw = ImageDraw.Draw(image)
# 填充每个像素:
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())
# 输出文字:
for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
# 模糊:
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg');



TCP编程

## 客户端
# 导入socket库:
import socket
# 创建一个socket:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect(('www.sina.com.cn', 80))
# 发送数据:
s.send('GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
# 接收数据:
buffer = []
while True:
    # 每次最多接收1k字节:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = ''.join(buffer)
# 关闭连接:
s.close()
header, html = data.split('\r\n\r\n', 1)
print header
# 把接收的数据写入文件:
with open('sina.html', 'wb') as f:
    f.write(html)

## 服务端
# 创建socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 监听端口:
s.bind(('127.0.0.1', 9999))
# listen(n)，n表示等待连接的最大数量
s.listen(5)
print 'Waiting for connection...'
# 永久循环，接受来自客户端的连接
while True:
    # 接受一个新连接:
    sock, addr = s.accept()
    # 创建新线程来处理TCP连接:
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()
# 每个连接都必须创建新线程（或进程）来处理，否则，单线程在处理连接的过程中，无法接受其他客户端的连接：
def tcplink(sock, addr):
    print 'Accept new connection from %s:%s...' % addr
    sock.send('Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if data == 'exit' or not data:
            break
        sock.send('Hello, %s!' % data)
    sock.close()
    print 'Connection from %s:%s closed.' % addr



电子邮件
MUA：Mail User Agent        邮件用户代理
MTA：Mail Transfer Agent    邮件传输代理
MDA：Mail Delivery Agent    邮件投递代理
邮件从投递方，通过MUA投递到MTA，MTA将邮件传递到MDA，等待收件方的MUA抓取。

# SMTP发送邮件

# Message
# +- MIMEBase
#    +- MIMEMultipart
#    +- MIMENonMultipart
#       +- MIMEMessage
#       +- MIMEText
#       +- MIMEImage

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(( \
        Header(name, 'utf-8').encode(), \
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))

from_addr = raw_input('From: ')
password = raw_input('Password: ')
to_addr = raw_input('To: ')
smtp_server = raw_input('SMTP server: ')

# 利用MIMEMultipart就可以组合一个HTML和Plain
# msg = MIMEMultipart('alternative')
# msg.attach(MIMEText('hello', 'plain', 'utf-8'))
# msg.attach(MIMEText('<html><body><h1>Hello</h1></body></html>', 'html', 'utf-8'))
msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
msg['From'] = _format_addr(u'Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr(u'管理员 <%s>' % to_addr)
msg['Subject'] = Header(u'来自SMTP的问候……', 'utf-8').encode()

# 邮件正文是MIMEText:
msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))

# 添加附件就是加上一个MIMEBase，从本地读取一个图片:
with open('/Users/michael/Downloads/test.png', 'rb') as f:
    # 设置附件的MIME和文件名，这里是png类型:
    mime = MIMEBase('image', 'png', filename='test.png')
    # 加上必要的头信息:
    mime.add_header('Content-Disposition', 'attachment', filename='test.png')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来:
    mime.set_payload(f.read())
    # 用Base64编码:
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart:
    msg.attach(mime)

server = smtplib.SMTP(smtp_server, 25)
# starttls()方法创建安全连接
server.starttls()
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()



MySQL
# 导入MySQL驱动:
>>> import mysql.connector
# 注意把password设为你的root口令:
>>> conn = mysql.connector.connect(user='root', password='password', database='test', use_unicode=True)
>>> cursor = conn.cursor()
# 创建user表:
>>> cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# 插入一行记录，注意MySQL的占位符是%s:
>>> cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
>>> cursor.rowcount
1
# 提交事务:
>>> conn.commit()
>>> cursor.close()
# 运行查询:
>>> cursor = conn.cursor()
>>> cursor.execute('select * from user where id = %s', '1')
>>> values = cursor.fetchall()
>>> values
[(u'1', u'Michael')]
# 关闭Cursor和Connection:
>>> cursor.close()
True
>>> conn.close()


ORM Object-Relational Mapping 把数据库表的行与相应的对象建立关联，互相转换
SQLAlchemy
# pip install sqlalchemy
# 导入:
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'user'

    # 表的结构:
    id = Column(String(20), primary_key=True)
    name = Column(String(20))

# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://root:password@localhost:3306/test')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

# 有了ORM，查询出来的可以不再是tuple，而是User对象
# 创建Session:
session = DBSession()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
user = session.query(User).filter(User.id=='5').one()
# 打印类型和对象的name属性:
print 'type:', type(user)
print 'name:', user.name
# 关闭Session:
session.close()

# 一个User拥有多个Book，可以定义一对多关系如下
class User(Base):
    __tablename__ = 'user'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    # 一对多:
    books = relationship('Book')

class Book(Base):
    __tablename__ = 'book'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    # 多的一方的book表是通过外键关联到user表的:
    user_id = Column(String(20), ForeignKey('user.id'))


python协程gevent
gevent是第三方库，通过greenlet实现协程，其基本思想是：
当一个greenlet遇到IO操作时，比如访问网络，就自动切换到其他的greenlet，等到IO操作完成，再在适当的时候切换回来继续执行。由于IO操作非常耗时，经常使程序处于等待状态，有了gevent为我们自动切换协程，就保证总有greenlet在运行，而不是等待IO。

[root@galileo1 ~/scripts/gevent]# cat t.py 
#!/usr/bin/env python
# coding: utf-8

# gevent需要修改Python自带的一些标准库，这一过程在启动时通过monkey patch完成
from gevent import monkey; monkey.patch_socket()
import gevent

def f(n):
    for i in range(n):
        print gevent.getcurrent(), i
        # gevent.sleep可以交出单个greenlet的控制权
        # gevent.sleep(0)

count = 3

g1 = gevent.spawn(f, count)
g2 = gevent.spawn(f, count)
g3 = gevent.spawn(f, count)
g1.join()
g2.join()
g3.join()
[root@galileo1 ~/scripts/gevent]# python t.py    
<Greenlet at 0x2b0626148d70: f(3)> 0
<Greenlet at 0x2b0626148d70: f(3)> 1
<Greenlet at 0x2b0626148d70: f(3)> 2
<Greenlet at 0x2b06261489b0: f(3)> 0
<Greenlet at 0x2b06261489b0: f(3)> 1
<Greenlet at 0x2b06261489b0: f(3)> 2
<Greenlet at 0x2b0626148e10: f(3)> 0
<Greenlet at 0x2b0626148e10: f(3)> 1
<Greenlet at 0x2b0626148e10: f(3)> 2


一旦产生IO，gevent就会主动切换控制权，无需自己调用gevent.sleep()方法
[root@galileo1 ~/scripts/gevent]# cat u.py 
#!/usr/bin/env python
# coding: utf-8

from gevent import monkey; monkey.patch_all()
import gevent
import urllib2
import datetime

def f(url):
    print('GET: %s' % url)
    resp = urllib2.urlopen(url)
    data = resp.read()
    print('%d bytes received from %s.' % (len(data), url))

def orderCurl():
    orderCurlBegin = datetime.datetime.now()
    f('http://www.qq.com/');
    f('http://www.baidu.com/');
    f('http://so.com/');
    f('http://www.12306.cn/');
    orderCurlEnd = datetime.datetime.now()
    print orderCurlEnd - orderCurlBegin

def geventCurl():
    geventCurlBegin = datetime.datetime.now()
    gevent.joinall([
        gevent.spawn(f, 'http://www.qq.com/'),
        gevent.spawn(f, 'http://www.baidu.com/'),
        gevent.spawn(f, 'http://so.com/'),
        gevent.spawn(f, 'http://www.12306.cn/'),
        ])
    geventCurlEnd = datetime.datetime.now()
    print geventCurlEnd - geventCurlBegin

orderCurl()
geventCurl()

[root@galileo1 ~/scripts/gevent]# python u.py 
GET: http://www.qq.com/
126609 bytes received from http://www.qq.com/.
GET: http://www.baidu.com/
93549 bytes received from http://www.baidu.com/.
GET: http://so.com/
235466 bytes received from http://so.com/.
GET: http://www.12306.cn/
1480 bytes received from http://www.12306.cn/.
0:00:00.521138
GET: http://www.qq.com/
GET: http://www.baidu.com/
GET: http://so.com/
GET: http://www.12306.cn/
1480 bytes received from http://www.12306.cn/.
93674 bytes received from http://www.baidu.com/.
235466 bytes received from http://so.com/.
126609 bytes received from http://www.qq.com/.
0:00:00.184309

从结果可以看出来，并发的效率明显比顺序的效率高很多，
而代码这边只需要先import，再把并发的多个func写成先spawn再join即可。


鸭子类型, 在不使用继承的情况下使用多态:
class Duck:
    def quack(self):
        print("Quaaaaaack!")

class Person:
    def quack(self):
        print("I'm a person, can't quaaack.")

def if_can_quack(someone):
    someone.quack()

def go():
    duck = Duck()
    person = Person()
    if_can_quack(duck)
    if_can_quack(person)

go()

[root@galileo1 ~/scripts/gevent]# python duck.py 
Quaaaaaack!
I'm a person, can't quaaack.




web开发

python的前端模版引擎 jinja2  じんじゃ?  神社?
python的mysql驱动 mysql-connector-python

项目结构
awesome-python-webapp/   <-- 根目录
|
+- backup/               <-- 备份目录
|
+- conf/                 <-- 配置文件
|
+- dist/                 <-- 打包目录
|
+- www/                  <-- Web目录，存放.py文件
|  |
|  +- static/            <-- 存放静态文件
|  |
|  +- templates/         <-- 存放模板文件
|
+- LICENSE               <-- 代码LICENSE


