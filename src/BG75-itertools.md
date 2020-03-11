# itertools加速你的Python程序

如果你听到有一个人在抱怨Python，那么他十有八九正在承受Python程序运行速度慢的煎熬。如果你也感觉到了Python程序运行时的低效，那么是时候作出一些改变了，优化循环结构可能是收益比较大的一项工作。使用何种工具来优化呢？itertools是一个不错的选择，它提供了很多常用功能的迭代器，不仅能加速，还能让你的程序更简洁，甚至提升开发效率。

如果有需要实现任意多步的循环，那么“无穷迭代器”会很有帮助；如果想对序列数据进行一些常规操作，那么“有限迭代器”会比较有用；如果需要实现一些排列组合的需求，那么“排列组合迭代器”会是不二的选择。除了介绍这三种迭代器的常用功能，下文还会对每一类迭代器与自己手动实现相同功能的程序进行性能的对比。可以先剧透一下结论，用过itertools提供的迭代器之后，你再也不想自己实现这些功能了。

## 1. 无穷迭代器

所谓“无穷迭代器”是指，可以从迭代器中取值任意次数。如果直接对这样的迭代器进行遍历，而不进行跳出操作，那么将会是一个死循环。

|函数名|功能解释|
|:---:|:---:|
|count|等差数列|
|cycle|循环遍历序列元素|
|repeat|重复数值任意次数|

### (1). count()

如果需要生成一个任意长度的等差数列，count()函数是一个比range()更好的选择，因为它支持浮点数步长。下面的例子可以说明这一点。

```Python
import itertools as it

it_count = it.count(12, 2.5)
print('type(it_count)={}'.format(type(it_count)))

ret = []
for i in it_count:
    ret.append(i)
    # 如果不加这一行就是死循环
    if i > 20:
        break
print(ret)
```

Output:

```
type(it_count)=<class 'itertools.count'>
[12, 14.5, 17.0, 19.5, 22.0]
```

### (2). cycle()

如果需要循环获取一个有效序列中的每一个元素，cycle()会很有帮助。

```Python
it_cycle = it.cycle([1,2,3,4])
print('type(it_cycle)={}'.format(type(it_cycle)))

ret = []
for i in it_cycle:
    ret.append(i)
    if len(ret) >= 10:
        break
print(ret)
```

Output:

```
type(it_cycle)=<class 'itertools.cycle'>
[1, 2, 3, 4, 1, 2, 3, 4, 1, 2]
```

### (3). repeat()

如果需要重复一个数值任意次数，可以使用repeat()函数；如果需要重复有限次，可以将次数作为第二个参数传入。

```Python
it_repeat = it.repeat(2)
print('type(it_repeat)={}'.format(type(it_repeat)))

ret = []
for i in it_repeat:
    ret.append(i)
    if len(ret) >= 10:
        break
print(ret)
```

Output:

```
type(it_repeat)=<class 'itertools.repeat'>
[2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
```

### (4). 性能对比

要说这三个函数所提供的功能更加高效，那总不能空开说白话，需要给出实验数据才有说服力。我们先实现一个与count()功能一致的函数。

```Python
def my_count(n, step):
    """使用python代码实现itertools.count的功能
    """
    while True:
        yield n
        n += step
```

为了便于测试，我们还需要实现一个测试函数，用于完成正常的功能调用。

```Python
def test_count(it_count):
    """用于测试count生成器的性能
    """
    for i in it_count: 
        if i > 20: 
            break
```

借助notebook的魔术方法，我们测试一下itertools提供的count()和自己动手实现的my_count()在相同参数下的运行耗时。

```Python
# 测试itertools提供的函数    
it_mycount = my_count(12, 2.5)
%timeit test_count(it_count)
it_count = it.count(12, 2.5)
%timeit test_count(it_mycount)
```

Output:

```
177 ns ± 2.3 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)
220 ns ± 2.57 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
```

评测数据说明，自己实现的my_count()至少比itertools提供的count()慢了16%。结论也就显而易见了，能用已有的，千万别瞎动手。

## 2. 有限迭代器

相比于“无穷迭代器”，更常用的还是“有限迭代器”。在日常开发的代码中使用这些接口，会比自己实现省事得多。

|函数名|功能解释|函数名|功能解释|
|:---:|:---:|:---:|:---:|
|accumulate|累加|chain|序列融合|
|compress|元素掩膜|dropwhile|从第一个false开始|
|takewhile|到第一个不满足结束|filterfalse|保留false|
|groupby|相邻同值元素分组|islice|切片|
|starmap|处理序列的序列|zip_longest|逐个依次组合|

### (1). accumulate()

