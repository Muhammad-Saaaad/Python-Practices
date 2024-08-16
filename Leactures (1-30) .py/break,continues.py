# Break

#Break is only use to exit from the loop 

i=0
while i<10:
    if i==7:
        break
    print(i)
    i+=1
# it will print from 0 to 6 and then exit the loop

# Continue     

# continue is use to skip the particular iteration : 

for i in range(20):
    if i==7:
        continue
    print(i)
# it will print foem o to 6 and then skip the 7th iteration and then again start printing form 8 to 19    