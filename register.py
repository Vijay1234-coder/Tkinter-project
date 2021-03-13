from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import pymysql
# from windows import set_dpi_awareness
# set_dpi_awareness()
 #imagetk hleps to handle jpeg file
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Registeration Window")
        self.root.geometry("1350x700")
        self.root.configure(background='black')
        #......BG IMAGE.............
        self.bg=ImageTk.PhotoImage(file="image3.jpg")
        bg_label=Label(self.root,image=self.bg).place(x=250,y=0,relwidth=1,relheight=1)

        # ......side IMAGE.............
        self.lefbg = ImageTk.PhotoImage(file="lefbg.jpg")
        lefbg_label = Label(self.root, image=self.lefbg).place(x=80, y=100,width=400,height=500)

        #================Register Frame=====================ROW 0

        frame1=Frame(self.root,bg="white")
        frame1.place(x=480,y=100,width=700,height=500)

        title=Label(frame1,text="REGISTER HERE",font=("times new roman",20,"bold"),bg="white",fg="green").place(x=50,y=30)
        self.input=StringVar()
         #===================================================ROW 1

        fname=Label(frame1,text="First Name",font=("times new roman",15,"bold"),bg="white",fg="gray").place( x=50, y=100)

        self.text_fname=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.text_fname.place(x=50,y=130,width=250)

        lname = Label(frame1, text="Last Name", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(
            x=370, y=100)
        self.text_lname = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.text_lname.place(x=370,y=130, width=250)

        #========================================================ROW2

        contact = Label(frame1, text="Contact No.", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=170)
        self.text_contact = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.text_contact.place(x=50, y=200, width=250)

        Email = Label(frame1, text="Email id", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(
            x=370, y=170)
        self.text_Email = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.text_Email.place(x=370, y=200, width=250)

 #========================================================ROW3

        Question = Label(frame1, text="Security Question", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=240)
        self.cmb_quest =ttk.Combobox(frame1, font=("times new roman", 13),state="readonly",justify=CENTER)
        self.cmb_quest["values"]=("Select","what is pet name","what is your fav color","whats your goal")
        self.cmb_quest.place(x=50, y=270, width=250)
        self.cmb_quest.current(0)

        answer = Label(frame1, text="Answer", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(
            x=370, y=240)
        self.text_answer = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.text_answer.place(x=370, y=270, width=250)

        # ========================================================ROW4

        password= Label(frame1, text="Password", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(
            x=50, y=310)
        self.text_password = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.text_password.place(x=50, y=340, width=250)

        cnfpassword = Label(frame1, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(
            x=370, y=310)
        self.text_cnfpassword = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.text_cnfpassword.place(x=370, y=340, width=250)

       #+==========================================================================
        self.check_var=IntVar()

        check=Checkbutton(frame1,text="I Agree All the Terms & Conditions",onvalue=1,offvalue=0,bg="white",font=("times new roman",13 ),variable=self.check_var).place(x=50, y=380)




        btn_register=Button(frame1,text="Register",bd=0,cursor="hand2",font=("times new roman",18,"bold"),bg="green",fg="white",command=self.register_data).place(x=50,y=420,width=500)


        btn_login=Button(self.root,text="Sign In",font=("times new roman",20),bd=0,cursor="hand2",bg="green",fg="white").place(x=190,y=480,width=200)

    def register_data(self):
        if self.text_fname.get()=="" or self.text_contact.get()=="" or self.text_Email.get()=="" or self.text_answer.get()=="" or  self.text_password.get()=="" or self.text_cnfpassword.get()=="" or self.cmb_quest.get()=="Select":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        elif self.text_password.get()!=self.text_cnfpassword.get():
            messagebox.showerror("Error","Password & Confirm Password not match",parent=self.root)
        elif self.check_var.get()==0:
            messagebox.showerror("Error", "Agree our Terms & Conditions", parent=self.root)

        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="employees")
                cur=con.cursor()
                cur.execute("insert into emplyoeedata (f_name,l_name,Contact,Email,Question,Answer,Password)values(%s,%s,%s,%s,%s,%s,%s)",
                            (
                                self.text_fname.get(),
                                self.text_lname.get(),
                                self.text_contact.get(),
                                self.text_Email.get(),
                                self.cmb_quest.get(),
                                self.text_answer.get(),
                                self.text_password.get()
                            ))
                con.commit()
                con.close()
                messagebox.showinfo("Success", "Resister Successful", parent=self.root)

            except Exception as es:
                messagebox.showerror("Error", f"Error is :{str(es)}", parent=self.root)








root= Tk()
obj = Register(root)
root.mainloop()