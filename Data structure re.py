import math
import random
import matplotlib.pyplot as plt
import numpy as np

#全局变量聚集地
from matplotlib.ticker import MultipleLocator
import networkx as nx
from matplotlib import pyplot as plt
kstr = [0]*2

class ListNode():
    def __init__(self,val,wig=1):
        self.val = val
        self.wig = wig
        self.next = None
    def showlast(self,head):
        p = head
        if p is None:
            print("空链表")
            return 0
        while p is not None:
            print(p.val,end=",")
            p = p.next
        return 0
class Bintree():
    def __init__(self,val=0):
        self.val = val
        self.left = None
        self.right = None
class Graph(ListNode):
    def __init__(self,nodenum):
        self.nodelist = [ListNode(i,0) for i in range(nodenum)]
        # self.edge = ListNode()
    def add_edges(self,edgelist):
        for i in edgelist:
            edge = ListNode(val=i[1],wig=i[2])
            edge.next = self.nodelist[i[0]].next
            self.nodelist[i[0]].next = edge
        return 0


def pathlen(root,floor=''):
    if root is None:
        return 0
    # floor = floor + 1
    if root.left is None and root.right is None:
        print(floor,root.val)
    pathlen(root.left,floor = floor+'0')
    pathlen(root.right,floor = floor+'1')

#汉诺塔递归实现
def TowersOfHanoi(n,frompeg,topeg,auxpeg):
    '''towerofhanoi by zhsong \n
    n : disk number \n
    frompeg : disk where move from \n
    topeg : disk to which tower \n
    auxpeg : assistance for moving disk\n
    output ：each step of moving disk'''
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

def kstring(n,k):
    """
    n：生成的字符串长度\n
    A列表：长度为k的字符混合型列表\n
    功能：用A列表中的任意元素，生成长度为n的所有可能字符串"""
    if n<1:
        print(kstr)
    else:
        for i in range(0,k):
            kstr[n-1] = i
            kstring(n-1,k)

def Josephus_list(n,m,k):
    """共n人围成圈，从第k个开始报数，每报到m出列，输出出列顺序"""
    idlst = []
    head = ListNode(n)
    last = head
    for i in range(n-1,0,-1):
        p = ListNode(i)
        p.next = head
        head = p
    q , idx =head,1
    p.showall(p)
    while q is not None:
        if q.val == k:
            last.next = head
            break
        else:
            q,idx = q.next,idx+1
    # print(q.val)
    while q is not None:
        for i in range(m-1):
            pre = q
            q = q.next
        idlst.append(q.val)
        # print(q.val)
        pre.next = q.next
        if pre.next == pre:
            break
        q = pre.next

    return idlst

def naive_string_searching(t,p):
    i ,j =0,0 #i指开端，j指p中的序号
    idxlst = []
    while i<len(t) and j<len(p):
        if i+j>=len(t):
            return -1
        else:
            if t[i+j] == p[j]:
                if j == len(p) - 1:
                    idxlst.append(i)
                    i,j = i+1,-1
                j = j+1
            else:
                i,j = i+1,0

    return idxlst

def KMP(t,p):
    """求模式串的前缀pre和后缀la中相同部分的最长的长度k

    即下一次模式串p的下标为k的位置移到这一次匹配失败的位置i处"""
    i,j = 0,0
    tlen,plen = len(t),len(p)
    F = getnext(p)
    idlst = []
    while i<tlen:
        if t[i]==p[j]:
            if j==plen-1:
                return (i-j)
            else:
                i,j=i+1,j+1
        elif j>0:
            j = F[j-1]
        else:
            i ,j = i+1,0
    return -1

def getnext(p):
    """构造F表时，F[i]应该表示i之前的字符串（不包括第i个）前后缀最大长度，但此处表示了i+1之前的字符串

    所以当匹配失败移动j的时候采用F[i-1]，即（i-1）+1之前的字符串"""
    F = [0] * len(p)
    i,j,F[0]= 1,0,0
    while i < len(p):
        if p[i]==p[j]:
            F[i]=F[i-1]+1
            i ,j= i+1,j+1
        elif j>0:
            j = F[j-1]  #思想与KMP中查F表一样，这里嵌套操作即查F表的F表
        else:
            F[i] = 0
            i = i+1
    # print(F)
    return F

