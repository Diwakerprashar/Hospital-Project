#Hospital Record system.

from tkinter import *
from tkinter import messagebox
from tkinter.font import Font
from tkinter import ttk
import mysql.connector
 
root=Tk()
root.title('Welcome to Hospital')
root.configure(background='burlywood4')

#root.geometry("1600x600")

rwidth=root.winfo_screenwidth()
rheight=root.winfo_screenheight()
root.geometry(('%dx%d')%(rwidth,rheight))

myfont=Font(family='Aerial',size=16,slant='italic')


#*******************___________Def database___________***************

"""def fetch_database(hospital):
        con=mysql.connector.connect(host='localhost',user='root',password='',db='hospital')
        cur=con.cursor()"""

#f0
#f0
#_________________________________Button def_____________________________
def admin():
        root.withdraw()
        root1.deiconify()
        

def doctor():
        root.withdraw()
        root1_1.deiconify()

def reception():
        root.withdraw()
        root1_2.deiconify()

def room_find():
        root1_3.deiconify()
        con=mysql.connector.connect(host='localhost',user='root',password='',db='hospital')
        cur=con.cursor()
        print('cur')
        query="select name,room from patient"
        print('query')
        cur.execute(query,)
        print('cur')
        value=cur.fetchall()
        try:
                x = tree17.get_children()
                for item in x: tree17.delete(item)
                for i in range(0,len(value)):
                        tree17.insert('','end',values=value[i])
                        print('done')
        except:
                print('Not executed')

def withdraw_all():
        root.destroy()
        root1.destroy()
        root1_1.destroy()
        root1_2.destroy()
        root2.destroy()
        root3.destroy()
        root4.destroy()
        root4_1.destroy()
        root4_2.destroy()
        root4_3.destroy()
        root4_4.destroy()
        root5.destroy()
        root6.destroy()
        root6_1.destroy()
        root6_2.destroy()
        root6_3.destroy()
        root6_4.destroy()
        root7.destroy()
        root8.destroy()
        root9.destroy()
        root10.destroy()
        root11.destroy()
        root12.destroy()
        
        
#_________________________________f1_____________________________________
f1=Frame(root,height=800,width=1500,bd=4,relief='solid',padx=50,pady=20,bg='burlywood')
f1.grid(row=1,column=1,padx=10,pady=10)

#__________________________________f2____________________________________
myfont=Font(family='Aerial',size=20,slant='italic')

f2=Frame(f1,height=40,width=1400,bd=4,relief='solid',bg='peachpuff3',padx=50,pady=20)
f2.pack()
#grid(row=0,column=0,padx=10,pady=10)

l2=Label(f2,text='Hospital Management',font=myfont,fg='Brown',bg='peachpuff3')
l2.grid(row=0,column=15,padx=350,pady=10)
#------------------------------------------------------------------------

"""l1=Label(f1,text='Login As',font=myfont,fg='Brown',relief='solid',bg='burlywood2',anchor='w')
l1.pack(padx=5,pady=10)"""

l3=Label(f1,text='Welcome to Hospital  ',bd=3,relief='solid',font=myfont,fg='Brown',bg='peachpuff3',anchor='n')
l3.pack(padx=10,pady=50)

l1=Label(f1,text='Login As',font=myfont,fg='Brown',relief='solid',bg='burlywood2',anchor='w')
l1.pack(side=LEFT,anchor='w',padx=5,pady=10)

b1=Button(f1,text='Admin',height=5,width=10,command=admin,relief='solid',font=myfont,fg='Brown')
b1.pack(side=LEFT,padx=70,pady=120)

b2=Button(f1,text='Doctor',height=5,width=10,command=doctor,relief='solid',font=myfont,fg='Brown')
b2.pack(side=LEFT,padx=70,pady=120)

b3=Button(f1,text='Reception',height=5,width=10,command=reception,relief='solid',font=myfont,fg='Brown')
b3.pack(side=LEFT,padx=70,pady=120)

b_room=Button(f1,text='Room',height=5,width=10,command=room_find,relief='solid',font=myfont,fg='Brown')
b_room.pack(side=LEFT,padx=70,pady=120)

b4=Button(f1,text='Exit',height=1,width=4,command=withdraw_all,relief='solid',font=myfont,fg='Brown')
b4.pack(side=TOP,anchor=CENTER,ipadx=5,ipady=10)

#_______________________________window1(For Admin)_________________________________
root1=Tk()
root1.withdraw()
root1.title('Welcome to Hospital')
root1.configure(background='burlywood4')

rwidth=root1.winfo_screenwidth()
rheight=root1.winfo_screenheight()
root1.geometry(('%dx%d')%(rwidth,rheight))

myfont=Font(family='Aerial',size=16,slant='italic')

user_name=StringVar()
pass_word=StringVar()

def login():
        root1.withdraw()
        print(e4.get())
        getusername=e4.get()
        print(getusername)
        getpassword=e5.get()
        print(getpassword)
        con=mysql.connector.connect(host='localhost',user='root',password='',db='hospital')
        cur=con.cursor()
        
        query="select count(*) from admin where username=%s and password=%s"
        cur.execute(query,(getusername,getpassword,))
        count=cur.fetchone()
        if (count[0]==1):
                print("You are successfully login")
                root2.deiconify()
                messagebox.showinfo("Info","Logged in successfully") 
        
                
        else:
                messagebox.showerror("Error",'invalid username or password')



def back():
        root.deiconify()

f3=Frame(root1,height=600,width=600,bd=4,padx=100,pady=20,relief='solid',bg='Orange')
f3.grid(row=4,column=10,padx=480,pady=200)

l4=Label(f3,text='Username',font=myfont,fg='Brown')
l4.grid(row=0,column=0,padx=10,pady=20)

e4=Entry(f3,textvariable=user_name,font=myfont,fg='Brown')
e4.grid(row=0,column=2,padx=10,pady=20)

l5=Label(f3,text='Password',font=myfont,fg='Brown')
l5.grid(row=2,column=0,padx=10,pady=20)

e5=Entry(f3,textvariable=pass_word,show='*',font=myfont,fg='Brown')
e5.grid(row=2,column=2,padx=10,pady=20)

b5=Button(f3,text='Login',command=login,font=myfont,fg='Brown')
b5.grid(row=4,column=2,padx=10,pady=20)

bex=Button(f3,text='Back',command=back,font=myfont,fg='Brown')
bex.grid(row=4,column=0,padx=10,pady=20)


#_____________________________window1_1(For Doctor)______________________________
root1_1=Tk()
root1_1.withdraw()
root1_1.title('Welcome to Hospital')
root1_1.configure(background='burlywood4')

rwidth=root1_1.winfo_screenwidth()
rheight=root1_1.winfo_screenheight()
root1_1.geometry(('%dx%d')%(rwidth,rheight))

myfont=Font(family='Aerial',size=16,slant='italic')

user_name_1=StringVar()
pass_word_1=StringVar()

def login_1():
        print(e4_1.get())
        getusername=e4_1.get()
        print(getusername)

        print(e5_1.get())
        getpassword=e5_1.get()
        print(getpassword)
        
        con=mysql.connector.connect(host='localhost',user='root',password='',db='hospital')
        cur=con.cursor()
        
        query="select count(*) from doctor where username=%s and password=%s"
        cur.execute(query,(getusername,getpassword,))
        count=cur.fetchone()
        if (count[0]==1):
                print("You are successfully login")
                root2.deiconify()
                messagebox.showinfo("Info","Logged in successfully")
        else:
                messagebox.showerror("Error",'invalid username or password')


def back_1():
        root.deiconify()

f3_1=Frame(root1_1,height=600,width=600,bd=4,padx=100,pady=20,relief='solid',bg='Orange')
f3_1.grid(row=4,column=10,padx=480,pady=200)

l4_1=Label(f3_1,text='Username',font=myfont,fg='Brown')
l4_1.grid(row=0,column=0,padx=10,pady=20)

e4_1=Entry(f3_1,textvariable=user_name,font=myfont,fg='Brown')
e4_1.grid(row=0,column=2,padx=10,pady=20)

l5_1=Label(f3_1,text='Password',font=myfont,fg='Brown')
l5_1.grid(row=2,column=0,padx=10,pady=20)

e5_1=Entry(f3_1,textvariable=pass_word,show='*',font=myfont,fg='Brown')
e5_1.grid(row=2,column=2,padx=10,pady=20)



b5_1=Button(f3_1,text='Login',command=login_1,font=myfont,fg='Brown')
b5_1.grid(row=4,column=2,padx=10,pady=20)

bex_1=Button(f3_1,text='Back',command=back_1,font=myfont,fg='Brown')
bex_1.grid(row=4,column=0,padx=10,pady=20)





#_____________________________window1_2(For Receptionist)___________________________
root1_2=Tk()
root1_2.withdraw()
root1_2.title('Welcome to Hospital')
root1_2.configure(background='burlywood4')

rwidth=root1_2.winfo_screenwidth()
rheight=root1_2.winfo_screenheight()
root1_2.geometry(('%dx%d')%(rwidth,rheight))

myfont=Font(family='Aerial',size=16,slant='italic')

user_name_2=StringVar()
pass_word_2=StringVar()

def login_2():
        print('Receptionist')
        print(e4_2.get())
        getusername=e4_2.get()
        print(getusername)

        print(e5_2.get())
        getpassword=e5_2.get()
        print(getpassword)
        
        con=mysql.connector.connect(host='localhost',user='root',password='',db='hospital')
        cur=con.cursor()
        
        query="select count(*) from receptionist where username=%s and password=%s"
        cur.execute(query,(getusername,getpassword,))
        count=cur.fetchone()
        if (count[0]==1):
                print("You are successfully login")
                root2.deiconify()
                messagebox.showinfo("Info","Logged in successfully")
        else:
                messagebox.showerror("Error",'invalid username or password')


def back_2():
        root.deiconify()

f3_2=Frame(root1_2,height=600,width=600,bd=4,padx=100,pady=20,relief='solid',bg='Orange')
f3_2.grid(row=4,column=10,padx=480,pady=200)

l4_2=Label(f3_2,text='Username',font=myfont,fg='Brown')
l4_2.grid(row=0,column=0,padx=10,pady=20)

e4_2=Entry(f3_2,textvariable=user_name,font=myfont,fg='Brown')
e4_2.grid(row=0,column=2,padx=10,pady=20)

l5_2=Label(f3_2,text='Password',font=myfont,fg='Brown')
l5_2.grid(row=2,column=0,padx=10,pady=20)

e5_2=Entry(f3_2,textvariable=pass_word,show='*',font=myfont,fg='Brown')
e5_2.grid(row=2,column=2,padx=10,pady=20)



b5_2=Button(f3_2,text='Login',command=login_2,font=myfont,fg='Brown')
b5_2.grid(row=4,column=2,padx=10,pady=20)

bex_2=Button(f3_2,text='Back',command=back_2,font=myfont,fg='Brown')
bex_2.grid(row=4,column=0,padx=10,pady=20)



##___________window for room

def exit_bl3():
        root.deiconify()
        root1_3.withdraw()

root1_3=Tk()
root1_3.withdraw()
root1_3.title('Welcome to Hospital')
root1_3.configure(background='burlywood4')

rwidth=root1_3.winfo_screenwidth()
rheight=root1_3.winfo_screenheight()
root1_3.geometry(('%dx%d')%(rwidth,rheight))

myfont=Font(family='Aerial',size=16,slant='italic')

ll_3=Label(root1_3,text='Rooms ',bd=3,relief='solid',width=120,font=myfont,fg='Brown',bg='peachpuff3',anchor='n')
ll_3.grid(row=0,column=0,columnspan=6,padx=10,pady=50)

f_room=Frame(root1_3,height=10,width=10,bd=4,relief='solid',padx=50,pady=20)
f_room.grid(row=4,column=1,columnspan=4,padx=10,pady=20)

bl_3=Button(root1_3,text='Exit',height=1,width=4,command=exit_bl3,relief='solid',font=myfont,fg='Brown')
bl_3.grid(row=4,column=5,padx=10,pady=10)


#*******_____table
tree17=ttk.Treeview(f_room)

tree17['columns']=("3","12")
"""tree17.column("0",width=80)
tree17.column("1",width=80)
tree17.column("2",width=80)"""
tree17.column("3",width=80)
"""tree17.column("4",width=80)
tree17.column("5",width=80)
tree17.column("6",width=80)
tree17.column("7",width=80)
tree17.column("8",width=80)
tree17.column("9",width=80)
tree17.column("10",width=80)
tree17.column("11",width=80)"""
tree17.column("12",width=80)
"""tree17.column("13",width=80)
tree17.column("14",width=80)"""

"""tree17.heading("0",text="Count")
tree17.heading("1",text="Date")
tree17.heading("2",text="Id")"""
tree17.heading("3",text="Name")
"""tree17.heading("4",text="Age")
tree17.heading("5",text="Gender")
tree17.heading("6",text="Blood")
tree17.heading("7",text="Dept.")
tree17.heading("8",text="Phone")
tree17.heading("9",text="Email")
tree17.heading("10",text="Status")
tree17.heading("11",text="Address")"""
tree17.heading("12",text="Room")
"""tree17.heading("13",text="Username")
tree17.heading("14",text="Password")"""


