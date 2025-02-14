listfruit=["orange","apple","banana","pineapple","mango","pawpaw","groundnut"]
for i in listfruit:
    if i=="mango":
        print(i)
        listfruit.remove(i)
        
print(listfruit)