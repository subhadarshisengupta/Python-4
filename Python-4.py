
# coding: utf-8

# In[26]:


#Area of a Triange taking inputs of all 3 sides
class triangle:
    def area(TRG):
        s=(TRG.side1+TRG.side2+TRG.side3)/2
        return (s*(s-TRG.side1)*(s-TRG.side2)*(s-TRG.side3))**0.5
    
    def __init__(TRG,side1,side2,side3):
        TRG.side1=side1
        TRG.side2=side2
        TRG.side3=side3
    
a=float(input('Enter the value of side 1: '))
b=float(input('Enter the value of side 2: '))
c=float(input('Enter the value of side 3: '))
print('Area of the triangle',triangle(a,b,c).area())


# In[18]:


# A function that takes a list of words and an integer n and returns the list of words that are longer than n
def filter_long_words(string,integer):
    wordlist=[]
    for i in string.split():
        if len(i)>integer:
            wordlist.append(i)
    return wordlist
filter_long_words('haJLDHjldhaLJDHjlhjlDH fjkfjk;fj;kfj;kfj;KFJ fjfkjafja;kfjak;kj UY yty QW',7)


# In[36]:


#Write a program that maps a list of words into a list of integers representing the lengths of the corresponding words.
 
listOfWords = ['Subhadarshi','Sengupta','Sarbajit','Bhutum','Baban']
 
listOfInts = []
 
for i in range(len(listOfWords)):
    listOfInts.append(len(listOfWords[i]))
print("List of words:"+str(listOfWords))    
print ("List of wordlength:"+str(listOfInts))


# In[49]:


def checkvowel(s):
    if len(s)!=1:
        print("Only String of length 1 is allowed")
        return None

    if s in "aeiouAEIOU":
        return True
    else:
        return False

def main():
    s = input("Enter Char (Length 1) : ")

    isV = checkvowel(s)

    if isV==True:
        print("TRUE : %s is a vowel" % s)
    elif isV==False:
        print(" FALSE : %s is not a vowel" % s)
    
main()

