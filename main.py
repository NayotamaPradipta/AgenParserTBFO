# Main program 
import lexer
from CYKparser import Parser
import time



if __name__ == '__main__':
    initTime = time.time()
    # Lexing 
    # Check fungsi time berhasil atau tidak dg program sederhana
    a = 0
    for i in range(1000):
        a += 2 ** i
    # Parsing 

    finalTime = time.time()
    print("Time Execution: ", "{:.5f}".format(finalTime - initTime), "second(s)")