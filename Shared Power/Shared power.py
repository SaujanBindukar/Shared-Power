from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import datetime

class User:
    def __init__(self):
        global register
        self.root=Tk()#creatig a window
        self.root.title('Shared Power')
        self.root.geometry('680x480+270+100')
        self.root.resizable(False,False)
        self.root.config(bg='#7E7E7E')
        frame=Frame(self.root)
        frame.config(bg='#7E7E7E')    
        self.p1=PhotoImage(file='login.png')
        Log=Button(frame,text='Login',image=self.p1,width=50,height=20,borderwidth=0,command=self.Login)
        Button.image2=self.p1#making an object so that the image doesn't get garbage collected
        Log.pack(side=RIGHT,fill=X,padx=50)
        self.z=PhotoImage(file='logo1.png')
        Label(frame,image=self.z,bg='#7E7E7E').pack(side=LEFT,fill=Y)
        Label.image=self.z
        Label(frame,text='Welcome to Shared Power',font=('Monotype Corsiva',30),bg='#7E7E7E').pack(side=LEFT,padx=20)
        
        frame.pack(fill=BOTH)
        frame2=Frame(self.root)
        self.P=PhotoImage(file='main1.png')
        Label(frame2,image=self.P,width=700,height=230,bg='#7E7E7E').pack(fill=BOTH)
        Label.main=self.P
        frame2.pack(fill=BOTH)
        frame1=Frame(self.root)
        Label(frame1,text='SharedPower is an information system to help tradesmen to share expensive and specialist tools rather than buying them themselves. Registered owners add details of the tools they have available including the per day and per half day rate for each unit and other users can hire the tools.',wraplength=650,justify=LEFT,font=('Times New Roman',12),bg='#7E7E7E').pack(padx=10)
        Label(frame1,text='Register now to start:',font=('Times New Roman',12),bg='#7E7E7E').pack()
        self.p3=PhotoImage(file='register.png')
        Register=Button(frame1,text='Register',image=self.p3,width=50,height=20,borderwidth=0,command=self.register)
        Button.image3=self.p3
        Register.pack(side=BOTTOM,pady=10)
        frame1.pack(fill=X,side=TOP)
        frame1.config(bg='#7E7E7E')
        
        self.root.mainloop()
    def register(self):#creates a register window
        global root
        global Mail
        global Pswd
        global name
        global first
        global last
        global DOB
        global r        
        
        self.root.destroy()#destroying a window
        self.root=Tk()#recreating a window
        
        self.root.geometry('680x480+270+100')
        self.root.resizable(False,False)
        self.root.title("register")
        self.root.configure(background='#7E7E7E')
        frame1=Frame(self.root)
        
        
        frame1.grid(sticky=W)
        Label(frame1, text="Register to be a part of us!",font=('Monotype Corsiva',20),bg='#7E7E7A').grid(row=0,column=1,padx=100)
        frame1.configure(background='#7E7E7E')
        back=Button(frame1,text="Sign In",font=('Times New Roman',12),bg='#7E7E7E',command=self.Login).grid(row=0,column=2,sticky=E,ipadx=5)
        self.image=PhotoImage(file='logo1.png')
        Label(frame1,image=self.image,background='#7E7E7E').grid(row=0,column=0,sticky=W)
        Label.me=self.image
        
        frame=Frame(self.root)
        frame.configure(background='#7E7E7E')        
        frame.grid(sticky=W,pady=30,padx=70)
        Label(frame, text='First Name',font=('Times New Roman',12),bg='#7E7E7E').grid(row=0,column=0,sticky=W)
        self.first=Entry(frame,bg='#8D8D8D')
        self.first.grid(row=0,column=1)
        
        Label(frame, text='Last Name',font=('Times New Roman',12),bg='#7E7E7E').grid(row=0,column=4,padx=20)
        self.last=Entry(frame,bg="#8D8D8D")
        self.last.grid(row=0,column=5)
        Label(frame, text='Date of Birth',font=('Times New Roman',12),bg='#7E7E7E').grid(row=1,column=0,sticky=W)
        self.DOB=Entry(frame,bg="#8D8D8D")
        self.DOB.grid(row=1,column=1,padx=12)
        
        Label(frame, text='Email',font=('Times New Roman',12),bg='#7E7E7E').grid(row=2,column=0,sticky=W)
        self.Mail=Entry(frame,bg="#8D8D8D")
        self.Mail.grid(row=2,column=1)
        
        Label(frame, text='Password',font=('Times New Roman',12),bg='#7E7E7E').grid(row=3,column=0,sticky=W)
      
        self.Pswd=Entry(frame,show="*",bg="#8D8D8D")
        self.Pswd.grid(row=3,column=1)
        
        self.val=StringVar()
        Label(frame, text='Gender',font=('Times New Roman',12),bg='#7E7E7E').grid(row=5,column=0,sticky=W)
        Radiobutton(frame, text='Male',value=1,font=('Times New Roman',12),bg='#7E7E7E',variable=self.val).grid(row=5,column=1,sticky=W)
        Radiobutton(frame,text='Female',value=0,font=('Times New Roman',12),bg='#7E7E7A',variable=self.val).grid(row=6,column=1,sticky=W)
        
        signup=Button(frame,text="Submit",font=('Times New Roman',12),bg='#7E7E7E',command=self.CheckReg).grid(row=8,column=1,sticky=W)

        
        frame.config(bg='#7E7E7E')
        self.root.mainloop()
    def CheckReg(self):#verifies registry inputs for errors and writes them to data.txt
        i=0
        if not self.Mail.get() or not self.Pswd.get() or not self.DOB or not self.first or not self.last:
            messagebox.showerror('Error','Fields are empty')
            i=1
        elif '@' not in self.Mail.get() or '.com'not in self.Mail.get():
            messagebox.showerror('Error','Invalid email')
            i=1
        else:
            for line in open('data.txt','r').readlines():#checking if email is already taken
                l=line.split()
                r=self.Mail.get().rstrip()
                if  r in l[0]:
                    messagebox.showerror('Error','Email taken')
                    i=1
                    break
        if i!=1:
            with open('data.txt','a') as user:#opening data.txt in append mode
                user.write(self.Mail.get())#writing data from register seperated by space
                user.write(' ')
                user.write(self.Pswd.get())
                user.write(' ')            
                user.write(self.first.get())
                user.write(' ')
                user.write(self.last.get())
                user.write(' ')
                user.write(self.DOB.get())
                user.write(' ')
                user.write(self.val.get())             
                user.write('\n')
                user.close()
            messagebox.showinfo('Info','You are now registered')
            self.Login()
    def Login(self):#creates a login window
        global root
        global pwd
        global namez
        global pwdz
        self.root.destroy()
        self.root= Tk ()
        self.root.title('Login')
        self.root.resizable(False,False)
        self.root.geometry("680x480+270+100")
        self.root.config(background='#7E7E7E')

        
        frame= Frame(self.root)
        frame.grid()
        frame.config(background='#7E7E7E')
        
        Label(frame, text="Login to SharedPower",font=('Monotype Corsiva',25),bg='#7E7E7E').grid(row=0,column=0,ipadx=225)
        self.image=PhotoImage(file='logo1.png')
        Label(frame,image=self.image,background='#7E7E7E').grid(row=0,column=0,sticky=W)
        Label.me=self.image        
        frame1=Frame(self.root)
        frame1.grid()
        frame1.config(background='#7E7E7E')
        
        Label(frame1, text="Email:       ",font=('Monotype Corosiva',15),bg='#7E7E7E').grid(row=1,column=1, pady=15,)
        self.name=Entry(frame1, bd=1,bg='#7E7E7E')
        self.name.grid(row=1,column=2, pady=25,ipadx=20)
        Label(frame1, text="Password:",font=('Monotype Corosiva',15),bg='#7E7E7E').grid(row=2,column=1, pady=15)
        self.pwd=Entry(frame1, show='*', bd=1,bg='#7E7E7A')
        self.pwd.grid(row=2,column=2, pady=25,ipadx=20)
        frame2=Frame(self.root)
        frame2.grid()
        Button(frame2, text="Login", height=1, width=10,bg='#7E7E7E',command=self.CheckLogin).grid(row=1,column=2)
        frame3=Frame(self.root)
        frame3.grid()    
        Label(frame3,text='Dont have an account?',bg='#7E7E7E').grid(row=1,column=3,sticky=N)
        Button(frame3, text="Sign Up", height=1, width=10,bg='#7E7E7E',command=self.register).grid(row=2,column=3,rowspan=2,sticky=S)
        frame3.config(bg='#7E7E7E')
             
        self.root.mainloop()
                 
    
        
    
    def CheckLogin(self):#reads registered email and password from data.txt and tallies with input email and password
        global ll
        c=0
        self.namez=self.name.get()
        self.pwdz=self.pwd.get()          
        ll=self.namez
        global pwdz
   
        for line in open('data.txt','r').readlines():#reading data.txt line by line
            self.linea=line.split()
            self.cname=self.linea[0].rstrip()
            self.cpwd=self.linea[1].rstrip()
        
            if self.namez==self.cname and self.pwdz==self.cpwd:#validating entered email and password
                ll=self.linea[0].rstrip()
                self.r=Tk()
                self.r.config(bg='#7E7E7E')
                c=1
                self.r.resizable(0,0)
                self.r.geometry('150x80+500+250')
                status=Label(self.r,text='\n[+] Login succesful',bg='#7E7E7E')
                status.pack()
                self.m=Searchtools
                self.ok=Button(self.r,text='Ok',bg='#7E7E7E',command=self.trans)
                self.ok.pack(ipadx=8)
                try:
                    self.root.destroy()
                except TclError:
                    pass
                self.r.mainloop()
                break
        if c!=1:
            messagebox.showerror('Error','Please input valid email and password')

  
    
    def trans(self):
        self.r.destroy()
        Searchtools()  
       
         
