price = list(map(int,input().split(";")))

price.sort(reverse=True)

for i in price:
    i = format(i,',')
    i = i.rjust(9)
    print(i)