tree17.pack(side="right")




############################################################################

#########################   ADMIN BLOCK FOR LOGIN FINISHED #################

############################################################################





#______________________________________window2________________________________________
##################################First window after Login############################
root2=Tk()
root2.withdraw()
root2.title('Welcome to Hospital')
root2.configure(background='burlywood4')

rwidth=root2.winfo_screenwidth()
rheight=root2.winfo_screenheight()
root2.geometry(('%dx%d')%(rwidth,rheight))

myfont=Font(family='Aerial',size=16,slant='italic')

#_____________________________________Button def______________________________________

def patient_info():
        print('patient info')    #####   Going to patient's panel to add new,delete,view,
        root7.deiconify()        #####   search etc.
        

def doctor_info():              ######   Going to Doctor's panel to add new,delete,view,
        print('Doctor')         ######   search etc.
        root5.deiconify()
def reception1():               ######   Going to Receptionist's panel to add new,delete,view,
        print('reception2')     ######   search etc.
        root3.deiconify()

def exit_all():
        root.deiconify()
        root2.withdraw()
        root1.withdraw()
        root1_1.withdraw()
        root3.withdraw()
        root4.withdraw()
        root4_1.withdraw()
        root4_2.withdraw()
        root4_3.withdraw()
        root4_4.withdraw()
        root5.withdraw()
        root6.withdraw()
        root6_1.withdraw()
        root6_2.withdraw()
        root6_3.withdraw()
        root6_4.withdraw()
        root7.withdraw()
        root8.withdraw()
        root9.withdraw()
        root10.withdraw()
        root11.withdraw()
        root12.withdraw()
        

####   Admin Panel  Full Control.

f4=Frame(root2,height=800,width=1500,bd=4,padx=50,pady=20,relief='solid',bg='Orange')
f4.grid(row=0,column=1,padx=10,pady=80)


f5=Frame(f4,height=40,width=1400,bd=4,relief='solid',padx=50,pady=10)
f5.pack()

l6=Label(f5,text='Admin Portal',font=myfont,fg='Brown')
l6.grid(row=1,column=15,padx=6,pady=20)

l7=Label(f4,text='Welcome to Admin Portal',font=myfont,fg='Brown',bg='Yellow',anchor='w')
l7.pack(side=LEFT,padx=10,pady=10)


b6=Button(f4,text='Patient info',height=5,width=10,command=patient_info,font=myfont,fg='Brown')
b6.pack(side=LEFT,padx=100,pady=150)

b7=Button(f4,text='Doctor info',height=5,width=10,command=doctor_info,font=myfont,fg='Brown')
b7.pack(side=LEFT,padx=100,pady=150)

b8=Button(f4,text='Reception',height=5,width=10,command=reception1,font=myfont,fg='Brown')
b8.pack(side=LEFT,padx=130,pady=150)

b9=Button(f4,text='Exit',height=1,width=4,command=exit_all,font=myfont,fg='Brown')
b9.pack(anchor=CENTER,padx=8)


####################################################################################
######################_______First window of login finished______###################
####################################################################################



#_______________________________________root3________________________________

#______________________________________def button root3______________________

def add_new_receptionist():
        root3.withdraw()
        root4.deiconify()

def update_receptionist():
        root4_1.deiconify()
        con=mysql.connector.connect(host='localhost',user='root',password='',db='hospital')
        cur=con.cursor()

        query="select * from receptionist Order By count"
        cur.execute(query)
        try:
                up_r=cur.fetchall()
                x = tree.get_children()
                for item in x: Tree.delete(item)

                for i in range(0,len(up_r)):
                        tree.insert('','end',values=up_r[i])
        except:
                print('Not updated')
        

def delete_receptionist():
        root4_2.deiconify()
        con=mysql.connector.connect(host='localhost',user='root',password='',db='hospital')
        cur=con.cursor()

        query="select * from receptionist Order By count"
        cur.execute(query)
        del_r=cur.fetchall()
        try:
                x = tree1.get_children()
                for item in x: tree17.delete(item)
                for i in range(0,len(del_r)):
                        tree1.insert('','end',values=del_r[i])
        except:
                print('Not executed')

def search_receptionist():
        root4_3.deiconify()
        con=mysql.connector.connect(host='localhost',user='root',password='',db='hospital')
        cur=con.cursor()

        query="select * from receptionist Order By count"
        cur.execute(query)
        ser_r=cur.fetchall()
        try:
                x = tree2.get_children()
                for item in x: tree2.delete(item)
                for i in range(0,len(ser_r)):
                        tree2.insert('','end',values=ser_r[i])
        except:
                print('Not executed')

def view_receptionist():
        root4_4.deiconify()
        con=mysql.connector.connect(host='localhost',user='root',password='',db='hospital')
        cur=con.cursor()

        query="select * from receptionist Order By count"
        cur.execute(query)
        vie_r=cur.fetchall()
        try:
                x = tree3.get_children()
                for item in x: tree3.delete(item)
                for i in range(0,len(vie_r)):
                        tree3.insert('','end',values=vie_r[i])

        except:
                print('Not executed')

def exit14_1():
        root3.withdraw()
        root2.deiconify()

        
#____________________________________________________________________________
root3=Tk()
root3.withdraw()
root3.title('Receptionist Panel')
root3.configure(background='burlywood4')

rwidth=root3.winfo_screenwidth()
rheight=root3.winfo_screenheight()
root3.geometry(('%dx%d')%(rwidth,rheight))

myfont=Font(family='Aerial',size=16,slant='italic')



##########################_________Receptionist Main Panel____________#####################

f6=Frame(root3,height=40,width=1400,bd=4,relief='solid',padx=50,pady=10)
f6.pack(pady=5)

l8=Label(f6,text='Receptionist Management',height=5,width=60,font=myfont,fg='Brown',bg='Black')
l8.grid(padx=5,pady=10,row=0,column=2,columnspan=4)

l9=Label(f6,text='''Welcome

  to Receptionist
  
    Managemet''',height=10,width=15,font=myfont,fg='Brown',bg='Black')
l9.grid(padx=10,pady=5,row=2,column=0)

b10=Button(f6,text='Add New',command=add_new_receptionist,height=5,width=10,font=myfont,fg='Brown')
b10.grid(row=2,column=2,padx=10,pady=20)

b11=Button(f6,text='Update',command=update_receptionist,height=5,width=10,font=myfont,fg='Brown')
b11.grid(row=2,column=3,padx=10,pady=20)

b12=Button(f6,text='Delete',command=delete_receptionist,height=5,width=10,font=myfont,fg='Brown')
b12.grid(row=2,column=4,padx=10,pady=20)

b13=Button(f6,text='Search',command=search_receptionist,height=5,width=10,font=myfont,fg='Brown')
b13.grid(row=2,column=5,padx=10,pady=20)

b14=Button(f6,text='view',command=view_receptionist,height=5,width=10,font=myfont,fg='Brown')
b14.grid(row=3,column=2,padx=10,pady=20)

b14_1=Button(f6,text='Exit',command=exit14_1,height=5,width=10,font=myfont,fg='Brown')
b14_1.grid(row=3,column=3,padx=10,pady=20)


#____________________________________Root4__________________________________________
dt=StringVar()
idr=StringVar()
namer=StringVar()
ager=IntVar()
genderr=StringVar()
bloodr=StringVar()
phoner=StringVar()
emailr=StringVar()
addressr=StringVar()
martialr=StringVar()
usr=StringVar()
pwr=StringVar()



def back7_1():
        root3.deiconify()

def back7_2():
        root4.withdraw()
        root4_1_1.withdraw()
        root2.deiconify()

def add_new():
        con=mysql.connector.connect(host='localhost',user='root',password='',db='hospital')
        cur=con.cursor()

        getdt=e7_2.get()
        print(getdt)
        getidr=e7_3.get()
        print(getidr)
        getnamer=e7_4.get()
        getager=e7_5.get()
        getgenderr=e7_6.get()
        getbloodr=e7_7.get()
        getphoner=e8_8.get()
        getemailr=e9_9.get()
        getaddressr=e10_10.get()
        getmartialr=e10.get()
        getusr=e11.get()
        getpwr=e12.get()

        

        query="insert into receptionist(joining,id,name,age,gender,blood,email,phone,address,status,username,password) Values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cur.execute(query,(getdt,getidr,getnamer,getager,getgenderr,getbloodr,getemailr,getphoner,getaddressr,getmartialr,getusr,getpwr,))
        messagebox.showinfo("Info","Added Successfully")

        
root4=Tk()
root4.withdraw()
root4.title('Welcome to Hospital')
root4.configure(background='burlywood4')

rwidth=root4.winfo_screenwidth()
rheight=root4.winfo_screenheight()
root4.geometry(('%dx%d')%(rwidth,rheight))

myfont4=Font(family='Aerial',size=50,slant='italic')
myfont=Font(family='Aerial',size=16,slant='italic')


####     To Add new  Receptionist


f7=Frame(root4,height=40,width=1400,bd=4,relief='solid',padx=50,pady=10)
f7.pack(padx=5,pady=10)

l7_1=Label(f7,text='Add Receptionist',height=5,width=120,font=myfont4,fg='Brown',bg='burlywood4')
l7_1.grid(padx=5,pady=10,row=0,column=0,columnspan=6)

b7_1=Button(f7,text='Back',command=back7_1,height=1,width=4,font=myfont,fg='Brown')
b7_1.grid(row=0,column=4,padx=5,pady=10)

b7_2=Button(f7,text='Exit',command=back7_2,height=1,width=4,font=myfont,fg='Brown')
b7_2.grid(row=0,column=5,padx=5,pady=10)


b7_2=Button(f7,text='Add',command=add_new,height=1,width=4,font=myfont,fg='Brown')
b7_2.grid(row=4,column=5,padx=5,pady=10)



l7_2=Label(f7,text='Date',font=myfont,fg='burlywood4')
l7_2.grid(padx=5,pady=10,row=2,column=0)

e7_2=Entry(f7,textvariable=dt,font=myfont,fg='burlywood4')
e7_2.grid(row=2,column=1,padx=5,pady=10)

l7_3=Label(f7,text='Id',font=myfont,fg='burlywood4')
l7_3.grid(padx=5,pady=10,row=3,column=0)

e7_3=Entry(f7,textvariable=idr,font=myfont,fg='burlywood4')
e7_3.grid(row=3,column=1,padx=5,pady=10)

l7_4=Label(f7,text='Name',font=myfont,fg='burlywood4')
l7_4.grid(padx=5,pady=10,row=4,column=0)

e7_4=Entry(f7,textvariable=namer,font=myfont,fg='Brown')
e7_4.grid(row=4,column=1,padx=5,pady=10)

l7_5=Label(f7,text='Age',font=myfont,fg='burlywood4')
l7_5.grid(padx=5,pady=10,row=5,column=0)

e7_5=Entry(f7,textvariable=ager,font=myfont,fg='burlywood4')
e7_5.grid(row=5,column=1,padx=5,pady=10)

l7_6=Label(f7,text='Gender',font=myfont,fg='burlywood4')
l7_6.grid(padx=5,pady=10,row=6,column=0)

e7_6=Entry(f7,textvariable=genderr,font=myfont,fg='burlywood4')
e7_6.grid(row=6,column=1,padx=5,pady=10)


#####______


l7_7=Label(f7,text='Blood Group',font=myfont,fg='burlywood4')
l7_7.grid(padx=5,pady=10,row=2,column=2)

e7_7=Entry(f7,textvariable=bloodr,font=myfont,fg='burlywood4')
e7_7.grid(row=2,column=3,padx=5,pady=10)

l8_8=Label(f7,text='Phone Number',font=myfont,fg='burlywood4')
l8_8.grid(padx=5,pady=10,row=3,column=2)

e8_8=Entry(f7,textvariable=phoner,font=myfont,fg='burlywood4')
e8_8.grid(row=3,column=3,padx=5,pady=10)

l9_9=Label(f7,text='Email',font=myfont,fg='burlywood4')
l9_9.grid(padx=5,pady=10,row=4,column=2)

e9_9=Entry(f7,textvariable=emailr,font=myfont,fg='burlywood4')
e9_9.grid(row=4,column=3,padx=5,pady=10)

l10_10=Label(f7,text='Address',font=myfont,fg='burlywood4')
l10_10.grid(padx=5,pady=10,row=5,column=2)

e10_10=Entry(f7,textvariable=addressr,font=myfont,fg='burlywood4')
e10_10.grid(row=5,column=3,padx=5,pady=10)

l10=Label(f7,text='Martial Status',font=myfont,fg='burlywood4')
l10.grid(padx=5,pady=10,row=6,column=2)

e10=Entry(f7,textvariable=martialr,font=myfont,fg='burlywood4')
e10.grid(row=6,column=3,padx=5,pady=10)





