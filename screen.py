from tkinter import *
import tkinter.messagebox
import database
import log_data


def Next():
    log_data.existing_next_logfile(existing_name_entry.get(),quantity_entry.get(),rate_entry.get(),igst_entry.get(),cgst_entry.get(),sgst_entry.get(),taxablevalue.get(),amount.get())
    quantity_entry.delete(0,END)
    rate_entry.delete(0,END)
    igst_entry.delete(0,END)
    cgst_entry.delete(0,END)
    sgst_entry.delete(0,END)
    taxablevalue_entry.delete(0,END)
    amount_entry.delete(0,END)

def Save():
    log_data.existing_save_logfile(existing_name_entry.get(),quantity_entry.get(),rate_entry.get(),igst_entry.get(),cgst_entry.get(),sgst_entry.get(),taxablevalue.get(),amount.get(),totaltaxablevalue_entry.get(),totalamount_entry.get())
    screen4.destroy()

def Proceed():
    global screen4
    global quantity_entry
    global rate_entry
    global igst_entry
    global cgst_entry
    global sgst_entry
    global taxablevalue_entry
    global amount_entry
    global totaltaxablevalue_entry
    global totalamount_entry
    
    log_num=IntVar()
    log_quantity=IntVar()
    log_rate=IntVar()
    log_igst=IntVar()
    log_cgst=IntVar()
    log_sgst=IntVar()
    log_taxablevalue=IntVar()
    log_amount=IntVar()
    log_totaltaxablevalue=IntVar()
    log_totalamount=IntVar()

    log_products=["Silicone Sealant 12.5g","Silicone Sealant 15g","Silirub PS Clear","Adhesive Sealant 15g"]
    
    selectedproduct=StringVar()
    selectedproduct.set(log_products[0])
    
    screen3.destroy()
    screen4=Toplevel()
    screen4.geometry("700x500+0+0")
    screen4.title("New Customer Information")
    screen4.resizable(width=FALSE,height=FALSE)
    screen4.config(bg="cadet blue")

    head2=Label(screen4,text="TAX INOVICE SOFTWARE",bg="black",fg="white",font="arial",width="200",height="2")
    head2.pack()

    screen4_frame=Frame(screen4,bg="Ghost White",width="657",height="300")
    screen4_frame.place(x=20,y=80)

    product_label=Label(screen4_frame,text="Products:",bg="Ghost White")
    product_label.place(x=10,y=15)
    product_list=OptionMenu(screen4_frame,selectedproduct,*log_products)
    product_list.place(x=80,y=10)

    quantity_label=Label(screen4_frame,text="Quantity:",bg="Ghost White")
    quantity_label.place(x=10,y=50)
    quantity_entry=Entry(screen4_frame,textvariable=log_quantity,width="20")
    quantity_entry.place(x=80,y=50)

    rate_label=Label(screen4_frame,text="Rate:",bg="Ghost White")
    rate_label.place(x=10,y=80)
    rate_entry=Entry(screen4_frame,textvariable=log_rate,width="20")
    rate_entry.place(x=80,y=80)

    igst_label=Label(screen4_frame,text="IGST:",bg="Ghost White")
    igst_label.place(x=10,y=110)
    igst_entry=Entry(screen4_frame,textvariable=log_igst,width="20")
    igst_entry.place(x=80,y=110)

    cgst_label=Label(screen4_frame,text="CGST:",bg="Ghost White")
    cgst_label.place(x=10,y=140)
    cgst_entry=Entry(screen4_frame,textvariable=log_cgst,width="20")
    cgst_entry.place(x=80,y=140)

    sgst_label=Label(screen4_frame,text="SGST:",bg="Ghost White")
    sgst_label.place(x=10,y=170)
    sgst_entry=Entry(screen4_frame,textvariable=log_sgst,width="20")
    sgst_entry.place(x=80,y=170)
    
    taxablevalue_label=Label(screen4_frame,text="Taxable Value:",bg="Ghost White")
    taxablevalue_label.place(x=250,y=50)
    taxablevalue_entry=Entry(screen4_frame,textvariable=log_taxablevalue,width="20")
    taxablevalue_entry.place(x=330,y=50)

    amount_label=Label(screen4_frame,text="Amount:",bg="Ghost White")
    amount_label.place(x=250,y=80)
    amount_entry=Entry(screen4_frame,textvariable=log_amount,width="20")
    amount_entry.place(x=330,y=80)

    totaltaxablevalue_label=Label(screen4_frame,text="Total Taxable Value:",bg="Ghost White")
    totaltaxablevalue_label.place(x=250,y=140)
    totaltaxablevalue_entry=Entry(screen4_frame,textvariable=log_totaltaxablevalue,width="20")
    totaltaxablevalue_entry.place(x=360,y=140)

    totalamount_label=Label(screen4_frame,text="Total Amount:",bg="Ghost White")
    totalamount_label.place(x=250,y=170)
    totalamount_entry=Entry(screen4_frame,textvariable=log_totalamount,width="20")
    totalamount_entry.place(x=360,y=170)

    next_button=Button(screen4_frame,text="Next Entry",width="10",command=Next)
    next_button.place(x=240,y=230)

    save_button=Button(screen4_frame,text="Save & Exit",width="10",command=Save)
    save_button.place(x=330,y=230)

