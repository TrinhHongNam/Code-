from tkinter import *
import random
import time
import datetime
from tkinter import messagebox

#Cửa sổ cơ bản được tạo
root = Tk()
root.geometry("1350x850")
root.title("Cô Đơn Quán")
root.configure(background = "White")
#kết thúc cửa sổ cơ bản

# tạo khung
Tops = Frame(root, width = 200, height =  225, bd = 8, relief = "raise")
Tops.pack(side = TOP)

f1 = Frame(root, width = 300, height =200, bd = 8, relief = "raise")
f1.pack(side = LEFT)

f2 = Frame(root, width = 187, height = 200, bd = 8, relief = "raise")
f2.pack(side = RIGHT)


f1a = Frame(f1, width = 500, height = 137, bd = 8, relief = "raise")
f1a.pack(side = TOP)    

f2a = Frame(f1, width =500, height = 135, bd = 8, relief = "raise")
f2a.pack(side = BOTTOM)

ft2 = Frame(f2, width = 550, height = 187, bd = 8, relief = "raise")
ft2.pack(side = TOP)
fb2 = Frame(f2, width = 550, height = 250, bd = 20, relief = "raise")
fb2.pack(side = BOTTOM)

f1aa = Frame(f1a, width =1350, height = 250, bd = 20, relief = "raise")
f1aa.pack(side = LEFT)
f1ab = Frame(f1a, width =1350, height = 250, bd =20, relief = "raise")
f1ab.pack(side = RIGHT)

f2aa = Frame(f2a, width = 187, height = 137, bd = 20, relief = "raise")
f2aa.pack(side = LEFT)

f2ab = Frame(f2a, width = 187, height = 137, bd = 20, relief = "raise")
f2ab.pack(side = RIGHT)


Tops.configure (background = 'White')
f1.configure (background = 'White')
f2.configure (background = 'White')
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>TIÊU ĐỀ<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

