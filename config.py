# name,rid,cid
courses = [
    ('高等数学应用案例锦集', 42707, 2100685),
    ('高等数学（上）知识汇总与典型题解析', 41788, 2101263),
    ('线性代数与空间解析几何案例', 35262, 2101231),
    ('线性代数与空间解析几何', 35257, 2100446),
    ('线性代数与空间解析几何典型题解析', 33430, 2097866)
]

# username,password
users = [
]

FQAs = [
    ('矩阵的合同，等价，相似这三个关系有什么联系呢？', [
     '相似，合同一定等价，反之则不成立', '相似和合同之间没有必然的联系，但是相似或合同一定等价']),
    ('中值定理为什么可导区间是开区间', ['区间边界左右导数存在即可，不用闭区间', '对，左右导数存在就行']),
    ('函数在某一点导数大于零，那么在这一点上某邻域函数单调递增么', [
     '不对，一点处的导数决定不了函数的变化趋势', '不是，如果存在震荡点', '不对']),
    ('矩阵的行列式的在几何变换上的意义是什么', ['行列式表示的是矩阵变换缩放的因子',
                             '如果行列式为0，表示矩阵变换把点变换到低维空间，也叫退化空间']),
    ('正交矩阵为什么能保证向量的点乘不变性呢', ['因为正交矩阵对应的变换，把一个向量变换到另外一个正交基下面的向量，所以点乘不变']),
    ('矩阵的行向量线性相关，列向量也线性相关么', ['不一定，如果矩阵行向量线性相关，只能说明秩小于行数，如果等于列数，那么列向量线性无关']),
    ('如果题目中出现二层积分，怎么算', ['一般是用分部积分法，把内层积分求导，消掉']),
    ('收敛反常积分看似面积无穷大，为什么还能算出一个正确的常数呢', ['可以把面积比作是数列，积分比作是求和，数列极限为0，那么数列和收敛']),
]

MAX_LEN = 1000
