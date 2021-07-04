from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
import sqlite3  as db
import matplotlib.pyplot as plt
from dateutil import parser
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)


def init():
    connectionObjn = db.connect("expenseTracker.db")
    curr = connectionObjn.cursor()
    query = '''
    create table if not exists expenses (
        
        date string,
        name string,
        title string,
        expense number
        )
    '''
    curr.execute(query)
    connectionObjn.commit()
    connectionObjn.close()




# functions
def submitexpense():
    connectionObjn = db.connect("expenseTracker.db")
    curr = connectionObjn.cursor()
    values=[dateEntry.get(),Name.get(),Title.get(),Expense.get()]
    print(values)
    expense_table.insert('','end',values=values)
    query = '''
    INSERT INTO expenses VALUES 
    (?, ?, ?, ?)
    '''
    curr.execute(query,(dateEntry.get(),Name.get(),Title.get(),Expense.get()))
    print(curr.lastrowid)
    connectionObjn.commit()
    connectionObjn.close()
    
    
def viewexpense():
    connectionObjn = db.connect("expenseTracker.db")
    curr = connectionObjn.cursor()
    query = '''
    select * from expenses
    '''
    curr.execute(query)
    rows=curr.fetchall()
    
    TOPlevel1=Toplevel(root)
    TOPlevel1.title("View expense table")
    TOPlevel1.geometry('1050x300')
    
    searched_table_frame=Frame(TOPlevel1 ,bd=4,relief=RIDGE,bg="crimson")
    searched_table_frame.place(x=0,y=0,width=1050,height=200)
    
    y_scroll=Scrollbar(searched_table_frame,orient=VERTICAL)
    x_scroll=Scrollbar(searched_table_frame,orient=HORIZONTAL)
    
    list=['Date','Name','Title','Expense']
    vexpense_table=ttk.Treeview(searched_table_frame,column=list,yscrollcommand=y_scroll.set,xscrollcommand=x_scroll.set)
    y_scroll.pack(side=RIGHT,fill=Y)
    y_scroll.config(command=expense_table.yview)
    x_scroll.pack(side=BOTTOM,fill=X)
    x_scroll.config(command=expense_table.xview)
    # expense_table.heading("Date",text="Date")
    # expense_table.heading("Name",text="Date")
    # expense_table.heading("Title",text="Date")
    # expense_table.heading("Expense",text="Date")
    vexpense_table['show'] = 'headings'
    for c in list:
        vexpense_table.heading(c,text=c.title())
    for row in rows :
            vexpense_table.insert("","end",values=row) 
    vexpense_table.pack(fill=BOTH)
    total='''
    select sum(expense) from expenses
    '''
    curr.execute(total)
    amount=curr.fetchall()[0]
    print(amount)
    
    tamount_label=Label(TOPlevel1,font=('arial',15,'bold'), text="Your total expenditure is",bg="#eb346b",fg="white",width=12)
    tamount_label.place(x=0,y=200,width=1050,height=40)
    
    amount_label=Label(TOPlevel1,font=('arial',15,'bold'),text=amount,bg="#eb346b",fg="white",width=12)
    amount_label.place(x=0,y=240,width=1050,height=60)
    
    connectionObjn.commit()
    connectionObjn.close()
    # -------------------------search 
