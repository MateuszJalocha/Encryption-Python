import tkinter, sys, math
def wyjdz():
    sys.exit()

def szyfruj1():
    z = e.get()
    klucz = s.get()
    # klucz = ord(klucz) - 48 If you have to type it manually
    n = z.upper()
    n = n.replace(" ", "")  #Omits the spaces in the text to be encrypted
    zaszyfrowany = ''
    for ch in n:
        if ord('A') <= ord(ch) <= ord('Z'): #Converts letters into values and checks whether they are between A and Z
            kod = ord(ch) + klucz           #Adds the value of the key to the value of the letter, resulting in a new letter
        if kod > ord('Z'):                  #If the letters go beyond the alphabet range, the counting continues from the beginning
            kod -= 26
        zaszyfrowany += chr(kod)
    l.config(text=zaszyfrowany)

def deszyfruj1():
    z = e.get()
    klucz1 = s.get()
    # klucz = ord(klucz) - 48
    f = z.upper()
    odszyfrowany = ''
    for ch in f:
        if ord('A') <= ord(ch) <= ord('Z'): #Converts letters into values and checks whether they are between A and Z
            kod = ord(ch) - klucz1          #Subtracts the value of the key from the value of a given letter, which results in a new letter
        if kod < ord('A'):                  #If the value of a letter is less than the value of 'A' it subtracts from 'Z'
            kod += 26
        odszyfrowany += chr(kod)
    l.config(text=odszyfrowany)

klucz2 = ["BACDFEHGJILKNMORSTPWUVYXZ", "ZXYVUWPTSROMNKLIJGHEFDCAB"]
def szyfruj2():
    g = e.get()
    z = g.upper()
    z = z.replace(" ", "")  #Omits the spaces in the text to be encrypted
    zaszyfrowany = ""
    if len(z) % 2 != 0:     #Checks whether the text is even in length, if not, it adds an X to it
        p = 0
    while p < len(z):
        a1 = z[p]           #Assigning to a1 a given letter from the text you type
        if p + 1 < len(z):
            a2 = z[p + 1]   #Assigning to a2 the text you type in
            p += 2
        g1 = a1
        g2 = a2
        idx1 = klucz2[0].find(a1)   #Assign to idx1 the position in the first square of the letter with a1
        idx2 = klucz2[1].find(a2)   #Assigning to idx2 a position in the second square on which the letter from a2 is located

        if math.floor(idx1/5) != math.floor(idx2/5):
            g1 = klucz2[0][((5 * math.floor(idx2/5)) + idx1 % 5)]   #Assigning to g1 a letter from the first square in place of the result of an action
            g2 = klucz2[1][((5 * math.floor(idx1/5)) + idx2 % 5)]   #Assigning to g2 a letter from the first square in place of the result of an action

        zaszyfrowany = zaszyfrowany + g1
        zaszyfrowany = zaszyfrowany + g2

    l.config(text=zaszyfrowany)

def deszyfruj2():       #The same as in szyfruj2(), with a slight exception at the end
    f = e.get()
    z = f.upper()
    zaszyfrowany = ""
    if len(z) % 2 != 0:
        z += "X"
    p = 0
    while p < len(z):
        a1 = z[p]
        if p + 1 < len(z):
            a2 = z[p + 1]
            p += 2
        g1 = a1
        g2 = a2

        idx1 = klucz2[0].find(a1)
        idx2 = klucz2[1].find(a2)
        if idx2 == -1:
            idx2 = -idx2
        if math.floor(idx1/5) != math.floor(idx2/5):
            g1 = klucz2[0][((5 * math.floor(idx2/5)) + idx1 % 5)]
            g2 = klucz2[1][((5 * math.floor(idx1/5)) + idx2 % 5)]

        zaszyfrowany = zaszyfrowany + g1
        zaszyfrowany = zaszyfrowany + g2
        if zaszyfrowany[-1] is 'X':                 #Delete X at the end of the deciphered text
            zaszyfrowany = zaszyfrowany[:-1]
    l.config(text=zaszyfrowany)