lblInfo = Label(Tops, font  = ('arial', 52 , 'bold'), text = " \t CÔ ĐƠN QUÁN  \t\t", bd = 25)
lblInfo.grid(row = 0, column = 0)
#Frame Creation ends
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>KẾT THÚC TIÊU ĐỀ<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>CHI PHÍ MẶT HÀNG<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def CostofItems():
    Item1 = float(E_Latte.get())
    Item2 = float(E_Espresso.get())
    Item3 = float(E_Iced_Latte.get())
    Item4 = float(E_Vale_Coffee.get())
    Item5 = float(E_Cappuccino.get())
    Item6 = float(E_African_Coffee.get())
    Item7 = float(E_American_Coffee.get())
    Item8 = float(E_Iced_Cappuccino.get())

    Item9 = float(E_Coffee_Cakes.get())
    Item10 = float(E_Red_Velvet_Cake.get())
    Item11 = float(E_Black_Forest_Cake.get())
    Item12 = float(E_Boston_Cream_Cake.get())
    Item13 = float(E_Lagos_Chocolate_Cake.get())
    Item14 = float(E_Kilburn_Chocolate_Cake.get())
    Item15 = float(E_Carlton_Hill_Chocolate_Cake.get())
    Item16 = float(E_Queen_Park_Chocolate_Cake.get())

    PriceofDrinks = (Item1 * 10000) + (Item2 * 10000) + (Item3 * 20000) + (Item4 * 10000) + (Item5 * 10000) + (Item6 * 20000) + (Item7 * 20000) + (Item8 * 10000)
    PriceofCakes =  (Item9 * 10000) + (Item10 * 20000) + (Item11 * 10000) + (Item12 * 10000) + (Item13 * 10000) + (Item14 * 10000) + (Item15 * 10000) + (Item16 * 10000)

    DrinksPrice =  str('%.2f'%(PriceofDrinks)) + "VND" 
    CakesPrice =  str('%.2f'%(PriceofCakes)) + "VND" 
    CostofCakes.set(CakesPrice)
    CostofDrinks.set(DrinksPrice)
    SC =  str('%.2f'%(1000)) + "VND" 
    ServiceCharge.set(SC)

    SubTotalofITEMS =  str('%.2f'%(PriceofDrinks + PriceofCakes + 1500)) + "VND" 
    SubTotal.set(SubTotalofITEMS)
    Tax =  str('%.2f'%((PriceofDrinks + PriceofCakes + 1000))) + "VND" 
    PaidTax.set(Tax)
    TT = ((PriceofDrinks + PriceofCakes + 1500))
    TC =  str('%.2f'%(PriceofDrinks + PriceofCakes + 1000 + TT)) + "VND" 
    TotalCost.set(TC)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>COST OF ITEMS END<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>CREATING METHOD FOR EXIT<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def qExit():
    qExit = messagebox.askyesno("Quit System", "Bạn có muốn thoát không?")
    if qExit:
        root.quit()
        return
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>CHI PHÍ MẶT HÀNG KẾT THÚC<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>PHƯƠNG PHÁP THIẾT LẬP BẮT ĐẦU<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def reset():
    PaidTax.set("")
    SubTotal.set("")
    TotalCost.set("")
    CostofDrinks.set("")
    CostofCakes.set("")
    ServiceCharge.set("")
    txtReceipt.delete("1.0", END)

    E_Latte.set("0")
    E_Espresso.set("0")
    E_Iced_Latte.set("0")
    E_Vale_Coffee.set("0")
    E_Cappuccino.set("0")
    E_African_Coffee.set("0")
    E_American_Coffee.set("0")
    E_Iced_Cappuccino.set("0")
    E_Coffee_Cakes.set("0")
    E_Red_Velvet_Cake.set("0")
    E_Black_Forest_Cake.set("0")
    E_Boston_Cream_Cake.set("0")
    E_Lagos_Chocolate_Cake.set("0")
    E_Kilburn_Chocolate_Cake.set("0")
    E_Carlton_Hill_Chocolate_Cake.set("0")
    E_Queen_Park_Chocolate_Cake.set("0")

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)

    txtLatte.configure(state = DISABLED)
    txtEspresso.configure(state = DISABLED)
    txtIced_Latte.configure(state = DISABLED)
    txtVale_Coffee.configure(state = DISABLED)
    txtAfrican_Coffee.configure(state = DISABLED)
    txtAmerican_Coffee.configure(state = DISABLED)
    txtIced_Cappuccino.configure(state = DISABLED)
    txtCoffeeCake.configure(state = DISABLED)
    txtRed_Velvet_Cake.configure(state = DISABLED)
    txtBlack_Forest_Cake.configure(state = DISABLED)
    txtBoston_Cream_Cake.configure(state = DISABLED)
    txtLagos_Chocolate_Cake.configure(state = DISABLED)
    txtKilburn_Chocolate_Cake.configure(state = DISABLED)
    txtCappuccino.configure(state = DISABLED)
    txtCarlton_Hill_Cake.configure(state = DISABLED)
    txtQueen_park_Cake.configure(state = DISABLED)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>PHƯƠNG PHÁP THIEST LẬP KẾT THÚC<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>KIỂM TRA<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

