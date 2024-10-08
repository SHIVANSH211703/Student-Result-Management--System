from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3

class studentClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()

        # Title
        title = Label(self.root, text="Manage Student Details", font=("goudy old style", 20, "bold"), bg="#033054", fg="white")
        title.place(x=10, y=15, width=1180, height=35)

        # Variables
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_email = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_contact = StringVar()
        self.var_course = StringVar()
        self.var_a_date = StringVar()
        self.var_state = StringVar()
        self.var_city = StringVar()
        self.var_pincode = StringVar()
        self.var_search = StringVar()
        self.var_duration = StringVar()
        self.var_charges = StringVar()

        # Widgets
        # Column 1
        lbl_roll = Label(self.root, text="Roll No.", font=("goudy old style", 20, "bold"), bg='white')
        lbl_roll.place(x=10, y=60)
        lbl_name = Label(self.root, text="Name", font=("goudy old style", 20, "bold"), bg='white')
        lbl_name.place(x=10, y=100)
        lbl_email = Label(self.root, text="Email", font=("goudy old style", 20, "bold"), bg='white')
        lbl_email.place(x=10, y=140)
        lbl_gender = Label(self.root, text="Gender", font=("goudy old style", 20, "bold"), bg='white')
        lbl_gender.place(x=10, y=180)
        lbl_state = Label(self.root, text="State", font=("goudy old style", 20, "bold"), bg='white')
        lbl_state.place(x=10, y=220)
        lbl_city = Label(self.root, text="City", font=("goudy old style", 20, "bold"), bg='white')
        lbl_city.place(x=310, y=220)
        lbl_pin = Label(self.root, text="PIN", font=("goudy old style", 20, "bold"), bg='white')
        lbl_pin.place(x=500, y=220)
        lbl_address = Label(self.root, text="Address", font=("goudy old style", 20, "bold"), bg='white')
        lbl_address.place(x=10, y=260)

        # Entry fields
        self.txt_roll = Entry(self.root, textvariable=self.var_roll, font=("goudy old style", 20, "bold"), bg='lightyellow')
        self.txt_roll.place(x=135, y=60, width=200)
        txt_name = Entry(self.root, textvariable=self.var_name, font=("goudy old style", 20, "bold"), bg='lightyellow')
        txt_name.place(x=135, y=100, width=200)
        txt_email = Entry(self.root, textvariable=self.var_email, font=("goudy old style", 20, "bold"), bg='lightyellow')
        txt_email.place(x=135, y=140, width=200)
        txt_gender = ttk.Combobox(self.root, textvariable=self.var_gender, values=("Select", "Male", "Female", "Other"), font=("goudy old style", 20, "bold"), state='readonly', justify=CENTER)
        txt_gender.place(x=135, y=180, width=200)
        txt_gender.current(0)
        self.txt_state = Entry(self.root, textvariable=self.var_state, font=("goudy old style", 20, "bold"), bg='lightyellow')
        self.txt_state.place(x=135, y=220, width=150)
        self.txt_city = Entry(self.root, textvariable=self.var_city, font=("goudy old style", 20, "bold"), bg='lightyellow')
        self.txt_city.place(x=380, y=220, width=100)
        self.txt_pin = Entry(self.root, textvariable=self.var_pincode, font=("goudy old style", 20, "bold"), bg='lightyellow')
        self.txt_pin.place(x=560, y=220, width=130)

        # Column 2
        lbl_dob = Label(self.root, text="D.O.B", font=("goudy old style", 20, "bold"), bg='white')
        lbl_dob.place(x=350, y=60)
        lbl_contact = Label(self.root, text="Contact", font=("goudy old style", 20, "bold"), bg='white')
        lbl_contact.place(x=350, y=100)
        lbl_addmission = Label(self.root, text="Admission", font=("goudy old style", 20, "bold"), bg='white')
        lbl_addmission.place(x=350, y=140)
        lbl_course = Label(self.root, text="Course", font=("goudy old style", 20, "bold"), bg='white')
        lbl_course.place(x=350, y=180)

        # Entry fields
        self.course_list = []
        self.txt_dob = Entry(self.root, textvariable=self.var_dob, font=("goudy old style", 20, "bold"), bg='lightyellow')
        self.txt_dob.place(x=488, y=60, width=200)
        txt_contact = Entry(self.root, textvariable=self.var_contact, font=("goudy old style", 20, "bold"), bg='lightyellow')
        txt_contact.place(x=488, y=100, width=200)
        txt_addmission = Entry(self.root, textvariable=self.var_a_date, font=("goudy old style", 20, "bold"), bg='lightyellow')
        txt_addmission.place(x=488, y=140, width=200)
        txt_course = ttk.Combobox(self.root, textvariable=self.var_course, values=self.course_list, font=("goudy old style", 20, "bold"), state='readonly', justify=CENTER)
        txt_course.place(x=488, y=180, width=200)
        txt_course.set("Empty")

        # Address field
        self.txt_address = Text(self.root, font=("goudy old style", 20, "bold"), bg='lightyellow')
        self.txt_address.place(x=135, y=260, width=555, height=100)

        # Buttons
        self.btn_add = Button(self.root, text="Save", font=("goudy old style", 15, "bold"), bg="#2196f3", fg="white", cursor="hand2", command=self.add)
        self.btn_add.place(x=150, y=400, width=110, height=40)
        self.btn_update = Button(self.root, text="Update", font=("goudy old style", 15, "bold"), bg="#4caf50", fg="white", cursor="hand2", command=self.update)
        self.btn_update.place(x=270, y=400, width=110, height=40)
        self.btn_delete = Button(self.root, text="Delete", font=("goudy old style", 15, "bold"), bg="#f44336", fg="white", cursor="hand2", command=self.delete)
        self.btn_delete.place(x=390, y=400, width=110, height=40)
        self.btn_clear = Button(self.root, text="Clear", font=("goudy old style", 15, "bold"), bg="#607d8b", fg="white", cursor="hand2", command=self.clear)
        self.btn_clear.place(x=510, y=400, width=110, height=40)

        # Search panel
        lbl_search_roll = Label(self.root, text="Roll No.", font=("goudy old style", 20, "bold"), bg='white')
        lbl_search_roll.place(x=700, y=60)
        txt_search_roll = Entry(self.root, textvariable=self.var_search, font=("goudy old style", 20, "bold"), bg='lightyellow')
        txt_search_roll.place(x=870, y=60, width=180)
        btn_search = Button(self.root, text="Search", font=("goudy old style", 15, "bold"), bg="#03a9f4", fg="white", cursor="hand2", command=self.search)
        btn_search.place(x=1070, y=60, width=120, height=28)

        # Content Frame
        self.C_Frame = Frame(self.root, bd=2, relief=RIDGE)
        self.C_Frame.place(x=720, y=100, width=470, height=340)

        # Treeview
        scrolly = Scrollbar(self.C_Frame, orient=VERTICAL)
        scrollx = Scrollbar(self.C_Frame, orient=HORIZONTAL)
        self.CourseTable = ttk.Treeview(self.C_Frame, columns=("roll", "name", "email", "gender", "dob","contact","addmission","course","state","city","pin","address"), xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)

       

        
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.CourseTable.xview)
        scrolly.config(command=self.CourseTable.yview)
 
        self.CourseTable.pack(fill=BOTH, expand=1)

        self.CourseTable.heading("roll",text="Roll No.")
        self.CourseTable.heading("name",text="Name")
        self.CourseTable.heading("email",text="Email")
        self.CourseTable.heading("gender",text="Gender")
        self.CourseTable.heading("dob",text="D.O.B")
        self.CourseTable.heading("contact",text="Contact")
        self.CourseTable.heading("addmission",text="Addmission")
        self.CourseTable.heading("course",text="Course")
        self.CourseTable.heading("state",text="State")
        self.CourseTable.heading("city",text="City")
        self.CourseTable.heading("pin",text="PIN")
        self.CourseTable.heading("address",text="Address")
        self.CourseTable["show"]='headings'
        self.CourseTable.column("roll",width=100)
        self.CourseTable.column("name",width=100)
        self.CourseTable.column("email",width=100 )
        self.CourseTable.column("gender",width=100)
        self.CourseTable.column("dob",width=100 )
        self.CourseTable.column("contact",width=100)
        self.CourseTable.column("addmission",width=100)
        self.CourseTable.column("course",width=100 )
        self.CourseTable.column("state",width=100)
        self.CourseTable.column("city",width=100 )
        self.CourseTable.column("pin",width=100)
        self.CourseTable.column("address",width=200 )
        self.CourseTable.pack(fill=BOTH, expand=1)
        self.CourseTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()

