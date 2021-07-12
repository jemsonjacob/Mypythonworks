lst=[2,3,4,8,10,7]

res=list(map(lambda num:num-1 if num<5 else num+1 if num>5  else num,lst))
print(res)

