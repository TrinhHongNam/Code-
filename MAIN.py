from tkinter import *
import tkinter.messagebox
import stdDatabase


class Student:

    def __init__(selfs, root):
        selfs.root = root
        selfs.root.title("Systems")
        selfs.root.geometry("1350x7500+0+0")
        selfs.root.config(bg="cadet blue")

        StdID = StringVar()
        Firstname = StringVar()
        Surname = StringVar()
        DoB = StringVar()
        Age = StringVar()
        Gender = StringVar()
        Address = StringVar()
        Mobile = StringVar()

        #=========================Function========================

        def iExit():
            iExit= tkinter.messagebox.askyesno(" Students Database Management Systems","Confirm if you want to exit")
            if iExit >0:
                root.destroy()
                return

        def clearData():
            selfs.txtStdID.delete(0,END)
            selfs.txtfna.delete(0, END)
            selfs.txtSna.delete(0, END)
            selfs.txtDoB.delete(0, END)
            selfs.txtAge.delete(0, END)
            selfs.txtGender.delete(0, END)
            selfs.txtAdr.delete(0, END)
            selfs.txtMobile.delete(0, END)

        def addData():
            if(len(StdID.get())!=0):
                stdDatabase.addStdRec(StdID.get(), Firstname.get(), Surname.get(),DoB.get(), Age.get(), Gender.get(), Address.get(), Mobile.get())
                studentlist.delete(0, END)
                studentlist.insert(END,(StdID.get(), Firstname.get(), Surname.get(),DoB.get(), Age.get(), Gender.get(), Address.get(), Mobile.get()))

        def DisplayData():
            studentlist.delete(0,END)
            for row in stdDatabase.viewData():
              studentlist.insert(END,row,str(""))

        def StudentRec(event):
            global sd
            searchStd= studentlist.curselection()[0]
            sd = studentlist.get(searchStd)

            selfs.txtStdID.delete(0, END)
            selfs.txtStdID.insert(END,sd[1])
            selfs.txtfna.delete(0, END)
            selfs.txtfna.insert(END, sd[2])
            selfs.txtSna.delete(0, END)
            selfs.txtSna.insert(END, sd[3])
            selfs.txtDoB.delete(0, END)
            selfs.txtDoB.insert(END, sd[4])
            selfs.txtAge.delete(0, END)
            selfs.txtAge.insert(END, sd[5])
            selfs.txtGender.delete(0, END)
            selfs.txtGender.insert(END, sd[6])
            selfs.txtAdr.delete(0, END)
            selfs.txtAdr.insert(END, sd[7])
            selfs.txtMobile.delete(0, END)
            selfs.txtMobile.insert(END, sd[8])

        def DeleteData():
            if (len(StdID.get())!= 0):
                stdDatabase.deleteRec(sd[0])
                clearData()
                DisplayData()

        def searchDatabase():
            studentlist.delete(0,END)
            for row in stdDatabase.searchData(StdID.get(),Firstname.get(),Surname.get(),DoB.get(),Age.get(), Gender.get(), Address.get(), Mobile.get()):
                studentlist.insert(END,row,str(""))

        def update():
            if (len(StdID.get())!=0):
                stdDatabase.deleteRec(sd[0])
            if (len(StdID.get())!= 0):
                stdDatabase.addStdRec(StdID.get(), Firstname.get(), Surname.get(),DoB.get(), Age.get(), Gender.get(), Address.get(), Mobile.get())
                studentlist.delete(0,END)
                studentlist.insert(END,(StdID.get(), Firstname.get(), Surname.get(),DoB.get(), Age.get(), Gender.get(), Address.get(), Mobile.get()))


        #=========================Frames============================

        MainFrame = Frame(selfs.root, bg='cadet blue')
        MainFrame.grid()

        TitFrame = Frame(MainFrame, bd=2, padx=54, pady=8, bg='Ghost White', relief=RIDGE)
        TitFrame.pack(side=TOP)

        selfs.lblTit = Label(TitFrame, font=('arial', 47, 'bold'), text="Hệ Thống Quản Lí Sinh Viên",
                             bg='Ghost White')
        selfs.lblTit.grid()

        ButtonFrame = Frame(MainFrame, bd=2, width=1350, height=70, padx=18, pady=10, bg='Ghost White', relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame = Frame(MainFrame, bd=1, width=1300, height=400, padx=20, pady=20, relief=RIDGE, bg='cadet blue')
        DataFrame.pack(side=BOTTOM)

        DataFrameLEFT = LabelFrame(DataFrame, bd=1, width=1000, height=600, padx=20, pady=20, relief=RIDGE,
                                   bg='Ghost White', font=('arial', 20, 'bold'), text=' Student Info\n')
        DataFrameLEFT.pack(side=LEFT)

        DataFrameRIGHT = LabelFrame(DataFrame, bd=1, width=450, height=300, padx=31, pady=3, relief=RIDGE,
                                    bg='Ghost White', font=('arial', 20, 'bold'), text=' Student Details\n')
        DataFrameRIGHT.pack(side=RIGHT)


        # ============== Label and Entry Widget======================
        selfs.lblStdID = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text='MSSV:', padx=2, pady=2,
                               bg="Ghost White")
        selfs.lblStdID.grid(row=0, column=0, sticky=W)
        selfs.txtStdID = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=StdID, width=39)
        selfs.txtStdID.grid(row=0, column=1)

        selfs.lblfna = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text='Họ:', padx=2, pady=2,
                             bg="Ghost White")
        selfs.lblfna.grid(row=1, column=0, sticky=W)
        selfs.txtfna = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Firstname, width=39)
        selfs.txtfna.grid(row=1, column=1)

        selfs.lblSna = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text='Tên:', padx=2, pady=2,
                             bg="Ghost White")
        selfs.lblSna.grid(row=2, column=0, sticky=W)
        selfs.txtSna = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Surname, width=39)
        selfs.txtSna.grid(row=2, column=1)

        selfs.lblDoB = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text='Ngày sinh:', padx=2, pady=2,
                             bg="Ghost White")
        selfs.lblDoB.grid(row=3, column=0, sticky=W)
        selfs.txtDoB = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=DoB, width=39)
        selfs.txtDoB.grid(row=3, column=1)

        selfs.lblAge = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text='Tuổi', padx=2, pady=2, bg="Ghost White")
        selfs.lblAge.grid(row=4, column=0, sticky=W)
        selfs.txtAge = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Age, width=39)
        selfs.txtAge.grid(row=4, column=1)

        selfs.lblGender= Label(DataFrameLEFT, font=('arial', 20, 'bold'), text='Giới tính:', padx=2, pady=2,
                             bg="Ghost White")
        selfs.lblGender.grid(row=5, column=0, sticky=W)
        selfs.txtGender = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Gender, width=39)
        selfs.txtGender.grid(row=5, column=1)

        selfs.lblAdr = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text='Địa chỉ:', padx=2, pady=2,
                             bg="Ghost White")
        selfs.lblAdr.grid(row=6, column=0, sticky=W)
        selfs.txtAdr = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Address, width=39)
        selfs.txtAdr.grid(row=6, column=1)

        selfs.lblMobile = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text='SĐT', padx=2, pady=2, bg="Ghost White")
        selfs.lblMobile.grid(row=7, column=0, sticky=W)
        selfs.txtMobile = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Mobile, width=39)
        selfs.txtMobile.grid(row=7, column=1)


        # ============== ListBox &  ScrollBar Widget======================
        scrollbar = Scrollbar(DataFrameRIGHT)
        scrollbar.grid(row=0, column=1, sticky='ns')

        studentlist = Listbox(DataFrameRIGHT, width=50, height=16, font=('arial', 12, ' bold'),
                              yscrollcommand=scrollbar.set)
        studentlist.bind('<<ListboxSelect>>', StudentRec)
        studentlist.grid(row=0, column=0, padx=8)
        scrollbar.config(command=studentlist.yview)


        # ============== Button Widget======================
        selfs.btnAddDate = Button(ButtonFrame, text=" Thêm mới ", font=('arial', 20, 'bold'), height=1, width=10, bd=4, command=addData)
        selfs.btnAddDate.grid(row=0, column=0)

        selfs.btnDisplayData = Button(ButtonFrame, text=" Display ", font=('arial',20, 'bold'), height=1, width=10, bd=4, command=DisplayData)
        selfs.btnDisplayData.grid(row=0, column=1)

        selfs.btnClearData = Button(ButtonFrame, text=" Dọn dẹp ", font=('arial', 20, 'bold'), height=1, width=10, bd=4, command=clearData)
        selfs.btnClearData.grid(row=0, column=2)

        selfs.btnDeleteData = Button(ButtonFrame, text=" Xóa ", font=('arial', 20, 'bold'), height=1, width=10, bd=4, command=DeleteData)
        selfs.btnDeleteData.grid(row=0, column=3)

        selfs.btnSearchData = Button(ButtonFrame, text=" Tìm kiếm ", font=('arial', 20, 'bold'), height=1, width=10, bd=4,command=searchDatabase)
        selfs.btnSearchData.grid(row=0, column=4)

        selfs.btnUpdateData = Button(ButtonFrame, text=" Cập nhật ", font=('arial', 20, 'bold'), height=1, width=10, bd=4, command=update)
        selfs.btnUpdateData.grid(row=0, column=5)

        selfs.btnExit= Button(ButtonFrame, text=" Thoát ", font=('arial', 20, 'bold'), height=1, width=10, bd=4,  command=iExit)
        selfs.btnExit.grid(row=0, column=6)


if __name__ == '__main__':
    root = Tk()
    application = Student(root)
    root.mainloop()



