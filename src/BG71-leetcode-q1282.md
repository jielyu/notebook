# ​面试刷题：将人们按给定组的大小归为同一组 | 第41期

## 1. 题目 (Leetcode Q1282)

有n个ID从0到n-1的人，每个人恰好属于一个组。给定长度为n的数组groupSizes告诉每个人所属的组大小，返回存在的组以及每个组包括的人的ID。您可以按任何顺序返回任何解决方案，ID也一样。另外，可以保证至少存在一种解决方案。

## 2. 约束条件

(a) groupSizes.length == n

(b) 1 <= n <= 500

(c) 1 <= groupSizes[i] <= n


## 示例 1

```
Input: groupSizes = [3,3,3,3,3,1,3]
Output: [[5],[0,1,2],[3,4,6]]
```

解释：其他的可能方案是：[[2,1,6],[5],[0,4,3]] 和 [[5],[0,6,2],[4,3,1]]。

## 示例 2

```
Input: groupSizes = [2,1,3,3,3,2]
Output: [[1],[0,5],[2,3,4]]
```

## 3. 解决思路 1

首先，阅读题目之后会有一个很直观的方案，大概表述如下：

逐个获取每个人的id和所属组的大小groupsize，然后逐个安置人的id。如果当前人的groupsize已经存在了并且改组还没满，则将当前人的id放入这个组；否则，创建新的组并安排当前人的id。

这个表述理解起来似乎并不是太容易，我们可以使用伪代码重新描述一下：

```
step 1: 取人的id和对应的组大小groupsize
step 2: 查找当前groupsize的组
        如果组未满，将当前id放入对应的组
        如果组不存在或已满，创建新组并加入id
step 3: 返回step 1，直到所有人安排完成
```

### (1) 复杂度

在最差的情况下，每个人的组大小都等于1，则该算法的时间复杂度为O(n^2)。

### (2) C++解决方案

按照这个算法流程可以使用C++实现如下：

```C++
class Solution {
public:
    // Runtime: 28 ms, faster than 55.03% 
    // Memory Usage: 11.2 MB, less than 100.00%
    vector<vector<int>> groupThePeople(vector<int>& groupSizes) {
        int n = groupSizes.size();
        // to record all groups
        vector<vector<int>> ret; 
        // to record limitation of groups
        vector<int> ret_limit;   
        // to mark if successful in inserting 
        bool succ = false;        
        for (int i=0; i<n; ++i) {
            int s = groupSizes[i];
            int len = ret.size();
            succ = false;
            // insert current person into existing group
            for (int j=0; j<len; ++j) {
                int limit = ret_limit[j];
                // valid group
                if (s == limit && limit > ret[j].size()) {
                    ret[j].push_back(i);
                    succ = true;
                    break;
                }
            }
            // create a new group
            if (!succ) {
                vector<int> new_group;
                new_group.push_back(i);
                ret_limit.push_back(s);
                ret.push_back(new_group);
            }
        }
        return ret;
    }
};
```

在leetcode网站上评测，以上实现的C++解决方案能够超过55.03%的提交。虽然不算太好，但勉强也还过得去。


### (3) Python解决方案

接下来可以使用python代码来实现一下这个算法思路。

```Python
class Solution:
    # Runtime: 228 ms, faster than 5.69%
    # Memory Usage: 12.8 MB, less than 100.00%
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        n = len(groupSizes)
        # to record all groups
        ret = []     
        # to record limitation of groups     
        ret_limit = []    
        # to mark if successful in inserting
        succ = False;     
        for i in range(n):
            s = groupSizes[i]
            length = len(ret)
            succ = False
            # insert current person into existing group
            for j in range(length):
                limit = ret_limit[j]
                # valid group
                if s == limit and limit > len(ret[j]):
                    ret[j].append(i)
                    succ = True
                    break
            # create a new group
            if not succ:
                ret_limit.append(s)
                ret.append([i])
        return ret
```

在leetcode网站评测，发现以上python解决方案的运行速度只超过了5.69%的提交，这一点实在是不能接受。我们仔细看看python实现的细节，发现并没有太多实现细节上的优化，因此只能考虑新的解决思路了。


## 4. 解决思路 2

我们重新来考虑这个问题，发现要求组大小groupsize相同的人被分配到满足该条件的任何一组都是允许的。那么如果先按照groupsize将人的id归类到一起，然后将同一类的id平均分成几份即可。

这个思路可以使用伪代码描述如下：

```
step 1: 以groupsize为key，将人的id组成一个列表作为value
step 2: 将每个value平均分成 length(value)/key 份 
```

### (1) 复杂度

在最差的情况下，由于以key-value形式存储可以使用dict或者map，其构建时间复杂度是n*log(n)。其后划分组所需时间比归类组大小所需时间少，在估算时间复杂度时可忽略，因此时间复杂度为n*log(n)。从时间复杂度分析来看，应该是比第一个解决思路要快一些。


(2) Python解决方案

python中的dict类型能够满足要求，而且简单易用，我们首先给出一种python的解决方案。‍

```Python
class Solution:
    # Runtime: 72 ms, faster than 95.14%
    # Memory Usage: 12.8 MB, less than 100.00%
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        d = {}
        for idx, v in enumerate(groupSizes):
            if v not in d:
                d[v] = [idx]
            else:
                d[v].append(idx)
        ret = []
        for k, vals in d.items():
            for i in range(len(vals) // k):
                ret.append(vals[i * k : (i + 1) * k])
        return ret
```

从评测的结果来看，这个python的解决方案运行速度已经超过了95.14%的提交。与之前相比，已经有很大的提升，可以表明这个解决思路确实优于上一个解决思路。

### (3) C++解决方案

我们在使用C++实现一下这个更优的思路试试

```C++
class Solution {
public:
    // Runtime: 24 ms, faster than 85.14%
    // Memory Usage: 11 MB, less than 100.00%
    vector<vector<int>> groupThePeople(vector<int>& groupSizes) {
        // build a dict mapping size to idx
        unordered_map<int, vector<int>> d;
        int len = groupSizes.size();
        for (int i = 0; i < len; ++i) {
            d[groupSizes[i]].push_back(i);
        }
        // get results
        vector<vector<int>> ret;
        vector<int> m;
        for (auto & p : d) {
            int step = p.second.size() / p.first;
            for (int j = 0; j < step; ++j) {
                m.clear();
                for (int k = j*p.first; k < (j+1)*p.first; ++k) {
                    m.push_back(p.second[k]);
                }
                ret.push_back(m);
            }
        }
        return ret;
    }
};
```

评测结果显示以上C++实现的解决思路2运行速度超过了85.14%的提交。相比较与思路1的C++实现提升了大约60%，也是个不错的优化结果。从代码简化程度来看，第二种解决思路也更加简洁。从评测结果来看还应有更好的解决方案，可以继续探索。