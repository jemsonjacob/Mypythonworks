# binary
a = [1, 2, 3, 4, 5, 6, 7, 88, 90]
mid = len(a) / 2
ser = int(input("enter ele to search"))
for i in range(len(a)):
    if ser <= mid:
        for j in range(0,mid):
            if a[i]<a[j]:
                temp=a[i]
                a[i]=a[j]
                temp=a[j]

    else:
        if ser > mid:
           for i in range(mid):
            if ser == a[i]:
                print("element found", a[i])
            else:
                print("not found")
