#WAP to find the consonent and vowels from the entered text.

def char():
    ch= str(input("Enter a number"))
    chr=ch.replace(" ","")
    ch=ch.lower()
    vow=0
    cons=0
    vowlist=[]
    conslist=[]
    vowels='aieou'
    for i in ch:
        if i in vowels:
            vow+=1
            vowlist.append(i)
        else:
            cons=cons+1
            conslist.append(i)
    print("Total vowels is:",vowlist,'=',vow,"\nTotal consonent is:",conslist,'=',cons) 
char()
    