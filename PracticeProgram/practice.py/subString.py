# class nospace(Exception):
#     pass

# sentence_list=list(input('Enter a sentence no space : '))
# alphabets='abcdefghojklmnopqrstuvwxyz'

# A_String=''.join(sentence_list)

# e_h=A_String.split(' ')
# length=len(e_h)
# if length >1:
#     raise nospace('You have enter a space : ')

# list_=[]
# length=len(sentence_list)
# pred=0
# for i , j in zip(range(length) ,range(1,length)):

#     if ord(sentence_list[i])==ord(sentence_list[j]) -1 :
#         pred+=1
#         list_.append(sentence_list[i])
#     else :
#         if pred >1:
#             list_.append(sentence_list[i])
#             pred=0
#         pass

# print(list_)

# A_String=''.join(list_)
# print(A_String)


# Question 1: Find the Longest Substring Without Repeating Characters
# Given a string, find the length of the longest substring without repeating characters

# def longest_sub_String(String):
#     s=set()
#     i=0
#     while i<len(String):
#         s.add(String[i])
#         i+=1
#     print('Length of the sub String : ',len(s))

# longest_sub_String('abcabcdrf')

# Question 2: Implement Trie (Prefix Tree)
# Implement a trie with insert, search, and startsWith methods.
Trie=[]
def Prefix_Tree():
    option=0
    while option!=4:
        try:
            option=int(input('Enter 1: Insert value \nEnter 2: Search value \nEnter 3: startsWith methods \nEnter 4: Exit '))
            match option:
                case 1:
                    insert()
                case 2:
                    search()
                case 3:
                    Startwith()
                case 4:
                    print('Exit : ')
        except:
            print('Invalid value Entered : ')
        
def insert():
    word=input('Enter a word : ')
    Trie.append(word)

def search():
    word=input('Enter a word : ')
    if word in Trie:
        print(word,' Exist : ')

def Startwith():
    word=input('Enter a word : ')
    return_trie=[]    
    if word in Trie:
        iterate=0
        for i in Trie:
            if i!=word:
                iterate+=1

        for i in Trie[iterate+1:]:
            return_trie.append(i)
        print(return_trie)
    else :
        print('word does not exist : ')

Prefix_Tree()