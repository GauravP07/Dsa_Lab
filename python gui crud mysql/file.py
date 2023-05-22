from tkinter.ttk import *
from tkinter import *
import mysql.connector
#import cx_Oracle
from tkinter import messagebox
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Aditya123",
    database="2018btecs00034"
)


mycursor=mydb.cursor()
root=Tk()
root.title("Mysql CRUD operations")
root.geometry("1200x700")
# photo=PhotoImage(file='image.png')
label12=Label(root).grid(row=8,column=5)
label1=Label(root,text="EmpNo",width=60,height=2,bg="yellow").grid(row=0,column=0)
label2=Label(root,text="Name",width=60,height=2,bg="blue").grid(row=1,column=0)
label4=Label(root,text="address",width=60,height=2,bg="red").grid(row=2,column=0)
label5=Label(root,text="Grade",width=60,height=2,bg="pink").grid(row=3,column=0)
label6=Label(root,text="Salary",width=60,height=2,bg="pink").grid(row=4,column=0)
label7=Label(root,text="Date_of_joining",width=60,height=2,bg="pink").grid(row=5,column=0)
label8=Label(root,width=10,height=2).grid(row=7,column=2)
label9=Label(root,width=10,height=2).grid(row=7,column=4)
label10=Label(root,width=10,height=2).grid(row=7,column=6)
label11=Label(root,width=10,height=2).grid(row=7,column=8)
e1=Entry(root,width=30,borderwidth=8)
e1.grid(row=0,column=1)
e2=Entry(root,width=30,borderwidth=8)
e2.grid(row=1,column=1)
e3=Entry(root,width=30,borderwidth=8)
e3.grid(row=2,column=1)
e4=Entry(root,width=30,borderwidth=8)
e4.grid(row=3,column=1)
e5=Entry(root,width=30,borderwidth=8)
e5.grid(row=4,column=1)
e6=Entry(root,width=30,borderwidth=8)
e6.grid(row=5,column=1)


def register():
    EmpNo=e1.get()
    dbPrn=""
    select_query="select Empno from employee where Empno='%s'" %(EmpNo)
    mycursor.execute(select_query)
    result=mycursor.fetchall()
    for i in result:
        dbPrn=i[0]
    if(EmpNo == dbPrn):
        messagebox.askokcancel("Information","Record Already exists")
    else:
        insert_query="insert into employee values(%s,%s,%s,%s,%s,%s)"
        EmpNo=e1.get()
        Name=e2.get()
        address=e3.get()
        Grade=e4.get()
        Salary=e5.get()
        Date_of_joining=e6.get()
        
        if(EmpNo != "" and Name != "" and address != "" and Grade != "" and Salary != "" and Date_of_joining != ""):
            values=(EmpNo,Name,address,Grade,Salary,Date_of_joining)
            mycursor.execute(insert_query,values)
            mydb.commit()
            messagebox.askokcancel("Information","Record inserted")
            e1.delete(0, END)
            e2.delete(0, END)
            e3.delete(0, END)
            e4.delete(0, END)
            e5.delete(0, END)
            e6.delete(0, END)

        else:
            messagebox.askokcancel("Information", "Please fill all details!")
def show_record():
    EmpNo=e1.get()
    dbPrn=""
    select_query="select EmpNo from employee where EmpNo='%s'" %(EmpNo)
    mycursor.execute(select_query)
    result1=mycursor.fetchall()
    for i in result1:
        dbPrn=i[0]
    select_query1="select Name,address,Grade,Salary,Date_of_joining from student where EmpNo='%s'" %(EmpNo)
    mycursor.execute(select_query1)
    result2=mycursor.fetchall()
    Name=""
    address=""
    Grade=""
    Salary=""
    Date_of_joining=""
    if(EmpNo == dbPrn):
        for i in result2:
            Name=i[0]
            address=i[1]
            Grade=i[2]
            Salary=i[3]
            Date_of_joining=i[4]
    
        e2.insert(0,Name)
        e3.insert(0,address)
        e4.insert(0,Grade)
        e5.insert(0,Salary)
        e6.insert(0,Date_of_joining)

    else:
        messagebox.askokcancel("Information","No such Record exist!")

def delete():
    EmpNo=e1.get()
    delete_query="delete from employee where EmpNo='%s'" %(EmpNo)
    mycursor.execute(delete_query)
    mydb.commit()
    messagebox.showinfo("Information","Record deleted successfully!")
    e1.delete(0,END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)

def update():
    EmpNo=e1.get()
    Name=e2.get()
    address=e3.get()
    Grade=e4.get()
    Salary=e5.get()
    Date_of_joining=e6.get()

    update_query="update employee set Name='%s', address='%s', Grade='%s',Salary='%s', Date_of_joining='%s' where EmpNo='%s'" %(Name,address,Grade,Salary,Date_of_joining,EmpNo)
    mycursor.execute(update_query)
    mydb.commit()
    messagebox.showinfo("Info","Record updated successfully!")

# def Showall():
#     class A(Frame):
#         def _init_(self, parent):
#             Frame._init_(self, parent)
#             self.CreateUI()
#             self.LoadTable()
#             self.grid(sticky=(N, S, W, E))
#             parent.grid_rowconfigure(0, weight=1)
#             parent.grid_columnconfigure(0, weight=1)
#         def CreateUI(self):
#             tv= Treeview(self)
#             tv['columns']=('prn', 'name', 'dept', 'class_name', 'City', 'State', 'Age')
#             tv.heading('#0',text='prn',anchor='center')
#             tv.column('#0',anchor='center')
#             tv.heading('#1', text='name', anchor='center')
#             tv.column('#1', anchor='center')
#             tv.heading('#2', text='dept', anchor='center')
#             tv.column('#2', anchor='center')
#             tv.heading('#3', text='class_name', anchor='center')
#             tv.column('#3', anchor='center')
#             tv.heading('#4', text='City', anchor='center')
#             tv.column('#4', anchor='center')
#             tv.heading('#5', text='State', anchor='center')
#             tv.column('#5', anchor='center')
#             tv.heading('#6', text='Age', anchor='center')
#             tv.column('#6', anchor='center')
#             tv.grid(sticky=(N,S,W,E))
#             self.treeview = tv
#             self.grid_rowconfigure(0,weight=1)
#             self.grid_columnconfigure(0,weight=1)
#         def LoadTable(self):
#             select_query="select_query * from student"
#             mycursor.execute(select_query)
#             result=mycursor.fetchall()
#             prn=""
#             name=""
#             dept=""
#             class_name=""
#             City=""
#             State=""
#             Age=""
#             for i in result:
#                 prn=i[0]
#                 name=i[1]
#                 dept=i[2]
#                 class_name=i[3]
#                 City=i[4]
#                 State=i[5]
#                 Age=i[6]
#                 self.treeview.insert("",'end',text=prn,values=(name,dept,class_name,City,State,Age))
    root=Tk()
    root.title("Overview Page")
    # A(root)
def Clear():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)

button1=Button(root,text="Register",width=10,height=2,command=register).grid(row=7,column=0)
button2=Button(root,text="Delete",width=10,height=2,command=delete).grid(row=7,column=1)
button3=Button(root,text="Update",width=10,height=2,command=update).grid(row=7,column=3)
button4=Button(root,text="Show record",width=10,height=2,command=show_record).grid(row=7,column=5)
# button5=Button(root,text="Show All",width=10,height=2,command=Showall).grid(row=7,column=7)
button6=Button(root,text="Clear",width=10,height=2,command=Clear).grid(row=7,column=9)
root.mainloop()