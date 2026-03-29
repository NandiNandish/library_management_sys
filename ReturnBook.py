from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

# Global variables - will be set by main.py
con = None
cur = None
issueTable = "books_issued" #Issue Table
bookTable = "books" #Book Table

allBid = [] #List To store all Book IDs

def returnn():
    
    global SubmitBtn,labelFrame,lb1,bookInfo1,quitBtn,root,Canvas1,status
    
    bid = bookInfo1.get()
    
    if not bid:
        messagebox.showerror("Error", "Book ID is required!")
        return

    extractBid = "select bid from "+issueTable
    try:
        cur.execute(extractBid)
        con.commit()
        for i in cur:
            allBid.append(i[0])
        
        if bid in allBid:
            checkAvail = "select status from "+bookTable+" where bid = %s"
            cur.execute(checkAvail, (bid,))
            con.commit()
            for i in cur:
                check = i[0]
                
            if check == 'issued':
                status = True
            else:
                status = False

        else:
            messagebox.showinfo("Error", "Book ID not present in issued books")
    except Exception as e:
        messagebox.showerror("Error", f"Can't fetch Book IDs: {str(e)}")
    
    
    issueSql = "delete from "+issueTable+" where bid = %s"
  
    print(bid in allBid)
    print(status)
    updateStatus = "update "+bookTable+" set status = %s where bid = %s"
    try:
        if bid in allBid and status == True:
            cur.execute(issueSql, (bid,))
            con.commit()
            cur.execute(updateStatus, ('available', bid))
            con.commit()
            messagebox.showinfo('Success', "Book Returned Successfully")
        else:
            allBid.clear()
            messagebox.showinfo('Message', "Please check the book ID")
            root.destroy()
            return
    except Exception as e:
        con.rollback()
        messagebox.showerror("Error", f"Can't return book: {str(e)}")
    
    
    allBid.clear()
    root.destroy()
    
def returnBook(): 
    
    global bookInfo1,SubmitBtn,quitBtn,Canvas1,con,cur,root,labelFrame, lb1
    
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    
    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#006B38")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Return Book", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)   
        
    # Book ID to Delete
    lb1 = Label(labelFrame,text="Book ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.5)
        
    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3,rely=0.5, relwidth=0.62)
    
    #Submit Button
    SubmitBtn = Button(root,text="Return",bg='#d1ccc0', fg='black',command=returnn)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()