def chkbutton_value():

    if(var1.get() == 1):
        txtLatte.configure(state = NORMAL)
    elif var1.get() == 0:
        txtLatte.configure(state = DISABLED)
        E_Latte.set("0")
    if(var2.get() == 1):
        txtEspresso.configure(state = NORMAL)
    elif var2.get() == 0:
        txtEspresso.configure(state = DISABLED)
        E_Espresso.set("0")
    if(var3.get() == 1):
        txtIced_Latte.configure(state = NORMAL)
    elif var3.get() == 0:
        txtIced_Latte.configure(state = DISABLED)
        E_Iced_Latte.set("0")
    if(var4.get() == 1):
        txtVale_Coffee.configure(state = NORMAL)
    elif var4.get() == 0:
        txtVale_Coffee.configure(state = DISABLED)
        E_Vale_Coffee.set("0")
    if(var5.get() == 1):
        txtCappuccino.configure(state = NORMAL)
    elif var5.get() == 0:
        txtCappuccino.configure(state = DISABLED)
        E_Cappuccino.set("0")
    if(var6.get() == 1):
        txtAfrican_Coffee.configure(state = NORMAL)
    elif var6.get() == 0:
        txtAfrican_Coffee.configure(state = DISABLED)
        E_African_Coffee.set("0")
    if(var7.get() == 1):
        txtAmerican_Coffee.configure(state = NORMAL)
    elif var7.get() == 0:
        txtAmerican_Coffee.configure(state = DISABLED)
        E_American_Coffee.set("0")
    if(var8.get() == 1):
        txtIced_Cappuccino.configure(state = NORMAL)
    elif var8.get() == 0:
        txtIced_Cappuccino.configure(state = DISABLED)
        E_Iced_Cappuccino.set("0")
    if(var9.get() == 1):
        txtCoffeeCake.configure(state = NORMAL)
    elif var9.get() == 0:
        txtCoffeeCake.configure(state = DISABLED)
        E_Coffee_Cakes.set("0")
    if(var10.get() == 1):
        txtRed_Velvet_Cake.configure(state = NORMAL)
    elif var10.get() == 0:
        txtRed_Velvet_Cake.configure(state = DISABLED)
        E_Red_Velvet_Cake.set("0")
    if(var11.get() == 1):
        txtBlack_Forest_Cake.configure(state = NORMAL)
    elif var11.get() == 0:
        txtBlack_Forest_Cake.configure(state = DISABLED)
        E_Black_Forest_Cake.set("0")
    if(var12.get() == 1):
        txtBoston_Cream_Cake.configure(state = NORMAL)
    elif var12.get() == 0:
        txtBoston_Cream_Cake.configure(state = DISABLED)
        E_Boston_Cream_Cake.set("0")
    if(var13.get() == 1):
        txtLagos_Chocolate_Cake.configure(state = NORMAL)
    elif var13.get() == 0:
        txtLagos_Chocolate_Cake.configure(state = DISABLED)
        E_Lagos_Chocolate_Cake.set("0")
    if(var14.get() == 1):
        txtKilburn_Chocolate_Cake.configure(state = NORMAL)
    elif var14.get() == 0:
        txtKilburn_Chocolate_Cake.configure(state = DISABLED)
        E_Kilburn_Chocolate_Cake.set("0")
    if(var15.get() == 1):
        txtCarlton_Hill_Cake.configure(state = NORMAL)
    elif var15.get() == 0:
        txtCarlton_Hill_Cake.configure(state = DISABLED)
        E_Carlton_Hill_Chocolate_Cake.set("0")
    if(var16.get() == 1):
        txtQueen_park_Cake.configure(state = NORMAL)
    elif var16.get() == 0:
        txtQueen_park_Cake.configure(state = DISABLED)
        E_Queen_Park_Chocolate_Cake.set("0")
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Nhận Bắt Đầu<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def Receipt():
    txtReceipt.delete("1.0", END)
    x = random.randint(1, 500)
    randomRef = str(x)
    Receipt_Ref.set("BILL" + randomRef)

    txtReceipt.insert(END, 'Hóa Đơn Gồm Có: \t\t\t'+Receipt_Ref.get()+"\t\t\t"+DateofOrder.get()+"\n")
    txtReceipt.insert(END, 'Sản phẩm\t\t\t'+'Số lượng\t\t\t'+"Giá cả \n\n")

    if E_Latte.get() > 0:
        txtReceipt.insert(END, 'Latte:\t\t\t'+str(E_Latte.get())+'\t\t\t'+str('VND%.2f'%(E_Latte.get()*10000))+'\n')
    if E_Espresso.get() > 0:
        txtReceipt.insert(END, 'Espresso:\t\t\t'+str(E_Espresso.get())+'\t\t\t'+str('VND%.2f'%(E_Espresso.get()*10000))+'\n')
    if E_Iced_Latte.get() > 0:
        txtReceipt.insert(END, 'Iced Latte:\t\t\t'+str(E_Iced_Latte.get())+'\t\t\t'+str('VND%.2f'%(E_Iced_Latte.get()*20000))+'\n')
    if E_Vale_Coffee.get() > 0:
        txtReceipt.insert(END, 'Vale Coffee:\t\t\t'+str(E_Vale_Coffee.get())+'\t\t\t'+str('VND%.2f'%(E_Vale_Coffee.get()*10000))+'\n')
    if E_Cappuccino.get() > 0:
        txtReceipt.insert(END, 'Cappuccino:\t\t\t'+str(E_Cappuccino.get())+'\t\t\t'+str('VND%.2f'%(E_Cappuccino.get()*10000))+'\n')
    if E_African_Coffee.get() > 0:
        txtReceipt.insert(END, 'African Coffee:\t\t\t'+str(E_African_Coffee.get())+'\t\t\t'+str('VND%.2f'%(E_African_Coffee.get()*2000))+'\n')
    if E_American_Coffee.get() > 0:
        txtReceipt.insert(END, 'American Coffee:\t\t\t'+str(E_American_Coffee.get())+'\t\t\t'+str('VND%.2f'%(E_American_Coffee.get()*2000))+'\n')
    if E_Iced_Cappuccino.get() > 0:
        txtReceipt.insert(END, 'Iced Cappuccino:\t\t\t'+str(E_Iced_Cappuccino.get())+'\t\t\t'+str('VND%.2f'%(E_Iced_Cappuccino.get()*1000))+'\n')
    if E_Coffee_Cakes.get() > 0:
        txtReceipt.insert(END, 'Coffee Cake:\t\t\t'+str(E_Coffee_Cakes.get())+'\t\t\t'+str('VND%.2f'%(E_Coffee_Cakes.get()*1000))+'\n')
    if E_Red_Velvet_Cake.get() > 0:
        txtReceipt.insert(END, 'Red Velvet Cake:\t\t\t'+str(E_Red_Velvet_Cake.get())+'\t\t\t'+str('VND%.2f'%(E_Red_Velvet_Cake.get()*2000))+'\n')
    if E_Black_Forest_Cake.get() > 0:
        txtReceipt.insert(END, 'Black Forest Cake:\t\t\t'+str(E_Black_Forest_Cake.get())+'\t\t\t'+str('VND%.2f'%(E_Black_Forest_Cake.get()*1000))+'\n')
    if E_Boston_Cream_Cake.get() > 0:
        txtReceipt.insert(END, 'Boston Cream Cake:\t\t\t'+str(E_Boston_Cream_Cake.get())+'\t\t\t'+str('VND%.2f'%(E_Boston_Cream_Cake.get()*1000))+'\n')
    if E_Lagos_Chocolate_Cake.get() > 0:
        txtReceipt.insert(END, 'Lagos Chocolate Cake:\t\t\t'+str(E_Lagos_Chocolate_Cake.get())+'\t\t\t'+str('VND%.2f'%(E_Lagos_Chocolate_Cake.get()*1000))+'\n')
    if E_Kilburn_Chocolate_Cake.get() > 0:
        txtReceipt.insert(END, 'Kilburn Chocolate Cake:\t\t\t'+str(E_Kilburn_Chocolate_Cake.get())+'\t\t\t'+str('VND%.2f'%(E_Kilburn_Chocolate_Cake.get()*1000))+'\n')
    if E_Carlton_Hill_Chocolate_Cake.get() > 0:
        txtReceipt.insert(END, 'Carlton Hill Chocolate Cake:\t\t\t'+str(E_Carlton_Hill_Chocolate_Cake.get())+'\t\t\t'+str('VND%.2f'%(E_Carlton_Hill_Chocolate_Cake.get()*1000))+'\n')
    if E_Queen_Park_Chocolate_Cake.get() > 0:
        txtReceipt.insert(END, 'Queen Park Chocolate Cake:\t\t\t'+str(E_Queen_Park_Chocolate_Cake.get())+'\t\t\t'+str('VND%.2f'%(E_Queen_Park_Chocolate_Cake.get()*1000))+'\n')

    txtReceipt.insert(END, '\nGiá đồ uống:\t'+CostofDrinks.get()+"\tTax Paid:\t"+ PaidTax.get()+"\n")
    txtReceipt.insert(END, 'Giá Bánh:\t'+CostofCakes.get()+"\tSubTotal:\t"+ SubTotal.get()+"\n")
    txtReceipt.insert(END, 'Chi Phí Khác:\t'+ServiceCharge.get()+"\tTotal Cost:\t"+ TotalCost.get()+"\n")


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>RECEIPT END<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>CHECKBUTTONS END<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()

