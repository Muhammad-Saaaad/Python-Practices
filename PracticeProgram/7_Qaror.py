question1=[' Dragon Ball Anime movie is from which contary : ' ]
question2=[' What is the name of world biggest animal : ']
question3=[' What is GDP of pakitan : ']
question4=[' What is the size of the worlds smallest transistor : ']
question5=[' How much speed an object needs to escape from a black hole : '] 
question6=[' What is the frequency of electricity that is use in our houses : ']
question7=[' What is the date of you wedding anniversary : ']

All_Questions=question1+question2+question3+question4+question5+question6+question7

ans1=['A.Pakistan','B.Japan','C.south Korea','D.USA']
ans2=['A.Sperm Whale','B.Killer Whale','C.Elephant','D.giraffe']
ans3=['A.90 Billion $','B.70 Billion $','C.80 Billion $','D.100 Billion $ ']
ans4=['A.Smaller then finger nail','B.Smaller then an atom','C.Smaller then a red blood cell','D.smaller then a grain os sand']
ans5=['A.300000 km/s','B.400000 km/s','C.350000','D.250000']
ans6=['A.250Hz','B.150Hz','C.100Hz','D.50Hz']
ans7=['A.i Forgot : ',"B. Don't speak",'C. Give up','D.Do a back FLip and win :']

print('Every question is for 1 caror : \n If you won u will get 7 sath caror!!!... : \n ')

money=0
for i in range(7):
    print('Question no ',(i+1),All_Questions[i])
    if i==0 :
        print('Answer : ',ans1[0],ans1[1],ans1[2],ans1[3])
        pick=input()
        if pick=='B' or pick=='b':
            print('Correct Answer : \t 10000000 Added ')
            money=money+10000000
        else:
            print('Wrong Answer')
    elif i==1:
        print('Answer : ',ans2[0],ans2[1],ans2[2],ans2[3])
        pick=input()
        if pick=='A' or pick=='a':
            print('Correct Answer : \t 10000000 Added ')
            money=money+10000000
        else:
            print('Wrong Answer')
    elif i==2:
        print('Answer : ',ans3[0],ans3[1],ans3[2],ans3[3])
        pick=input()
        if pick=='A' or pick=='a':
            print('Correct Answer : \t 10000000 Added ')
            money=money+10000000
        else:
            print('Wrong Answer')
    elif i==3:
        print('Answer : ',ans4[0],ans4[1],ans4[2],ans4[3])
        pick=input()
        if pick=='C' or pick=='c':
            print('Correct Answer : \t 10000000 Added ')
            money=money+10000000
        else:
            print('Wrong Answer')
    elif i==4:
        print('Answer : ',ans5[0],ans5[1],ans5[2],ans5[3])
        pick=input()
        if pick=='B' or pick=='b':
            print('Correct Answer : \t 10000000 Added ')
            money=money+10000000
        else:
            print('Wrong Answer')
    elif i==5:
        print('Answer : ',ans6[0],ans6[1],ans6[2],ans6[3])
        pick=input()
        if pick=='D' or pick=='d':
            print('Correct Answer : \t 10000000 Added ')
            money=money+10000000
        else:
            print('Wrong Answer')
    elif i==6:
        print('Answer : ',ans7[0],ans7[1],ans7[2],ans7[3])
        pick=input()
        if pick=='D' or pick=='d':
            print('Correct Answer : \t 10000000 Added ')
            money=money+10000000
        else:
            print('Wrong Answer')

print('Congrulation you won ',money,'$$')