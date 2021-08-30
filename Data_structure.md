#<center><font size=7>数据结构与算法回顾</font></center>
##<center><font size=7>抽象数据类型</font></center>
- 不可变数据类型：str、tuple、forzenset
- 可变数据类型：list、set、dict
- 数据定义+模块（方法操作）接口实现

### <font size=6>Python类</font>
- __init__（self，相应需要的若干参数）：初始化方法，在构造该类的新对象时自动调用，self表示调用该方法的实例对象
- 以“_”开头的属性名和函数名，约定只有类对象和子类对象可访问，实际上外部对象等可以访问（不能用“from name import *”导入）
- 以“__”开头但`不以其结尾`的属性和函数，私有的，类定义外不能直接用该名字访问，但系统会自动更名，可用更名后的名称变相访问
- [Python 中下划线的 5 种含义](https://www.runoob.com/w3cnote/python-5-underline.html)
- 静态方法：非实例方法（所以无self参数），名字前加@staticmethod，调用方式可从类也可从实例对象来调用
- [Python实例方法、静态方法和类方法详解（包含区别和用法）](http://c.biancheng.net/view/4552.html)
- 算数运算规定特殊方法名：开头和结尾都以“__”为前缀

 

      class Rational:         #构造有理数类，例：有理数3/5
         @staticmethod        #静态方法
         def _gcd(m,n):       #求最大公约数
            if n == 0:
               m, n = n, m
            while m != 0:
               m, n = n%m, m
            return n
         def __init__(self,num,den = 1):
            if not isinstance(num,int) or not isinstance(den,int):
               raise TypeError
            if den == 0:
               raise ZeroDrivaionError
            sign = 1
            if num<0:
               num,sign = -num,-sign
            if den<0:
               den,sign = -den,-sign
            g = Ratioal._gcd(num,den)
            self._num = sign*(num//g)
            self._den = den//g               #“//”为整除，“/”普通除法结果为浮点数

         def num(self): return self._num     #对于内部变量通过实例方法来访问
         def den(self): return self._den

         def __mul__(self,another):
            return (self._num*another.num(),self._den*another.den())

         def __str__(self):
            return str(self._num)+'/'+str(self._den)


- 方法对象和函数对象：方法对象如C类的实例对象p，其中 C 类中定义了 m 函数，则 变量 q = p.m 可用变量 q() 来代替实例方法的调用


      class Countable:
      """统计该类的对象数量"""
         counter = 0                #类似于全局变量
         def __init__(self):
            Countable.counter +=1   #如果改为self.counter,相应的取数改为非类方法，则只能输出1，不能计数
         @classmethod
         def get_count(cls):
            return Countable.counter   #类的数据属性作用域不会延伸到类的函数属性中所以采用圆点类引用方法

#### <font size=5>Python类的继承</font>

- 目的：在子类扩充父类的数据及方法，包括某个方法中功能的扩展


      class Sonclass(Fatherclass,Motherclass):     #该子类对象也为父类对象，即可调用父类方法也可使用子类数据方法
         def __init__(self,sonpars):               #在子类方法中不覆盖父类的方法而拓展
            Fatherclass.__init__(self,fatherpars)  #包含了父类初始化的操作
            Motherclass.__init__(self,motherpars)
            ... #sonclass init process             #子类独有的拓展的初始化操作



- 方法查找 ：子类中有则覆盖父类中的方法，子类中没有该方法就寻找父类中的方法
- 动态约束
  
      class B():
         def f(self):
            self.g()
         def g(self):
            print("B.g")
      class C(B):
         def g(self):
            print("C.g")
      obj = C()
      obj.f()
      #调用C类对象的f函数，但C类没有f函数，沿着继承关系寻找到B类，B类中f函数调用self.g()
      #此时self指C类对象obj，所以调用C类中的g函数
      output:
      C.g


- super()：表示属性直接从父类开始检索，而不是从子类本身开始，可指定参数某个父类及其对象来调用，也可无参数

- 异常流程：发现异常，查找异常处理器，若无则输出异常信息，终止当前执行
- 各异常都为class，每次出现异常则创建对应异常的实例对象

##<center><font size=7>集合</font></center>
- 线性集合：除了开头结尾，其他每项都有唯一的前驱和后继 （列表、队列、栈、字符串）
- 层级集合：除了最顶端外，其他都有唯一一个前驱可能有多个后继（二叉搜索树、堆）
- 图集合：每个都可能有多个前驱和后继
- 无序集合：无序（包、字典、集）
##<center><font size=7>线性表</font></center>

### 顺序表

- 存储时占用连续一大块内存，逻辑关系通过存储的物理地址反映
- 需记录和更新表的最大容量以及现存数量
- 优点：查找O(1)
- 缺点：插入删除操作可能移动之前或之后的其他元素较复杂，固定容量等造成存储满或空
- 表存储满就换一块广大的存储区，把元素一一复制过去，而记录表信息的表头采用链接式

### 链表
- 单链表：单项顺序
- 生成器用法：yield作用相当于return返回一个值，然后停止执行下一条语句并记住这个位置，下一次直接接着这个位置执行

## <center><font size=7>哈希</font></center>
- 哈希为了降低时间复杂度，而采用一种映射，将出现的字符数字等（称为键类似与字典中的键）一一分别映射到内存不同位置中，可以直接查找，时间O(1)
- 哈希技术4个组成部分：哈希表，哈希函数，冲突，冲突解决技术
### 哈希表
- 存放键与对应值的数据结构，根据哈希函数将键映射到对应位置上
- 用空间换取时间
### 哈希函数
- 将键转换为index，键数量如果大于哈希表长度，采用取余操作发生哈希碰撞
![img.png](img.png)
- 哈希碰撞：解决方法有*拉链法*和*线性探测法*
- 拉链法：发生冲突的元素都存储在该索引对应的链表中
- 线性探测法：前提tablesize>datasize，冲突时，从冲突的位置向下寻找一个空位置存储
- 常见哈希结构：set、dic

## <center><font size=7>字符串</font></center>
- python中字符串是不可变型，长度和内容都不可变
- python中字符串采用一体式存储，表头记录长度以及其他管理信息
- 通配符：*（匹配任意一串字符）以及？（匹配任意一个字符） 
- 正则表达式之元字符：.^$*+?\|{}[]()
 - \不作转义符
- 主要操作：生成正则表达式对象、检索、匹配、分割以及找出所有匹配串
- 区间形式：[0-9a-z]表示匹配方括号中任意一个字符        [^0-9]则表示匹配除了0到9之外的所有字符
- .匹配任一个字符；\d：匹配十进制数字 \s：匹配所有空白字符 \w：匹配所有字母数字字符 上述若用大写字母则表示匹配除此之外的字符

## <center><font size=7>堆</font></center>
有序的树结构
堆排序：先将每个叶节点（视为排好的堆）构建新堆，即将要添加的元素放在堆顶，向下比较，寻找合适的位置，所走路径最长不超过log（n）


## <center><font size=7>栈 队列 树以及图相关程序直接见相应文件</font></center>




##<center><font size=7>递归与回溯</font></center>

###<font size=6>**递归**</font>
**应用**
- 斐波那契数列
- 归并排序 快速排序
- 二分搜索
- 树（前中后序）以及图（深度优先和广度优先）的遍历
- 一些动态规划
- 分治算法
- 汉诺塔

#### <font size=5>汉诺塔问题</font>
1. 把上面的n-1个disk从frompeg挪到auxpeg 
2. 把第n个disk从frompeg挪到topeg 
3. 再把前面n-1个disk从auxpeg挪回topeg

        def TowersOfHanoi(n,frompeg,topeg,auxpeg):
            if (n == 1):
                #---------基本条件------------
                print("Move disk 1 from peg "+frompeg+" to peg "+topeg)
            else:
                #----------递归条件-----------
                #把上面的n-1个disk从frompeg挪到auxpeg
                TowersOfHanoi(n-1,frompeg,auxpeg,topeg)
                #把第n个disk从frompeg挪到topeg
                print("Move disk "+str(n)+" from peg "+frompeg+" to peg "+topeg)
                #再把前面n-1个disk从auxpeg挪回topeg
                TowersOfHanoi(n-1, auxpeg, topeg, frompeg)
            return 0



###<font size=6>回溯</font>
基本思想：一种采用分治法来实现的类似与穷尽式搜索，即从解空间树上某个节点开始深度优先遍历

1. 任一个解的生成，都采用逐步扩大的方法，且每次扩大，都有一个可选的候选集从中选择下一个解空间树的结点
2. 从该节点的候选集中选择一个并拓展为下一个树结点，若当前节点再无法扩展，则回溯到上一个父结点
3. 开始父结点新的扩展，如果此父结点还无法扩展则再回溯，直到找到最近的活结点，逐步生成整个解空间状态树
  
**应用**
- 背包问题、八皇后问题
- 哈密尔顿回路
- 图染色问题
- 生成字符串，二进制串
  

        def kstring(n,k):
          """
          n：生成的字符串长度\n
          功能：用[1,k-1]范围中的数，生成长度为n的所有可能字符串"""
          if n<1:
              print(kstr)
          else:
              for i in range(0,k):
                  kstr[n-1] = i
                  kstring(n-1,k)