#####_________


l11=Label(f7,text='Username',font=myfont,fg='burlywood4')
l11.grid(padx=5,pady=10,row=2,column=4)

e11=Entry(f7,textvariable=usr,font=myfont,fg='burlywood4')
e11.grid(row=2,column=5,padx=5,pady=10)

l12=Label(f7,text='Password',font=myfont,fg='burlywood4')
l12.grid(padx=5,pady=10,row=3,column=4)

e12=Entry(f7,textvariable=pwr,font=myfont,fg='burlywood4')
e12.grid(row=3,column=5,padx=5,pady=10)





#####Update Receptionist
def back7_1_1():
        root3.deiconify()
        root4_1.withdraw()

def back7_1_2():
        root4_1.withdraw()
        root2.deiconify()

"""def update_r():
        root4_1_1.deiconify()
        con=mysql.connector.connect(host='localhost',user='root',password='',db='hospital')
        cur=con.cursor()

        query="insert into receptionist(joining,id,name,age,gender,blood,email,phone,address,status,username,password) Values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cur.execute(query,(getdt,getidr,getnamer,getager,getgenderr,getbloodr,getemailr,getphoner,getaddressr,getmartialr,getusr,getpwr,))"""

        

root4_1=Tk()
root4_1.withdraw()
root4_1.title('Welcome to Hospital')
root4_1.configure(background='burlywood4')

rwidth=root4_1.winfo_screenwidth()
rheight=root4_1.winfo_screenheight()
root4_1.geometry(('%dx%d')%(rwidth,rheight))

myfont4_1=Font(family='Aerial',size=50,slant='italic')
myfont=Font(family='Aerial',size=16,slant='italic')

f7_1_1=Frame(root4_1,height=40,width=1400,bd=4,relief='solid',padx=50,pady=10)
f7_1_1.pack(padx=5,pady=10)

l7_1_1=Label(f7_1_1,text='Update Receptionist',height=5,width=120,font=myfont4,fg='Brown',bg='burlywood4')
l7_1_1.grid(padx=5,pady=10,row=0,column=0,columnspan=8)

b7_1_1=Button(f7_1_1,text='Back',command=back7_1_1,height=1,width=5,font=myfont,fg='Brown')
b7_1_1.grid(row=0,column=2,padx=10,pady=10,columnspan=2)

b7_1_2=Button(f7_1_1,text='Exit',command=back7_1_2,height=1,width=5,font=myfont,fg='Brown')
b7_1_2.grid(row=0,column=3,padx=10,pady=10,columnspan=2)

"""b7_1_3=Button(f7_1_1,text='Update',command=update_r,height=1,width=8,font=myfont,fg='Brown')
b7_1_3.grid(row=10,column=2,padx=5,pady=10)"""


f7_1_1_1=Frame(f7_1_1,height=550,width=600,bd=4,relief='solid',padx=50,pady=10)
f7_1_1_1.grid(row=1,column=0,columnspan=4,padx=5,pady=10)

#*******_____table
tree=ttk.Treeview(f7_1_1_1)

tree['columns']=("0","one","two","three","four","five","six","seven","eight","nine","10","11","12")
tree.column("0",width=80)
tree.column("one",width=80)
tree.column("two",width=80)
tree.column("three",width=80)
tree.column("four",width=80)
tree.column("five",width=80)
tree.column("six",width=80)
tree.column("seven",width=80)
tree.column("eight",width=80)
tree.column("nine",width=80)
tree.column("10",width=80)
tree.column("11",width=80)
tree.column("12",width=80)

tree.heading("0",text="Count")
tree.heading("1",text="Joining")
tree.heading("2",text="Id")
tree.heading("3",text="Name")
tree.heading("4",text="Age")
tree.heading("5",text="Gender")
tree.heading("6",text="Blood")
tree.heading("7",text="Email")
tree.heading("8",text="Phone")
tree.heading("9",text="Address")
tree.heading("10",text="Status")
tree.heading("11",text="Username")
tree.heading("12",text="Password`")


tree.pack(side="left")




#  update window
root4_1_1=Tk()
root4_1_1.withdraw()
root4_1_1.title('Welcome to Hospital')
root4_1_1.configure(background='burlywood4')

rwidth=root4_1_1.winfo_screenwidth()
rheight=root4_1_1.winfo_screenheight()
root4_1_1.geometry(('%dx%d')%(rwidth,rheight))

myfont4_1=Font(family='Aerial',size=50,slant='italic')
myfont=Font(family='Aerial',size=16,slant='italic')



f4up=Frame(root4_1_1,height=40,width=1400,bd=4,relief='solid',padx=50,pady=10)
f4up.pack(padx=5,pady=10)

l4u_1=Label(f4up,text='Update patient',height=5,width=120,font=myfont4,fg='Brown',bg='burlywood4')
l4u_1.grid(padx=5,pady=10,row=0,column=0,columnspan=6)

b4u_1=Button(f4up,text='Back',command=back7_1,height=1,width=4,font=myfont,fg='Brown')
b4u_1.grid(row=0,column=4,padx=5,pady=10)

b4u_2=Button(f4up,text='Exit',command=back7_2,height=1,width=4,font=myfont,fg='Brown')
b4u_2.grid(row=0,column=5,padx=5,pady=10)


b4u_3=Button(f4up,text='Add',command=add_new,height=1,width=4,font=myfont,fg='Brown')
b4u_3.grid(row=4,column=5,padx=5,pady=10)



l4u_2=Label(f4up,text='Date',font=myfont,fg='burlywood4')
l4u_2.grid(padx=5,pady=10,row=2,column=0)

e4u_1=Entry(f4up,textvariable=e7_2,font=myfont,fg='burlywood4')
e4u_1.grid(row=2,column=1,padx=5,pady=10)

l4u_3=Label(f4up,text='Id',font=myfont,fg='burlywood4')
l4u_3.grid(padx=5,pady=10,row=3,column=0)

e4u_2=Entry(f4up,textvariable=idr,font=myfont,fg='burlywood4')
e4u_2.grid(row=3,column=1,padx=5,pady=10)

l4u_4=Label(f4up,text='Name',font=myfont,fg='burlywood4')
l4u_4.grid(padx=5,pady=10,row=4,column=0)

e4u_3=Entry(f4up,textvariable=namer,font=myfont,fg='Brown')
e4u_3.grid(row=4,column=1,padx=5,pady=10)

l4u_5=Label(f4up,text='Age',font=myfont,fg='burlywood4')
l4u_5.grid(padx=5,pady=10,row=5,column=0)

e4u_4=Entry(f4up,textvariable=ager,font=myfont,fg='burlywood4')
e4u_4.grid(row=5,column=1,padx=5,pady=10)

l4u_6=Label(f4up,text='Gender',font=myfont,fg='burlywood4')
l4u_6.grid(padx=5,pady=10,row=6,column=0)

e4u_5=Entry(f4up,textvariable=genderr,font=myfont,fg='burlywood4')
e4u_5.grid(row=6,column=1,padx=5,pady=10)


#####______


l4u_7=Label(f4up,text='Blood Group',font=myfont,fg='burlywood4')
l4u_7.grid(padx=5,pady=10,row=2,column=2)

e4u_6=Entry(f4up,textvariable=bloodr,font=myfont,fg='burlywood4')
e4u_6.grid(row=2,column=3,padx=5,pady=10)

l4u_8=Label(f4up,text='Phone Number',font=myfont,fg='burlywood4')
l4u_8.grid(padx=5,pady=10,row=3,column=2)

e4u_7=Entry(f4up,textvariable=phoner,font=myfont,fg='burlywood4')
e4u_7.grid(row=3,column=3,padx=5,pady=10)

l4u_9=Label(f4up,text='Email',font=myfont,fg='burlywood4')
l4u_9.grid(padx=5,pady=10,row=4,column=2)

e4u_8=Entry(f4up,textvariable=emailr,font=myfont,fg='burlywood4')
e4u_8.grid(row=4,column=3,padx=5,pady=10)

l4u_10=Label(f4up,text='Address',font=myfont,fg='burlywood4')
l4u_10.grid(padx=5,pady=10,row=5,column=2)

e4u_9=Entry(f4up,textvariable=addressr,font=myfont,fg='burlywood4')
e4u_9.grid(row=5,column=3,padx=5,pady=10)

l4u_11=Label(f4up,text='Martial Status',font=myfont,fg='burlywood4')
l4u_11.grid(padx=5,pady=10,row=6,column=2)

e4u_10=Entry(f4up,textvariable=martialr,font=myfont,fg='burlywood4')
e4u_10.grid(row=6,column=3,padx=5,pady=10)





#####_________


l4u_12=Label(f4up,text='Username',font=myfont,fg='burlywood4')
l4u_12.grid(padx=5,pady=10,row=2,column=4)

e4u_11=Entry(f4up,textvariable=usr,font=myfont,fg='burlywood4')
e4u_11.grid(row=2,column=5,padx=5,pady=10)

l4u_13=Label(f4up,text='Password',font=myfont,fg='burlywood4')
l4u_13.grid(padx=5,pady=10,row=3,column=4)

e4u_12=Entry(f4up,textvariable=pwr,font=myfont,fg='burlywood4')
e4u_12.grid(row=3,column=5,padx=5,pady=10)


######Delete receptionist
del_recp=StringVar()

def back7_2_1():
        root3.deiconify()
        root4_2.withdraw()
        
def back7_2_2():
        root4_2.withdraw()
        root2.deiconify()
        

def delete_r():
        print('del receptionist')
        con=mysql.connector.connect(host='localhost',user='root',password='',db='hospital')
        cur=con.cursor()
        
        getname=e7_2_1.get()

        query="delete from receptionist where name=%s"
        cur.execute(query,(getname,))
        print('query executed')
        messagebox.showinfo('info','Deleted successfully')
                    
        print('Deleted successfully')

root4_2=Tk()
root4_2.withdraw()
root4_2.title('Delete Receptionist')
root4_2.configure(background='burlywood4')

rwidth=root4_2.winfo_screenwidth()
rheight=root4_2.winfo_screenheight()
root4_2.geometry(('%dx%d')%(rwidth,rheight))

myfont4_2=Font(family='Aerial',size=30,slant='italic')
myfont4_2_1=Font(family='Aerial',size=20,slant='italic')

f7_2_1=Frame(root4_2,height=40,width=1400,bd=4,relief='solid',padx=50,pady=10)
f7_2_1.pack(padx=10,pady=10)

l7_2_1=Label(f7_2_1,text='Delete Receptionist',height=5,width=120,font=myfont4_2_1,fg='Brown',bg='burlywood4')
l7_2_1.grid(padx=5,pady=10,row=0,column=0,columnspan=8)


l7_2_2=Label(f7_2_1,text='Name of Receptionist',height=2,width=20,font=myfont4_2,fg='Brown',bg='burlywood4')
l7_2_2.grid(padx=5,pady=10,row=2,column=0)

e7_2_1=Entry(f7_2_1,textvariable=del_recp,font=myfont,fg='burlywood4')
e7_2_1.grid(row=2,column=1,padx=5,pady=10)



b7_2_1=Button(f7_2_1,text='Back',command=back7_2_1,height=1,width=4,font=myfont,fg='Brown')
b7_2_1.grid(row=0,column=2,padx=5,pady=10)

b7_2_2=Button(f7_2_1,text='Exit',command=back7_2_2,height=1,width=4,font=myfont,fg='Brown')
b7_2_2.grid(row=0,column=3,padx=5,pady=10)

b7_2_3=Button(f7_2_1,text='Delete',command=delete_r,height=1,width=8,font=myfont,fg='Brown')
b7_2_3.grid(row=2,column=3,padx=5,pady=10)


f7_2_1_1=Frame(f7_2_1,height=550,width=600,bd=4,relief='solid',padx=50,pady=10)
f7_2_1_1.grid(row=3,column=0,columnspan=4,padx=5,pady=10)



#*******_____table
tree1=ttk.Treeview(f7_2_1_1)

tree1['columns']=("0","1","2","3","4","5","6","7","8","9","10","11","12")
tree1.column("0",width=80)
tree1.column("1",width=80)
tree1.column("2",width=80)
tree1.column("3",width=80)
tree1.column("4",width=80)
tree1.column("5",width=80)
tree1.column("6",width=80)
tree1.column("7",width=80)
tree1.column("8",width=80)
tree1.column("9",width=80)
tree1.column("10",width=80)
tree1.column("11",width=80)
tree1.column("12",width=80)


tree1.heading("0",text="Count")
tree1.heading("1",text="Joining")
tree1.heading("2",text="Id")
tree1.heading("3",text="Name")
tree1.heading("4",text="Age")
tree1.heading("5",text="Gender")
tree1.heading("6",text="Blood")
tree1.heading("7",text="Email")
tree1.heading("8",text="Phone")
tree1.heading("9",text="Address")
tree1.heading("10",text="Status")
tree1.heading("11",text="Username")
tree1.heading("12",text="Password`")



