listme=["orange","yam","chiz","chiz","pineapple","pineapple","mango","pawpaw","groundnut"]
for i in listme:
    if i=="chiz":
        print(i)
        listme.remove(i)
        print(listme)
listme.remove('chiz')
