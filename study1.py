# comment
'''
multi line comment
'''

# reference variable

a= 5
b = 10
c = b
print(id(a), id(b),id(c))
print( a is b, b is c)  # False,  True

import keyword
print(keyword.kwlist)

print(type( 3+4j ))
print( type( (1,) ) )  # tuple
print( type( [1,2] ) ) # list
print( type( {1,2} ) )  #set
print( type( {'name':2} ) )  #dic

print('output',end='$');print('output2')  # output$output2

# packing
v1, *v2 = 1,2,3,4,5
print(v1, v2)

# a++ ++a 증감 연산자 없음
print( bool(0), bool(None),bool('') ) # all False
print(format(1.5432,'100.3f'))
print('name {0}, age {1}'.format("korean",30))
print('name {}, age {}'.format("korean",50))
print('name {2}, age {0}'.format("ko",20,30))

print('aa\tbb')
print(r'aa\tbb')

str1 = 'sequence'
print(str1.find('e'), str1.find('e',3),str1.rfind('e'))

# 아래의 코드는 string 이 immutable한 것을 보여준다.
# 해당 변수의 값이 변경된 것이 아니라 새로운 참조객체를 만든 후 새로운 객체의 주소로 링킹해 준다.
ss1 = 'mbc'
print(ss1,id(ss1))

ss1='abc'
print(ss1,id(ss1))

str2 = ['123','456','234']
str2.sort(key=int)
print(str2)

# shallow copy
names=['tom','james','charles']
names2 = names
print(id(names), id(names2))

# deep copy
import copy
names3 = copy.deepcopy(names)
print(id(names), id(names2),id(names3))

names2[2]='X'
print(names, names2,names3)

# tuple read only
t='a','d','e',
print(t,len(t),t.index('d'))

t1 = (10,20)
x,y = t1
t2 = y,x
print(t2)

# set - not duplication
s1 = {1,2,3}
s2={3,4}

print(s1.union(s2))
print(s1.intersection(s2))
print(s1-s2, s1|s2, s1&s2)
# print(s1[0])   'set' object does not support indexing

s1.add(5)
s1.update({5,6})
s1.update([8,9])
s1.update((10,11))
print(s1)

#s1.remove(20)  # 값이 없으면 에러
s1.discard('eden')  # 값이 없으면 통과

s3 = s1  # shallow copy
s3.clear() #  s3, s1 clear
print(s1,s3)

# dict 순서가 없다.
mydict = dict(k1=1, k2='abc',k3=3.4)
print(mydict)

del mydict['k1']
print(mydict)

# Regular Expression
import  re

str1 = '123 abc가나다ABC_555_6_78mbc'
print(re.findall(r'123', str1,))  # ['123']
print(re.findall(r'[0-9]', str1,)) # ['1', '2', '3', '5', '5', '5', '6', '7', '8']
print(re.findall(r'[0-9]+', str1,)) # ['123', '555', '6', '78']
print(re.findall(r'[0-9]{2}', str1,)) # ['12', '55', '78']
print(re.findall(r'[0-9]{2,3}', str1,)) # ['123', '555', '78']
print(re.findall(r'.bc', str1,))  # ['abc', 'mbc']
print(re.findall(r'^1+', str1,))        #1로 시작  ['1']
print(re.findall(r'^1.', str1,))        #1로 시작   ['12']
print(re.findall(r'[^1].+', str1,))  # 1을 제외하고 모든 문자  ['23 abc가나다ABC_555_6_78mbc']
print(re.findall(r'mbc$', str1,))  # ['mbc']




