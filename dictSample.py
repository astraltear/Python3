# -*- coding: utf-8 -*-
d={'jan':1,'feb':2,'mar':3,'apr':4,'aug':8,'dec':12}

print( d['jan'], d['feb'], d['mar'] )

d2 = dict(jan=1,feb=2,mar=3,apr=4,may=5,jun=6,jul=7,aug=8,sep=9,oct=10,nov=11,dec=12)

print(d2)

month_names=[('jan',1),('feb',2),('mar',3),('apr',4),('may',5),('jun',6),('jul',7),('aug',8),('sep',9),('oct',10),('nov',11),('dec',12)]
print(dict(month_names))
print(month_names)


print( {name: num for name, num in month_names} )
print( {name: num for name, num in month_names if num %2==0} )

months = dict(month_names)
print( {v: k for k,v in months.items()} )

print(months.get('Jan'))    # None
print(months.get('Jan',1))  # 1
print(months.get('Jan'))    #None

print(months.setdefault('Jan',1))   # 1
print(months.get('Jan'))            # 1
