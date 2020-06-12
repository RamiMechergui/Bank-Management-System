from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from random import randint
import csv
#**********************************************************About*********************************************************
def forget(widget):
    widget.forget()
def retrieve(widget):
    widget.pack(side='bottom', fill='both', expand='no', pady=80)
#*****************************************************Operations Class***************************************************
class Operations :
    def __init__(self,window,logo,Name,ID,Type,Balance):
        self.New_Name=StringVar()
        self.Deposit_Amount_var = IntVar()
        self.Deposit_Amount_var.set(0)
        self.Withdraw_Amount_var = StringVar()
        self.Withdraw_Amount_var.set('0')
        self.Name=StringVar()
        self.Name.set(Name)
        self.ID=StringVar()
        self.ID.set(ID)
        self.Type=StringVar()
        self.Type.set(Type)
        self.Balance=StringVar()
        self.Balance.set(Balance)
        self.logo = logo
        self.chb1variable=StringVar()
        self.chb2variable=StringVar()
        self.chb1variable.set('0')
        self.chb2variable.set('0')
        self.window=window
        self.Lb=LabelFrame(self.window,text='Operations to pursue',bg='#87CEFA',bd=4,highlightthickness=3,relief=RAISED,highlightcolor='#008000',highlightbackground='#00BFFF',font=('Times New Roman',18,'bold','italic'))
        self.Lb.pack(padx=500,pady=140,expand='yes',fill='both')
        self.NameLabel=Label(self.Lb, text='Name  :',font=('Times New Roman', 15, 'bold', 'italic'), bg='#87CEFA', bd=4)
        self.NameLabel.place(relx=0.01,y=50)
        self.NameEn=Entry(self.Lb,justify='center',bg='#D9D7E3',font=('Times New Roman',13,'bold','italic'),textvariable=self.Name,state='readonly')
        self.NameEn.place(relx=0.4,y=60)
        self.IDLabel = Label(self.Lb,text='Identification \n Number : ', font=('Times New Roman', 15, 'bold', 'italic'), bg='#87CEFA', bd=4)
        self.IDLabel.place(relx=0.01, y=108)
        self.IDEn = Entry(self.Lb,bg='#D9D7E3',justify='center',font=('Times New Roman', 13, 'bold', 'italic'),textvariable=self.ID,state='readonly')
        self.IDEn.place(relx=0.4,y=120)
        self.OperationLabel = Label(self.Lb, text='Operation to pursue : ',font=('Times New Roman', 15, 'bold', 'italic'), bg='#87CEFA', bd=4)
        self.OperationLabel.place(x=10,y=170)
        self.EnterButton=Button(self.Lb,text='Pursue the operation --> ',font=('Times New Roman', 13, 'bold', 'italic'),activebackground='blue',command = lambda:self.PURSUEOPERATIONFN())
        self.EnterButton.place(x=150,y=375)
        self.OperationCombobox=ttk.Combobox(self.Lb,values=('Deposit','withdraw','Update an account','close an account'))
        self.OperationCombobox.place(x=200,y=175)
        self.OperationCombobox.bind("<<ComboboxSelected>>",self.Call)
        self.BackButton = Button(self.Lb, image=self.logo, activebackground='green',command=lambda : self.Mainwelcome(self.Lb))
        self.BackButton.place(x=10, y=10)
        self.Choicelabel = Frame(self.Lb, bg='#87CEFA', width=100, height=100)
        self.Choicelabel.pack(side='bottom', fill='both', expand='no', pady=90)
        self.Quitlogo = PhotoImage(file='Exit.png')
        self.QuitButton = Button(self.Lb, image=self.Quitlogo, activebackground='green',command=lambda: self.QuitFN())
        self.QuitButton.place(x=300, y=10)

    def QuitFN(self):
        Ms = messagebox.askquestion('Quitting', 'Did you want really to quit Bank Management System')
        if Ms == 'yes':
            self.window.destroy()
    def PURSUEOPERATIONFN(self):
        if self.OperationCombobox.current() == -1 :
            Message = messagebox.showerror('Error','Choose one of operations to pursue')
        elif self.OperationCombobox.get() == 'Deposit':
            M=str(self.Deposit_Amount_var.get())
            if M == '0' :
               Message = messagebox.showerror('Error', 'Put the amount to deposit')
            elif M.isdigit() != True :
               Message = messagebox.showerror('Error', 'Put a numerical amount')
            else :
                K=int(self.Balance.get())
                O=self.Balance.get()
                R=K+self.Deposit_Amount_var.get()
                self.Balance.set(R)
                Message = messagebox.showinfo('Congratulations', 'The amount of money has been \n successfully desposited ')
                self.Deposit_Amount_var.set(0)
                with open('Bank Data.csv','r', newline='') as file:
                    P=file.read()
                with open('Bank Data.csv', 'w',newline='') as file:
                    F=self.Name.get()+','+self.ID.get()+','+self.Type.get()+','+O
                    U=str(self.Balance.get())
                    T=self.Name.get()+','+self.ID.get()+','+self.Type.get()+','+U
                    I=P.replace(F,T)
                    file.write(I)
        elif self.OperationCombobox.get() == 'withdraw' :
            if self.Withdraw_Amount_var.get().isdigit() != True :
                Message = messagebox.showerror('Error', 'Put a numerical amount')
                self.Withdraw_Amount_var.set('0')
            elif self.Withdraw_Amount_var.get() == '0' :
                Message = messagebox.showerror('Error', 'Put the amount to withdraw')
                self.Withdraw_Amount_var.set('0')
            elif int(self.Withdraw_Amount_var.get()) < 0 :
                Message = messagebox.showerror('Error', 'Put a positive amount')
                self.Withdraw_Amount_var.set('0')
            elif self.Withdraw_Amount_var.get().isdigit() != True :
                Message = messagebox.showerror('Error', 'Put a numerical amount')
                self.Withdraw_Amount_var.set('0')
            elif int(self.Withdraw_Amount_var.get()) > int(self.Balance.get()) :
                Message = messagebox.showerror('Error', 'Put an amount inferior to your balance')
                self.Withdraw_Amount_var.set('0')
            else :
                K=int(self.Withdraw_Amount_var.get())
                R=int(self.Balance.get())
                Actual_balance =R-K
                N=str(Actual_balance)
                with open('Bank Data.csv','r', newline='') as file:
                    P=file.read()
                with open('Bank Data.csv', 'w',newline='') as file:
                    F =self.Name.get()+','+self.ID.get()+','+self.Type.get()+','+self.Balance.get()
                    Y =self.Name.get()+','+self.ID.get()+','+self.Type.get()+','+str(Actual_balance)
                    d=P.replace(F,Y)
                    file.write(d)
                    self.Withdraw_Amount_var.set('0')
                    self.Balance.set(N)
                    Message = messagebox.showinfo('Congratulations','The amount of money has been \n successfully withdrawed ')
        elif self.OperationCombobox.get() == 'Update an account' :
            Condition1=False
            Condition2=False
            R=self.New_Name.get().replace(' ','')
            if self.New_Name.get() == '' and self.chb2variable.get() == '0' and self.chb1variable.get() == '0' :
                Message = messagebox.showerror('Error','You cannot puruse this operation')
            elif R.isalpha() == False :
                Message = messagebox.showerror('Error','Choose an alphabetic Name ')
            elif True :
                    if   self.New_Name != '' :
                         with open('Bank Data.csv','r', newline='') as file:
                              P=file.read()
                         with open('Bank Data.csv', 'w',newline='') as file:
                              F = self.Name.get() + ',' + self.ID.get() + ',' + self.Type.get() + ',' + self.Balance.get()
                              Y = self.New_Name.get() + ',' + self.ID.get() + ',' + self.Type.get() + ',' + self.Balance.get()
                              d = P.replace(F,Y)
                              file.write(d)
                              self.Name.set(self.New_Name.get())
                    if self.chb1variable.get() != '0':
                          with open('Bank Data.csv','r', newline='') as file:
                              P=file.read()
                          with open('Bank Data.csv', 'w',newline='') as file:
                             F = self.Name.get() + ',' + self.ID.get() + ',' + self.Type.get() + ',' + self.Balance.get()
                             Y = self.Name.get() + ',' + self.ID.get() + ',' + self.chb1variable.get() + ',' + self.Balance.get()
                             d = P.replace(F,Y)
                             file.write(d)
                             self.Type.set(self.chb1variable.get())
                    elif self.chb2variable.get() != '0':
                          with open('Bank Data.csv','r', newline='') as file:
                             P=file.read()
                          with open('Bank Data.csv', 'w',newline='') as file:
                             F = self.Name.get() + ',' + self.ID.get() + ',' + self.Type.get() + ',' + self.Balance.get()
                             Y = self.Name.get() + ',' + self.ID.get() + ',' + self.chb2variable.get() + ',' + self.Balance.get()
                             d = P.replace(F,Y)
                             file.write(d)
                             self.Type.set(self.chb2variable.get())
                    Message = messagebox.showinfo('Error', 'Your changes have been made ')
        elif self.OperationCombobox.get() == 'close an account' :
            with open('Bank Data.csv', 'r',newline='') as file:
                P = file.read()
            with open('Bank Data.csv', 'w',newline='') as file:
                F = self.Name.get() + ',' + self.ID.get() + ',' + self.Type.get() + ',' + self.Balance.get()
                Y = ''
                d = P.replace(F, Y)
                file.write(d)
                Message = messagebox.showinfo('Info','Your account has been deleted')
    def Mainwelcome(self,widget):
        self.widget=widget
        self.widget.forget()
        A=Welcome(self.window)
    def forget(widget):
        widget.forget()
    def Call(self,event):
        if self.OperationCombobox.get() == 'Deposit' :
            self.Choicelabel.forget()
            self.Choicelabel = Frame(self.Lb, bg='#87CEFA', width=100, height=100)
            self.Choicelabel.pack(side='bottom', fill='both', expand='no', pady=80)
            self.DepositLabel = Label(self.Choicelabel, text='Actual balance  : ',font=('Times New Roman', 15, 'bold', 'italic'), bg='#87CEFA', bd=4)
            self.DepositLabel.place(x=8,y=3)
            self.DepositAmountLabel = Label(self.Choicelabel, text='Amount to deposit  : ',font=('Times New Roman', 15, 'bold', 'italic'), bg='#87CEFA', bd=4)
            self.DepositAmountLabel.place(x=6, y=40)
            self.DepositEn = Entry(self.Choicelabel, bg='#D9D7E3', justify='center', font=('Times New Roman', 13, 'bold', 'italic'),textvariable=self.Balance, state='readonly', width=13)
            self.DepositEn.place(x=210,y=6)
            self.DepositAmountEn = Entry(self.Choicelabel, bg='#D9D7E3', justify='center', textvariable=self.Deposit_Amount_var,font=('Times New Roman', 13, 'bold', 'italic'), width=13)
            self.DepositAmountEn.place(x=210,y=44)
        elif self.OperationCombobox.get() == 'withdraw' :
            self.Choicelabel.forget()
            self.Choicelabel = Frame(self.Lb, bg='#87CEFA', width=100, height=100)
            self.Choicelabel.pack(side='bottom', fill='both', expand='no', pady=80)
            self.WithdrawLabel = Label(self.Choicelabel, text='Actual balance  : ',font=('Times New Roman', 15, 'bold', 'italic'), bg='#87CEFA', bd=4)
            self.WithdrawLabel.place(x=6,y=3)
            self.WithdrawAmountLabel = Label(self.Choicelabel, text='Amount to withdraw: ',font=('Times New Roman', 15, 'bold', 'italic'), bg='#87CEFA', bd=4)
            self.WithdrawAmountLabel.place(x=6, y=40)
            self.WithdrawEn = Entry(self.Choicelabel, bg='#D9D7E3', justify='center',font=('Times New Roman', 13, 'bold', 'italic'),textvariable=self.Balance, state='readonly', width=13)
            self.WithdrawEn.place(x=210,y=6)
            self.WithdrawAmountEn = Entry(self.Choicelabel, bg='#D9D7E3', justify='center', textvariable=self.Withdraw_Amount_var,font=('Times New Roman', 13, 'bold', 'italic'), width=13)
            self.WithdrawAmountEn.place(x=210,y=44)
        elif self.OperationCombobox.get() == 'Update an account' :
            self.Choicelabel.forget()
            self.Choicelabel = Frame(self.Lb, bg='#87CEFA', width=100, height=100)
            self.Choicelabel.pack(side='bottom', fill='both', expand='no', pady=80)
            self.ChangeNameLabel = Label(self.Choicelabel, text='Put new name : ',font=('Times New Roman', 15, 'bold', 'italic'), bg='#87CEFA', bd=4)
            self.ChangeNameLabel.place(x=6, y=3)
            self.NewNameEn = Entry(self.Choicelabel, bg='#D9D7E3', justify='center',font=('Times New Roman', 13, 'bold', 'italic'),textvariable=self.New_Name, width=13)
            self.NewNameEn.place(x=210, y=6)
            self.ChangeNameLabel = Label(self.Choicelabel, text='The new type\nof your account ',font=('Times New Roman', 15, 'bold', 'italic'), bg='#87CEFA', bd=4)
            self.ChangeNameLabel.place(x=3, y=45)
            self.Type1Checkbutton = Checkbutton(self.Choicelabel, text='Current\nAccount', bg='#87CEFA',font=('Times New Roman', 15, 'bold', 'italic'),onvalue='C',offvalue='0',highlightcolor='#87CEFA',variable=self.chb1variable, command=lambda: self.chb2variable.set('0'))
            self.Type1Checkbutton.place(x=150, y=45)
            self.Type2Checkbutton = Checkbutton(self.Choicelabel, text='Saving\nAccount', bg='#87CEFA',font=('Times New Roman', 15, 'bold', 'italic'),onvalue='S', offvalue='0', highlightcolor='#87CEFA',variable=self.chb2variable, command=lambda: self.chb1variable.set('0'))
            self.Type2Checkbutton.place(x=250, y=45)
        elif self.OperationCombobox.get() == 'close an account' :
            self.Choicelabel.forget()
