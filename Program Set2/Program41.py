#WAP to find the consonent and vowels from the entered text.

def case():
    st=str.lower(input("Enter a character:"))
    st1=st.upper()
    print("So the your entered character in uppercase is:",st1)
    vow=0
    vowList= []
    cons = 0
    consList=[]
    vowels='aeiou'
    for i in st:
        if i in vowels:
            vow = vow+1
            vowList.append(i)
        else:
            cons=cons+1
            consList.append(i)
    print("Total vowels is:",vowList,'=',vow,"\nTotal consonent is:",consList,'=',cons)
case()

