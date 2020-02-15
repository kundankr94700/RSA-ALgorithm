from threading import *
from tkinter import *
from tkinter import messagebox
from tkinter.font import Font
from playsound import playsound
from time import *
from webbrowser import *

class th1(Thread):

    def run(self):

        def login():
            s1 = ss1.get()
            s2 = ss2.get()
            if s1 == 'Kundan' and s2 == 'Hello':

                class th3(Thread):
                    def run(self):
                        ss1.set('')
                        ss2.set('')
                        top1 = Toplevel()
                        top1.title("RSA Algorithm")

                        def pri(x, y):
                            for i in range(2, x):
                                if x % i == 0:
                                    p = 2
                                    break
                                else:

                                    p = 1
                            for pp in range(2, y):
                                if y % pp == 0:
                                    k = 2
                                    break
                                else:

                                    k = 1
                            return p, k

                        def gcd(a, b):
                            while b != 0:
                                a, b = b, a % b
                            return a

                        def mod(e, fi):
                            for x in range(1, fi ** 2):
                                if (e * x) % fi == 1:
                                    return x
                            return None

                        def encrypt(e, Message, n):

                            cipher = [((ord(char) ** e) % n) for char in Message]
                            return cipher

                        def decrypt(d, ciphertext, n):

                            plain = [(chr((char ** d) % n)) for char in ciphertext]

                            return ''.join(plain)

                        def we1():
                            open('https://drive.google.com/file/d/19Mb40DGOrCDOeqhzYGyETV87t0o-nfIA/view?usp=sharing')

                        def we2():
                            open('https://drive.google.com/file/d/11PoOgTenxSIfj85Zd3dCmXdHpe-b2brY/view?usp=sharing')

                        def message2():
                            ans1 = messagebox.askyesno("Exit", "DO You Want to Exit")
                            if ans1 == True:
                                top1.quit()

                        def next():
                            S1 = (SS1.get())
                            S2 = (SS2.get())
                            S3 = SS3.get()
                            if S1 == '' or S2 == '' or S3 == '':

                                top11 = Toplevel()
                                top11.title("RSA ALGORITHM")
                                top11.geometry("320x80+600+200")
                                l3 = Label(top11, text="Some Details are Not Entered \n please Fill all the details",
                                           fg='skyblue', font=f1).place(x=50, y=15)
                                playsound('add1.mp3')

                            else:
                                try:
                                    S1 = int(SS1.get())
                                    S2 = int(SS2.get())
                                except Exception as e:
                                    top8 = Toplevel()
                                    top8.title("RSA ALGORITHM ")
                                    top8.geometry("350x50+600+300")
                                    l = Label(top8, text=e, font=f3, fg='red').pack()

                                else:
                                    S3 = SS3.get()
                                    SS1.set('')
                                    SS2.set('')
                                    SS3.set('')
                                    x, y = pri(S1, S2)
                                    if x == 1 and y == 1:
                                        def mess():
                                            top2 = Toplevel()
                                            top2.title("RSA ALGORITHM")
                                            top2.geometry("800x100+300+200")
                                            cip = encrypt(e, S3, n)
                                            my_message = decrypt(d, cip, n)
                                            L31 = Label(top2, text=my_message + '                          ', font=f3,
                                                        fg='green').place(x=240, y=40)
                                            LL15 = Label(top2, text="Message After Decryption  :: ", font=f3,
                                                         fg='red').place(x=30, y=40)

                                        n = S1 * S2
                                        fi = (S1 - 1) * (S2 - 1)
                                        e = 1
                                        while True:
                                            if gcd(e, fi):
                                                break
                                            e = +1
                                        d = mod(e, fi)

                                        cip = encrypt(e, S3, n)
                                        L2 = Label(top1,text='   ' + str(cip) + '                                         ',
                                                   font=f3).place(x=135, y=400)

                                        BB3 = Button(top1, text=" Display Message ", command=mess, width=15, bg='Green',
                                                     fg='white',
                                                     font=f1).place(x=140, y=450)

                                    else:
                                        playsound('prime.mp3')





                        LL7 = Label(top1, text="Fill The details To Perform RSA Algorithm", fg='red', font=f1).place(
                            x=90, y=60)

                        LL1 = Label(top1, text="Enter 1st Prime Number :", font=f3).place(x=90, y=100)
                        LL2 = Label(top1, text="Enter 2nd Prime Number :", font=f3).place(x=90, y=130)
                        SS1 = StringVar()
                        SS2 = StringVar()
                        SS3 = StringVar()

                        EE1 = Entry(top1, width=10, textvariable=SS1).place(x=280, y=100)
                        EE2 = Entry(top1, width=10, textvariable=SS2).place(x=280, y=130)
                        LL3 = Label(top1, text="Enter Message You Want To Encrypt ::", font=f3).place(x=90, y=160)
                        EE3 = Entry(top1, width=38, textvariable=SS3, font=f3, show='*').place(x=90, y=200)

                        BB2 = Button(top1, text="Encrypt", command=next, width=30, bg='green', fg='white',
                                     font=f1).place(x=90, y=250)
                        BB1 = Button(top1, text="Exit", command=message2, width=30, bg='red', fg='white',
                                     font=f1).place(x=90, y=340)
                        BB3 = Button(top1, text="Theory", command=we2, width=15, bg='skyblue', fg='white',
                                     font=f1).place(x=90, y=300)
                        BB3 = Button(top1, text="Source Code", command=we1, width=15, bg='Black', fg='white',
                                     font=f1).place(x=240, y=300)

                        LL4 = Label(top1, text="Cipher Text Generated :: ", font=f3).place(x=50, y=400)
                        c1 = Canvas(top1, width=10, height=400, bg='orange')
                        c1.pack(side=LEFT)
                        c1 = Canvas(top1, width=30, height=400, bg='white')
                        c1.pack(side=LEFT)
                        c1 = Canvas(top1, width=30, height=400, bg='White')
                        c1.pack(side=RIGHT)
                        c1 = Canvas(top1, width=10, height=400, bg='orange')
                        c1.pack(side=RIGHT)

                        top1.geometry("500x500+550+100")
                class th4(Thread):
                    def run(self):
                        playsound('1234.mp3')

                t3=th3()
                t4=th4()
                t3.start()
                sleep(0.02)
                t4.start()

            elif s1 == '' and s2 == '':

                o1="Message: Please Enter Username and Password"
                playsound('sound3.mp3')
                L1=Label(root,text=o1,font=f3).place(x=130,y=320)
            else:
                o2="Please Enter valid Username Or Password"
                ss1.set('')
                ss2.set('')
                L2 = Label(root, text=o2, font=f3).place(x=130, y=320)
                playsound('sound4.mp3')
        def win():
            ans1 = messagebox.askyesno("Exit", "DO You Want to Exit")
            if ans1 == True:
                root.quit()

        p, k = 0, 0
        root = Tk()
        f1 = Font(family="Time New Roman", size=12, weight="bold",underline=1)
        f2 = Font(family="Time New Roman", size=15, weight="bold", underline=1)
        f3 = Font(family="Time New Roman", size=10, weight="bold")


        c1 = Canvas(root,width=100, height=400)
        c1.pack(side=LEFT)
        p1 = PhotoImage(file="1.png")
        c1.create_image(0, 0, image=p1)
        c1 = Canvas(root, width=30, height=400, bg='White')
        c1.pack(side=RIGHT)
        c1 = Canvas(root, width=10, height=400, bg='orange')
        c1.pack(side=RIGHT)
        root.title("RSA Algorithm")
        l3 = Label(root, text="RSA ALgorithm", fg='red', font=f2).place(x=180,y=30)
        l3 = Label(root, text=" Welcome", fg='red', font=f2).place(x=200, y=60)
        l3 = Label(root, text="Enter Username and Password", fg='red', font=f1).place(x=140,y=120)
        l3 = Label(root, text="Copyright @ Kundan Kumar & Team", fg='Blue').place(x=250, y=380)

        l1 = Label(root, text='Username', fg='Blue',font=f1).place(x=120,y=160)
        l2 = Label(root, text='Password', fg='Blue',font=f1).place(x=120,y=200)
        ss1=StringVar()
        ss2 = StringVar()
        e1 = Entry(root,textvariable=ss1).place(x=220,y=160)
        e2 = Entry(root,textvariable=ss2, show='*').place(x=220,y=200)
        b1 = Button(root, text='Login', command=login, width=30, height=1, bg='green', fg='white',font=f3).place(x=150,y=250)
        b3 = Button(root, text='Exit', command=win, width=30, height=1,font=f3).place(x=150,y=280)
        root.geometry("500x400+500+100")
        root.mainloop()

class th2(Thread):
    def run(self):
        playsound('rsa1.mp3')


t1=th1()
t2=th2()
t1.start()
sleep(0.1)
t2.start()