class Searchtools():
    
    def __init__(self):
        self.roota= Tk()
        self.roota.geometry('680x480+270+100')
        self.roota.resizable(False,False)
        self.roota.title("Shared Power")
        
        frame1=Frame(self.roota)
        
        frame1.configure(background='#7E7E7E')
        frame1.grid()
        
        
        Label(frame1, text="You are logged in to the Shared Power!",font=('Monotype Corsiva',20),bg='#7E7E7E').grid(row=0,column=0,padx=33)
        Button(frame1,text=" Sign out",font=('Times New Roman',12),bg='#7E7E7E',command=self.trans4).grid(row=0,column=1,sticky=E,padx=15)
        frame1.config(bg='#7E7E7E')
        frame2=Frame(self.roota)
        frame2.config(bg='#7E7E7E')
        frame2.grid(padx=200)

        self.machines=["Welding Machine", "Generator","Electric Motor","Driller"]#an option menu for 4 tools
        self.e=StringVar()
        self.e.set(self.machines[0])
        self.f=OptionMenu(frame2,self.e,*self.machines)
        self.f.grid(row=2,column=3,columnspan=2,sticky=W,pady=50)
        self.f.config(bg='#7E7E7E')
         
        
        Button(frame2, text='Search',font=('Times New Roman',12),bg='#7E7E7E',command=self.GetOption).grid(row=2,column=6,sticky=E,pady=50)
        if ll=='a@gmail.com':#for admin account
            Button(frame2, text='Monthly status',font=('Times New Roman',12),bg='#7E7E7E',command=self.checkStatus).grid(row=2,column=7,sticky=E,pady=50,padx=50)
        frame3=Frame(self.roota)
        frame3.configure(background='#7E7E7E')
        frame3.grid(sticky=W,pady=100)
        Label(frame3,text=" Do you want to add the tools?",bg='#7E7E7E',font=("Monotype Corsiva",15)).grid(row=1,column=0,sticky=W,padx=200)
        
        
        
        
        Button(frame3, text='Add tools!',font=('Times New Roman',12),bg='#7E7E7E',command=self.trans2).grid(row=2,column=0,sticky=W,padx=270)
        Label(frame3,text="Are you going to return the tools?",font=("Monotype Corsiva",15),bg='#7E7E7E').grid(row=3,column=0,padx=200,sticky=W)
        
        Button(frame3, text='Return tools!',font=('Times New Roman',12),bg='#7E7E7E',command=self.trans99).grid(row=4,column=0,sticky=W,padx=270)
        self.roota.configure(background='#7E7E7E')
        self.roota.mainloop()
    def checkStatus(self):#showing monthly status
        global namez
        self.root=Tk()
        j=0
        Label(self.root,text='S.N.').grid(column=0,row=0)
        Label(self.root,text='Name of the tool').grid(column=1,row=0)
        Label(self.root,text='Hired from').grid(column=2,row=0)
        Label(self.root,text='Phone no').grid(column=3,row=0)
        Label(self.root,text='Payment').grid(column=4,row=0)
        Label(self.root,text='Date').grid(column=5,row=0)
        Label(self.root,text='Hired by').grid(column=6,row=0)
 
            
        
        for lines in open('status.txt','r').readlines():
            meh=lines.split()
            j+=1
            Label(self.root,text=j).grid(column=0,row=j)
            Label(self.root,text=meh[0]).grid(column=1,row=j)
            Label(self.root,text=meh[2]).grid(column=2,row=j)
            Label(self.root,text=meh[1]).grid(column=3,row=j)
            Label(self.root,text=str(int(meh[3])*3+5)).grid(column=4,row=j)
            Label(self.root,text=meh[7]).grid(column=5,row=j)
            Label(self.root,text=meh[6]).grid(column=6,row=j)

            
           
        self.root.mainloop()
    
    
    def trans4(self):
        messagebox.showinfo('Sign out','you have been signed out') 
        self.roota.destroy()
    
        
        User()
    def GetOption(self):
        d=Hires()
        self.roota.destroy()
        self.opt=self.e.get()
        if self.opt=='Welding Machine':#checking options selected in optin menu
            d.WeildingMachine()
        elif self.opt=='Generator':
            d.Generator()
        elif self.opt=="Electric Motor":
            d.ElectricMotor()
        elif self.opt=='Driller':
            d.Driller()
    
    def trans2(self):
        self.roota.destroy()
        AddTools() 
    
    def trans99(self):
        self.roota.destroy()
        Returntools()
    
    