def search_the_expenses(event):
    connectionObjn = db.connect("expenseTracker.db")
    curr = connectionObjn.cursor()
    values=[tar.get()]
    TOPlevel03=Toplevel(root)
    TOPlevel03.title("see the expense")
    TOPlevel03.geometry('1050x300')  
    if  option.get()== "Name" : 
        curr.execute('SELECT *FROM expenses WHERE name = ?',(tar.get(),))
        searched_data = curr.fetchall()
        y_scroll=Scrollbar(TOPlevel03,orient=VERTICAL)
        x_scroll=Scrollbar(TOPlevel03,orient=HORIZONTAL)
        list=['Date','Name','Title','Expense']
        sexpense_table=ttk.Treeview(TOPlevel03,column=list,yscrollcommand=y_scroll.set,xscrollcommand=x_scroll.set)
        y_scroll.pack(side=RIGHT,fill=Y)
        y_scroll.config(command=expense_table.yview)
        x_scroll.pack(side=BOTTOM,fill=X)
        x_scroll.config(command=expense_table.xview)
        # expense_table.heading("Date",text="Date")
        # expense_table.heading("Name",text="Date")
        # expense_table.heading("Title",text="Date")
        # expense_table.heading("Expense",text="Date")
        sexpense_table['show'] = 'headings'
            
        for c in list:
            sexpense_table.heading(c,text=c.title())
                
        for searched in searched_data :
            sexpense_table.insert("","end",values=searched) 
        sexpense_table.pack(fill=BOTH)
        connectionObjn.commit()
        connectionObjn.close()
            
    elif option.get()== "Title" : 
        
        curr.execute('SELECT *FROM expenses WHERE title = ?',(tar.get(),)) 
        searched_data = curr.fetchall()
        y_scroll=Scrollbar(TOPlevel03,orient=VERTICAL)
        x_scroll=Scrollbar(TOPlevel03,orient=HORIZONTAL)
        list=['Date','Name','Title','Expense']
        sexpense_table=ttk.Treeview(TOPlevel03,column=list,yscrollcommand=y_scroll.set,xscrollcommand=x_scroll.set)
        y_scroll.pack(side=RIGHT,fill=Y)
        y_scroll.config(command=expense_table.yview)
        x_scroll.pack(side=BOTTOM,fill=X)
        x_scroll.config(command=expense_table.xview)
        # expense_table.heading("Date",text="Date")
        # expense_table.heading("Name",text="Date")
        # expense_table.heading("Title",text="Date")
        # expense_table.heading("Expense",text="Date")
        sexpense_table['show'] = 'headings'
            
        for c in list:
            sexpense_table.heading(c,text=c.title())
                
        for searched in searched_data :
            sexpense_table.insert("","end",values=searched) 
        sexpense_table.pack(fill=BOTH)
        connectionObjn.commit()
        connectionObjn.close()
        
    elif option.get()== "Dates" : 
        curr.execute('SELECT *FROM expenses WHERE date = ?',(tar.get(),)) 
        searched_data = curr.fetchall()
        y_scroll=Scrollbar(TOPlevel03,orient=VERTICAL)
        x_scroll=Scrollbar(TOPlevel03,orient=HORIZONTAL)
        list=['Date','Name','Title','Expense']
        sexpense_table=ttk.Treeview(TOPlevel03,column=list,yscrollcommand=y_scroll.set,xscrollcommand=x_scroll.set)
        y_scroll.pack(side=RIGHT,fill=Y)
        y_scroll.config(command=expense_table.yview)
        x_scroll.pack(side=BOTTOM,fill=X)
        x_scroll.config(command=expense_table.xview)
        # expense_table.heading("Date",text="Date")
        # expense_table.heading("Name",text="Date")
        # expense_table.heading("Title",text="Date")
        # expense_table.heading("Expense",text="Date")
        sexpense_table['show'] = 'headings'
            
        for c in list:
            sexpense_table.heading(c,text=c.title())
                
        for searched in searched_data :
            sexpense_table.insert("","end",values=searched) 
        sexpense_table.pack(fill=BOTH)
        connectionObjn.commit()
        connectionObjn.close()
    elif option.get()== "Expenses" : 
        
        curr.execute('SELECT *FROM expenses WHERE expense = ?',(int(tar.get()),))

        searched_data = curr.fetchall()
        y_scroll=Scrollbar(TOPlevel03,orient=VERTICAL)
        x_scroll=Scrollbar(TOPlevel03,orient=HORIZONTAL)
        list=['Date','Name','Title','Expense']
        sexpense_table=ttk.Treeview(TOPlevel03,column=list,yscrollcommand=y_scroll.set,xscrollcommand=x_scroll.set)
        y_scroll.pack(side=RIGHT,fill=Y)
        y_scroll.config(command=expense_table.yview)
        x_scroll.pack(side=BOTTOM,fill=X)
        x_scroll.config(command=expense_table.xview)
        # expense_table.heading("Date",text="Date")
        # expense_table.heading("Name",text="Date")
        # expense_table.heading("Title",text="Date")
        # expense_table.heading("Expense",text="Date")
        sexpense_table['show'] = 'headings'
            
        for c in list:
            sexpense_table.heading(c,text=c.title())
                
        for searched in searched_data :
            sexpense_table.insert("","end",values=searched) 
        sexpense_table.pack(fill=BOTH)
        connectionObjn.commit()
        connectionObjn.close() 
        
           
    # -----------------------delete record----------------
    # def delete_record() :
    #         connectionObjn = db.connect("expenseTracker.db")
    #         curr = connectionObjn.cursor()
    #         x = vexpense_table.selection()[0]
    #         vexpense_table.delete(x)
    #         query = '''
    #         DELETE FROM expenses WHERE dates=?
    #         '''
    #         curr.execute(query)
    #         connectionObjn.commit()
            
    # delete_frame=Frame(TOPlevel1,bd=4,relief=RIDGE,bg="crimson")
    # delete_frame.place(x=0,y=200,width=1050,height=60)
    # deleterbtn=Button(delete_frame,command=delete_record,text="delete record",font=('arial',15,'bold'),bg="DodgerBlue2",fg="white" )
    # deleterbtn.pack()
    