#***************************************Create Account Class ***********************************************************
class CreateAccount :
     def __init__(self,window,logo):
        self.chb1variable=StringVar()
        self.chb1variable.set('0')
        self.chb2variable=StringVar()
        self.chb2variable.set('0')
        self.Name = StringVar()
        self.Name.set('Put your name here ')
        self.ID=IntVar()
        self.ID.set('Automatically Generated')
        self.logo = logo
        self.window=window
        self.Lb=LabelFrame(self.window,text='Create Account Page',bg='#87CEFA',bd=4,highlightthickness=3,relief=RAISED,highlightcolor='#008000',highlightbackground='#00BFFF',font=('Times New Roman',18,'bold','italic'))
        self.InitialAmmountvar=IntVar()
        self.Lb.pack(padx=430, pady=160, expand='yes', fill='both')
        self.NameLabel = Label(self.Lb, text='Name  :', font=('Times New Roman', 15, 'bold', 'italic'), bg='#87CEFA',bd=4)
        self.NameLabel.place(relx=0.01, rely=0.18)
        self.NameEn = Entry(self.Lb,fg='gray',bg='#D9D7E3',justify='center',font=('Times New Roman', 13, 'bold', 'italic'),highlightcolor='white',textvariable=self.Name)
        self.NameEn.place(relx=0.4, rely=0.201)
        self.NameEn.bind("<Button-1>", self.callback)
        self.IDLabel = Label(self.Lb, text='Identification \n Number : ',
                             font=('Times New Roman', 15, 'bold', 'italic'), bg='#87CEFA', bd=4)
        self.IDLabel.place(relx=0.01, rely=0.32)
        self.IDEn = Label(self.Lb, bg='#87CEFA',justify='center',font=('Times New Roman', 13, 'bold', 'italic'),highlightcolor='white',textvariable=self.ID)
        self.IDEn.place(relx=0.4, rely=0.35)
        self.TypeofAccountLabel = Label(self.Lb, text='Type of account :', font=('Times New Roman', 15, 'bold', 'italic'), bg='#87CEFA',bd=4)
        self.TypeofAccountLabel.place(x=10,y=190)
        self.Type1Checkbutton=Checkbutton(self.Lb,text='Current Account',bg='#87CEFA',font=('Times New Roman', 13, 'bold', 'italic')
                                          ,onvalue='C',offvalue='0',highlightcolor='#87CEFA',variable=self.chb1variable,command= lambda : self.chb2variable.set('0'))
        self.Type1Checkbutton.place(x=190,y=190)
        self.Type2Checkbutton = Checkbutton(self.Lb, text='Saving Account',bg='#87CEFA',font=('Times New Roman', 13, 'bold', 'italic')
                                            ,onvalue='S',offvalue='0',highlightcolor='#87CEFA',variable=self.chb2variable,command=lambda: self.chb1variable.set('0'))
        self.Type2Checkbutton.place(x=340,y=190)
        self.TheinitialAmmountLabel = Label(self.Lb, text='The initial amount (TND) :',font=('Times New Roman', 13, 'bold', 'italic'), bg='#87CEFA',bd=4)
        self.TheinitialAmmountLabel.place(x=10, y=240)
        self.TheinitialAmmountEn = Entry(self.Lb, bg='#D9D7E3',justify='center',font=('Times New Roman', 15, 'bold', 'italic'),width='18',highlightcolor='white',textvariable=self.InitialAmmountvar)
        self.TheinitialAmmountEn.place(x=200,y=243)
        self.CreaAccButton = Button(self.Lb, text='Create a new Account ',font=('Times New Roman', 13, 'bold', 'italic'), activebackground='green',command = lambda:self.Verif())
        self.CreaAccButton.place(x=205,y=290)
        self.BackButton = Button(self.Lb, image=self.logo, activebackground='green',command=lambda : self.Mainwelcome(self.Lb))
        self.BackButton.place(x=12 , y=10)
        self.Quitlogo = PhotoImage(file='Exit.png')
        self.QuitButton = Button(self.Lb, image=self.Quitlogo, activebackground='green',
                                 command=lambda: self.QuitFN())
        self.QuitButton.place(x=440, y=10)

     def QuitFN(self):
         Ms = messagebox.askquestion('Quitting', 'Did you want really to quit Bank Management System')
         if Ms == 'yes':
             self.window.destroy()
     def callback(self,event):
        self.NameEn.config(fg='black',bg='#D9D7E3',justify ='center',font = ('Times New Roman',13,'bold','italic'))
        self.Name.set('')
     def Mainwelcome(self,widget):
        self.widget=widget
        self.widget.forget()
        A=Welcome(self.window)
     def Save(self,ls):
         self.ls=ls
         with open('Bank Data.csv','a+',newline='') as file :
             fdnames=['Name','ID','Type','Balance']
             writer = csv.DictWriter(file,fieldnames=fdnames)
             writer.writerow(self.ls)
     def Verif(self):
        self.R = self.Name.get().upper()
        self.Name.set(self.R)
        l=len(self.R)
        f=self.R.replace(' ','')
        print(f)
        if f.isalpha() == False :
           Message=messagebox.showinfo('Error','Put an alphabetic Name')
           self.Name.set('')
        elif self.chb1variable.get() =='0' and self.chb2variable.get() =='0':
           self.Type1Checkbutton.flash()
           self.Type2Checkbutton.flash()
           Message = messagebox.showinfo('Error', 'Check the type of your account ')
        elif self.chb1variable.get() == 'C' and self.InitialAmmountvar.get() < 200 :
           if  self.InitialAmmountvar.get() == 0:
                Message = messagebox.showinfo('Error', 'Put the initial amount')
           else :
                Message = messagebox.showinfo('Error', 'Your initial ammount should be superior to 200 TND')
        elif self.chb2variable.get() == 'S' and self.InitialAmmountvar.get() < 500 :
           if  self.InitialAmmountvar.get() == 0:
                Message = messagebox.showinfo('Error', 'Put the initial amount')
           else :
                Message = messagebox.showinfo('Error', 'Your initial ammount should be superior to 500 TND')
        else :
            self.ID.set(randint(10000, 99999))
            Message = messagebox.showinfo('YOU ARE WELCOME', 'Your account has been created successfully')

            if self.chb1variable.get() == 'C':
               M = self.chb1variable.get()
            else :
               M = self.chb2variable.get()
            self.ls={'Name':self.Name.get(),'ID':self.ID.get(),'Type' : M,'Balance':self.InitialAmmountvar.get()}
            x=self.Save(self.ls)