class AddTools():
    def __init__(self):
    
        self.root =Tk()
        self.root.geometry('680x480+270+100')
        self.root.resizable(False,False)
        self.root.title("Shared Power")
        self.root.configure(background='#7E7E7E')
        frame1=Frame(self.root)
    
        self.pp=PhotoImage(file="logo1.png")
        Label(frame1,image=self.pp,height=100,width=100,bg='#7E7E7E').grid(row=0,column=0,sticky=W)
        Label.imager=self.pp
        frame1.grid(sticky=W)
        Label(frame1, text="You are adding the tools in the Shared Power!",font=('Monotype Corsiva',20),bg='#7E7E7E').grid(row=0,column=1,padx=100)
        frame1.configure(background='#7E7E7E')
    
        frame1=Frame(self.root)
        frame1.grid()
    
        frame1.configure(background='#7E7E7E') 
        global name
        global num
        global owner
        global half
        global full
    
        Label(frame1, text='Name of the machine',font=('Times New Roman',14),bg='#7E7E7E').grid(row=0,column=0,sticky=W)
    
        self.machines=["WeldingMachine", "Generator","ElectricMotor","Driller"]#an option menu for 4 tools
        self.e=StringVar()
        self.e.set(self.machines[0])
        self.f=OptionMenu(frame1,self.e,*self.machines)
        self.f.grid(row=0,column=1,columnspan=2,sticky=W)
        self.f.config(bg='#7E7E7E')

    
        Label(frame1, text='Phone no.',font=('Times New Roman',14),bg='#7E7E7E').grid(row=1,column=0,sticky=W)
    
        self.num=Entry(frame1,bg="#8D8D8D") 
        self.num.grid(row=1,column=1,sticky=W)
    
        Label(frame1, text='Owner',font=('Times New Roman',14),bg='#7E7E7E').grid(row=2,column=0,sticky=W)
        
    
        self.owner=Entry(frame1,bg="#8D8D8D") 
        self.owner.grid(row=2,column=1,sticky=W)    
        
        
        Label(frame1, text='Price per half day',font=('Times New Roman',14),bg='#7E7E7E').grid(row=3,column=0,sticky=W)
        self.half=Entry(frame1,bg="#8D8D8D") 
        self.half.grid(row=3,column=1,sticky=W)
        
        Label(frame1, text='Price per full day',font=('Times New Roman',14),bg='#7E7E7E').grid(row=4,column=0,sticky=W)
        self.full=Entry(frame1,bg="#8D8D8D") 
        self.full.grid(row=4,column=1,sticky=W)        
        
        
        frame2=Frame(self.root)
        frame2.grid()        
        frame2.configure(background='#7E7E7E')     
    
        Button(frame2,text="Save",font=('Times New Roman',14),bg='#7E7E7E',command=self.toolreg).grid(row=2,column=0,sticky=W,padx=100,pady=30)
        Button(frame2,text=" Back ",font=('Times New Roman',14),bg='#7E7E7E',command=self.trans5).grid(row=2,column=1,padx=0,sticky=W)
        
    def trans5(self):
        self.root.destroy()
        Searchtools()
    def toolreg(self):
                
            if not self.num.get() or not self.owner.get():#verifying entries in add tools
                messagebox.showerror('Error','Please fill all the fields')
            elif not len(self.num.get())==10 and not len(self.num.get())==7:
                messagebox.showerror('Error','Please enter a valid phone number.')
            elif self.full.get()<self.half.get():
                messagebox.showerror('Error',"Price for full day can't be less than price for half")
            else:
                try:
                    bbb=int(self.num.get())
                    nnn=int(self.half.get())
                    nuu=int(self.full.get())
                    messagebox.showinfo('Added','Your tool has been added Successfully')
                    self.t=datetime.date.today()
                    with open('a.txt','a') as user:
                        user.write(self.e.get())#adding input info to a.txt
                        user.write(' ')
                        user.write(self.num.get())
                        user.write(' ')
                        user.write(self.owner.get())
                        user.write(' ')
                        user.write(self.half.get())
                        user.write(' ')
                        user.write(self.full.get())
                        user.write(' ')                
                        user.write(str(self.t))
                        user.write('\n')
                                       
                        user.close()
                    self.root.destroy()
                    self.root.mainloop()
                    
                    Searchtools()
                except ValueError:    
                    messagebox.showerror('Error','Please enter a valid details.') 