def showarray(miap):
    # miap = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    #        [1,0,0,0,1,1,0,0,0,1,0,0,0,1],
    #        [1,0,1,0,0,0,0,1,0,1,0,1,0,1],
    #        [1,0,1,0,1,1,1,1,0,1,0,1,0,1],
    #        [1,0,1,0,0,0,0,0,0,1,1,1,0,1],
    #        [1,0,1,1,1,1,1,1,1,1,0,0,0,1],
    #        [1,0,1,0,0,0,0,0,0,0,0,1,0,1],
    #        [1,0,0,0,1,1,1,0,1,0,1,1,0,1],
    #        [1,0,1,0,1,0,1,0,1,0,1,0,0,1],
    #        [1,0,1,0,1,0,1,0,1,1,1,1,0,1],
    #        [1,0,1,0,0,0,1,0,0,1,0,0,0,1],
    #        [1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
    # map = [[0,1],[1,0]]
    data = np.array(miap)
    print(data.shape)
    ax = plt.gca()
    # ax.set_xlim(0, 14)
    # ax.set_ylim(0, 12)
    # miloc = plt.MultipleLocator(1)
    # ax.xaxis.set_minor_locator(miloc)
    # ax.yaxis.set_minor_locator(miloc)
    # ax.grid(c='g',which='both')
    plt.matshow(data,fignum=0)
    plt.show()

def migon(miap):
    cross = []
    # for i in range(1,10):
    #     for j in range(1,13):
    #         if miap[i+1][j]+miap[i][j+1]+miap[i-1][j]+miap[i][j-1]<=1 and miap[i][j]==0:
    #             miap[i][j]=0
    #             cross.append([i,j])
    # print(cross)

def findpath(miap,start,finish):
    dic = [[1, 0],[-1, 0],[0, 1] ,[0, -1]]
    miap[start[0]][start[1]] = 2
    if start == finish:
        print(start,end="")
        miap[start[0]][start[1]] = 3
        return True
    for i in range(4):
        nextp = start[0]+dic[i][0],start[1]+dic[i][1]
        nextp = list(nextp)
        if miap[nextp[0]][nextp[1]] == 0:#下一步在不在
            if findpath(miap,nextp,finish):#下一步能不能
                print(start,end="")
                miap[start[0]][start[1]] = 3
                return True
    return False

def huffuman(lst):
    stack,tree= [],[]
    for i in lst:
        tree.append(Bintree(i))
    leng = len(lst)
    def find(valu,tree):
        for i in tree:
            if i.val == valu:
                break
        return i
    def insertree(num,stack,tree):
        subtree = Bintree(num)
        subtree.left = find(stack.pop(0),tree)
        subtree.right = find(stack.pop(0),tree)
        return subtree
    while len(lst)>1:
        lst.sort(reverse = 1)           #排序降序
        stack.append(lst.pop())
        stack.append(lst.pop())
        sums = sum(stack)               #lst弹出两个最小的数求和得到sums
        lst.append(sums)                #和sums入lst
        subtree = Bintree(sums)
        subtree.left = find(stack.pop(0), tree)
        tree.remove(subtree.left)
        subtree.right = find(stack.pop(0), tree)
        tree.remove(subtree.right)
        tree.append(subtree)
        # tree = insertree(sums,stack,tree)     #将sums加入堆中
    pathlen(tree[-1])
    # for i in tree:
    #     print('root',i.val)
    #     if i.left is not None:
    #         print('L',i.left.val)
    #     else:
    #         print(None)
    #     if i.right is not None:
    #         print('R',i.right.val)
    #     else:
    #         print(None)
    # a = find(4,tree)
    # print(a)

def DFS(Graph,module):
    visit = [0] * len(Graph.nodelist)
    # print(visit)
    node = 0
    stack = []
    def VIS(Graph,node):
        if visit[node] == 1:
            return 0
        print(node,end=' ')
        visit[node] = 1
        nextnode = Graph.nodelist[node].next
        while nextnode is not None:
            VIS(Graph,nextnode.val)
            nextnode = nextnode.next
        return 0
    if module == 'rec':#递归
        VIS(Graph, node)
    elif module == 'iter':#迭代
        while len(stack)>=0:
            p = Graph.nodelist[node]
            if visit[p.val] == 0: #下一步怎么做
                stack.append(p)
                visit[p.val] = 1
                print(p.val,end=' ')
            if p.next is None:      #下一步不存在（该点边表检索完了）
                if len(stack)!=0:
                    p = stack.pop()
                else:
                    break
            else:                   #下一步存在
                while p.next is not None:
                    p = p.next
                    if visit[p.val] == 0:
                        break
            node = p.val

def BFS(Graph):
    visit = [0]*len(Graph.nodelist)
    floor = []
    i = 0
    while len(floor)>=0:
        p = Graph.nodelist[i]
        while p is not None:
            if visit[p.val] == 0:
                floor.append(p.val)
                visit[p.val] = 1
            p = p.next
        if len(floor)== 0:
            break
        else:
            i = floor.pop(0)
            # print(i,end=' ')
            yield  i
    # return 0

