#to check for duplicatee item and print them out ignore the extensions
listme1=["orange.txt","yam.txt","yam.txt","chiz.mb","pineapple.jpg","pineapple.jpg","mango.mb","pawpaw.doc","groundnut.jpg"]
opt=[]
duplicateitem=[]
for i in listme1:
    opt.append(i)
    if opt.count(i)>1:
       
        duplicateitem.append(i)
    else:
        continue  
print("Dublicate items found but stored anyway")       
print(duplicateitem)