tree1.pack(side="left")


######Search receptionist
search_recp=StringVar()

def back7_3_1():
        root3.deiconify()
        root4_3.withdraw()
        
def back7_3_2():
        root4_3.withdraw()
        root2.deiconify()
        

def search7_3_3():
        con=mysql.connector.connect(host='localhost',user='root',password='',db='hospital')
        cur=con.cursor()
        
        getname=e7_3_1.get()

        query="select * from receptionist where name=%s"
        cur.execute(query,(getname,))
        shw=cur.fetchall()
        try:
                for i in range(0,len(shw)):
                        tree2_1.insert('','end',values=shw[i])
                        messagebox.showinfo('info','Searched successfully')
        except:
                messagebox.showerror('info','Invalid Entry')
                    

root4_3=Tk()
root4_3.withdraw()
root4_3.title('search to Hospital')
root4_3.configure(background='burlywood4')

rwidth=root4_3.winfo_screenwidth()
rheight=root4_3.winfo_screenheight()
root4_3.geometry(('%dx%d')%(rwidth,rheight))

myfont4_3=Font(family='Aerial',size=30,slant='italic')
myfont4_3_1=Font(family='Aerial',size=20,slant='italic')

f7_3_1=Frame(root4_3,height=40,width=1400,bd=4,relief='solid',padx=50,pady=10)
f7_3_1.pack(padx=10,pady=10)

l7_3_1=Label(f7_3_1,text='Search Receptionist',height=5,width=120,font=myfont4_2_1,fg='Brown',bg='burlywood4')
l7_3_1.grid(padx=5,pady=10,row=0,column=0,columnspan=6)


l7_3_2=Label(f7_3_1,text='Name of Receptionist',height=2,width=20,font=myfont4_2,fg='Brown',bg='burlywood4')
l7_3_2.grid(padx=5,pady=10,row=2,column=0)

e7_3_1=Entry(f7_3_1,textvariable=search_recp,font=myfont,fg='burlywood4')
e7_3_1.grid(row=2,column=1,padx=5,pady=10)



b7_3_1=Button(f7_3_1,text='Back',command=back7_3_1,height=1,width=4,font=myfont,fg='Brown')
b7_3_1.grid(row=0,column=2,padx=5,pady=10)

b7_3_2=Button(f7_3_1,text='Exit',command=back7_3_2,height=1,width=4,font=myfont,fg='Brown')
b7_3_2.grid(row=0,column=3,padx=5,pady=10)

b7_3_3=Button(f7_3_1,text='Search',command=search7_3_3,height=1,width=8,font=myfont,fg='Brown')
b7_3_3.grid(row=2,column=2,padx=5,pady=10)



f7_3_1_1=Frame(f7_3_1,height=550,width=600,bd=4,relief='solid',padx=50,pady=10)
f7_3_1_1.grid(row=3,column=0,columnspan=4,padx=5,pady=10)



#*******_____table
tree2=ttk.Treeview(f7_3_1_1)

tree2['columns']=("0","1","2","3","4","5","6","7","8","9","10","11","12")
tree2.column("0",width=80)
tree2.column("1",width=80)
tree2.column("2",width=80)
tree2.column("3",width=80)
tree2.column("4",width=80)
tree2.column("5",width=80)
tree2.column("6",width=80)
tree2.column("7",width=80)
tree2.column("8",width=80)
tree2.column("9",width=80)
tree2.column("10",width=80)
tree2.column("11",width=80)
tree2.column("12",width=80)


tree2.heading("0",text="Count")
tree2.heading("1",text="Joining")
tree2.heading("2",text="Id")
tree2.heading("3",text="Name")
tree2.heading("4",text="Age")
tree2.heading("5",text="Gender")
tree2.heading("6",text="Blood")
tree2.heading("7",text="Email")
tree2.heading("8",text="Phone")
tree2.heading("9",text="Address")
tree2.heading("10",text="Status")
tree2.heading("11",text="Username")
tree2.heading("12",text="Password`")

tree2.pack(side="left")




f7_3_1_2=Frame(f7_3_1,height=550,width=600,bd=4,relief='solid',padx=50,pady=10)
f7_3_1_2.grid(row=5,column=0,columnspan=4,padx=5,pady=10)



#*******_____searched receptionist
tree2_1=ttk.Treeview(f7_3_1_2)

tree2_1['columns']=("0","1","2","3","4","5","6","7","8","9","10","11","12")
tree2_1.column("0",width=80)
tree2_1.column("1",width=80)
tree2_1.column("2",width=80)
tree2_1.column("3",width=80)
tree2_1.column("4",width=80)
tree2_1.column("5",width=80)
tree2_1.column("6",width=80)
tree2_1.column("7",width=80)
tree2_1.column("8",width=80)
tree2_1.column("9",width=80)
tree2_1.column("10",width=80)
tree2_1.column("11",width=80)
tree2_1.column("12",width=80)


tree2_1.heading("0",text="Count")
tree2_1.heading("1",text="Joining")
tree2_1.heading("2",text="Id")
tree2_1.heading("3",text="Name")
tree2_1.heading("4",text="Age")
tree2_1.heading("5",text="Gender")
tree2_1.heading("6",text="Blood")
tree2_1.heading("7",text="Email")
tree2_1.heading("8",text="Phone")
tree2_1.heading("9",text="Address")
tree2_1.heading("10",text="Status")
tree2_1.heading("11",text="Username")
tree2_1.heading("12",text="Password`")

tree2_1.pack(side="left")


#####View Receptionist
def back7_4_1():
        root3.deiconify()
        root4_4.withdraw()

def back7_4_2():
        root4_4.withdraw()
        root2.deiconify()

root4_4=Tk()
root4_4.withdraw()
root4_4.title('View Receptionist')
root4_4.configure(background='burlywood4')

rwidth=root4_4.winfo_screenwidth()
rheight=root4_4.winfo_screenheight()
root4_4.geometry(('%dx%d')%(rwidth,rheight))

myfont4_1=Font(family='Aerial',size=50,slant='italic')
myfont=Font(family='Aerial',size=16,slant='italic')

f7_4_1=Frame(root4_4,height=40,width=1400,bd=4,relief='solid',padx=50,pady=10)
f7_4_1.pack(padx=10,pady=10)

l7_4_1=Label(f7_4_1,text='View Receptionist',height=5,width=120,font=myfont4,fg='Brown',bg='burlywood4')
l7_4_1.grid(padx=5,pady=10,row=0,column=0,columnspan=6)

b7_4_1=Button(f7_4_1,text='Back',command=back7_4_1,height=1,width=4,font=myfont,fg='Brown')
b7_4_1.grid(row=0,column=3,padx=2,pady=10)

b7_4_2=Button(f7_4_1,text='Exit',command=back7_4_2,height=1,width=4,font=myfont,fg='Brown')
b7_4_2.grid(row=0,column=4,padx=2,pady=10)




f7_4_1_1=Frame(f7_4_1,height=550,width=600,bd=4,relief='solid',padx=50,pady=10)
f7_4_1_1.grid(row=2,column=0,columnspan=4,padx=5,pady=10)



#*******_____table
tree3=ttk.Treeview(f7_4_1_1)

tree3['columns']=("0","1","2","3","4","5","6","7","8","9","10","11","12")
tree3.column("0",width=80)
tree3.column("1",width=80)
tree3.column("2",width=80)
tree3.column("3",width=80)
tree3.column("4",width=80)
tree3.column("5",width=80)
tree3.column("6",width=80)
tree3.column("7",width=80)
tree3.column("8",width=80)
tree3.column("9",width=80)
tree3.column("10",width=80)
tree3.column("11",width=80)
tree3.column("12",width=80)

tree3.heading("0",text="Count")
tree3.heading("1",text="Joining")
tree3.heading("2",text="Id")
tree3.heading("3",text="Name")
tree3.heading("4",text="Age")
tree3.heading("5",text="Gender")
tree3.heading("6",text="Blood")
tree3.heading("7",text="Email")
tree3.heading("8",text="Phone")
tree3.heading("9",text="Address")
tree3.heading("10",text="Status")
tree3.heading("11",text="Username")
tree3.heading("12",text="Password`")


tree3.pack(side="left")




##@@@@@@@@@@@@@@@@@@@@@@@_________Reception panel Finished__________@@@@@@@@@@@@@@@@@@



######################################################################################
#########################________Doctor Panel Start_________##########################
######################################################################################


#_______________________________________root5________________________________
def add_doctor():
        print('add_doctor')
        root6.deiconify()   ###### Going to root6 to add new doctor

def update_doctor():
        root6_1.deiconify()
        con=mysql.connector.connect(host='localhost',user='root',password='',db='hospital')
        cur=con.cursor()

        query="select * from doctor"
        cur.execute(query)
        up_d=cur.fetchall()
        try:
                x = tree13.get_children()
                for item in x: tree13.delete(item)
        
                for i in range(0,len(up_d)):
                        tree13.insert('','end',values=up_d[i])

        except:
                print('Not executed')
        

def delete_doctor():
        root6_2.deiconify()
        con=mysql.connector.connect(host='localhost',user='root',password='',db='hospital')
        cur=con.cursor()

        query="select * from doctor"
        cur.execute(query)
        del_d=cur.fetchall()
        try:
                 x = tree14.get_children()
                 for item in x: tree14.delete(item)
        
                 for i in range(0,len(del_d)):
                         tree14.insert('','end',values=del_d[i])
        except:
                print('Not executed')

def search_doctor():
        root6_3.deiconify()
        con=mysql.connector.connect(host='localhost',user='root',password='',db='hospital')
        cur=con.cursor()

        query="select * from doctor"
        cur.execute(query)
        ser_d=cur.fetchall()
        try:
                 x = tree15.get_children()
                 for item in x: tree15.delete(item)
        
                 for i in range(0,len(ser_d)):
                        tree15.insert('','end',values=ser_d[i])
        except:
                print('Not executed')

def view_doctor():
        root6_4.deiconify()
        con=mysql.connector.connect(host='localhost',user='root',password='',db='hospital')
        cur=con.cursor()

        query="select * from doctor"
        cur.execute(query)
        vie_d=cur.fetchall()
        try:
                 x = tree16.get_children()
                 for item in x: tree16.delete(item)
        
                 for i in range(0,len(vie_d)):
                        tree16.insert('','end',values=vie_d[i])

        except:
                print('Not executed')

def b_patient():
        root6_4_1.deiconify()
        con=mysql.connector.connect(host='localhost',user='root',password='',db='hospital')
        cur=con.cursor()

        query="select * from appointment"
        cur.execute(query,)
        b_p=cur.fetchall()
        try:
                 x = tree16_2.get_children()
                 for item in x: tree16_2.delete(item)
        
                 for i in range(0,len(b_p)):
                        tree16_2.insert('','end',values=b_p[i])

        except:
                print('Not executed')

def exit19_2():
        root5.withdraw()
        root2.deiconify()
        
#____________________________________________________________________________
root5=Tk()
root5.withdraw()
root5.title('Welcome to Hospital')
root5.configure(background='burlywood4')

rwidth=root5.winfo_screenwidth()
rheight=root5.winfo_screenheight()
root5.geometry(('%dx%d')%(rwidth,rheight))

myfont=Font(family='Aerial',size=16,slant='italic')


#      Doctor Panel________



f8=Frame(root5,height=40,width=1400,bd=4,relief='solid',padx=50,pady=10)
f8.pack(pady=5)

l8=Label(f8,text='Doctor Panel',height=5,width=60,font=myfont,fg='Brown',bg='Black')
l8.grid(padx=5,pady=10,row=0,column=2,columnspan=4)

l9=Label(f8,text='''Welcome

  User to Doctor
  
    Panel''',height=10,width=15,font=myfont,fg='Brown',bg='Black')
l9.grid(padx=10,pady=5,row=2,column=0)

b15=Button(f8,text='Add New',command=add_doctor,height=5,width=10,font=myfont,fg='Brown')
b15.grid(row=2,column=2,padx=10,pady=20)

b16=Button(f8,text='Update',command=update_doctor,height=5,width=10,font=myfont,fg='Brown')
b16.grid(row=2,column=3,padx=10,pady=20)

b17=Button(f8,text='Delete',command=delete_doctor,height=5,width=10,font=myfont,fg='Brown')
b17.grid(row=2,column=4,padx=10,pady=20)

b18=Button(f8,text='Search',command=search_doctor,height=5,width=10,font=myfont,fg='Brown')
b18.grid(row=2,column=5,padx=10,pady=20)

b19=Button(f8,text='view',command=view_doctor,height=5,width=10,font=myfont,fg='Brown')
b19.grid(row=3,column=2,padx=10,pady=20)

b19_1=Button(f8,text='Patient',command=b_patient,height=5,width=10,font=myfont,fg='Brown')
b19_1.grid(row=3,column=3,padx=10,pady=20)

b19_2=Button(f8,text='Exit',command=exit19_2,height=5,width=10,font=myfont,fg='Brown')
b19_2.grid(row=3,column=3,padx=10,pady=20)