DateofOrder = StringVar()
Receipt_Ref = StringVar()
PaidTax = StringVar()
SubTotal = StringVar()
TotalCost = StringVar()
CostofCakes = StringVar()
CostofDrinks = StringVar()
ServiceCharge = StringVar()

E_Latte = IntVar()
E_Espresso = IntVar()
E_Iced_Latte = IntVar()
E_Vale_Coffee = IntVar()
E_Cappuccino = IntVar()
E_African_Coffee = IntVar()
E_American_Coffee = IntVar()
E_Iced_Cappuccino = IntVar()

E_Coffee_Cakes = IntVar()
E_Red_Velvet_Cake = IntVar()
E_Black_Forest_Cake = IntVar()
E_Boston_Cream_Cake = IntVar()
E_Lagos_Chocolate_Cake = IntVar()
E_Kilburn_Chocolate_Cake = IntVar()
E_Carlton_Hill_Chocolate_Cake = IntVar()
E_Queen_Park_Chocolate_Cake = IntVar()


E_Latte.set(0)
E_Espresso.set(0)
E_Iced_Latte.set(0)
E_Vale_Coffee.set(0)
E_Cappuccino.set(0)
E_African_Coffee.set(0)
E_American_Coffee.set(0)
E_Iced_Cappuccino.set(0)


