massage=input('Enter massage .. ')
# Decoding 
convert=input('which conversion do you want ? ')
if convert =='decode':
    if len(massage) <3:
        print(massage[::-1])
    else : 
        decode_massage=massage[1:]+massage[0]
        decode_massage='bac'+decode_massage+'kdd'
        print(decode_massage)
# Encoding
elif convert =='encode':
    if len(massage) <3:
        print(massage[::-1])
    else:
        encode_massage=massage[3:-3]
        encode_massage=encode_massage[-1]+encode_massage[0:-1]
        print(encode_massage)