def DisplayData():
    customer_list.delete(0,END)
    for row in database.view():
        customer_list.insert(END,row)

def CustomerRec():
    global sd
    select_customer=customer_list.curselection()[0]
    sd=customer_list.get(select_customer)

    existing_name_entry.delete(0,END)
    existing_name_entry.insert(tkinter.END,sd[0])
    existing_address_entry.delete(0,END)
    existing_address_entry.insert(tkinter.END,sd[1])
    existing_phno_entry.delete(0,END)
    existing_phno_entry.insert(tkinter.END,sd[2])
    existing_gstin_entry.delete(0,END)
    existing_gstin_entry.insert(tkinter.END,sd[3])
    existing_state_entry.delete(0,END)
    existing_state_entry.insert(tkinter.END,sd[4])
    existing_statecode_entry.delete(0,END)
    existing_statecode_entry.insert(tkinter.END,sd[5])
    
def DeleteData():
    x=sd[0]
    if (len(existing_name_entry.get())!=0):
       database.delete(x)
       ClearData()
       DisplayData()

def UpdateData():
    x=sd[0]
    if (len(existing_name_entry.get())!=0):
       database.delete(x)
    if (len(existing_name_entry.get())!=0):
        database.register(existing_name_entry.get(),existing_address_entry.get(),existing_phno_entry.get(),existing_gstin_entry.get(),existing_state_entry.get(),existing_statecode_entry.get())
        customer_list.delete(0,END)
        customer_list.insert(END,(existing_name_entry.get(),existing_address_entry.get(),existing_phno_entry.get(),existing_gstin_entry.get(),existing_state_entry.get(),existing_statecode_entry.get()))

def ClearData():
    existing_name_entry.delete(0,END)
    existing_address_entry.delete(0,END)
    existing_phno_entry.delete(0,END)
    existing_gstin_entry.delete(0,END)
    existing_state_entry.delete(0,END)
    existing_statecode_entry.delete(0,END)

def iExit():
    Exit=tkinter.messagebox.askyesno("Tax Inovice System","Confirm if you want to exit")
    if Exit>0:
        screen1.destroy()
        return

def register_proceed():
    if (len(new_name_entry.get())!=0):
        database.register(new_name_entry.get(),new_address_entry.get(),new_phno_entry.get(),new_gstin_entry.get(),new_state_entry.get(),new_statecode_entry.get())
    screen2.destroy()
    
def new_customer_info():
    global screen2
    global new_name_entry
    global new_address_entry
    global new_phno_entry
    global new_gstin_entry
    global new_state_entry
    global new_statecode_entry

    screen2=Toplevel()
    screen2.geometry("700x500+0+0")
    screen2.title("New Customer Information")
    screen2.resizable(width=FALSE,height=FALSE)
    screen2.config(bg="cadet blue")

    head2=Label(screen2,text="TAX INOVICE SOFTWARE",bg="black",fg="white",font="arial",width="200",height="2")
    head2.pack()

    screen2_frame=Frame(screen2,bg="Ghost White",width="657",height="300")
    screen2_frame.place(x=20,y=80)

    new_name=StringVar()
    new_address=StringVar()
    new_phno=StringVar()
    new_gstin=StringVar()
    new_state=StringVar()
    new_statecode=StringVar()

    n1=Label(screen2_frame,bg="Ghost White",text="Name:")
    n1.place(x=10,y=50)
    new_name_entry=Entry(screen2_frame,textvariable=new_name,width="80")
    new_name_entry.place(x=80,y=50)

    n2=Label(screen2_frame,bg="Ghost White",text="Address:")
    n2.place(x=10,y=80)
    new_address_entry=Entry(screen2_frame,textvariable=new_address,width="80")
    new_address_entry.place(x=80,y=80)

    n3=Label(screen2_frame,bg="Ghost White",text="Phone No.:")
    n3.place(x=10,y=110)
    new_phno_entry=Entry(screen2_frame,textvariable=new_phno,width="80")
    new_phno_entry.place(x=80,y=110)

    n4=Label(screen2_frame,bg="Ghost White",text="GSTIN:")
    n4.place(x=10,y=140)
    new_gstin_entry=Entry(screen2_frame,textvariable=new_gstin,width="80")
    new_gstin_entry.place(x=80,y=140)

    n5=Label(screen2_frame,bg="Ghost White",text="State:")
    n5.place(x=10,y=170)
    new_state_entry=Entry(screen2_frame,textvariable=new_state,width="80")
    new_state_entry.place(x=80,y=170)

    n6=Label(screen2_frame,bg="Ghost White",text="StateCode:")
    n6.place(x=10,y=200)
    new_statecode_entry=Entry(screen2_frame,textvariable=new_statecode,width="80")
    new_statecode_entry.place(x=80,y=200)

    register=Button(screen2_frame,text="Register & Proceed To Billing",width="30",command=register_proceed)
    register.place(x=230,y=250)
    
