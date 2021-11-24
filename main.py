# Main program 
from lexer import Changing
import CYKparser as parser
import time
from lexerRules import lexerRules
from testdfa import dfa


if __name__ == '__main__':
    
    # Menerima input file, dibuka pathnya kemudian menggunakan fungsi open dan method read.
    # Read akan mengembalikan string yang sangat panjang
    input_file = input("Input file to check : ")
    initTime = time.time()
    file_path = './' + input_file
    file = open(file_path, 'r')
    readstring = file.read()
    file.close()
    files = open(file_path,'r')
    reading = files.readlines()
    files.close()
    # Lexing 
    # membuat objek
    lx = Changing(lexerRules, skip_whitespace=False)
    output = ''

    try:
        for tok in lx.tokens(readstring):
            if tok == '' :
                output = output
            else :
                output += tok + ' '
    except :
        print('LexerError')
    
    kumpulstring = output.split('NEWLINE')
    # print(string_container)
    komenmulti = False
    total_string = len(kumpulstring)
    berhasil = 0
    jmlerror = 0
    countbaris = 0
    key = 0
    ifkasus = 0
    print("Parsing {} line(s) of code...".format(total_string))
    
    # Parsing
    CYK = parser.Parser('grammar.txt', " COMMENT ")

    def checking(kalimat) :
        CYK.__call__(kalimat)
        CYK.parse()
        return CYK.print_tree()
    for readstring in kumpulstring :
            countbaris  += 1

            if readstring.find('TRIPLEQUOTE') != -1 and komenmulti == False :
                    komenmulti = True
                    berhasil += 1
                    key = 1
            elif (readstring.find('TRIPLEQUOTE') != -1) and komenmulti == True :
                    komenmulti = False
                    berhasil += 1
                    key = 2
            elif (key == 0 or key ==2 ):
                if (readstring == ' ' or readstring == ''):
                    print("",end='')
                    berhasil += 1
                elif komenmulti == False :
                    if readstring.find(' IF') != -1 :
                        ifkasus += 1
                        if not checking(readstring):
                            jmlerror += 1
                    elif readstring.find('ELIF') != -1 :
                        if ifkasus > 0 :
                            readstring = 'ELIFTOK' + readstring
                        if not checking(readstring) :
                            jmlerror += 1
                    elif readstring.find('ELSE') != -1 :
                        if ifkasus > 0 :
                            readstring = 'ELIFTOK' + readstring
                        ifkasus -= 1
                        if not checking(readstring) :
                            jmlerror += 1
                    else :
                        if not checking(readstring) :
                            jmlerror += 1
            elif (countbaris  == total_string and key == 1 ):
                jmlerror+=1
    
    # Cek apakah ada error yang ditemukan atau tidak
    errorvar = dfa(reading)
    if (jmlerror == 0 and errorvar == 0):
        print("Accepted!")
    else :
        print("Syntax Error! {} error yang ditemukan dalam file.".format(jmlerror + errorvar))
    finalTime = time.time()
    print("Time Execution: ", "{:.5f}".format(finalTime - initTime), "second(s)")