# ===================================================================================

    
    def clear(self):
        self.show()
        self.var_roll.set("")
        self.var_search.set("")
        self.var_duration.set("")
        self.var_charges.set("")
        self.txt_description.delete('1.0',END)
        self.txt_roll.config(state=NORMAL)

    def delete(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_roll.get() == "":
                messagebox.showerror("Error", "Course Name should be required", parent=self.root)
            else:
                cur.execute("SELECT * from course WHERE name = ?", (self.var_roll.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "please select course from the list first", parent=self.root)
                else: 
                     op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                     if op:
                         cur.execute("DELETE FROM course WHERE name=?",(self.var_roll.get(),))
                         con.commit()
                         messagebox.showinfo("Deleted","Course deleted successully",parent=self.root)
                         self.clear()
                         self.show()
                         
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    def get_data(self,ev):
        self.txt_roll.config(state='readonly')
        r=self.CourseTable.focus()
        content=self.CourseTable.item(r)
        row=content["values"]
        print(row)
        # print (row)
        self.var_roll.set(row[1])
        self.var_duration.set(row[2])
        self.var_charges.set(row[3])
        # self.course.var_roll.set(row[1])
        self.txt_description.delete('1.0',END)
        self.txt_description.insert(END,row[4])


    def add(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_roll.get() == "":
                messagebox.showerror("Error", "Course Name should be required", parent=self.root)
            else:
                cur.execute("SELECT * from course WHERE name = ?", (self.var_roll.get(),))
                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "Course Name already present", parent=self.root)
                else:
                    cur.execute("INSERT INTO course (name, duration, charges, description) VALUES (?, ?, ?, ?)", (
                        self.var_roll.get(),
                        self.var_duration.get(),
                        self.var_charges.get(),
                        self.txt_description.get("1.0", END)
                    ))    
                    con.commit()
                    messagebox.showinfo("Success", "Course added successfully", parent=self.root)
                    self.show()
                  
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)



    def  update(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_roll.get() == "":
                messagebox.showerror("Error", "Select Course From List", parent=self.root)
            else:
                cur.execute("SELECT * from course WHERE name = ?", (self.var_roll.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Course Name already present", parent=self.root)
                else:
                    cur.execute("UPDATE  course set  duration=?, charges=?, description=? WHERE name=?  ", (
                        
                        self.var_duration.get(),
                        self.var_charges.get(),
                        self.txt_description.get("1.0", END),
                        self.var_roll.get(),
                    ))    
                    con.commit()
                    messagebox.showinfo("Success", "Course update successfully", parent=self.root)
                    self.show()
                  
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)



    def show(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT * from student")
            rows = cur.fetchall()

            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert('',END,values=row)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)


    def search(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT * from course where name LIKE ?", ('%' + self.var_search.get() + '%',))
            rows = cur.fetchall()

            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert('',END,values=row)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

     
        
if __name__ == "__main__":
    root = Tk()
    obj = studentClass(root)
    root.mainloop()