def Prim(Graph):
    E = [0]
    U = list(BFS(Graph))
    U.remove(0)
    print(U)
    def findsmall(i,E,U):#找到一行中最小的wig
        p = Graph.nodelist[i]
        node,small = 0,100
        while p is not None:
            if p.val not in U:
                p = p.next
                continue
            elif p.wig <small:
                node,small = p.val,p.wig
            p = p.next
        return node,small

    while len(U)>=0: #U是最小生成树集的补集
        node, es, ws = 0, 0, 100  # ws为一个巨大的数
        for i in E:#E 是最小生成树集（栈）
            edge,wig = findsmall(i,E,U)
            # print(i,edge,wig)
            if wig<ws:
                node,es,ws = i,edge,wig
        print(node,es)
        E.append(es)#最小生成树集添加顶点
        print(E)
        U.remove(es)#补集去除元素
        print(U)
        if len(U)==0:
            break

def Dijkstra(Graph,nodnum,start=0):
    BIG = float("inf")
    def init():
        v = [i for i in range(nodnum)]
        v.remove(start)
        d = [0]*nodnum
        for i in v:
            d[i] = dis(start,i)
        pre = [start]*nodnum
        return v,d,pre
    def least(v,d):
        lea = BIG
        for i in v:
            if d[i] < lea:
                lea = d[i]
        # print('lea',lea)
        return d.index(lea)
    def dis(start,i):
        p = Graph.nodelist[start]
        while p is not None:
            if p.val == i:
                return p.wig
            p = p.next
        return BIG
    def update(node,v,d,pre):
        # print('distace',d[node])
        for i in v:
            newd = d[node] + dis(node,i)
            # print('newd',newd)
            if newd < d[i]:
                d[i] = newd
                pre[i] = node
                return 0

    ### main
    v,d,pre = init()      #  visit , distance , pre-node
    print(v,d,pre)
    while len(v)>0:
        # print('update v', v)
        # print('update d', d)
        node = least(v,d)
        # print('node',node)
        v.remove(node)
        update(node,v,d,pre)

    print(d,pre)

def Flod(Graph,nodnum):
    for i in range(nodnum):
        for j in range(nodnum):
            for k in range(nodnum):
                if i!=j and j!=k and i!=k:
                    newd = dis(j, i) + dis(i, k)
                    if dis(j,k) > newd:
                        update(j,k,newd)#更新距离以及前驱节点
                else:
                    continue
    #递归中间结点来寻找两点之间的路径

def AOVsort(Graph):
    '''AOV（activity on vertex networks）:一个工程分解为多个子工程，用有向图表示各子工程的先后顺序，如a→b表示先完成a才能执行活动b\

    找到入度为0的节点输出，并将以其为出发连接的点入度减去1，循环

    可检测网中有没有环路，如有则没有入度为0的节点'''
    pass
def AOE(Graph):
    """节点表示事件，有向边表示活动，权值，表示时间，从前往后推断事件最早发生的时间，从后往前推断最迟发生时间
    
    其中最后一个事件的最早和最迟时间一样，要保证两事件之间的所有种遍历方法都能完成（满足最长时间）
    
    活动的最早时间与事件的最早相同，最晚时间从后向前推，即后一个事件减去活动时间
    
    活动的最早和最晚时间差就是可以伸缩的，时间差为0的是关键路径"""

if __name__ == '__main__':
    #TowersOfHanoi(4,'A','B','C')
    # kstring(2,10)
    # print(Josephus_list(8,3,1))
    # print(naive_string_searching('abaabb','ab'))
    # print(KMP('bbaabb','ab'))
    # miap = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    #         [1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1],
    #         [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
    #         [1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1],
    #         [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1],
    #         [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1],
    #         [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    #         [1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1],
    #         [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
    #         [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
    #         [1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
    #         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
    # # showarray(miap)
    #
    # findpath(miap,[1,1],[10,12])
    # showarray(miap)
    # a = Bintree(2)
    # b = Bintree(3)
    # c = Bintree(1)
    # c.left = a
    # c.right = b
    # a.right = Bintree(2)
    # pathlen(c)
    # huffuman([2,2,5,10,4,3,7])
    # head = ListNode(0)
    # i = 4
    # while i>0:
    #     a = ListNode(i)
    #     a.next = head.next
    #     head.next = a
    #     i = i-1
    # p = head
    # while p.next is not None:
    #     print(p.val)
    #     p = p.next
    # print(head.showall(head))
    G = Graph(5)
    # G.add_edges([(0,3,1),(0,2,2),(1,5,3),(1,2,2),(1,0,6),(2,4,5),(2,1,5),(3,4,4),(4,6,2),(5,6,1)])
    G.add_edges([(0,1,10),(0,3,30),(0,4,100),(1,2,50),(2,4,10),(3,2,20),(3,4,60)])
    # G.nodelist[2].showlast(G.nodelist[2])
    # DFS(G,module='iter')
    # for i in BFS(G):
    #     print(i)
    # print(list(BFS(G)))
    # print(G.nodelist[0].next.wig)
    # Prim(G)
    Dijkstra(G,5)