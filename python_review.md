#<center><font size=6>30 Mins Fundamentals of Python Review</font></center>


##<font size=5>‘is’ 运算符与‘==’运算符比较</font>
  - == : 比较两数据结构内容是否相等，调用对象的__eq__()函数
  - is : 比较两个对象的id是否相同，即是否指向同一个内存，也即两对象为同一个实例对象
  - [代码实例](https://www.cnblogs.com/lilz/p/9410319.html)
  - **注意**：
    - 两int数值在[-5，256]范围内，python将不再创建新的对象，而是直接调用
    - 同一个代码块中的不可变对象，只要值是相等的就不会重复创建新的对象。
    - 不能有特殊字符串，全部由字母组成的字符串，否则is返回False
##<font size=5>字符串 str</font>
- 字符串不可变，即创建后不能修改内部内容
- 操作：可用下标及负索引查找，可切片
##<font size=5>格式化输出</font>
    示例表示输出7到10对应的10的指数及其对齐

    #%-3d表示i输出的格式，3表示格式化后即补空格后字段宽度，‘-’负号表示左对齐，d表示整数
    #%14.2f表示10**i输出的格式，右对齐，字段宽14（包含小数位宽），格式化浮点数，精度为2
    #格式化字符串将d替换为s

    for i in range(7,11):
            print("%-3d%14.2f" % (i ,10**i))

    output：
    7     10000000.00
    8    100000000.00
    9   1000000000.00
    10 10000000000.00

##<font size=5>列表 list</font>
- 列表可变，可用切片（切片后为新列表）
- split和join分别拆分字符串和合并list


    oldlist = ['God','Bless','you']
    print(" ".join(oldlist))

    output:
    God Bless you

##<font size=5>元组 tuple</font>
- 元组不可变,两个元组用+连接生成新元组

##<font size=5>字典 dictionary</font>
- 键值对，keys返回键的可迭代对象，values返回字典中值的可迭代对象，for遍历字典的键

##<font size=5>函数参数</font>
- 必需参数一定要放在可选参数前

##<font size=5>高阶函数</font>
- map或者filter
- input:函数，可迭代对象
- 功能：对于可迭代对象中每个元素，都通过该函数的计算处理
- functools.reduce
- 输入两个参数，返回单个参数
- 这两个参数中一个是下一项要参与该函数计算的值和前一次该函数计算的返回值




    #将oldlist中每个元素都转换为对应字符串型
    map(str,oldlist)
    #计算1到5之间累加，其中x为前一次函数返回，y为下一项
    sumlist = functools.reduce(lambda x,y:x+y,range(1,5))

##<font size=5>lambda创建匿名函数</font>
    lambda <argument list> : <experssion>
    lambda x,y : x+y
    #相当于以下函数
    def name(x,y) :
        return x+y
##<font size=5>捕获异常</font>
    def safe(i):
    """如果用户输入不符合要求，强制重复输入，直到输入为正确整数，返回该数"""
        inputstr = input(i)
        try:
            #语句代码块,若其中一条语句引发except中包含的异常类型，则立即执行except语句
            number = int(inputstr)
            return number
        except ValueError: #<用户指定想要捕获并作出相应处理的 异常类型>
            #对捕获到的异常作何反应处理
            print("error in number format:",inputstr)
            #利用类似于递归方式重复输入直到输入符合规定
            return safe(i)
  
##<font size=5>文件及其操作</font> 
    f = open("filename.txt",'w')
    #w:写入文件，其中输入输出都必须为字符串
    f.write(str(number)+"\n")
    #将数字写入文件，先转换为字符串，并两两之间用换行或者空格隔开
    text = f.read()
    #read()将文件内容作为一整个字符串返回，可用for i in f 来一行一行读取
    testline = f.readline()
    #readline()将文件每一行作为一个字符串输出，且每次输出一行
###<font size=5>封装存储 pickle</font> 
    import pickle

    fileobject = open("items.dat","wb")
    #以二进制流方式打开文件

    pickle.dump(item,fileobject)
    #item:存储到文件items.dat中的对象，对于链表等需要把item中单个项循环存储进去，不能一块存储
    #fileobject:目标文件对象

    fileobj = open("items.dat","rb")
    itemo = pickle.load(fileobj)
    #利用try except判断读取文件结束（即出现EOFError异常）
##<font size=5>类 class</font> 
- 调用类变量从类来而不是对象
- 待补充


