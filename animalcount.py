animal=["Yes",  "Yes", "Yes", "No","Yes","Yes", "Yes","Yes","Yes", "No","Yes", "No", "Yes", "No",   "No", "Yes","Yes", "Yes", "Yes", "Yes","No",  "No",  "Yes","Yes", "No","Yes"]
cowcount=0
cowspresent=[]

for i in animal:
    if i =="Yes": #meaning present
        cowcount=cowcount=+1
        
        cowspresent.append(i)
            
    else:
        continue
        print
    
print(cowspresent.count(i)) 
    
 # call the function for the final outcome