累加，这是一个常用的数学操作，自己实现起来也不复杂，但在这里，我们还是先看看itertools的接口。

```Python
a = list(range(10))

it_acc = it.accumulate(a)
print('type(it_acc)={}'.format(type(it_acc)))
print(list(it_acc))
```

Output:

```
type(it_acc)=<class 'itertools.accumulate'>
[0, 1, 3, 6, 10, 15, 21, 28, 36, 45]
```

### (2). chain()

如果需要把若干个序列融合成一个序列的时候，chain()函数可以解决。

```Python
it_chain = it.chain([1,2,3], [4,5])
print('type(it_chain)={}'.format(type(it_chain)))
print(list(it_chain))
```

Output:

```
type(it_chain)=<class 'itertools.chain'>
[1, 2, 3, 4, 5]
```

### (3). compress()

想要使用掩膜板从一个序列中提取若干元素形成一个新的序列，compress()函数可以实现。

```Python
it_comp = it.compress([1,2,3,4,5], [0,1,1,0,0])
print('type(it_comp)={}'.format(type(it_comp)))
print(list(it_comp))
```

Output:

```
type(it_comp)=<class 'itertools.compress'>
[2, 3]
```

### (4). dropwhile()

有一个奇怪的需求，对序列的元素逐个遍历，遇到第一个不满足条件的元素时，接受该元素及其以后的所有元素形成一个新的序列。这个拗口的描述就是dropwhile()函数实现的功能。

```Python
it_dw = it.dropwhile(lambda x:x<3, [1,2,3,4,5,6])
print('type(it_dw)={}'.format(type(it_dw)))
print(list(it_dw))
```

Output:

```
type(it_dw)=<class 'itertools.dropwhile'>
[3, 4, 5, 6]
```


### (5). takewhile()

takewhile()函数提供的功能与dropwhile()刚好相反，即接受第一个不满足条件的元素之前的所有元素。

```Python
it_tw = it.takewhile(lambda x: x<3, [1,2,3,4,5])
print('type(it_tw)={}'.format(type(it_tw)))
print(list(it_tw))
```

Output:

```
type(it_tw)=<class 'itertools.takewhile'>
[1, 2]
```

### (6). filterfalse()

如果需要删除序列中满足条件的元素，可以选择filterfalse()函数。

```Python
it_ff = it.filterfalse(lambda x:x<3, [1,2,3,4,5,6])
print('type(it_ff)={}'.format(type(it_ff)))
print(list(it_ff))
```

Output:

```
type(it_ff)=<class 'itertools.filterfalse'>
[3, 4, 5, 6]
```

### (7). groupby()

将序列中排放在相邻位置的相同元素归为同一组,并以该元素为key，以该组元素为value生成词典，这是groupby()函数的功能。

```Python
it_gb = it.groupby([1,2,2,3,3,3,4,5,5,5])
print('type(it_gb)={}'.format(type(it_gb)))
print([k for k,g in it_gb])
it_gb = it.groupby([1,2,2,3,3,3,4,5,5,5])
print([list(g) for k,g in it_gb])
```

Output:

```
type(it_gb)=<class 'itertools.groupby'>
[1, 2, 3, 4, 5]
[[1], [2, 2], [3, 3, 3], [4], [5, 5, 5]]
```

### (8). islice()

如果需要对序列进行切片，可以使用islice()函数，虽然比Python自带的切片复杂一点。

```Python
# 传参顺序：sequence, start, end, step
it_is = it.islice([1,2,3,4,5], 1, 3, 1)
print('type(it_is)={}'.format(type(it_is)))
print(list(it_is))
```

Output:

```
type(it_is)=<class 'itertools.islice'>
[2, 3]
```

### (9). starmap()

如果需要对元素为序列的序列进行处理，starmap()可以提供对应的功能。

```Python
it_sm = it.starmap(lambda x,y: x*y, [(1,2),(3,4),(5, 6)])
print('type(it_sm)={}'.format(type(it_sm)))
print(list(it_sm))
```

Output:

```
type(it_sm)=<class 'itertools.starmap'>
[2, 12, 30]
```

### (10). zip_longest()

将两个序列逐个元素组合起来进行处理也是比较常用的操作，zip_longest()可以提供更加通用的功能。

```Python
it_zl = it.zip_longest([1,2,3,4], [5,6], fillvalue=0)
print('type(it_zl)={}'.format(type(it_zl)))
print(list(it_zl))
```

Output:

```
type(it_zl)=<class 'itertools.zip_longest'>
[(1, 5), (2, 6), (3, 0), (4, 0)]
```

### (11). 性能对比