#____________________________________root6__________________________________________

dtd=StringVar()
idd=StringVar()
named=StringVar()
aged=IntVar()
genderd=StringVar()
bloodd=StringVar()
deptd=StringVar()
phoned=StringVar()
emaild=StringVar()
martiald=StringVar()
addressd=StringVar()
roomd=IntVar()
usrd=StringVar()
pswd=StringVar()
def back13_1():
        root5.deiconify()

def exit13_2():
        root6.withdraw()
        root2.deiconify()

def add_d():
        con=mysql.connector.connect(host='localhost',user='root',password='',db='hospital')
        cur=con.cursor()

        getdtd=e14.get()
        print(getdtd)
        getidd=e15.get()
        getnamed=e16.get()
        getaged=e17.get()
        print(getaged)
        getgenderd=e18.get()
        getbloodd=e19.get()
        getdeptd=e20.get()
        getphoned=e21.get()
        getemaild=e22.get()
        getmartiald=e23.get()
        getaddressd=e24.get()
        getroomd=e25.get()
        getusrd=e26.get()
        getpswd=e27.get()
        

        query="insert into doctor(date,id,name,age,gender,blood,dept,phone,email,status,address,room,username,password) Values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cur.execute(query,(getdtd,getidd,getnamed,getaged,getgenderd,getbloodd,getdeptd,getphoned,getemaild,getmartiald,getaddressd,getroomd,getusrd,getpswd,))
        messagebox.showinfo("Info","Added Successfully")

        
root6=Tk()
root6.withdraw()
root6.title('Welcome to Hospital')
root6.configure(background='burlywood4')

rwidth=root6.winfo_screenwidth()
rheight=root6.winfo_screenheight()
root6.geometry(('%dx%d')%(rwidth,rheight))

myfont4=Font(family='Aerial',size=50,slant='italic')
myfont=Font(family='Aerial',size=16,slant='italic')



f9=Frame(root6,height=40,width=1400,bd=4,relief='solid',padx=50,pady=10)
f9.pack(padx=10,pady=10)


#####to Add new doctor to database.(window)

l13=Label(f9,text='Add Doctor',height=5,width=100,font=myfont4,fg='Brown',bg='burlywood4')
l13.grid(padx=5,pady=10,row=0,column=0,columnspan=8)



b13_1=Button(f9,text='Back',command=back13_1,height=1,width=4,font=myfont,fg='Brown')
b13_1.grid(row=0,column=5,padx=5,pady=10)

b13_2=Button(f9,text='Exit',command=exit13_2,height=1,width=4,font=myfont,fg='Brown')
b13_2.grid(row=0,column=6,padx=5,pady=10)


b13_3=Button(f9,text='Add',command=add_d,height=1,width=8,font=myfont,fg='Brown')
b13_3.grid(row=8,column=4,padx=10,pady=10)





l14=Label(f9,text='Joining Date',font=myfont,fg='burlywood4')
l14.grid(padx=10,pady=20,row=1,column=0)

e14=Entry(f9,textvariable=dtd,font=myfont,fg='burlywood4')
e14.grid(row=1,column=1,padx=10,pady=10)

l15=Label(f9,text='Id',font=myfont,fg='burlywood4')
l15.grid(padx=10,pady=20,row=2,column=0)

e15=Entry(f9,textvariable=idd,font=myfont,fg='burlywood4')
e15.grid(row=2,column=1,padx=10,pady=20)

l16=Label(f9,text='Name',font=myfont,fg='burlywood4')
l16.grid(padx=10,pady=20,row=3,column=0)

e16=Entry(f9,textvariable=named,font=myfont,fg='burlywood4')
e16.grid(row=3,column=1,padx=10,pady=20)

l17=Label(f9,text='Age',font=myfont,fg='burlywood4')
l17.grid(padx=10,pady=20,row=4,column=0)

e17=Entry(f9,textvariable=aged,font=myfont,fg='burlywood4')
e17.grid(row=4,column=1,padx=10,pady=20)

l18=Label(f9,text='Gender',font=myfont,fg='burlywood4')
l18.grid(padx=10,pady=20,row=5,column=0)

e18=Entry(f9,textvariable=genderd,font=myfont,fg='burlywood4')
e18.grid(row=5,column=1,padx=10,pady=20)

l19=Label(f9,text='Blood Group',font=myfont,fg='burlywood4')
l19.grid(padx=10,pady=20,row=6,column=0)

e19=Entry(f9,textvariable=bloodd,font=myfont,fg='burlywood4')
e19.grid(row=6,column=1,padx=10,pady=20)

#######______________


l20=Label(f9,text='Department',font=myfont,fg='burlywood4')
l20.grid(padx=10,pady=20,row=1,column=3)

e20=Entry(f9,textvariable=deptd,font=myfont,fg='burlywood4')
e20.grid(row=1,column=4,padx=10,pady=20)


l21=Label(f9,text='Phone Number',font=myfont,fg='burlywood4')
l21.grid(padx=10,pady=20,row=2,column=3)

e21=Entry(f9,textvariable=phoned,font=myfont,fg='burlywood4')
e21.grid(row=2,column=4,padx=10,pady=20)


l22=Label(f9,text='Email',font=myfont,fg='burlywood4')
l22.grid(padx=10,pady=20,row=3,column=3)

e22=Entry(f9,textvariable=emaild,font=myfont,fg='burlywood4')
e22.grid(row=3,column=4,padx=10,pady=20)


l23=Label(f9,text='Martial Status',font=myfont,fg='burlywood4')
l23.grid(padx=10,pady=20,row=4,column=3)

e23=Entry(f9,textvariable=martiald,font=myfont,fg='burlywood4')
e23.grid(row=4,column=4,padx=10,pady=20)


l24=Label(f9,text='Address',font=myfont,fg='burlywood4')
l24.grid(padx=10,pady=20,row=5,column=3)

e24=Entry(f9,textvariable=addressd,font=myfont,fg='burlywood4')
e24.grid(row=5,column=4,padx=10,pady=20)


l25=Label(f9,text='Ward/Room no',font=myfont,fg='burlywood4')
l25.grid(padx=10,pady=20,row=6,column=3)

e25=Entry(f9,textvariable=roomd,font=myfont,fg='burlywood4')
e25.grid(row=6,column=4,padx=10,pady=20)

#####________

l26=Label(f9,text='Username',font=myfont,fg='burlywood4')
l26.grid(padx=10,pady=20,row=1,column=5)

e26=Entry(f9,textvariable=usrd,font=myfont,fg='burlywood4')
e26.grid(row=1,column=6,padx=10,pady=20)


l27=Label(f9,text='Password',font=myfont,fg='burlywood4')
l27.grid(padx=10,pady=20,row=2,column=5)

e27=Entry(f9,textvariable=pswd,font=myfont,fg='burlywood4')
e27.grid(row=2,column=6,padx=10,pady=20)



#####Update Doctor
def back6_1_1():
        root5.deiconify()
        root6_1.withdraw()

def exit6_1_2():
        root6_1.withdraw()
        root2.deiconify()

"""def update_d():
        print('')"""
               

root6_1=Tk()
root6_1.withdraw()
root6_1.title('Update Doctor')
root6_1.configure(background='burlywood4')

rwidth=root6_1.winfo_screenwidth()
rheight=root6_1.winfo_screenheight()
root6_1.geometry(('%dx%d')%(rwidth,rheight))

myfont6_1=Font(family='Aerial',size=50,slant='italic')
myfont=Font(family='Aerial',size=16,slant='italic')

f6_1_1=Frame(root6_1,height=40,width=1400,bd=4,relief='solid',padx=50,pady=10)
f6_1_1.pack(padx=5,pady=10)

l6_1_1=Label(f6_1_1,text='Update Doctor',height=5,width=120,font=myfont4,fg='Brown',bg='burlywood4')
l6_1_1.grid(padx=5,pady=10,row=0,column=0,columnspan=8)

b6_1_1=Button(f6_1_1,text='Back',command=back6_1_1,height=1,width=4,font=myfont,fg='Brown')
b6_1_1.grid(row=0,column=2,padx=5,pady=10,columnspan=2)

b6_1_2=Button(f6_1_1,text='Exit',command=exit6_1_2,height=1,width=4,font=myfont,fg='Brown')
b6_1_2.grid(row=0,column=3,padx=5,pady=10,columnspan=2)

"""b6_1_3=Button(f6_1_1,text='Update',command=update_d,height=1,width=8,font=myfont,fg='Brown')
b6_1_3.grid(row=10,column=2,padx=5,pady=10)"""




f6_1_1_1=Frame(f6_1_1,height=550,width=600,bd=4,relief='solid',padx=50,pady=10)
f6_1_1_1.grid(row=1,column=0,columnspan=4,padx=5,pady=10)


#*******_____table
tree13=ttk.Treeview(f6_1_1_1)

tree13['columns']=("0","one","two","three","four","five","six","seven","8","9","10","11","12","13","14")
tree13.column("0",width=70)
tree13.column("one",width=70)
tree13.column("two",width=70)
tree13.column("three",width=70)
tree13.column("four",width=70)
tree13.column("five",width=70)
tree13.column("six",width=70)
tree13.column("seven",width=70)
tree13.column("8",width=70)
tree13.column("9",width=70)
tree13.column("10",width=70)
tree13.column("11",width=70)
tree13.column("12",width=70)
tree13.column("13",width=70)
tree13.column("14",width=70)


tree13.heading("0",text="Count")
tree13.heading("one",text="Date")
tree13.heading("two",text="Id")
tree13.heading("three",text="Name")
tree13.heading("four",text="Age")
tree13.heading("five",text="Gender")
tree13.heading("six",text="blood")
tree13.heading("seven",text="dept")
tree13.heading("8",text="phone")
tree13.heading("9",text="Email")
tree13.heading("10",text="Status")
tree13.heading("11",text="Address")
tree13.heading("12",text="room")
tree13.heading("13",text="username")
tree13.heading("14",text="Password")


tree13.pack(side="left")




######Delete Doctor
del_doct=StringVar()

def back6_2_1():
        root5.deiconify()
        root6_2.withdraw()
        
def exit6_2_2():
        root6_2.withdraw()
        root2.deiconify()
        

def delete_d():
        print('del doctor')
        con=mysql.connector.connect(host='localhost',user='root',password='',db='hospital')
        cur=con.cursor()
        
        getname=e6_2_1.get()

        query="delete from doctor where name=%s"
        cur.execute(query,(getname,))
        print('query executed')
        messagebox.showinfo('info','Deleted successfully')
                    
        print('Deleted successfully')

root6_2=Tk()
root6_2.withdraw()
root6_2.title('Delete Doctor')
root6_2.configure(background='burlywood4')

rwidth=root6_2.winfo_screenwidth()
rheight=root6_2.winfo_screenheight()
root6_2.geometry(('%dx%d')%(rwidth,rheight))

myfont4_2=Font(family='Aerial',size=50,slant='italic')
myfont4_2_1=Font(family='Aerial',size=20,slant='italic')

f6_2_1=Frame(root6_2,height=40,width=1400,bd=4,relief='solid',padx=50,pady=10)
f6_2_1.pack(padx=10,pady=10)

l6_2_1=Label(f6_2_1,text='Delete Doctor',height=5,width=120,font=myfont4_2_1,fg='Brown',bg='burlywood4')
l6_2_1.grid(padx=5,pady=10,row=0,column=0,columnspan=8)


l6_2_2=Label(f6_2_1,text='Name of Doctor',height=2,width=20,font=myfont4_2,fg='Brown',bg='burlywood4')
l6_2_2.grid(padx=3,pady=10,row=2,column=0)

e6_2_1=Entry(f6_2_1,textvariable=del_doct,width=20,font=myfont4_2,fg='burlywood4')
e6_2_1.grid(row=2,column=1,padx=5,pady=10)



b6_2_1=Button(f6_2_1,text='Back',command=back6_2_1,height=1,width=4,font=myfont,fg='Brown')
b6_2_1.grid(row=0,column=2,padx=5,pady=10)

b6_2_2=Button(f6_2_1,text='Exit',command=exit6_2_2,height=1,width=4,font=myfont,fg='Brown')
b6_2_2.grid(row=0,column=3,padx=2,pady=10)

b7_2_3=Button(f6_2_1,text='Delete',command=delete_d,height=1,width=8,font=myfont,fg='Brown')
b7_2_3.grid(row=2,column=2,padx=5,pady=10)



f6_2_1_1=Frame(f6_2_1,height=550,width=600,bd=4,relief='solid',padx=50,pady=10)
f6_2_1_1.grid(row=3,column=0,columnspan=4,padx=5,pady=10)



#*******_____table
tree14=ttk.Treeview(f6_2_1_1)

