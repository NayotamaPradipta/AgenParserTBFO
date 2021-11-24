import re

def dfa(readstring):
    hasil = []
    hasil1 = []
    hasil2 = []
    countvarerror = 0
    # dfa states

    listingalphabets =[chr(c) for c in range(97,123)]
    listingKapital = [chr(c) for c in range(65,91)]
    listingNumber = [chr(c) for c in range(48,58)]
    commentstring = ['#','\'','\"']
    restriction = ['$','&','?','@','^','~']
    pembandingoperator = ['=','>','<','!']
    mathoperator = ['+','-','/','*','%']
    pembuka = ['{','[','(',',']
    penutup = ['}',']',')']
    dfa = {0:{},1:{},2:{},3:{},4:{},5:{}}

    # untuk state 0

    for x in listingalphabets:
        dfa[0][x]=2
    for x in listingKapital:
        dfa[0][x]= 2
    for x in listingNumber:
        dfa[0][x] = 3
    for x in commentstring:
        dfa[0][x] = 1
    for x in restriction:
        dfa[0][x] = 4
    for x in pembandingoperator:
        dfa[0][x] = 0
    for x in pembuka:
        dfa[0][x] = 0
    for x in penutup:
        dfa[0][x] = 0
    for x in mathoperator:
        dfa[0][x] = 0
    dfa[0]['_'] = 2
    dfa[0]['.'] = 0
    dfa[0][':'] = 0
    # untuk state 1

    for x in listingalphabets:
        dfa[1][x]=1
    for x in listingKapital:
        dfa[1][x]= 1
    for x in listingNumber:
        dfa[1][x] = 1
    for x in commentstring:
        dfa[1][x] = 0
    for x in restriction:
        dfa[1][x] = 1
    for x in pembandingoperator:
        dfa[1][x] = 1
    for x in pembuka:
        dfa[1][x] = 1
    for x in penutup:
        dfa[1][x] = 1
    for x in mathoperator:
        dfa[1][x] = 1
    dfa[1]['_'] = 1
    dfa[1]['.'] = 1
    dfa[1][':'] = 1
    # untuk state 2
    for x in listingalphabets :
        dfa[2][x]=2
    for x in listingKapital:
        dfa[2][x]= 2
    for x in listingNumber:
        dfa[2][x] =2
    for x in commentstring:
        dfa[2][x] = 1
    for x in restriction:
        dfa[2][x] = 4
    for x in pembandingoperator:
        dfa[2][x] = 0
    for x in pembuka:
        dfa[2][x] = 0
    for x in penutup:
        dfa[2][x] = 0
    for x in mathoperator:
        dfa[2][x] = 0
    dfa[2]['_'] = 2
    dfa[2]['.'] = 0
    dfa[2][':'] = 0

    # untuk state 3
    for x in listingalphabets :
        dfa[3][x]=4
    for x in listingKapital:
        dfa[3][x]= 4
    for x in listingNumber:
        dfa[3][x] =3
    for x in commentstring:
        dfa[3][x] = 0
    for x in restriction:
        dfa[3][x] = 4
    for x in pembandingoperator:
        dfa[3][x] = 0
    for x in pembuka:
        dfa[3][x] = 4
    for x in penutup:
        dfa[3][x] = 0
    for x in mathoperator:
        dfa[3][x] = 0
    dfa[3]['_'] = 4
    dfa[3]['.'] = 5
    dfa[3][':'] = 0
    # untuk state 5
    for x in listingalphabets :
        dfa[5][x]=4
    for x in listingKapital:
        dfa[5][x]= 4
    for x in listingNumber:
        dfa[5][x] =5
    for x in commentstring:
        dfa[5][x] = 0
    for x in restriction:
        dfa[5][x] = 4
    for x in pembandingoperator:
        dfa[5][x] = 0
    for x in pembuka:
        dfa[5][x] = 4
    for x in penutup:
        dfa[5][x] = 4
    for x in mathoperator:
        dfa[5][x] = 0
    dfa[5]['_'] = 4
    dfa[5]['.'] = 5
    dfa[5][':'] = 0

    def accepts(transition, start, s):
        states = start
        for char in s:
            print(char)
            try:
                states = transition[states][char]
                print("this stataes", states)
            except KeyError:
                return False
        return (states != 4)

    for i in readstring:
        thisstring = re.sub('and','=',i)
        hasil.append(thisstring)
    for j in hasil:
        thisstring1 = re.sub('or','=',j)
        hasil1.append(thisstring1)
    for k in hasil1:
        thisstring2 = re.sub('\s+','',k)
        hasil2.append(thisstring2)
    print(hasil2)
    for l in range(len(hasil2)):
        if (accepts(dfa,0,hasil2[l])):
            consider = 'Accepted'
        else:
            consider = 'Rejected'
            countvarerror += 1
            print(hasil[l], consider)
    return(countvarerror)