#********************************************Welcome Class***************************************************************
class Welcome():
    def __init__(self,window):
        self.Textv=StringVar()
        self.Type=StringVar()
        self.Balance=StringVar()
        self.Quitlogo=PhotoImage(file='Exit.png')
        self.logo=PhotoImage(file='Back Button.png')
        self.window=window
        self.Name = StringVar()
        self.ID = StringVar()
        self.Lb=LabelFrame(self.window,text='Welcome Page',bg='#87CEFA',bd=4,highlightthickness=3,relief=RAISED,highlightcolor='#008000',highlightbackground='#00BFFF',font=('Times New Roman',18,'bold','italic'))
        self.Lb.pack(padx=500,pady=200,expand='yes',fill='both')
        self.BackButton = Button(self.Lb, image=self.logo, activebackground='green',
                                 command=lambda: self.Mainwelcome(self.Lb))
        self.BackButton.place(x=12, y=10)
        self.QuitButton = Button(self.Lb, image=self.Quitlogo, activebackground='green',
                                 command=lambda: self.QuitFN())
        self.QuitButton.place(x=290, y=10)
        self.NameLabel=Label(self.Lb, text='Name  :', font=('Times New Roman', 15, 'bold', 'italic'), bg='#87CEFA', bd=4)
        self.NameLabel.place(relx=0.01, rely=0.18)
        self.NameEn=Entry(self.Lb,bg='#D9D7E3',font=('Times New Roman',13,'bold','italic'),textvariable=self.Name)
        self.NameEn.place(relx=0.4,rely=0.201)
        self.IDLabel = Label(self.Lb, text='Identification \n Number : ', font=('Times New Roman', 15, 'bold', 'italic'), bg='#87CEFA', bd=4)
        self.IDLabel.place(relx=0.01, rely=0.45)
        self.IDEn = Entry(self.Lb, bg='#D9D7E3', font=('Times New Roman', 13, 'bold', 'italic'),textvariable=self.ID)
        self.IDEn.place(relx=0.4, rely=0.5)
        self.EnterButton=Button(self.Lb,text='Enter',font=('Times New Roman', 13, 'bold', 'italic'),activebackground='blue',command=lambda : self.Check())
        self.EnterButton.place(x=270,rely=0.8)
        with open('Bank Data.csv', 'r',newline='') as file:
            f=file.read()
        self.CreaAccButton = Button(self.Lb, text='Create a new Account ', font=('Times New Roman', 13, 'bold', 'italic'),activebackground='green',command=lambda : self.CreaAccounfn(self.Lb))
        self.CreaAccButton.place(x=60, rely=0.8)
        self.ListAllAccounts = Button(self.window, text='List all accounts',font=('Times New Roman', 13, 'bold', 'italic'),activebackground='green')
        self.ListAllAccounts.place(relx=0.9, y=0)
        self.Hide=Button(self.window, text='Hide All Accounts',font=('Times New Roman', 13, 'bold', 'italic'), activebackground='green')
        self.Hide.place(relx=0.79, y=0)
        self.Hide.bind('<Button 1>', self.HideList)
        self.AlllistLabel = Label(self.window, font=('Times New Roman', 13, 'bold', 'italic'),bg='#87CEFA', textvariable=self.Textv, bd=4)
        self.AlllistLabel.place(relx=0.78, y=35)
        self.ListAllAccounts.bind('<Button 1>',self.ListAccounts)

    def ListAccounts(self, event):
        self.AlllistLabel.place(relx=0.78, y=35)
        with open('Bank Data.csv', 'r', newline='') as file:
            f = file.read()
        self.Textv.set(f)

    def HideList(self,event):
        self.AlllistLabel.place_forget()

    def QuitFN(self):
       Ms=messagebox.askquestion('Quitting','Did you want really to quit Bank Management System')
       if Ms == 'yes':
          self.window.destroy()

    def Check(self):
        if self.Name.get() == '':
            Message = messagebox.showinfo('Erro', ' Try to put the User name')
        elif self.ID.get() == '':
            Message = messagebox.showinfo('Erro', ' Try to put the identification number')
        else :
           with open('Bank Data.csv','r+',newline='') as file:
                 Ch=False
                 reader=csv.DictReader(file)
                 for row in reader :
                     if row['Name'] == self.Name.get() and row['ID'] == self.ID.get() :
                        Ch=True
                        self.Type.set(row['Type'])
                        self.Balance.set(row['Balance'])
           if Ch == False :
               Message = messagebox.showinfo('Error', 'Check The user Name and the identification number')
           else:
               x=self.Enterfn(self.Lb)
    def Enterfn(self,widget):
        self.widget=widget
        self.widget.forget()
        B=Operations(window,self.logo,self.Name.get(),self.ID.get(),self.Type.get(),self.Balance.get())
    def CreaAccounfn(self, widget):
        self.widget = widget
        self.widget.forget()
        B = CreateAccount(window,self.logo)