tree14['columns']=("0","1","2","3","4","5","6","7","8","9","10","11","12","13","14")
tree14.column("0",width=70)
tree14.column("1",width=70)
tree14.column("2",width=70)
tree14.column("3",width=70)
tree14.column("4",width=70)
tree14.column("5",width=70)
tree14.column("6",width=70)
tree14.column("7",width=70)
tree14.column("8",width=70)
tree14.column("9",width=70)
tree14.column("10",width=70)
tree14.column("11",width=70)
tree14.column("12",width=70)
tree14.column("13",width=70)
tree14.column("14",width=70)


tree14.heading("0",text="Count")
tree14.heading("1",text="Date")
tree14.heading("2",text="Id")
tree14.heading("3",text="Name")
tree14.heading("4",text="Age")
tree14.heading("5",text="Gender")
tree14.heading("6",text="Blood")
tree14.heading("7",text="Dept.")
tree14.heading("8",text="Phone")
tree14.heading("9",text="Email")
tree14.heading("10",text="Status")
tree14.heading("11",text="Address")
tree14.heading("12",text="Room")
tree14.heading("13",text="username")
tree14.heading("14",text="password")






tree14.pack(side="left")



######Search Doctor
search_recp=StringVar()

def back6_3_1():
        root5.deiconify()
        root6_3.withdraw()
        
def exit6_3_2():
        root6_3.withdraw()
        root2.deiconify()
        

def search6_3_3():
        con=mysql.connector.connect(host='localhost',user='root',password='',db='hospital')
        cur=con.cursor()
        
        getname=e6_3_1.get()

        query="select * from doctor where name=%s"
        cur.execute(query,(getname,))
        shw=cur.fetchall()
        try:
                for i in range(0,len(shw)):
                        tree15_1.insert('','end',values=shw[i])
                        messagebox.showinfo('info','Searched successfully')
        except:
                messagebox.showerror('info','Invalid Entry')
                    


root6_3=Tk()
root6_3.withdraw()
root6_3.title('search to Hospital')
root6_3.configure(background='burlywood4')

rwidth=root6_3.winfo_screenwidth()
rheight=root6_3.winfo_screenheight()
root6_3.geometry(('%dx%d')%(rwidth,rheight))

myfont4_3=Font(family='Aerial',size=30,slant='italic')
myfont4_3_1=Font(family='Aerial',size=20,slant='italic')

f6_3_1=Frame(root6_3,height=40,width=1400,bd=4,relief='solid',padx=50,pady=10)
f6_3_1.pack(padx=10,pady=10)

l6_3_1=Label(f6_3_1,text='Search Doctor',height=5,width=120,font=myfont4_2_1,fg='Brown',bg='burlywood4')
l6_3_1.grid(padx=5,pady=10,row=0,column=0,columnspan=4)


l6_3_2=Label(f6_3_1,text='Name of Doctor',height=2,width=20,font=myfont4_2,fg='Brown',bg='burlywood4')
l6_3_2.grid(padx=5,pady=10,row=2,column=0)

e6_3_1=Entry(f6_3_1,textvariable=search_recp,font=myfont,fg='burlywood4')
e6_3_1.grid(row=2,column=1,padx=5,pady=10)



b6_3_1=Button(f6_3_1,text='Back',command=back6_3_1,height=1,width=4,font=myfont,fg='Brown')
b6_3_1.grid(row=0,column=2,padx=5,pady=10)

b6_3_2=Button(f6_3_1,text='Exit',command=exit6_3_2,height=1,width=4,font=myfont,fg='Brown')
b6_3_2.grid(row=0,column=3,padx=5,pady=10)

b6_3_3=Button(f6_3_1,text='Search',command=search6_3_3,height=1,width=8,font=myfont,fg='Brown')
b6_3_3.grid(row=2,column=2,padx=5,pady=10)




f6_3_1_1=Frame(f6_3_1,height=500,width=600,bd=4,relief='solid',padx=50,pady=10)
f6_3_1_1.grid(row=3,column=0,columnspan=4,padx=5,pady=10)



#*******_____table
tree15=ttk.Treeview(f6_3_1_1)

tree15['columns']=("0","1","2","3","4","5","6","7","8","9","10","11","12","13","14")
tree15.column("0",width=80)
tree15.column("1",width=80)
tree15.column("2",width=80)
tree15.column("3",width=80)
tree15.column("4",width=80)
tree15.column("5",width=80)
tree15.column("6",width=80)
tree15.column("7",width=80)
tree15.column("8",width=80)
tree15.column("9",width=80)
tree15.column("10",width=80)
tree15.column("11",width=80)
tree15.column("12",width=80)
tree15.column("13",width=80)
tree15.column("14",width=80)


tree15.heading("0",text="Count")
tree15.heading("1",text="Date")
tree15.heading("2",text="Id")
tree15.heading("3",text="Name")
tree15.heading("4",text="Age")
tree15.heading("5",text="Gender")
tree15.heading("6",text="Blood.")
tree15.heading("7",text="Dept")
tree15.heading("8",text="Phone")
tree15.heading("9",text="Email")
tree15.heading("10",text="Status")
tree15.heading("11",text="Address")
tree15.heading("12",text="Room")
tree15.heading("13",text="Username")
tree15.heading("14",text="Password")



tree15.pack(side="left")


f6_3_1_2=Frame(f6_3_1,height=50,width=600,bd=4,relief='solid',padx=50,pady=10)
f6_3_1_2.grid(row=5,column=0,columnspan=4,padx=5,pady=10)



#*******____show searched doctor
tree15_1=ttk.Treeview(f6_3_1_2)

tree15_1['columns']=("0","1","2","3","4","5","6","7","8","9","10","11","12","13","14")
tree15_1.column("0",width=80)
tree15_1.column("1",width=80)
tree15_1.column("2",width=80)
tree15_1.column("3",width=80)
tree15_1.column("4",width=80)
tree15_1.column("5",width=80)
tree15_1.column("6",width=80)
tree15_1.column("7",width=80)
tree15_1.column("8",width=80)
tree15_1.column("9",width=80)
tree15_1.column("10",width=80)
tree15_1.column("11",width=80)
tree15_1.column("12",width=80)
tree15_1.column("13",width=80)
tree15_1.column("14",width=80)


tree15_1.heading("0",text="Count")
tree15_1.heading("1",text="Date")
tree15_1.heading("2",text="Id")
tree15_1.heading("3",text="Name")
tree15_1.heading("4",text="Age")
tree15_1.heading("5",text="Gender")
tree15_1.heading("6",text="Blood.")
tree15_1.heading("7",text="Dept")
tree15_1.heading("8",text="Phone")
tree15_1.heading("9",text="Email")
tree15_1.heading("10",text="Status")
tree15_1.heading("11",text="Address")
tree15_1.heading("12",text="Room")
tree15_1.heading("13",text="Username")
tree15_1.heading("14",text="Password")



tree15_1.pack(side="left")



####View Doctor
def back6_4_1():
        root5.deiconify()
        root6_4.withdraw()

def exit6_4_2():
        root6_4.withdraw()
        root2.deiconify()

root6_4=Tk()
root6_4.withdraw()
root6_4.title('View Doctor')
root6_4.configure(background='burlywood4')

rwidth=root6_4.winfo_screenwidth()
rheight=root6_4.winfo_screenheight()
root6_4.geometry(('%dx%d')%(rwidth,rheight))

myfont6_1=Font(family='Aerial',size=50,slant='italic')
myfont=Font(family='Aerial',size=16,slant='italic')

f6_4_1=Frame(root6_4,height=40,width=1400,bd=4,relief='solid',padx=50,pady=10)
f6_4_1.pack(padx=10,pady=10)

l6_4_1=Label(f6_4_1,text='View Doctor',height=5,width=120,font=myfont4,fg='Brown',bg='burlywood4')
l6_4_1.grid(padx=5,pady=10,row=0,column=0,columnspan=8)

b6_4_1=Button(f6_4_1,text='Back',command=back6_4_1,height=1,width=4,font=myfont,fg='Brown')
b6_4_1.grid(row=0,column=2,padx=5,pady=10)

b6_4_2=Button(f6_4_1,text='Exit',command=exit6_4_2,height=1,width=4,font=myfont,fg='Brown')
b6_4_2.grid(row=0,column=3,padx=5,pady=10)



f6_4_1_1=Frame(f6_4_1,height=550,width=600,bd=4,relief='solid',padx=50,pady=10)
f6_4_1_1.grid(row=2,column=0,columnspan=4,padx=5,pady=10)



#*******_____table
tree16=ttk.Treeview(f6_4_1_1)

tree16['columns']=("0","1","2","3","4","5","6","7","8","9","10","11","12","13","14")
tree16.column("0",width=80)
tree16.column("1",width=80)
tree16.column("2",width=80)
tree16.column("3",width=80)
tree16.column("4",width=80)
tree16.column("5",width=80)
tree16.column("6",width=80)
tree16.column("7",width=80)
tree16.column("8",width=80)
tree16.column("9",width=80)
tree16.column("10",width=80)
tree16.column("11",width=80)
tree16.column("12",width=80)
tree16.column("13",width=80)
tree16.column("14",width=80)

tree16.heading("0",text="Count")
tree16.heading("1",text="Date")
tree16.heading("2",text="Id")
tree16.heading("3",text="Name")
tree16.heading("4",text="Age")
tree16.heading("5",text="Gender")
tree16.heading("6",text="Blood")
tree16.heading("7",text="Dept.")
tree16.heading("8",text="Phone")
tree16.heading("9",text="Email")
tree16.heading("10",text="Status")
tree16.heading("11",text="Address")
tree16.heading("12",text="Room")
tree16.heading("13",text="Username")
tree16.heading("14",text="Password")


tree16.pack(side="left")




####View Patients Booked
def back6_4_1_1():
        root5.deiconify()
        root6_4_1.withdraw()

def exit6_4_2_1():
        root6_4_1.withdraw()
        root2.deiconify()

root6_4_1=Tk()
root6_4_1.withdraw()
root6_4_1.title('View Patient')
root6_4_1.configure(background='burlywood4')

rwidth=root6_4_1.winfo_screenwidth()
rheight=root6_4_1.winfo_screenheight()
root6_4_1.geometry(('%dx%d')%(rwidth,rheight))

myfont6_1=Font(family='Aerial',size=50,slant='italic')
myfont=Font(family='Aerial',size=16,slant='italic')

f6_5=Frame(root6_4_1,height=40,width=1400,bd=4,relief='solid',padx=50,pady=10)
f6_5.pack(padx=10,pady=10)

l6_4_1=Label(f6_5,text='Patient',height=5,width=120,font=myfont4,fg='Brown',bg='burlywood4')
l6_4_1.grid(padx=5,pady=10,row=0,column=0,columnspan=6)

b6_4_1=Button(f6_5,text='Back',command=back6_4_1_1,height=1,width=4,font=myfont,fg='Brown')
b6_4_1.grid(row=0,column=4,padx=5,pady=10)

b6_4_2=Button(f6_5,text='Exit',command=exit6_4_2_1,height=1,width=4,font=myfont,fg='Brown')
b6_4_2.grid(row=0,column=5,padx=5,pady=10)



f6_5_1=Frame(f6_5,height=550,width=600,bd=4,relief='solid',padx=50,pady=10)
f6_5_1.grid(row=2,column=0,columnspan=4,padx=5,pady=10)



#*******_____table
tree16_2=ttk.Treeview(f6_5_1)

tree16_2['columns']=("0","1","2")
tree16_2.column("0",width=100)
tree16_2.column("1",width=100)
tree16_2.column("2",width=100)

tree16_2.heading("0",text="Doctor")
tree16_2.heading("1",text="Patient")
tree16_2.heading("2",text="Room")


tree16_2.pack(side="left")


##################################################################################
###################_________________Doctor Panel Finished______________###########
##################################################################################





##################################################################################
###################_________________Patient panel start______________#############
##################################################################################



#_______________________________________root7________________________________

#______________________________________def button root7______________________

def add_new_patient():
        print('add_new_patient')
        root8.deiconify()

def update_patient():
        root9.deiconify()
        con=mysql.connector.connect(host='localhost',user='root',password='',db='hospital')
        cur=con.cursor()
        query="select * from patient"
        cur.execute(query,)
        up_p=cur.fetchall()
        try:
                 x = tree9.get_children()
                 for item in x: tree9.delete(item)
                 for i in range(0,len(up_p)):
                         tree9.insert('','end',values=up_p[i])
        except:
                print('Not executed')

def delete_patient():
        root10.deiconify()
        con=mysql.connector.connect(host='localhost',user='root',password='',db='hospital')
        cur=con.cursor()
        query="select * from patient"
        cur.execute(query,)
        del_p=cur.fetchall()
        try:
                 x = tree10.get_children()
                 for item in x: tree10.delete(item)
                 for i in range(0,len(del_p)):
                        tree10.insert('','end',values=del_p[i])
        except:
                print('Not executed')

def search_patient():
        root11.deiconify()
        con=mysql.connector.connect(host='localhost',user='root',password='',db='hospital')
        cur=con.cursor()
        query="select * from patient"
        cur.execute(query,)
        ser_p=cur.fetchall()
        try:
                 x = tree11.get_children()
                 for item in x: tree11.delete(item)
                 for i in range(0,len(ser_p)):
                        tree11.insert('','end',values=ser_p[i])
        except:
                print('Not executed')