def szyfruj3():
    tekst1 = e.get()
    klucz3 = s1.get()
    tekst = tekst1.upper()
    zaszyfrowany = ""
    tabelaplotek = [None]*klucz3        #Creates a 3-element keyboard filled with None
    a = 0
    i = len(tekst)
    while a < klucz3:                   #Replaces the None board with an i-element board
        tabelaplotek[a] = [None] * i
        a += 1
    r = 0
    kierunek = 1
    a = 0
    for c in range(len(tekst1)):
        tabelaplotek[r][a] = tekst[c]   #Assign a letter from the text to the appropriate place in the relevant table in the 'tabelaplotek'
        if (r == klucz3 - 1) & (kierunek == 1) | (r == 0) & (kierunek == -1):  #Verification to which table assign a letter
            kierunek = -kierunek
            a += 1
        r += kierunek
    for x in range(klucz3):
        poz = 0
        while poz < len(tekst):
            if tabelaplotek[x][poz] is None:        #Removes None
                tabelaplotek[x][poz] = ''
            zaszyfrowany = zaszyfrowany + tabelaplotek[x][poz]  #Writes into encrypted letters from the "tabelaplotek"
            poz += 1
    l.config(text=zaszyfrowany)

def deszyfruj33(): #Auxiliary code for decryption of the hurdle code. Encrypts the message with a user-selectable hurdle code
    tekst = e.get()
    klucz = s1.get()

    tabelaplotek = [None]*klucz
    a = 0
    i = len(tekst)
    while a < klucz:
        tabelaplotek[a] = [None]*i
        a += 1
    r = 0
    kierunek = 1
    a = 0
    for c in range(len(tekst)):
        tabelaplotek[r][a] = [ c , tekst[c] ]
        if(r == klucz - 1) & (kierunek == 1) | ( r == 0) & (kierunek == -1):
            kierunek = -kierunek
            a += 1
        r += kierunek

    asd = 0
    tabliczka = [None]*i
    s = 0
    for x in range(klucz):
        for y in range(i):
            if tabelaplotek[x][y] is None:
                asd += 1
            else:
                tabliczka[s] = tabelaplotek[x][y]
                s += 1



    return tabliczka
def deszyfruj3():
    tekst = e.get()
    zaszyfrowany3 = ''
    tabliczkatekstu = [None]*len(tekst)         #It makes us tables filled in with None with the number of elements of a row length of encrypted cardboard
    for x in range(len(tekst)):                 #It creates a number of two-part tables equal to the length of the encrypted text in the table
        tabliczkatekstu[x] = [None]*2
        tabliczkatekstu[x] = [ x , tekst[x] ]   #Indexing of letters

    tabliczkaiksu = deszyfruj33()               #Assigning the typed text encrypted to a bar, also having indexes assigned to each letter
    i = len(tekst)
    tabliczkaczekoladek = [None]*i



    for x in range(i):
        for y in range(i):
            if tabliczkatekstu[x][0] == tabliczkaiksu[y][0]:    #Checks whether the index of the letter in the "bar index" is equal to the index of the letter in the "tabliczkaiksu"
                tabliczkaczekoladek[x] = tabliczkatekstu[y][1]  #If so, he will assign this letter to place x
    for x in range(i):
        zaszyfrowany3 += tabliczkaczekoladek[x]
    l.config(text = zaszyfrowany3)


main = tkinter.Tk()
l = tkinter.Label(main, text="Wprowadz tekst")
l1 = tkinter.Label(main, text="Wprowadz klucz dla przestawieniowego:")
l2 = tkinter.Label(main, text="Wprowadz klucz dla plotkowego:")
l3 = tkinter.Label(main, text = "Szyfr Dwukwadratowy:")
e = tkinter.Entry(main, justify="center")
s = tkinter.Scale(main, orient="horizontal", from_=0, to=25)
s1 = tkinter.Scale(main, orient="horizontal", from_=2, to=7)
b = tkinter.Button(main, text="Zakończ", command=wyjdz)
b1 = tkinter.Button(main, text="Szyfrowanie Podstawieniowy", command=szyfruj1)
b2 = tkinter.Button(main, text="Deszyfracja Podstawieniowy", command=deszyfruj1)
b3 = tkinter.Button(main, text="Szyfrowanie Dwukwadratowy", command=szyfruj2)
b4 = tkinter.Button(main, text="Deszyfracja Dwukwadratowy", command=deszyfruj2)
b5 = tkinter.Button(main, text="Szyfrowanie Plotkowy", command=szyfruj3)
b6 = tkinter.Button(main, text="Deszyfrowanie Plotkowy", command=deszyfruj3)

l.pack()
e.pack()
l1.pack()
s.pack()
b1.pack()
b2.pack()
l2.pack()
s1.pack()
b5.pack()
b6.pack()
l3.pack()
b3.pack()
b4.pack()
b.pack(side = "bottom")

main.mainloop()