#********************************************************New Project*****************************************************
class NewProject:
      def __init__(self):
          window = Tk()
          Mn = Menu(window)
          def click():
              NewPr = NewProject()
          file = Menu(Mn, tearoff=0)
          Edit = Menu(Mn, tearoff=0)
          View = Menu(Mn, tearoff=0)
          Tools = Menu(Mn, tearoff=0)
          Help = Menu(Mn, tearoff=0)
          Mn.add_cascade(label='File', menu=file)
          file.add_command(label='New Project', command=click)
          file.add_command(label='Open')
          file.add_command(label='Settings')
          file.add_command(label='Exit', command=window.destroy)
          Mn.add_cascade(label='Edit', menu=Edit)
          Edit.add_command(label='Copy')
          Edit.add_command(label='Paste')
          Edit.add_command(label='Delete')
          Mn.add_cascade(label='View', menu=View)
          View.add_command(label='Tool Window')
          View.add_command(label='Appearance')
          View.add_command(label='Zoom')
          Mn.add_cascade(label='Tools', menu=Tools)
          Tools.add_command(label='Tasks & Context')
          Tools.add_command(label='Annual report')
          Tools.add_command(label='Monthly report')
          Tools.add_command(label='Daily report')
          Mn.add_cascade(label='Help', menu=Help)
          Help.add_command(label='About')
          f=open('Bank Data.csv', 'a', newline='')
          f.close()
          f=open('Bank Data.csv', 'r', newline='')
          M=f.readline()
          if M == '' :
              with open('Bank Data.csv', 'a+',newline='') as file:
                  fdnames = ['Name', 'ID', 'Type', 'Balance']
                  writer = csv.DictWriter(file, fieldnames=fdnames)
                  writer.writeheader()
          f.close()
          w, h = window.winfo_screenwidth(), window.winfo_screenheight()
          window.iconbitmap('Bank.ico')
          window.geometry("%dx%d+0+0" % (w, h))
          window.configure(bg='powder blue')
          window.title('Bank Management System')
          A = Welcome(window)
          window.configure(menu=Mn)
          window.mainloop()