def view_patient():
        root12.deiconify()
        con=mysql.connector.connect(host='localhost',user='root',password='',db='hospital')
        cur=con.cursor()
        query="select * from patient"
        cur.execute(query,)
        vie_p=cur.fetchall()
        try:
                 x = tree12.get_children()
                 for item in x: tree12.delete(item)
                 for i in range(0,len(vie_p)):
                        tree12.insert('','end',values=vie_p[i])
        except:
                print('Not executed')
                

def Appoinment():
        root13.deiconify()
        con=mysql.connector.connect(host='localhost',user='root',password='',db='hospital')
        cur=con.cursor()
        query="select count,id,name,dept,phone,room from doctor"
        cur.execute(query,)
        sh_d=cur.fetchall()
        try:
                 x = tree13_b.get_children()
                 for item in x: tree13_b.delete(item)
                 for i in range(0,len(sh_d)):
                        tree13_b.insert('','end',values=sh_d[i])
        except:
                print('Not executed')

def exit35_1():
        root7.withdraw()
        root2.deiconify()



#____________________________________________________________________________
root7=Tk()
root7.withdraw()
root7.title('Welcome to Patient panel')
root7.configure(background='burlywood4')

rwidth=root7.winfo_screenwidth()
rheight=root7.winfo_screenheight()
root7.geometry(('%dx%d')%(rwidth,rheight))

myfont=Font(family='Aerial',size=16,slant='italic')



###      Patient's Panel

f10=Frame(root7,height=40,width=1400,bd=4,relief='solid',padx=50,pady=10)
f10.pack(pady=5)

l28=Label(f10,text='Patient Management',height=5,width=60,font=myfont,fg='Brown',bg='Black')
l28.grid(padx=5,pady=10,row=0,column=2,columnspan=4)

l29=Label(f10,text='''Welcome

  to Patient
  
    Managemet''',height=10,width=15,font=myfont,fg='Brown',bg='Black')
l29.grid(padx=10,pady=5,row=2,column=0)

b30=Button(f10,text='Add New',command=add_new_patient,height=5,width=10,font=myfont,fg='Brown')
b30.grid(row=2,column=2,padx=10,pady=20)

b31=Button(f10,text='Update',command=update_patient,height=5,width=10,font=myfont,fg='Brown')
b31.grid(row=2,column=3,padx=10,pady=20)

b32=Button(f10,text='Delete',command=delete_patient,height=5,width=10,font=myfont,fg='Brown')
b32.grid(row=2,column=4,padx=10,pady=20)

b33=Button(f10,text='Search',command=search_patient,height=5,width=10,font=myfont,fg='Brown')
b33.grid(row=2,column=5,padx=10,pady=20)

b34=Button(f10,text='view',command=view_patient,height=5,width=10,font=myfont,fg='Brown')
b34.grid(row=3,column=2,padx=10,pady=20)

b35=Button(f10,text='Appoinment',command=Appoinment,height=5,width=10,font=myfont,fg='Brown')
b35.grid(row=3,column=3,padx=10,pady=20)

b35_1=Button(f10,text='Exit',command=exit35_1,height=5,width=10,font=myfont,fg='Brown')
b35_1.grid(row=3,column=4,padx=10,pady=20)


#____________________________________root8__________________________________________

def back49():
        root8.withdraw()
        root7.deiconify()

def exit48():
        root8.withdraw()
        root2.deiconify()

dtp=StringVar()
idp=StringVar()
namep=StringVar()
agep=IntVar()
genderp=StringVar()
addressp=StringVar()
phonep=StringVar()
statusp=StringVar()
diseasep=StringVar()
roomp=IntVar()

def add_p():
        con=mysql.connector.connect(host='localhost',user='root',password='',db='hospital')
        cur=con.cursor()

        getdtp=e36.get()
        getidp=e37.get()
        getnamep=e38.get()
        getagep=e39.get()
        getgenderp=e40.get()
        getaddressp=e41.get()
        getphonep=e42.get()
        getstatusp=e43.get()
        getdiseasep=e44.get()
        getroomp=e45.get()

        try:
                query="insert into patient(date,id,name,age,gender,address,phone,status,disease,room) Values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                cur.execute(query,(getdtp,getidp,getnamep,getagep,getgenderp,getaddressp,getphonep,getstatusp,getdiseasep,getroomp,))
                messagebox.showinfo("Info","Added Successfully")
        except:
                messagebox.showerror('Error','Not Added')
root8=Tk()
root8.withdraw()
root8.title('Welcome to Add patient')
root8.configure(background='burlywood4')

rwidth=root8.winfo_screenwidth()
rheight=root8.winfo_screenheight()
root8.geometry(('%dx%d')%(rwidth,rheight))

myfont4=Font(family='Aerial',size=50,slant='italic')
myfont=Font(family='Aerial',size=16,slant='italic')


###_____________To Add new  Patient__________________


f11=Frame(root8,height=40,width=1400,bd=4,relief='solid',padx=50,pady=10)
f11.pack(padx=10,pady=10)

l35=Label(f11,text='Add Patient',height=5,width=120,font=myfont4,fg='Brown',bg='burlywood4')
l35.grid(padx=5,pady=10,row=0,column=0,columnspan=8)


b48=Button(f11,text='Exit',command=exit48,height=1,width=4,font=myfont,fg='Brown')
b48.grid(row=0,column=5,columnspan=2,padx=5,pady=10)

b49=Button(f11,text='Back',command=back49,height=1,width=4,font=myfont,fg='Brown')
b49.grid(row=0,column=4,columnspan=2,padx=5,pady=10)



l36=Label(f11,text='Date',font=myfont,fg='burlywood4')
l36.grid(padx=10,pady=20,row=2,column=0)

e36=Entry(f11,textvariable=dtp,font=myfont,fg='burlywood4')
e36.grid(row=2,column=1,padx=10,pady=20)

l37=Label(f11,text='Id',font=myfont,fg='burlywood4')
l37.grid(padx=10,pady=20,row=3,column=0)

e37=Entry(f11,textvariable=idp,font=myfont,fg='burlywood4')
e37.grid(row=3,column=1,padx=10,pady=20)

l38=Label(f11,text='Name',font=myfont,fg='burlywood4')
l38.grid(padx=10,pady=20,row=4,column=0)

e38=Entry(f11,textvariable=namep,font=myfont,fg='Brown')
e38.grid(row=4,column=1,padx=10,pady=20)

l39=Label(f11,text='Age',font=myfont,fg='burlywood4')
l39.grid(padx=10,pady=20,row=5,column=0)

e39=Entry(f11,textvariable=agep,font=myfont,fg='burlywood4')
e39.grid(row=5,column=1,padx=10,pady=20)

l40=Label(f11,text='Gender',font=myfont,fg='burlywood4')
l40.grid(padx=10,pady=20,row=6,column=0)

e40=Entry(f11,textvariable=genderp,font=myfont,fg='burlywood4')
e40.grid(row=6,column=1,padx=10,pady=20)


###******______


l41=Label(f11,text='Address',font=myfont,fg='burlywood4')
l41.grid(padx=10,pady=20,row=2,column=3)

e41=Entry(f11,textvariable=addressp,font=myfont,fg='burlywood4')
e41.grid(row=2,column=4,padx=10,pady=20)

l42=Label(f11,text='Phone Number',font=myfont,fg='burlywood4')
l42.grid(padx=10,pady=20,row=3,column=3)

e42=Entry(f11,textvariable=phonep,font=myfont,fg='burlywood4')
e42.grid(row=3,column=4,padx=10,pady=20)

l43=Label(f11,text='Status',font=myfont,fg='burlywood4')
l43.grid(padx=10,pady=20,row=4,column=3)

e43=Entry(f11,textvariable=statusp,font=myfont,fg='burlywood4')
e43.grid(row=4,column=4,padx=10,pady=20)

l44=Label(f11,text='Disease',font=myfont,fg='burlywood4')
l44.grid(padx=10,pady=20,row=5,column=3)

e44=Entry(f11,textvariable=diseasep,font=myfont,fg='burlywood4')
e44.grid(row=5,column=4,padx=10,pady=20)

l45=Label(f11,text='Room',font=myfont,fg='burlywood4')
l45.grid(padx=10,pady=20,row=6,column=3)

e45=Entry(f11,textvariable=roomp,font=myfont,fg='burlywood4')
e45.grid(row=6,column=4,padx=10,pady=20)


###******_________

"""b46=Button(f11,text='clear',height=1,width=4,font=myfont,fg='Brown')
b46.grid(row=8,column=2,padx=5,pady=10)"""

b47=Button(f11,text='Add',command=add_p,height=1,width=4,font=myfont,fg='Brown')
b47.grid(row=8,column=3,padx=5,pady=10)




#####______Update Patient

def back52():
        root9.withdraw()
        root7.deiconify()

def exit53():
        root9.withdraw()
        root2.deiconify()


"""def update_p():
         con=mysql.connector.connect(host='localhost',user='root',password='',db='hospital')
         cur=con.cursor()

         query="insert into patient(joining,id,name,age,gender,blood,email,phone,address,status,username,password) Values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
         cur.execute(query,(getdt,getidr,getnamer,getager,getgenderr,getbloodr,getemailr,getphoner,getaddressr,getmartialr,getusr,getpwr,))"""

        

root9=Tk()
root9.withdraw()
root9.title('Welcome to update patient')
root9.configure(background='burlywood4')

rwidth=root9.winfo_screenwidth()
rheight=root9.winfo_screenheight()
root9.geometry(('%dx%d')%(rwidth,rheight))

myfont4_1=Font(family='Aerial',size=50,slant='italic')
myfont=Font(family='Aerial',size=16,slant='italic')

f12=Frame(root9,height=40,width=1400,bd=4,relief='solid',padx=50,pady=10)
f12.pack(padx=10,pady=10)

l51=Label(f12,text='Update Patient',height=5,width=120,font=myfont4,fg='Brown',bg='burlywood4')
l51.grid(padx=5,pady=10,row=0,column=0,columnspan=6)

b52=Button(f12,text='Back',command=back52,height=1,width=4,font=myfont,fg='Brown')
b52.grid(row=0,column=2,padx=5,pady=10,columnspan=2)

b53=Button(f12,text='Exit',command=exit53,height=1,width=4,font=myfont,fg='Brown')
b53.grid(row=0,column=3,padx=5,pady=10,columnspan=2)

"""b54=Button(f12,text='Update',command=update_p,height=1,width=8,font=myfont,fg='Brown')
b54.grid(row=10,column=2,padx=10,pady=10)"""


f12_1=Frame(f12,height=550,width=600,bd=4,relief='solid',padx=50,pady=10)
f12_1.grid(row=1,column=0,columnspan=4,padx=5,pady=10)


#*******_____table
tree9=ttk.Treeview(f12_1)

tree9['columns']=("0","one","two","three","four","five","six","seven","eight","nine","ten")
tree9.column("0",width=100)
tree9.column("one",width=100)
tree9.column("two",width=100)
tree9.column("three",width=100)
tree9.column("four",width=100)
tree9.column("five",width=100)
tree9.column("six",width=100)
tree9.column("seven",width=100)
tree9.column("eight",width=100)
tree9.column("nine",width=100)
tree9.column("ten",width=100)


tree9.heading("0",text="Count")
tree9.heading("one",text="Date")
tree9.heading("two",text="Id")
tree9.heading("three",text="Name")
tree9.heading("four",text="Age")
tree9.heading("five",text="Gender")
tree9.heading("six",text="Address")
tree9.heading("seven",text="phone")
tree9.heading("eight",text="status")
tree9.heading("nine",text="disease")
tree9.heading("ten",text="room")


tree9.pack(side="left")



######Delete patient

del_patie=StringVar()

def back58():
        root7.deiconify()
        root10.withdraw()
        
def exit59():
        root10.withdraw()
        root2.deiconify()
        

def delete_p():
        print('del patient')
        con=mysql.connector.connect(host='localhost',user='root',password='',db='hospital')
        cur=con.cursor()
        
        getname=e57.get()

        query="delete from Patient where name=%s"
        cur.execute(query,(getname,))
        messagebox.showinfo('info','Deleted successfully')
                    
        print('Deleted successfully')


root10=Tk()
root10.withdraw()
root10.title('Welcome to delete patient')
root10.configure(background='burlywood4')

rwidth=root10.winfo_screenwidth()
rheight=root10.winfo_screenheight()
root10.geometry(('%dx%d')%(rwidth,rheight))

myfont4_2=Font(family='Aerial',size=30,slant='italic')
myfont4_2_1=Font(family='Aerial',size=20,slant='italic')

f13=Frame(root10,height=40,width=1400,bd=4,relief='solid',padx=50,pady=10)
f13.pack(padx=10,pady=10)

