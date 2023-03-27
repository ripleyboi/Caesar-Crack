
#accept string and convert to lowercase, and init new string
string = input('>>').lower()
newstring = ''
#reset counter/shifter
shift = 0
#alphabet for shifting
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#break string into characters
charlist = [*string]
#UNCOMMENT FOR DEBUG
#print(charlist)
def recombine(inlist):
    liststring = ''.join([str(i) for i in inlist])
    return(liststring)

while shift < len(alphabet):
    newcharlist = []
    for i in charlist:
        if i.isalpha():
            if int(alphabet.index(i) - shift) <= 0:
                newcharlist.append(alphabet[alphabet.index('z') - shift])
            else:
                newcharlist.append(alphabet[alphabet.index(i) - shift])
        else:
            newcharlist.append(i)
    print(recombine(newcharlist))

    newcharlist = []
    for i in charlist:
        if i.isalpha():
            if int(alphabet.index(i) + shift) >= len(alphabet):
                newcharlist.append(alphabet[shift])
            else:
                newcharlist.append(alphabet[alphabet.index(i) + shift])
        else:
            newcharlist.append(i)
    print(recombine(newcharlist))
    shift += 1