#*********************************************************MainProgram****************************************************
window=Tk()
Mn=Menu(window)
def click():
    NewPr=NewProject()
file = Menu(Mn,tearoff=0)
Edit = Menu(Mn,tearoff=0)
View = Menu(Mn,tearoff=0)
Tools = Menu(Mn,tearoff=0)
Help = Menu(Mn, tearoff=0)
Mn.add_cascade(label='File',menu=file)
file.add_command(label='New Project',command=click)
file.add_command(label='Open')
file.add_command(label='Settings')
file.add_command(label='Exit',command = window.destroy)
Mn.add_cascade(label='Edit',menu=Edit)
Edit.add_command(label='Copy')
Edit.add_command(label='Paste')
Edit.add_command(label='Delete')
Mn.add_cascade(label='View',menu=View)
View.add_command(label='Tool Window')
View.add_command(label='Appearance')
View.add_command(label='Zoom')
Mn.add_cascade(label='Tools',menu=Tools)
Tools.add_command(label='Tasks & Context')
Tools.add_command(label='Annual report')
Tools.add_command(label='Monthly report')
Tools.add_command(label='Daily report')
Mn.add_cascade(label='About',menu=Help)
Help.add_command(label='About')
f=open('Bank Data.csv', 'a', newline='')
f.close()
f=open('Bank Data.csv', 'r', newline='')
M=f.readline()
if M == '' :
    with open('Bank Data.csv', 'a+',newline='') as file:
                  fdnames = ['Name', 'ID', 'Type', 'Balance']
                  writer = csv.DictWriter(file, fieldnames=fdnames)
                  writer.writeheader()
f.close()

w, h = window.winfo_screenwidth(), window.winfo_screenheight()
window.iconbitmap('Bank.ico')
window.geometry("%dx%d+0+0" % (w, h))
window.configure(bg='powder blue')
window.title('Bank Management System')
#window.state('zoomed')
window.resizable(0,0)
A=Welcome(window)
window.configure(menu=Mn)
window.attributes("-fullscreen", True)
def QUITMAINWINDOW():
    if messagebox.askokcancel("Quit","Did You Want to quit Bank Management System"):
        window.destroy()
window.protocol("WM_DELETE_WINDOW",QUITMAINWINDOW)
window.mainloop()