l55=Label(f13,text='Delete patient',height=5,width=120,font=myfont4_2_1,fg='Brown',bg='burlywood4')
l55.grid(padx=5,pady=10,row=0,column=0,columnspan=8)


l56=Label(f13,text='Name of Patient',height=2,width=20,font=myfont4_2,fg='Brown',bg='burlywood4')
l56.grid(padx=5,pady=10,row=2,column=1,columnspan=2)

e57=Entry(f13,textvariable=del_patie,font=myfont,fg='burlywood4')
e57.grid(row=2,column=2,padx=5,pady=10,columnspan=3)



b58=Button(f13,text='Back',command=back58,height=1,width=4,font=myfont,fg='Brown')
b58.grid(row=0,column=5,columnspan=2,padx=5,pady=10)

b59=Button(f13,text='Exit',command=exit59,height=1,width=4,font=myfont,fg='Brown')
b59.grid(row=0,column=6,columnspan=2,padx=5,pady=10)

b60=Button(f13,text='Delete',command=delete_p,height=1,width=8,font=myfont,fg='Brown')
b60.grid(row=2,column=4,columnspan=2,padx=5,pady=10)


f13_1=Frame(f13,height=550,width=600,bd=4,relief='solid',padx=50,pady=10)
f13_1.grid(row=3,column=0,columnspan=8,padx=5,pady=10)



#*******_____table
tree10=ttk.Treeview(f13_1)

tree10['columns']=("0","1","2","3","4","5","6","7","8","9","10")
tree10.column("0",width=80)
tree10.column("1",width=80)
tree10.column("2",width=80)
tree10.column("3",width=80)
tree10.column("4",width=80)
tree10.column("5",width=80)
tree10.column("6",width=80)
tree10.column("7",width=80)
tree10.column("8",width=80)
tree10.column("9",width=80)
tree10.column("10",width=80)

tree10.heading("0",text="Count")
tree10.heading("1",text="Date")
tree10.heading("2",text="Id")
tree10.heading("3",text="Name")
tree10.heading("4",text="Age")
tree10.heading("5",text="Gender")
tree10.heading("6",text="Address")
tree10.heading("7",text="Phone")
tree10.heading("8",text="Status")
tree10.heading("9",text="Disease")
tree10.heading("10",text="Room")




tree10.pack(side="left")


######Search patient
search_patie=StringVar()

def back64():
        root7.deiconify()
        root11.withdraw()
        
def exit65():
        root11.withdraw()
        root2.deiconify()
        

def search66():
        con=mysql.connector.connect(host='localhost',user='root',password='',db='hospital')
        cur=con.cursor()
        
        getname=e63.get()

        query="select * from Patient where name=%s"
        cur.execute(query,(getname,))
        shw=cur.fetchall()
        try:
                for i in range(0,len(shw)):
                        tree11_1.insert('','end',values=shw[i])
                        messagebox.showinfo('info','Searched successfully')
        except:
                messagebox.showerror('error','Invalid entry')
                    
        print('searched successfully')
        

root11=Tk()
root11.withdraw()
root11.title('search to Hospital')
root11.configure(background='burlywood4')

rwidth=root11.winfo_screenwidth()
rheight=root11.winfo_screenheight()
root11.geometry(('%dx%d')%(rwidth,rheight))

myfont4_3=Font(family='Aerial',size=30,slant='italic')
myfont4_3_1=Font(family='Aerial',size=20,slant='italic')

f14=Frame(root11,height=40,width=1400,bd=4,relief='solid',padx=50,pady=10)
f14.pack(padx=10,pady=10)

l61=Label(f14,text='Search Patient',height=5,width=120,font=myfont4_2_1,fg='Brown',bg='burlywood4')
l61.grid(padx=5,pady=10,row=0,column=0,columnspan=6)


l62=Label(f14,text='Name of Patient',height=2,width=20,font=myfont4_2,fg='Brown',bg='burlywood4')
l62.grid(padx=5,pady=10,row=2,column=0,columnspan=2)

e63=Entry(f14,textvariable=search_patie,font=myfont,fg='burlywood4')
e63.grid(row=2,column=1,padx=5,pady=10,columnspan=3)



b64=Button(f14,text='Back',command=back64,height=1,width=4,font=myfont,fg='Brown')
b64.grid(row=0,column=3,padx=5,pady=10,columnspan=2)

b65=Button(f14,text='Exit',command=exit65,height=1,width=4,font=myfont,fg='Brown')
b65.grid(row=0,column=4,padx=5,pady=10,columnspan=2)

b66=Button(f14,text='Search',command=search66,height=1,width=8,font=myfont,fg='Brown')
b66.grid(row=2,column=3,padx=5,pady=10,columnspan=2)



f14_1=Frame(f14,height=550,width=600,bd=4,relief='solid',padx=50,pady=10)
f14_1.grid(row=3,column=0,columnspan=8,padx=5,pady=10)



#*******_____table
tree11=ttk.Treeview(f14_1)

tree11['columns']=("0","1","2","3","4","5","6","7","8","9","10")
tree11.column("0",width=80)
tree11.column("1",width=80)
tree11.column("2",width=80)
tree11.column("3",width=80)
tree11.column("4",width=80)
tree11.column("5",width=80)
tree11.column("6",width=80)
tree11.column("7",width=80)
tree11.column("8",width=80)
tree11.column("9",width=80)
tree11.column("10",width=80)


tree11.heading("0",text="Count")
tree11.heading("1",text="Date")
tree11.heading("2",text="Id")
tree11.heading("3",text="Name")
tree11.heading("4",text="Age")
tree11.heading("5",text="Gender")
tree11.heading("6",text="Address")
tree11.heading("7",text="Phone")
tree11.heading("8",text="Status")
tree11.heading("9",text="Disease")
tree11.heading("10",text="Room")



tree11.pack(side="left")

#show patient i.e searched

f14_2=Frame(f14,height=550,width=600,bd=4,relief='solid',padx=50,pady=10)
f14_2.grid(row=5,column=0,columnspan=8,padx=5,pady=10)

tree11_1=ttk.Treeview(f14_2)

tree11_1['columns']=("0","1","2","3","4","5","6","7","8","9","10")
tree11_1.column("0",width=80)
tree11_1.column("1",width=80)
tree11_1.column("2",width=80)
tree11_1.column("3",width=80)
tree11_1.column("4",width=80)
tree11_1.column("5",width=80)
tree11_1.column("6",width=80)
tree11_1.column("7",width=80)
tree11_1.column("8",width=80)
tree11_1.column("9",width=80)
tree11_1.column("10",width=80)


tree11_1.heading("0",text="Count")
tree11_1.heading("1",text="Date")
tree11_1.heading("2",text="Id")
tree11_1.heading("3",text="Name")
tree11_1.heading("4",text="Age")
tree11_1.heading("5",text="Gender")
tree11_1.heading("6",text="Address")
tree11_1.heading("7",text="Phone")
tree11_1.heading("8",text="Status")
tree11_1.heading("9",text="Disease")
tree11_1.heading("10",text="Room")



tree11_1.pack(side="left")


#####View Patient
def back68():
        root7.deiconify()
        root12.withdraw()

def exit69():
        root12.withdraw()
        root2.deiconify()

root12=Tk()
root12.withdraw()
root12.title('View Patient')
root12.configure(background='burlywood4')

rwidth=root12.winfo_screenwidth()
rheight=root12.winfo_screenheight()
root12.geometry(('%dx%d')%(rwidth,rheight))

myfont4_1=Font(family='Aerial',size=50,slant='italic')
myfont=Font(family='Aerial',size=16,slant='italic')

f15=Frame(root12,height=40,width=1400,bd=4,relief='solid',padx=50,pady=10)
f15.pack(padx=10,pady=10)

l67=Label(f15,text='View Patient',height=5,width=120,font=myfont4,fg='Brown',bg='burlywood4')
l67.grid(padx=5,pady=10,row=0,column=0,columnspan=6)

b68=Button(f15,text='Back',command=back68,height=1,width=4,font=myfont,fg='Brown')
b68.grid(row=0,column=3,padx=5,pady=10,columnspan=2)

b69=Button(f15,text='Exit',command=exit69,height=1,width=4,font=myfont,fg='Brown')
b69.grid(row=0,column=4,padx=5,pady=10,columnspan=2)



f15_1=Frame(f15,height=550,width=600,bd=4,relief='solid',padx=50,pady=10)
f15_1.grid(row=2,column=0,columnspan=8,padx=5,pady=10)



#*******_____table
tree12=ttk.Treeview(f15_1)

tree12['columns']=("0","1","2","3","4","5","6","7","8","9","10")
tree12.column("0",width=80)
tree12.column("1",width=80)
tree12.column("2",width=80)
tree12.column("3",width=80)
tree12.column("4",width=80)
tree12.column("5",width=80)
tree12.column("6",width=80)
tree12.column("7",width=80)
tree12.column("8",width=80)
tree12.column("9",width=80)
tree12.column("10",width=80)


tree12.heading("0",text="Count")
tree12.heading("1",text="Date")
tree12.heading("2",text="Id")
tree12.heading("3",text="Name")
tree12.heading("4",text="Age")
tree12.heading("5",text="Gender")
tree12.heading("6",text="Address")
tree12.heading("7",text="Phone")
tree12.heading("8",text="Status")
tree12.heading("9",text="Disease")
tree12.heading("10",text="Room")


tree12.pack(side="right")




#####Appoinments
dname=StringVar()
pname=StringVar()
r=IntVar()

def backbb1():
        root7.deiconify()
        root13.withdraw()

def exitbb2():
        root13.withdraw()
        root2.deiconify()

def book_appoinment():
        con=mysql.connector.connect(host='localhost',user='root',password='',db='hospital')
        print('Con connected')
        cur=con.cursor()
        print('Con connected')
        
        gdname=eb2.get()
        print(gdname)
        gpname=eb3.get()
        print(gpname)
        gr=eb4.get()
        print(gr)
        
        query="insert into appointment(dName,pName,room) Values(%s,%s,%s)"
        print('query executed')
        cur.execute(query,(gdname,gpname,gr,))
        print('cur executed')
        messagebox.showinfo('info','Booked Appoinment')
        """except:
                messagebox.showerror('Error','Unable to book')"""
        
        
        

root13=Tk()
root13.withdraw()
root13.title('Appoinments')
root13.configure(background='burlywood4')

rwidth=root13.winfo_screenwidth()
rheight=root13.winfo_screenheight()
root13.geometry(('%dx%d')%(rwidth,rheight))

myfont4_1=Font(family='Aerial',size=50,slant='italic')
myfont=Font(family='Aerial',size=16,slant='italic')

fb=Frame(root13,height=40,width=1400,bd=4,relief='solid',padx=50,pady=10)
fb.pack(padx=10,pady=10)

lb1=Label(fb,text='Appoinment',height=5,width=120,font=myfont4,fg='Brown',bg='burlywood4')
lb1.grid(padx=5,pady=10,row=0,column=0,columnspan=6)

lb2=Label(fb,text='Doctor Name',font=myfont)
lb2.grid(row=1,column=0)

eb2=Entry(fb,textvariable=dname,font=myfont)
eb2.grid(row=1,column=1)

lb3=Label(fb,text='Patient Name',font=myfont)
lb3.grid(row=2,column=0)

eb3=Entry(fb,textvariable=pname,font=myfont)
eb3.grid(row=2,column=1)

lb4=Label(fb,text='Room',font=myfont)
lb4.grid(row=3,column=0)

eb4=Entry(fb,textvariable=r,font=myfont)
eb4.grid(row=3,column=1)

bb1=Button(fb,text='Back',command=backbb1,height=1,width=4,font=myfont,fg='Brown')
bb1.grid(row=0,column=3,padx=5,pady=10,columnspan=2)

bb2=Button(fb,text='Exit',command=exitbb2,height=1,width=4,font=myfont,fg='Brown')
bb2.grid(row=0,column=4,padx=5,pady=10,columnspan=2)

bb3=Button(fb,text='Book',command=book_appoinment,height=1,width=14,font=myfont,fg='Brown')
bb3.grid(row=2,column=2,padx=10,pady=10)



fb_1=Frame(fb,height=550,width=600,bd=4,relief='solid',padx=50,pady=10)
fb_1.grid(row=5,column=0,columnspan=8,padx=5,pady=10)



#*******_____table
tree13_b=ttk.Treeview(fb_1)

tree13_b['columns']=("1","2","3","4","5","6")
tree13_b.column("1",width=80)
tree13_b.column("2",width=80)
tree13_b.column("3",width=80)
tree13_b.column("4",width=80)
tree13_b.column("5",width=80)
tree13_b.column("6",width=80)


tree13_b.heading("1",text="Count")
tree13_b.heading("2",text="Id")
tree13_b.heading("3",text="Name")
tree13_b.heading("4",text="Dept")
tree13_b.heading("5",text="Phone")
tree13_b.heading("6",text="Room")


tree13_b.pack(side="left")

##@@@@@@@@@@@@@@@@@@@@@@@_________Patient panel Finished__________@@@@@@@@@@@@@@@@@@



