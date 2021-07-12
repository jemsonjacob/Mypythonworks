s="jemson1234"
n="123456"
count=0
countn=0
for i in s:
    if i in n:
        countn=countn+1
    else:
        count=count+1
print(countn)
print(count)