class Returntools():
    def __init__(self):

        self.root =Tk()
        self.root.geometry('680x480+270+100')
        self.root.resizable(False,False)
        self.root.title("Shared Power")
        self.root.configure(background='#7E7E7E')
        frame1=Frame(self.root)
    
        self.pp=PhotoImage(file="logo1.png")
        Label(frame1,image=self.pp,height=100,width=100,bg='#7E7E7E').grid(row=0,column=0,sticky=W)
        Label.imager=self.pp
        frame1.grid()                
        Label(frame1, text="Tools you hired!",font=('Monotype Corsiva',20),bg='#7E7E7E').grid(row=0,column=1,padx=100)
        frame1.configure(background='#7E7E7E')
        Label(frame1, text="You had hired the following machines previously:",font=('Times New Roman',12),bg='#7E7E7E').grid(row=1,column=1,padx=00)
        
        i=2
        for lines in open('hire.txt','r').readlines():
            self.new=lines.split()              
            Label(frame1, text=self.new[2]+'-'+self.new[1]+'-'+self.new[0],font=('Times New Roman',12),bg='#7E7E7E').grid(row=i,column=1,sticky=W)
            i+=1
        if i==2:
            messagebox.showerror('No tools taken','You havent taken any tools')
            
            self.root.destroy()
            Searchtools()
        try:
            frame2=Frame(self.root)
            frame2.grid(padx=20)
            frame2.configure(background='#7E7E7E')
            Button(frame2,text="Return the tools",font=('Times New Roman',12),bg='#7E7E7E',command=self.returnn).grid(row=1,column=0,padx=100,sticky=E)
            v=Button(frame2,text="Back",font=('Times New Roman',12),bg='#7E7E7E',command=self.trans9).grid(row=1,column=2,padx=50,sticky=W)
        except TclError:
            pass
                
        self.root.mainloop()
        
               
        
    def returnn(self):#a list of checkboxes to confirm returning of tool
        global ss
        a=messagebox.showinfo('Return Tools','You are about to return the tools.')
        open('hire.txt','w').close()
        
        
        b=messagebox.askquestion('Return Tools',"Is there anything wrong with the tools which you hired for after its utilization?")
        if b=='no':
            messagebox.showinfo('Return Tools',"Thank you for utilising our tools wisely. We hope you will follow up 'Shared Power' in coming days as well.")
            self.root.destroy()
            Searchtools()
        else:
            a1=messagebox.showinfo('Return Tools','Thanks for your honesty.Read the disclaimer of the Insurance company.')
            if a1=='ok':
                self.trans98()
            ss='available'
        
    def trans98(self):
        self.root.destroy()
        Insurance()
    def trans9(self):
        self.root.destroy()
        Searchtools()
    
                