E_Coffee_Cakes.set(0)
E_Red_Velvet_Cake.set(0)
E_Black_Forest_Cake.set(0)
E_Boston_Cream_Cake.set(0)
E_Lagos_Chocolate_Cake.set(0)
E_Kilburn_Chocolate_Cake.set(0)
E_Carlton_Hill_Chocolate_Cake.set(0)
E_Queen_Park_Chocolate_Cake.set(0)

DateofOrder.set(time.strftime("%d/%m/%Y"))


#Widget created
# f1aa == left hand box
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>DRINKS<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
Latte = Checkbutton(f1aa, text="Latte \t\t", variable = var1, onvalue = 1, offvalue = 0, command = chkbutton_value, font  = ('arial', 18, 'bold')).grid(row = 0, sticky = W)
Espresso = Checkbutton(f1aa, text="Espresso  \t\t", variable = var2, onvalue = 1, offvalue = 0,command = chkbutton_value, font  = ('arial', 18, 'bold')).grid(row = 1, sticky = W)
Iced_Latte = Checkbutton(f1aa, text="Iced Latte  \t\t", variable = var3, onvalue = 1, offvalue = 0, command = chkbutton_value, font  = ('arial', 18, 'bold')).grid(row = 2, sticky = W)
Vale_Coffee = Checkbutton(f1aa, text="Vale_Coffee  \t\t", variable = var4, onvalue = 1, offvalue = 0, command = chkbutton_value,font  = ('arial', 18, 'bold')).grid(row = 3, sticky = W)
Cappuccino  = Checkbutton(f1aa, text="Cappuccino  \t\t", variable = var5, onvalue = 1, offvalue = 0, command = chkbutton_value,font  = ('arial', 18, 'bold')).grid(row = 4, sticky = W)
African_Coffee = Checkbutton(f1aa, text="African Coffee  \t\t", variable = var6, onvalue = 1, offvalue = 0, command = chkbutton_value,font  = ('arial', 18, 'bold')).grid(row = 5, sticky = W)
American_Coffee = Checkbutton(f1aa, text=" Americano Coffee\t\t", variable = var7, onvalue = 1, offvalue = 0, command = chkbutton_value,font  = ('arial', 18, 'bold')).grid(row = 6, sticky = W)
Iced_Cappuccino = Checkbutton(f1aa, text="Iced Cappuccino  \t\t", variable = var8, onvalue = 1, offvalue = 0, command = chkbutton_value,font  = ('arial', 18, 'bold')).grid(row = 7, sticky = W)


#f1ab == right hand box
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>CAKES<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

