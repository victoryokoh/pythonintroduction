listme1=["orange.txt","yam.txt","chiz.mb","chiz.mb","chiz.mb","pineapple.jpg","pineapple.jpg","mango.mb","pawpaw.doc","groundnut.jpg"]
opt=[]
duplicateitem=[]
for i in listme1:
    opt.append(i)
    if opt.count(i)>1:
        duplicateitem.append(i)
    else:
        continue
print("Your duplicate items are: ", duplicateitem)
    