class Insurance():
    def __init__(self):
        self.root =Tk()
        self.root.geometry('680x480+270+100')
        self.root.resizable(False,False)
        self.root.title("Shared Power")
        self.root.configure(background='#7E7E7E')
        frame1=Frame(self.root)
    
        self.pp=PhotoImage(file="logo1.png")
        Label(frame1,image=self.pp,height=100,width=100,bg='#7E7E7E').grid(row=0,column=0,sticky=E)
        Label.imager=self.pp
        frame1.grid()
        Label(frame1, text="Reporting Mishandled Tools to Insurance Company ",font=('Monotype Corsiva',18),bg='#7E7E7E').grid(row=0,column=1,padx=00)
        frame1.configure(background='#7E7E7E')
        Label(frame1, text="Ethics",font=('Monotype Corsiva',18),bg='#7E7E7E').grid(row=1,column=1,padx=00)
       
        frame2=Frame(self.root)
        Label(frame2, text="Thank you, for your sinciere apologization shown to the Insurance Company. Our agent will get back to you",font=('Times New Roman',12),bg='#7E7E7E').grid(row=0,column=0,padx=00)
        Label(frame2,text='soon for inspection and to take necessary actions.',font=('Times New Roman',12),bg='#7E7E7E').grid(row=1,column=0,padx=00)
        frame2.grid()
        frame2.configure(background='#7E7E7E')
        Button(frame2,text='  Ok  ',bg='#7E7E7E',command=self.toolret).grid(row=2)
        ss='Unavailable'
    def toolret(self):  
        self.trans97()
    
    def trans97(self):
        self.root.destroy()
        Searchtools()       
            
        self.root.mainloop()
        
