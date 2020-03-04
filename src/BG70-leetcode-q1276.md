# 面试刷题：不浪费原料的汉堡数量 | 第36期

## 题目 (Leetcode Q1276)

给定两个整数TomatoSlices和CheeseSlices。不同汉堡的成分如下：

```
巨型汉堡：4个番茄片和1个奶酪片。
小汉堡：2个西红柿片和1个奶酪片。
```

返回`[total_jumbo，total_small]`，以使剩余的TomatoSlices数量等于0，并且剩余的CheeseSlices数量等于0。
如果不可能使剩余的TomatoSlices和cheeseSlices等于0，则返回[]。

## 约束条件

(a) 0 <= tomatoSlices <= 10^7

(b) 0 <= cheeseSlices <= 10^7

## 示例

### 例1:

```
Input: tomatoSlices = 16, cheeseSlices = 7
Output: [1,6]
```

解释: 要制作一个超大汉堡和6个小汉堡，我们需要4 * 1 + 2 * 6 = 16番茄和1 + 6 = 7奶酪。将没有剩余的成分。

### 例2:

```
Input: tomatoSlices = 17, cheeseSlices = 4
Output: []
```

解释:  没有办法使用所有成分来制作小型汉堡和巨型汉堡。

### 例3:

```
Input: tomatoSlices = 4, cheeseSlices = 17
Output: []
```

解释: 制作1个巨型汉堡将剩余16个奶酪，制作2个小汉堡将剩余15个奶酪。

### 例4:

```
Input: tomatoSlices = 0, cheeseSlices = 0
Output: [0,0]
```

### 例5:
```
Input: tomatoSlices = 2, cheeseSlices = 1
Output: [0,1]
```

## 解决思路
可以将这个问题看作是求解一个二元一次方程组的正整数解的问题。利用所给的条件，假设大汉堡数量为 x，小汉堡数量为 y，正好可以构建两个一次方程。
根据数学尝试我们知道，该方程组必定存在解，只是如果方程的解为负数或者小数，那么不符合实际情况，应当舍弃。

## 解决方案

```C++
class Solution {
public:
    // 8ms
    vector<int> numOfBurgers(int tomatoSlices, int cheeseSlices) {
        // equations
        // 4x+2y=c1 & x+y=c2
        // formatted to 4x+2y=c1 & 2x+2y=2c2
        vector<int> ret;
        int mid_val = tomatoSlices - 2*cheeseSlices;
        // check integer solver for x
        if (mid_val < 0 || mid_val % 2 == 1) {
            return ret;
        }
        int x = mid_val / 2;
        int y = cheeseSlices - x;
        // check postive for y
        if (y < 0) {
            return ret;
        }
        // return [x, y]
        ret.push_back(x);
        ret.push_back(y);
        return ret;
    }
};
```

## 复杂度分析

从以上算法的解决思路和实现代码看来，其时间和空间复杂度都是为O(1), 即常数复杂度。使用数学方法寻找解决方案常常能够得到高效的算法，但实际情况并不总能像这样找到合适的数学方法。