'''
Copyright: Amusi
Author:    Amusi
Date:      2018-06-09

题目描述
请实现一个函数，将一个字符串中的空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。

输入: 字符串和字符串最大长度
输出: 无


解题思路
此题重点在于get到形参传递（字符指针）的重要性（其实是"引用传递"问题）。
此题的目的不是返回新的字符串（这样操作很简单），而是对原来字符指针指向的内容进行修改。

既然是对原字符指针指向的内容进行修改，那我们应该要计算出字符指针所指向字符串的原始有效长度和空格数量。
根据原始长度和空格数量可以计算出新的字符串长度，再从右向左，对字符串内容进行修改。
此时字符串对象其实可以理解成两个，一个原始字符串，一个新字符串。虽然原始字符串和新字符串指向的内容都是同一个，
但从概念上理解，新字符串的有效长度比原始字符串有效长度要长，而且新字符串的值是下面不断添加进来的。

从右向左，原字符串起始索引值是原字符串长度-1，然后判断当前索引值指向的内容是不是空格，如果是空格，
则将新字符串当前索引值（新字符串起始索引值是新字符串长度-1）依次替换为'0', '2'和'%'。索引值每赋值一次，都要-1。

为什么是倒序呢？因为是从右向左嘛。注意咯，每次赋值后，索引值都要-1。如果不是空格，则直接将原字符串指向的元素替换成新字符串指向的元素即可。

那么什么时候停止上述运算呢？当然遍历完原字符串所有有效元素即可。

注：语文功底很差，上述内容写的较为繁琐，大家可以自行体会，嘻嘻。


解题步骤
上述思路其实写了个大概，这里不赘述。


PS: Amusi在今年四月份腾讯实习面试的时候遇到了这题，当初的解法很垃圾，所以充分验证了刷题的重要性。

'''

class Solution:
    '''将字符串中的空格替换成%20'''
    # str为源字符串
    def replaceSpace(self, str):
        return str.replace(' ', '%20')
	
if __name__ == '__main__':
    
    str = "We Are Happy"
    print(str)
    ss = Solution()
    str = ss.replaceSpace(str)
    print(str)
	
	