CoffeeCake= Checkbutton(f1ab, text="Bánh Coffee\t", variable = var9, onvalue = 1, offvalue = 0, command = chkbutton_value, font  = ('arial', 18, 'bold')).grid(row = 0, sticky = W)
Red_Velvet_Cake = Checkbutton(f1ab, text="Red Velvet Cake\t", variable = var10, onvalue = 1, offvalue = 0, command = chkbutton_value, font  = ('arial', 18, 'bold')).grid(row = 1, sticky = W)
Black_Forest_Cake = Checkbutton(f1ab, text="Black Forest\t", variable = var11, onvalue = 1, offvalue = 0, command = chkbutton_value, font  = ('arial', 18, 'bold')).grid(row = 2, sticky = W)
Boston_Cream_Cake = Checkbutton(f1ab, text="Boston Cream\t", variable = var12, onvalue = 1, offvalue = 0, command = chkbutton_value, font  = ('arial', 18, 'bold')).grid(row = 3, sticky = W)
Lagos_Chocolate_Cake = Checkbutton(f1ab, text="Lagos\t", variable = var13, onvalue = 1, offvalue = 0, command = chkbutton_value, font  = ('arial', 18, 'bold')).grid(row = 4, sticky = W)
Kilburn_Chocolate_Cake = Checkbutton(f1ab, text="Kilburn \t", variable = var14, onvalue = 1, offvalue = 0, command = chkbutton_value, font  = ('arial', 18, 'bold')).grid(row = 5, sticky = W)
Carlton_Hill_Cake = Checkbutton(f1ab, text="Carlton Hill\t", variable = var15, onvalue = 1, offvalue = 0, command = chkbutton_value, font  = ('arial', 18, 'bold')).grid(row = 6, sticky = W)
Queen_park_Cake = Checkbutton(f1ab, text="Queen's Park \t", variable = var16, onvalue = 1, offvalue = 0, command = chkbutton_value, font  = ('arial', 18, 'bold')).grid(row = 7, sticky = W)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Eter wet for DRINKS<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
txtLatte = Entry(f1aa, font=('arial', 16, 'bold'), bd = 8, width = 6, justify = 'left', textvariable = E_Latte, state = DISABLED)
txtLatte.grid(row = 0, column = 1)
txtEspresso = Entry(f1aa, font=('arial', 16, 'bold'), bd = 8, width = 6, justify = 'left', textvariable = E_Espresso, state = DISABLED )
txtEspresso.grid(row = 1, column = 1)
txtIced_Latte = Entry(f1aa, font=('arial', 16, 'bold'), bd = 8, width = 6, justify = 'left', textvariable = E_Iced_Latte, state = DISABLED )
txtIced_Latte.grid(row = 2, column = 1)
txtVale_Coffee = Entry(f1aa, font=('arial', 16, 'bold'), bd = 8, width = 6, justify = 'left', textvariable = E_Vale_Coffee, state = DISABLED )
txtVale_Coffee.grid(row = 3, column = 1)
txtCappuccino = Entry(f1aa, font=('arial', 16, 'bold'), bd = 8, width = 6, justify = 'left', textvariable = E_Cappuccino, state = DISABLED )
txtCappuccino.grid(row = 4, column = 1)
txtAfrican_Coffee = Entry(f1aa, font=('arial', 16, 'bold'), bd = 8, width = 6, justify = 'left', textvariable = E_African_Coffee, state = DISABLED )
txtAfrican_Coffee.grid(row = 5, column = 1)
txtAmerican_Coffee = Entry(f1aa, font=('arial', 16, 'bold'), bd = 8, width = 6, justify = 'left', textvariable = E_American_Coffee, state = DISABLED )
txtAmerican_Coffee.grid(row = 6, column = 1)
txtIced_Cappuccino = Entry(f1aa, font=('arial', 16, 'bold'), bd = 8, width = 6, justify = 'left', textvariable = E_Iced_Cappuccino, state = DISABLED )
txtIced_Cappuccino.grid(row = 7, column = 1)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Enter widget for CAKES<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
txtCoffeeCake = Entry(f1ab, font=('arial', 16, 'bold'), bd = 8, width = 6, justify = 'left', textvariable = E_Coffee_Cakes, state = DISABLED )
txtCoffeeCake.grid(row = 0, column = 1)
txtRed_Velvet_Cake = Entry(f1ab, font=('arial', 16, 'bold'), bd = 8, width = 6, justify = 'left', textvariable = E_Red_Velvet_Cake, state = DISABLED )
txtRed_Velvet_Cake.grid(row = 1, column = 1)
txtBlack_Forest_Cake = Entry(f1ab, font=('arial', 16, 'bold'), bd = 8, width = 6, justify = 'left', textvariable = E_Black_Forest_Cake, state = DISABLED )
txtBlack_Forest_Cake.grid(row = 2, column = 1)
txtBoston_Cream_Cake = Entry(f1ab, font=('arial', 16, 'bold'), bd = 8, width = 6, justify = 'left', textvariable = E_Boston_Cream_Cake, state = DISABLED )
txtBoston_Cream_Cake.grid(row = 3, column = 1)
txtLagos_Chocolate_Cake = Entry(f1ab, font=('arial', 16, 'bold'), bd = 8, width = 6, justify = 'left', textvariable = E_Lagos_Chocolate_Cake, state = DISABLED )
txtLagos_Chocolate_Cake.grid(row = 4, column = 1)
txtKilburn_Chocolate_Cake = Entry(f1ab, font=('arial', 16, 'bold'), bd = 8, width = 6, justify = 'left', textvariable = E_Kilburn_Chocolate_Cake, state = DISABLED )
txtKilburn_Chocolate_Cake.grid(row = 5, column = 1)
txtCarlton_Hill_Cake = Entry(f1ab, font=('arial', 16, 'bold'), bd = 8, width = 6, justify = 'left', textvariable = E_Carlton_Hill_Chocolate_Cake, state = DISABLED )
txtCarlton_Hill_Cake.grid(row = 6, column = 1)
txtQueen_park_Cake = Entry(f1ab, font=('arial', 16, 'bold'), bd = 8, width = 6, justify = 'left', textvariable = E_Queen_Park_Chocolate_Cake, state = DISABLED )
txtQueen_park_Cake.grid(row = 7, column = 1)


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>RECEIPT INFO<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
lblReceipt = Label(ft2, font=('arial', 12, 'bold'), text="Hóa Đơn",bd = 2, anchor = "w")
lblReceipt.grid(row = 0, column = 0, sticky = W)
txtReceipt = Text(ft2, font=('arial', 11, 'bold'), width = 59, height =22, bg="white", bd=8)
txtReceipt.grid(row = 1, column = 0)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Cost Item INFO<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