就以zip_longest()函数的为例来进行性能对比，我们需要先实现一下提供相同功能的函数。

```Python
def my_zip_longest(seq_1, seq_2, fillvalue):
    length = max(len(seq_1), len(seq_2))
    for i in range(length):
        first = seq_1[i] if i<len(seq_1) else fillvalue
        second = seq_2[i] if i<len(seq_2) else fillvalue 
        yield first,second
```

然后使用notebook的魔术方法来进行如下评测：

```Python
%timeit list(it.zip_longest([1,2,3,4,5,6,7,8,9], [1,2,3,4,5], fillvalue=0))
%timeit list(my_zip_longest([1,2,3,4,5,6,7,8,9], [1,2,3,4,5], fillvalue=0))
```

Output:

```
968 ns ± 5.16 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
3.58 µs ± 37.3 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)
```

评测数据告诉我们，itertools提供的zip_longest()比自己动手实现的my_zip_longest()要快3倍左右。

## 3. 排列组合迭代器

“排列组合迭代器”大概是性价比最高的一组接口，因为这些功能要是自己动手实现，且不说速度慢，代码不易读，甚至有些实现起来还不那么容易。

|函数名|功能解释|
|:---:|:---:|
|product|笛卡尔积|
|permutations|排列|
|combinations|组合|
|combinations_with_replacement|有重复组合|

### (1). product()

product()函数可以用于计算两个序列的笛卡尔积。

```Python
it_prod = it.product([1,2,3], [4,5,6])
print('type(it_prod)={}'.format(type(it_prod)))
print(list(it_prod))
```

Output:

```
type(it_prod)=<class 'itertools.product'>
[(1, 4), (1, 5), (1, 6), (2, 4), (2, 5), (2, 6), (3, 4), (3, 5), (3, 6)]
```

### (2). permutations()

如果需要对序列元素进行无重复元素的排列，可以使用permutations()，这里的无重复可不是针对数值而言，而是针对对象的。所以如果想要数值不重复，需要保证输入序列数值不重复。

```Python
it_perm = it.permutations([1,2,3], 2)
print('type(it_perm)={}'.format(type(it_perm)))
print(list(it_perm))
```

Output:

```
type(it_perm)=<class 'itertools.permutations'>
[(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]
```

### (3). combinations()

有排列就有组合，combinations()函数就是用来提供组合功能的。

```Python
it_comb = it.combinations([1,2,3], 2)
print('type(it_comb)={}'.format(type(it_comb)))
print(list(it_comb))
```

Output:

```
type(it_comb)=<class 'itertools.combinations'>
[(1, 2), (1, 3), (2, 3)]
```

### (4). combinations_with_replacement()

如果想要进行有重复元素的组合，该怎么办？使用combinations_with_replacement()解决。

```Python
it_cwr = it.combinations_with_replacement([1,2,3], 2)
print('type(it_cwr)={}'.format(type(it_cwr)))
print(list(it_cwr))
```

Output:

```
type(it_cwr)=<class 'itertools.combinations_with_replacement'>
[(1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)]
```

### (5). 性能对比

组合功能实现起来稍微复杂一点，我们就以组合功能来对比一下itertools提供的工具与手动实现的接口。首先实现一个与combinations()函数功能大体一致的函数。

```Python
def my_combinations(seq, times):
    length = len(seq)
    if length < times:
        return
    idx = list(range(times))
    yield tuple(seq[i] for i in idx)
    
    def find_idx_i(idx, times, length):
        for i in range(times-1, -1, -1):
            if idx[i] != i + length - times:
                return i
        return None
    
    while True:
        i = find_idx_i(idx, times, length)
        if i is not None:
            idx[i] += 1
            for j in range(i+1, times):
                idx[j] = idx[j-1]+1
            yield tuple(seq[k] for k in idx)
        else:
            return
print(list(my_combinations([1,2,3, 4], 3)))
```

Output:

```
[(1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4)]
```

从输出结果来看，实现的功能正常。

接下来使用notebook提供的魔术方法测试一下运行时间。

```Python
%timeit list(it.combinations([1,2,3,4], 3))
%timeit list(my_combinations([1,2,3,4], 3))
```

Output:

```
576 ns ± 12.7 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
7.52 µs ± 96.8 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)
```

从对比评测的数据来看，itertools提供的combinations()比自行实现的my_combinations()要快13倍左右。或许是我的实现方案有问题，大家也可以自己实现一个试试看。

经过三个性能评测的对比，很明显地，itertools提供的接口比自己实现的要快很多，而且调用简单，代码易读。因此，学会itertools工具优化程序中的循环结构，大概可以拯救那些低效缓慢的Python程序。