def plote_linegraph(): 
    connectionObjn = db.connect("expenseTracker.db")
    curr = connectionObjn.cursor()
    query = 'SELECT date, expense FROM expenses'
    curr.execute(query)
    data = curr.fetchall()
    date = []
    values = []
    for row in data:
        date.append(parser.parse(row[0]))
        values.append(row[1])
        
    
    plt_frame=Frame(root,bd=4,relief=RIDGE,bg="crimson")
    plt_frame.place(x=850,y=250,width=516,height=455)
    
    fig = plt.figure(figsize=(5, 4),dpi=100)
    # specify the window as master
    canvas = FigureCanvasTkAgg(fig, master=plt_frame)
    canvas.draw()
    canvas.get_tk_widget().grid(row=4, column=0,sticky=(N,E,S,W))

    # navigation toolbar
    toolbarFrame = ttk.Frame(master=plt_frame)
    toolbarFrame.grid(row=3,column=0,padx=7,sticky=(N,E,S,W))
    toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
    
    plt.plot(date, values, color='red', linestyle='solid', linewidth = 3, marker='o', markerfacecolor='blue', markersize=12) 
    plt.xlabel("DATE")
    plt.xticks(date, rotation=30)
    plt.ylabel("EXPENSE AMOUNT")
    plt.title("Our Expenses Tracking Plot")
    plt.tight_layout()
    connectionObjn.commit()
    connectionObjn.close()
    
    
def plote_graphBaR() : 
    connectionObjn = db.connect("expenseTracker.db")
    curr = connectionObjn.cursor()
    query = 'SELECT date, expense FROM expenses'
    curr.execute(query)
    data = curr.fetchall()
    dates = []
    values = []
    
    for row in data:
        dates.append(parser.parse(row[0]))
        values.append(row[1])

    plt.bar(dates,values,color="blue")
    plt.xlabel("Date")
    plt.xticks(dates, rotation=20)
    plt.ylabel("Expense")
    plt.title("Our Expenses Tracking Plot")
    plt.show()
    connectionObjn.commit()


def clearTextInput():
        NameEntry.delete("0","end")
        expenseEntry.delete("0","end")
        titleEntry.delete("0","end")
        expenseEntry.delete("0","end")

init()
root=Tk()
root.title("EXPENSE TRACKER")
root.geometry("1000x500")

# --------------search-----frame

search_tree_frame=Frame(root ,bd=4,relief=RIDGE,bg="#25b4db")
search_tree_frame.place(x=650,y=0,width=716,height=250)
search_title_label=Label(search_tree_frame,font=('arial',15,'bold'), text="Find your Expenses",bg="#eb346b",fg="white",width=23)
search_title_label.grid(row=0, column=0,padx=10,pady=10,sticky=(W))
# search_title_label.place(x=0,y=0)
search_label=Label(search_tree_frame,font=('arial',15,'bold'), text="search by",bg="#eb346b",fg="white",width=12)
search_label.grid(row=2,column=0,padx=10,pady=10,sticky=(W))
# search_label.place(x=0,y=40)
search_t_label = Label(search_tree_frame,font=('arial',15,'bold'), text="Enter the target",bg="#eb346b",fg="white",width=23)
search_t_label.grid(row=1,column=0,padx=10,pady=10,sticky=(W))
# search_t_label.place(x=0,y=75)
option=StringVar()
options =[
    "Name",
    "Title",
    "Dates",
    "Expenses",
]
option = StringVar()
# clicked.set(options[0])

combobox01 = ttk.Combobox(search_tree_frame,value=options,textvariable=option,font=('arial',15,'bold'))
combobox01.current(0)
# Optionmenu = OptionMenu(search_tree_frame,clicked,*options,command=search_the_expenses)
combobox01.bind("<<ComboboxSelected>>",search_the_expenses)    
# ssubmitbtn=Button(search_tree_frame,text="search_the_expenses",font=('arial',15,'bold'),bg="DodgerBlue2",fg="white",width=25,command=search_the_expenses)
# ubmitbtn.grid(row=3,column=0,padx=10,pady=10,sticky=(W))
# ssubmitbtn.place(x=350,y=100)
combobox01.grid(row=2,column=1,padx=10,pady=10,sticky=(W))
    
tar = StringVar()
tar_entry=Entry(search_tree_frame,textvariable=tar,width=23,font=('arial',15,'bold'))
tar_entry.grid(row=1,column=1,padx=10,pady=10,sticky=(W))
# tar_entry.place(x=350,y=75) 
frame=Frame(root,bd=4,relief=RIDGE,bg="#25b4db")
frame.place(x=0,y=0,width=650,height=250)