def existing_customer_info():
    global screen3
    global existing_name_entry
    global existing_address_entry
    global existing_phno_entry
    global existing_gstin_entry
    global existing_state_entry
    global existing_statecode_entry
    global customer_list
    
    screen3=Toplevel()
    screen3.geometry("700x500+0+0")
    screen3.title("Existing Customer Information")
    screen3.resizable(width=FALSE,height=FALSE)
    screen3.config(bg="cadet blue")

    head3=Label(screen3,text="TAX INOVICE SOFTWARE",bg="black",fg="white",font="arial",width="200",height="2")
    head3.pack()

    screen3_frame=Frame(screen3,bg="Ghost White",width="400",height="250")
    screen3_frame.place(x=20,y=80)

    button_frame=Frame(screen3,bg="Ghost White",width="485",height="40")
    button_frame.place(x=100,y=360)

    scroll_frame=Frame(screen3,bg="Ghost White",width="257",height="250")
    scroll_frame.place(x=430,y=70)

    existing_name=StringVar()
    existing_address=StringVar()
    existing_phno=StringVar()
    existing_gstin=StringVar()
    existing_state=StringVar()
    existing_statecode=StringVar()

    e1=Label(screen3_frame,bg="Ghost White",text="Name:")
    e1.place(x=15,y=50)
    existing_name_entry=Entry(screen3_frame,textvariable=existing_name,width="50")
    existing_name_entry.place(x=80,y=50)
    
    e2=Label(screen3_frame,bg="Ghost White",text="Address:")
    e2.place(x=15,y=80)
    existing_address_entry=Entry(screen3_frame,textvariable=existing_address,width="50")
    existing_address_entry.place(x=80,y=80)

    e3=Label(screen3_frame,bg="Ghost White",text="Phone No.:")
    e3.place(x=15,y=110)
    existing_phno_entry=Entry(screen3_frame,textvariable=existing_phno,width="50")
    existing_phno_entry.place(x=80,y=110)

    e4=Label(screen3_frame,bg="Ghost White",text="GSTIN:")
    e4.place(x=15,y=140)
    existing_gstin_entry=Entry(screen3_frame,textvariable=existing_gstin,width="50")
    existing_gstin_entry.place(x=80,y=140)

    e5=Label(screen3_frame,bg="Ghost White",text="State:")
    e5.place(x=15,y=170)
    existing_state_entry=Entry(screen3_frame,textvariable=existing_state,width="50")
    existing_state_entry.place(x=80,y=170)

    e6=Label(screen3_frame,bg="Ghost White",text="StateCode:")
    e6.place(x=15,y=200)
    existing_statecode_entry=Entry(screen3_frame,textvariable=existing_statecode,width="50")
    existing_statecode_entry.place(x=80,y=200)

    scrollbar=Scrollbar(scroll_frame)
    scrollbar.grid(row=0,column=1,sticky="ns")

    customer_list=Listbox(scroll_frame,width=40,height=17,yscrollcommand=scrollbar.set)
    customer_list.bind('<<ListboxSelect>>',lambda x: CustomerRec())
    customer_list.grid(row=0,column=0)
    scrollbar.config(command=customer_list.yview)

    proceed_button=Button(button_frame,width="17",text="Proceed To Billing",command=Proceed)
    proceed_button.place(x=10,y=8)

    update_button=Button(button_frame,width="8",text="Update",command=UpdateData)
    update_button.place(x=140,y=8)

    clear_button=Button(button_frame,width="8",text="Clear",command=ClearData)
    clear_button.place(x=206,y=8)

    delete_button=Button(button_frame,width="8",text="Delete",command=DeleteData)
    delete_button.place(x=273,y=8)

    display_button=Button(button_frame,width="8",text="Display",command=DisplayData)
    display_button.place(x=340,y=8)

    exit_button=Button(button_frame,width="8",text="Exit",command=iExit)
    exit_button.place(x=407,y=8)
    
global screen1
screen1=Tk()
screen1.geometry("700x500+0+0")
screen1.title("TAX INOVICE")
screen1.resizable(width=FALSE,height=FALSE)
screen1.config(bg="cadet blue")

head1=Label(screen1,text="TAX INOVICE SOFTWARE",bg="black",fg="white",font="arial",width="200",height="3")
head1.pack()

page_frame=Frame(screen1,bg="Ghost White",width="657",height="200")
page_frame.place(x=20,y=100)

page=Label(page_frame,text="Select One :-",bg="Ghost White",font=('arial',15,'bold'),height="2")
page.place(x=10,y=10)

new_customer=Button(page_frame,text="New Customer",width="70",height="2",command=new_customer_info)
new_customer.place(x=100,y=70)

existing_customer=Button(page_frame,text="Existing Customer",width="70",height="2",command=existing_customer_info)
existing_customer.place(x=100,y=120)
screen1.mainloop()
