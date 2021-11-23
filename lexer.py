import re
import os
import lexerRules
import CYKparser as parser


# menerima error lexer digunakan pada kelas Changing fungsi token dnegna mengoper-oper objeknya
# Jika tidak ada pasangan dalam matching sehingga mengembalikan string error position dan berhenti LEXERERROR, tapi ngga wajib, buat meriksanya nanti

class Changing(object):
    def __init__(self, rules, skip_whitespace):
        idx = 1
        regex_parts = []
        self.tipekelompok = {}

        for regex, type in rules:
            
            #merupakan nama state dari finite automata.
            kelompok = 'Kelompok%s' % idx
            #membuat list-list dari states yang ada
            regex_parts.append('(?P<%s>%s)' % (kelompok, regex))

            self.tipekelompok[kelompok] = type
            # membaca lexer rules perbaris nambah 1, jika valid.
            idx += 1

        self.regex = re.compile('|'.join(regex_parts))
        self.skip_whitespace = skip_whitespace
        self.re_ws_skip = re.compile('\S')


    def token(self):

        
        #mengembalikan None apabila di buffer tidak ada apa-apa sehingga panjang buffer 0 atau kurang dari 0.
        if self.pos >= len(self.buf):
            return None
        #jika buffer lebih besar dari posnya.
        else:
            # mencari pasangannya atau group kelompoknya yang benar seperti ";" terminalnya adalah SEMICOLON
            n = self.regex.match(self.buf, self.pos)

            if n:
                kelompok = n.lastgroup
                tipe = self.tipekelompok[kelompok]
                self.pos = n.end()
                if (tipe == 'WHITESPACE') :
                    return ''
                # mengembalikan jenis dari input 
                return tipe

    def tokens(self,buf):
        #menerima input
        self.buf = buf
        self.pos = 0
        # eksekusi dimulai dari dimana berhenti, jadi tidak menghapus fungsi local variabelnya, tetapi menyimpannya.
        # seperti word machine. Tapi menyimpan panjangnya, tidak mengulang dari nol sampai ketemu none dari token
        while True:
            hasiltoken = self.token()
            if hasiltoken is None: 
                break
            yield hasiltoken

CYK = parser.Parser('grammar.txt', " COMMENT ")