# -----inside  label and entry frame
dateLabel=Label(frame,text="Date",font=('arial',15,'bold'),bg="#eb346b",fg="white",width=12)
dateLabel.grid(row=0,column=0,padx=10,pady=10,sticky=(W))

dateEntry=DateEntry(frame,font=('arial',15,'bold'))
dateEntry.grid(row=0,column=1,padx=10,pady=7,sticky=(W))

Name=StringVar()
nameLabel=Label(frame, text="Name",font=('arial',15,'bold'),bg="#eb346b",fg="white",width=12)
nameLabel.grid(row=1,column=0,padx=10,pady=10,sticky=(W))

NameEntry=Entry(frame,textvariable=Name,font=('arial',15,'bold'))
NameEntry.grid(row=1,column=1,padx=10,pady=10,sticky=(W))

Title=StringVar()
titleLabel=Label(frame, text="Title",font=('arial',15,'bold'),bg="#eb346b",fg="white",width=12)
titleLabel.grid(row=2,column=0,padx=10,pady=10,sticky=(W))

titleEntry=Entry(frame,textvariable=Title,font=('arial',15,'bold'))
titleEntry.grid(row=2,column=1,padx=10,pady=10,sticky=(W))

Expense=IntVar()
expenseLabel=Label(frame,text="Expenditure",font=('arial',15,'bold'),bg="#eb346b",fg="white",width=12)
expenseLabel.grid(row=3,column=0,padx=10,pady=10,sticky=(W))

expenseEntry=Entry(frame,textvariable=Expense,font=('arial',15,'bold'))
expenseEntry.grid(row=3,column=1,padx=10,pady=10,sticky=(W))


# ------------buttons frame---------------------------------------
btn_frame=Frame(root,bd=4,relief=RIDGE,bg="#9145ba")
btn_frame.place(x=0,y=250,width=850,height=100)


submitbtn=Button(btn_frame,command=submitexpense,text="Submit",font=('arial',15,'bold'),bg="orange",fg="white" )
submitbtn.grid(row=4,column=0,padx=10,pady=10,sticky=(W)) 

viewtn=Button(btn_frame,command=viewexpense,text="View expenses",font=('arial',15,'bold'),bg="orange",fg="white" )
viewtn.grid(row=4,column=1,padx=10,pady=10,sticky=(W))

plot_graph=Button(btn_frame,command=plote_linegraph,text="plot Line-graph",font=('arial',15,'bold'),bg="orange",fg="white" )
plot_graph.grid(row=4,column=2 , padx=10,pady=10,sticky=(W))


plote_bar_graph_B=Button(btn_frame,command=plote_graphBaR,text="plot Bar-graph",font=('arial',15,'bold'),bg="orange",fg="white",width=12 )
plote_bar_graph_B.grid(row=4,column =3,padx=10,pady=10,sticky=(W))



cleartn=Button(btn_frame,command=clearTextInput,text="Clear",font=('arial',15,'bold'),bg="orange",fg="white" )
cleartn.grid(row=4,column=4,padx=10,pady=10,sticky=(W))


# title frame of treeveiw and title
titleFrame = Frame(root, bd=4,relief=RIDGE,bg="#fcba03",pady=5)
titleFrame.place(x=0,y=350,width=850,height=60)

title_in_frameLabel=Label(titleFrame, text="The submitted expense will appear below",font=('arial',15,'bold'),bg="#e32dc5",fg="white",relief=RIDGE,padx=5,pady=5)
title_in_frameLabel.place(x=200,y=0)

# -----------------submit frame and treeview---------
tree_frame=Frame(root,bd=4,relief=RIDGE,bg="crimson")
tree_frame.place(x=0,y=410,width=850,height=295)


y_scroll=Scrollbar(tree_frame,orient=VERTICAL)
x_scroll=Scrollbar(tree_frame,orient=HORIZONTAL)
list1=['Date','Name','Title','Expense']
expense_table=ttk.Treeview(tree_frame,column=list1,height=300,yscrollcommand=y_scroll.set,xscrollcommand=x_scroll.set)
y_scroll.pack(side=RIGHT,fill=Y)
y_scroll.config(command=expense_table.yview)
x_scroll.pack(side=BOTTOM,fill=X)
x_scroll.config(command=expense_table.xview)
# expense_table.heading("Date",text="Date")
# expense_table.heading("Name",text="Date")
# expense_table.heading("Title",text="Date")
# expense_table.heading("Expense",text="Date")
expense_table['show'] = 'headings'
for c in list1:
    expense_table.heading(c,text=c.title())    
expense_table.pack(fill=BOTH)


root.mainloop()