lblCostofDrinks = Label(f2aa, font=('arial', 16, 'bold'), text = "Giá đồ uống         \t", bd = 8, anchor="w")
lblCostofDrinks.grid(row = 0, column = 0, sticky = W)
txtCostofDrinks = Entry(f2aa,font=('arial', 16, 'bold'), bd = 8, justify = "left", textvariable = CostofDrinks)
txtCostofDrinks.grid(row = 0, column = 1, sticky = W)

lblCostofCakes = Label(f2aa, font=('arial', 16, 'bold'), text = "Giá bánh kem", bd = 8, anchor="w")
lblCostofCakes.grid(row = 1, column = 0, sticky = W)
txtCostofCakes = Entry(f2aa,font=('arial', 16, 'bold'), bd = 8, justify = "left", textvariable = CostofCakes)
txtCostofCakes.grid(row = 1, column = 1, sticky = W)

lblServiceCharge = Label(f2aa, font=('arial', 16, 'bold'), text = "Phí dịch vụ\t", bd = 8, anchor = "w")
lblServiceCharge.grid(row = 2, column = 0, sticky = W)
txtServiceCharge = Entry(f2aa,font=('arial', 16, 'bold'), bd = 8, justify = "left", textvariable = ServiceCharge)
txtServiceCharge.grid(row = 2, column = 1, sticky = W)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Payment INFO<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
lblPaidTax = Label(f2ab, font=('arial', 16, 'bold'), text = "Thuế", bd = 8)
lblPaidTax.grid(row = 0, column = 0, sticky = W)
txtPaidTax = Entry(f2ab,font=('arial', 16, 'bold'), bd = 8, justify = "left", textvariable = PaidTax)
txtPaidTax.grid(row = 0, column = 1, sticky = W)

lblSubTotal = Label(f2ab, font=('arial', 16, 'bold'), text = " Tổng Phụ         \t", bd = 8)
lblSubTotal.grid(row = 1, column = 0, sticky = W)
txtSubTotal = Entry(f2ab,font=('arial', 16, 'bold'), bd = 8, justify = "left", textvariable = SubTotal)
txtSubTotal.grid(row = 1, column = 1, sticky = W)

lblTotalCost = Label(f2ab, font=('arial', 16, 'bold'), text = "Toàn bộ", bd =8 )
lblTotalCost.grid(row = 2, column = 0, sticky = W)
txtTotalCost = Entry(f2ab,font=('arial', 16, 'bold'), bd = 8, justify = "left", textvariable = TotalCost)
txtTotalCost.grid(row = 2, column = 1, sticky = W)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>BUTTONS<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
btnTotal = Button(fb2, padx = 16, pady = 4, bd = 4, fg = "black", font = ('arial', 16, 'bold'), width = 5, text = "Toàn bộ", command = CostofItems).grid(row = 0, column = 0)
btnReceipt = Button(fb2, padx = 16, pady = 4, bd = 4, fg = "black", font = ('arial', 16, 'bold'), width = 5, text = "Hóa đơn", command = Receipt).grid(row = 0, column = 1)
btnReset = Button(fb2, padx = 16, pady = 4, bd = 4, fg = "black", font = ('arial', 16, 'bold'), width = 5, text = "Đặt lại", command = reset).grid(row = 0, column = 2)
btnExit = Button(fb2, padx = 16, pady = 4, bd = 4, fg = "black", font = ('arial', 16, 'bold'), width = 5, text = "Thoát", command=qExit).grid(row = 0, column = 3)



root.mainloop()
