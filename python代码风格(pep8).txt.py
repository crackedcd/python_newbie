4个空格为一个缩进层次
必须使用四个空格，不使用tab
vim中使用set expandtab，配置空格键替换tab键


每行限制80或72个字符，
1. python支持圆括号、方括号、花括号的行内延续
2. 使用反斜杠换行
3. 字符串换行


顶层函数和类的定义2个空行
类内的方法1个空行
逻辑段落1个空行


文件使用utf-8编码
使用LF换行符\n，而不使用CR换行符\r
文件结束需要一行空行，warning: no newline at the end of file

no!:
    import sys, os
yes!:
    import sys
    import os

不要有多余的空格
no!:
    x             = 1;
    y             = 2;
    long_variable = 3;
yes!:
    x = 1;
    y = 2;
    long_variable = 3;


注释应该是完整句子，修改代码前先修改注释
注释使用三重双引号，跟随代码段落结构缩进
行注释应该至少离开代码2个空格，注释内容与#间需要一个空格

"""
This is groups style docstring. -- Google
Parameters:
    param1 - this is a first param.
    param2 - this is a second param.
Return:
    this is a description of what is returned.
Raises:
    keyError - raises an exception.
"""

"""
This is javadoc style docstring.
@param1: this is a first param.
@param2: this is a second param.
@return: this is a description of what is returned.
@raise keyError: raises an exception.
"""

print 'test'  # This is a print.


TODO注释（非pep8规范，Google）
头处包含TODO字符串
紧跟着用括号括起来名字
可选的冒号
注释说明todo的内容是什么

# TODO(yuchao) Change the world.


命名应杜绝单字母，除非是内部for循环中的计数，使用i, j等
包名和模块名应不含下划线，简短，小写（windows不区分大小写，包会映射成文件夹，模块会映射成文件）
类名使用首字母大写单词串
不想被导入的全局变量、内部函数、类前加一个下划线
函数名小写，使用下划线单词风格
单下划线开头表示模块变量或函数是protected
双下划线开头表示实例变量或方法是类内私有

Type                        Public                          Internal
Modules                     lower_with_under                _lower_with_under
Packages                    lower_with_under
Classes                     CapWords                        _CapWords
Exceptions                  CapWords                        
Functions                   lower_with_under()              _lower_with_under                
Global/Class Constants      CAPS_WITH_UNDER                 _CAPS_WITH_UNDER
Global/Class Variables      lower_with_under                _lower_with_under
Instance Variables          lower_with_under                _lower_with_under(protected)
                                                            __lower_with_under(private)
Method Names                lower_with_under()              _lower_with_under(protected)
                                                            __lower_with_under(private)
Function/Method Parameters  lower_with_under
Local Variables             lower_with_under


BaseException:
    +-- SystemExit
    +-- KeyboardInterrupt
    +-- Exception

no!:
    try:
        pass
    except ValueError:
        raise exception.InvalidIntValue(key=key)
    except Exception:
        print "error occur"

yes!:
    try:
        pass
    except ValueError:
        raise exception.InvalidIntValue(key=key)
    except Exception as e:
        print e