class Hires():
    
    def __init__(self):
        pass
    def Driller(self):
        self.root =Tk()
        
        self.root.geometry('680x480+270+100')
        self.root.resizable(False,False)
        self.root.title("Shared Power")
        self.root.configure(background='#7E7E7E')
        frame1=Frame(self.root)

        self.pp=PhotoImage(file="logo1.png")
        Label(frame1,image=self.pp,height=100,width=100,bg='#7E7E7E').grid(row=0,column=0,sticky=W)
        Label.imager=self.pp
        frame1.grid(sticky=W)
        Label(frame1, text="Tools for hire",font=('Monotype Corsiva',20),bg='#7E7E7E').grid(row=0,column=1,padx=120)
        frame1.configure(background='#7E7E7E')
                
        
        frame2=Frame(self.root)
        frame2.grid(pady=20)
        frame2.configure(background='#7E7E7E')
        
        self.b=PhotoImage(file="driller.png")
        Label(frame2,image=self.b,height=93,width=93,bg='#7E7E7E').grid(row=0,column=0,sticky=W)
        Label.iii=self.b
        
        frame3=Frame(self.root)
        frame3.grid(pady=0)
        frame3.configure(background='#7E7E7E')
        r=0
        o=0
        for lines in open('a.txt','r').readlines():
            lineb=lines.split()
            if lineb[0]=='Driller':
                if o==0:
                    self.n=lines
                    Button(frame3,text="Hire this tool!",font=('Times New Roman',10),bg='#7E7E7E',command=self.hire).grid(row=6,column=0,padx=0,sticky=W)
                if o==1:
                    self.n2=lines
                    Button(frame3,text="Hire this tool!",font=('Times New Roman',10),bg='#7E7E7E',command=self.hire2).grid(row=6,column=1,padx=0,sticky=W)
                if o==2:
                    self.n3=lines
                    Button(frame3,text="Hire this tool!",font=('Times New Roman',10),bg='#7E7E7E',command=self.hire3).grid(row=6,column=2,padx=0,sticky=W)
                if o==3:
                    self.n4=lines
                    Button(frame3,text="Hire this tool!",font=('Times New Roman',10),bg='#7E7E7E',command=self.hire4).grid(row=6,column=3,padx=0,sticky=W)            
            
                Label(frame3, text="Name:"+lineb[0],font=('Times New Roman',10),bg='#7E7E7E').grid(row=0,column=o,padx=0,sticky=W)
                Label(frame3, text="Owner:"+lineb[2],font=('Times New Roman',10),bg='#7E7E7E').grid(row=1,column=o,padx=0,sticky=W)
                Label(frame3, text="Number:"+lineb[1],font=('Times New Roman',10),bg='#7E7E7E').grid(row=2,column=o,padx=0,sticky=W)
                Label(frame3, text="Half day Price:"+lineb[3],font=('Times New Roman',10),bg='#7E7E7E').grid(row=3,column=o,padx=0,sticky=W)
                Label(frame3, text="Full day Price:"+lineb[4],font=('Times New Roman',10),bg='#7E7E7E').grid(row=4,column=o,padx=0,sticky=W)
                r=1
                o+=1
        Button(frame3,text="  Back   ",font=('Times New Roman',10),bg='#7E7E7E',command=self.trans3).grid(row=7,column=3,padx=0,sticky=W)
                
        if r!=1:
            messagebox.showinfo('no tools','You need to add tools first')
            self.root.destroy()
    
            AddTools()
        
       
        self.root.mainloop()
    def WeildingMachine(self):
        self.root =Tk()
        
        self.root.geometry('680x480+270+100')
        self.root.resizable(False,False)
        self.root.title("Shared Power")
        self.root.configure(background='#7E7E7E')
        frame1=Frame(self.root)
        
        self.pp=PhotoImage(file="logo1.png")
        Label(frame1,image=self.pp,height=100,width=100,bg='#7E7E7E').grid(row=0,column=0,sticky=W)
        Label.imager=self.pp
        frame1.grid(sticky=W)
        Label(frame1, text="Book the Tools now!",font=('Monotype Corsiva',20),bg='#7E7E7E').grid(row=0,column=1,padx=120)
        frame1.configure(background='#7E7E7E')
        
        
        frame2=Frame(self.root)
        frame2.grid(pady=20)
        frame2.configure(background='#7E7E7E')
        
        self.pp1=PhotoImage(file="welding machine.png")
        Label(frame2,image=self.pp1,height=93,width=93,bg='#7E7E7E').grid(row=0,column=0,sticky=W)
        Label.imger1=self.pp1
        
        frame3=Frame(self.root)
        frame3.grid(pady=0)
        frame3.configure(background='#7E7E7E')
        r=0
        o=0
        for lines in open('a.txt','r').readlines():
            lineb=lines.split()
            if lineb[0]=='WeldingMachine':
                if o==0:
                    self.n=lines
                    Button(frame3,text="Hire this tool!",font=('Times New Roman',10),bg='#7E7E7E',command=self.hire).grid(row=6,column=0,padx=0,sticky=W)
                if o==1:
                    self.n2=lines
                    Button(frame3,text="Hire this tool!",font=('Times New Roman',10),bg='#7E7E7E',command=self.hire2).grid(row=6,column=1,padx=0,sticky=W)
                if o==2:
                    self.n3=lines
                    Button(frame3,text="Hire this tool!",font=('Times New Roman',10),bg='#7E7E7E',command=self.hire3).grid(row=6,column=2,padx=0,sticky=W)
                if o==3:
                    self.n4=lines
                    Button(frame3,text="Hire this tool!",font=('Times New Roman',10),bg='#7E7E7E',command=self.hire4).grid(row=6,column=3,padx=0,sticky=W)            
            
                Label(frame3, text="Name:"+lineb[0],font=('Times New Roman',10),bg='#7E7E7E').grid(row=0,column=o,padx=0,sticky=W)
                Label(frame3, text="Owner:"+lineb[2],font=('Times New Roman',10),bg='#7E7E7E').grid(row=1,column=o,padx=0,sticky=W)
                Label(frame3, text="Number:"+lineb[1],font=('Times New Roman',10),bg='#7E7E7E').grid(row=2,column=o,padx=0,sticky=W)
                Label(frame3, text="Half day Price:"+lineb[3],font=('Times New Roman',10),bg='#7E7E7E').grid(row=3,column=o,padx=0,sticky=W)
                Label(frame3, text="Full day Price:"+lineb[4],font=('Times New Roman',10),bg='#7E7E7E').grid(row=4,column=o,padx=0,sticky=W)                
                r=1
                o+=1
        Button(frame3,text="  Back   ",font=('Times New Roman',10),bg='#7E7E7E',command=self.trans3).grid(row=7,column=3,padx=0,sticky=W)
                
        if r!=1:
            messagebox.showinfo('no tools','You need to add tools first')
            self.root.destroy()
    
            AddTools()
        
       
    def ElectricMotor(self):
        self.root =Tk()
        
        self.root.geometry('680x480+270+100')
        self.root.resizable(False,False)
        self.root.title("Shared Power")
        self.root.configure(background='#7E7E7E')
        frame1=Frame(self.root)
    
        self.pp=PhotoImage(file="logo1.png")
        Label(frame1,image=self.pp,height=100,width=100,bg='#7E7E7E').grid(row=0,column=0,sticky=W)
        Label.imager=self.pp
        frame1.grid(sticky=W)
        Label(frame1, text="Book the Tools now!",font=('Monotype Corsiva',20),bg='#7E7E7E').grid(row=0,column=1,padx=120)
        frame1.configure(background='#7E7E7E')
            
        
        frame2=Frame(self.root)
        frame2.grid(pady=20)
        frame2.configure(background='#7E7E7E')
        
        b=PhotoImage(file="motor.png")
        Label(frame2,image=b,height=93,width=93,bg='#7E7E7E').grid(row=0,column=0,sticky=W)
        Label.zz=b
        
        frame3=Frame(self.root)
        frame3.grid(pady=0)
        frame3.configure(background='#7E7E7E')
        r=0
        o=0
        for lines in open('a.txt','r').readlines():
            lineb=lines.split()
            if lineb[0]=='ElectricMotor':
                if o==0:
                    self.n=lines
                    Button(frame3,text="Hire this tool!",font=('Times New Roman',10),bg='#7E7E7E',command=self.hire).grid(row=6,column=0,padx=0,sticky=W)
                if o==1:
                    self.n2=lines
                    Button(frame3,text="Hire this tool!",font=('Times New Roman',10),bg='#7E7E7E',command=self.hire2).grid(row=6,column=1,padx=0,sticky=W)
                if o==2:
                    self.n3=lines
                    Button(frame3,text="Hire this tool!",font=('Times New Roman',10),bg='#7E7E7E',command=self.hire3).grid(row=6,column=2,padx=0,sticky=W)
                if o==3:
                    self.n4=lines
                    Button(frame3,text="Hire this tool!",font=('Times New Roman',10),bg='#7E7E7E',command=self.hire4).grid(row=6,column=3,padx=0,sticky=W)            
            
                Label(frame3, text="Name:"+lineb[0],font=('Times New Roman',10),bg='#7E7E7E').grid(row=0,column=o,padx=0,sticky=W)
                Label(frame3, text="Owner:"+lineb[2],font=('Times New Roman',10),bg='#7E7E7E').grid(row=1,column=o,padx=0,sticky=W)
                Label(frame3, text="Number:"+lineb[1],font=('Times New Roman',10),bg='#7E7E7E').grid(row=2,column=o,padx=0,sticky=W)
                Label(frame3, text="Half day Price:"+lineb[3],font=('Times New Roman',10),bg='#7E7E7E').grid(row=3,column=o,padx=0,sticky=W)
                Label(frame3, text="Full day Price:"+lineb[4],font=('Times New Roman',10),bg='#7E7E7E').grid(row=4,column=o,padx=0,sticky=W)                
                r=1
                o+=1
        Button(frame3,text="  Back   ",font=('Times New Roman',10),bg='#7E7E7E',command=self.trans3).grid(row=7,column=3,padx=0,sticky=W)
                
        if r!=1:
            messagebox.showinfo('no tools','You need to add tools first')
            self.root.destroy()
    
            AddTools()
        
          
    def Generator(self):
        global n
        self.root =Tk()
        
        self.root.geometry('680x480+270+100')
        self.root.resizable(False,False)
        self.root.title("Shared Power")
        self.root.configure(background='#7E7E7E')
        frame1=Frame(self.root)
    
        self.pp=PhotoImage(file="logo1.png")
        Label(frame1,image=self.pp,height=100,width=100,bg='#7E7E7E').grid(row=0,column=0,sticky=W)
        Label.imager=self.pp
        frame1.grid(sticky=W)
        Label(frame1, text="Book the Tools now!",font=('Monotype Corsiva',20),bg='#7E7E7E').grid(row=0,column=1,padx=120)
        frame1.configure(background='#7E7E7E')
        frame2=Frame(self.root)
        frame2.grid(pady=20)
        frame2.configure(background='#7E7E7E')
        
        b=PhotoImage(file="Generator.png")
        Label(frame2,image=b,height=93,width=93,bg='#7E7E7E').grid(row=0,column=0,sticky=W)
        Label.imgar=b
        
        frame3=Frame(self.root)
        frame3.grid(pady=0)
        frame3.configure(background='#7E7E7E')
        r=0
        o=0
        for lines in open('a.txt','r').readlines():
            lineb=lines.split()
            if lineb[0]=='Generator':
                if o==0:
                    self.n=lines
                    Button(frame3,text="Hire this tool!",font=('Times New Roman',10),bg='#7E7E7E',command=self.hire).grid(row=6,column=0,padx=0,sticky=W)
                if o==1:
                    self.n2=lines
                    Button(frame3,text="Hire this tool!",font=('Times New Roman',10),bg='#7E7E7E',command=self.hire2).grid(row=6,column=1,padx=0,sticky=W)
                if o==2:
                    self.n3=lines
                    Button(frame3,text="Hire this tool!",font=('Times New Roman',10),bg='#7E7E7E',command=self.hire3).grid(row=6,column=2,padx=0,sticky=W)
                if o==3:
                    self.n4=lines
                    Button(frame3,text="Hire this tool!",font=('Times New Roman',10),bg='#7E7E7E',command=self.hire4).grid(row=6,column=3,padx=0,sticky=W)            
            
                Label(frame3, text="Name:"+lineb[0],font=('Times New Roman',10),bg='#7E7E7E').grid(row=0,column=o,padx=0,sticky=W)
                Label(frame3, text="Owner:"+lineb[2],font=('Times New Roman',10),bg='#7E7E7E').grid(row=1,column=o,padx=0,sticky=W)
                Label(frame3, text="Number:"+lineb[1],font=('Times New Roman',10),bg='#7E7E7E').grid(row=2,column=o,padx=0,sticky=W)
                Label(frame3, text="Half day Price:"+lineb[3],font=('Times New Roman',10),bg='#7E7E7E').grid(row=3,column=o,padx=0,sticky=W)
                Label(frame3, text="Full day Price:"+lineb[4],font=('Times New Roman',10),bg='#7E7E7E').grid(row=4,column=o,padx=0,sticky=W)                
                r=1
                o+=1
        Button(frame3,text="  Back   ",font=('Times New Roman',10),bg='#7E7E7E',command=self.trans3).grid(row=7,column=3,padx=0,sticky=W)
                
        if r!=1:
            messagebox.showinfo('no tools','You need to add tools first')
            self.root.destroy()
    
            AddTools()
   
            
       
    
    def hire(self):
        if self.n in open('hire.txt').readlines():
            messagebox.showinfo('Unavailable','This tool is already being hired.') 
        else:
            tt=datetime.date.today()
            with open('hire.txt','a') as use:
                use.write(self.n)
                use.close()
            for lines in open('hire.txt','r').readlines():
                with open ('status.txt','a') as asd:
                    linez=lines.rstrip()
                    asd.write(linez+' '+ll+' '+str(tt)+'\n')            
            self.dispatchrider()
            
            
        self.root.mainloop()
    def hire2(self):
        if self.n2 in open('hire.txt').readlines():
            messagebox.showinfo('Unavailable','This tool is already being hired.') 
        else:
            tt=datetime.date.today()
            with open('hire.txt','a') as use:
                use.write(self.n2)
                use.close()
            for lines in open('hire.txt','r').readlines():
                with open ('status.txt','a') as asd:
                    linez=lines.rstrip()
                    asd.write(linez+' '+ll+' '+str(tt)+'\n')           
            self.dispatchrider()
                            
        self.root.mainloop()
    def hire3(self):
        if self.n3 in open('hire.txt').readlines():
            messagebox.showinfo('Unavailable','This tool is already being hired.') 
        else:
            tt=datetime.date.today()
            with open('hire.txt','a') as use:
                use.write(self.n3)
                use.close()           
            for lines in open('hire.txt','r').readlines():
                with open ('status.txt','a') as asd:
                    linez=lines.rstrip()
                    asd.write(linez+' '+ll+' '+str(tt)+'\n')                         
            self.dispatchrider()          
            
        self.root.mainloop()      
    def hire4(self):
        
        if self.n4 in open('hire.txt').readlines():
            messagebox.showinfo('Unavailable','This tool is already being hired.') 
        else:
            tt=datetime.date.today()
            with open('hire.txt','a') as use:
                use.write(self.n4)
                use.close()           
            for lines in open('hire.txt','r').readlines():
                with open ('status.txt','a') as asd:
                    linez=lines.rstrip()
                    asd.write(linez+' '+ll+' '+str(tt)+'\n')                      
            self.dispatchrider()           
            
        self.root.mainloop()
    def trans3(self):
        self.root.destroy()
        
        Searchtools()
    def dispatchrider(self):
        global b1
      
        self.root.destroy()
        self.root=Tk()
        self.frame=Frame(self.root)
        self.root.geometry('680x480+270+100')
        self.root.resizable(False,False)
        self.root.title("register")
        self.root.configure(background='#7E7E7E')
        frame1=Frame(self.root)
        
        
        
        frame1.grid(sticky=W)
        Label(frame1, text="You are about to hire the tools!",font=('Monotype Corsiva',20),bg='#7E7E7A').grid(row=0,column=1,padx=100)
        frame1.configure(background='#7E7E7E')
        
        self.image=PhotoImage(file='logo1.png')
        Label(frame1,image=self.image,background='#7E7E7E').grid(row=0,column=0,sticky=W)
        Label.me=self.image
        
        frame2=Frame(self.root)
        Label(frame2,text="Days you want to hire",font=('Times New Roman',14),background='#7E7E7E').grid(row=0,column=0)
        self.b1=Entry(frame2,background='#7E7E7A')
        self.b1.grid(row=0,column=1)
        self.a1=Button(frame2,text='Hire',background='#7E7E7A',command=self.feild)
        self.a1.grid(row=1,column=0,padx=100,pady=50)    
        frame2.grid(padx=100)
        frame2.configure(background='#7E7E7E')
        
        
        
        self.root.mainloop()
   
    def feild(self):
        if not self.b1.get():
            messagebox.showerror('Error','Please fill all the fields')
        elif self.b1.get()=='1' or self.b1.get()=='1.5' or  self.b1.get()=='2' or  self.b1.get()=='2.5' or  self.b1.get()=='3':
            b1=messagebox.showinfo('Hired','Successfully hired the tools.')
            if b1=='ok':
                b=messagebox.askquestion('Dispatch rider',"Are you in Uregnt?  Do you need dispatcher rider to deliver your tools?")
                if b=='no':
                    
                    self.root.destroy()
                    Searchtools()
                else:
                    a1=messagebox.showinfo('Dispatch rider','Your tool will be delivered by dispatch rider very soon.')
                    if a1=='ok':
                        self.root.destroy()
                        Searchtools()
        else:
            messagebox.showinfo('Hired','Fill the feilds upto 3 days.')
   
a=User()