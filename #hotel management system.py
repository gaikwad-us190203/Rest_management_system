#hotel management system
from random import randint
from tkinter import *
from tkinter import messagebox
from turtle import left, title
import time
import random
from tkinter import filedialog  #for activating save button
from PIL import ImageTk,Image
import requests
import json


#functions

#functions for reset button
def reset():
    textreceipt.delete(1.0,END)
    e_roti.set('0')
    e_daal.set('0')
    e_rice.set('0')
    e_chilipaneer.set('0')
    e_mixveg.set('0')
    e_alugobi.set('0')
    e_dalmakh.set('0')
    e_gobimt.set('0')
    e_dumal.set('0')
    e_chnam.set('0')
    e_chnam.set('0')
    e_pavbji.set('0')

    e_lassi.set('0')
    e_pepsi.set('0')
    e_butmlk.set('0')
    e_cofe.set('0')
    e_mstea.set('0')
    e_faluda.set('0')
    e_lmpni.set('0')
    e_ksmlk.set('0')
    e_wtrbtle.set('0')
    e_sting.set('0')
    e_lmnsoda.set('0')

    e_glbjmn.set('0')
    e_rsmli.set('0')
    e_basundi.set('0')
    e_rsgulla.set('0')
    e_pulanpli.set('0')
    e_jlebi.set('0')
    e_hlava.set('0')
    e_kjtktli.set('0')
    e_ghevar.set('0')
    e_barfi.set('0')
    e_srknd.set('0')

    textroti.config(state=DISABLED)
    textdaal.config(state=DISABLED)
    textrice.config(state=DISABLED)
    textchilipaneer.config(state=DISABLED)
    textmixveg.config(state=DISABLED)
    textalugobi.config(state=DISABLED)
    textdaalmakh.config(state=DISABLED)
    textgobimt.config(state=DISABLED)
    textdumal.config(state=DISABLED)
    textchnam.config(state=DISABLED)
    textpavbji.config(state=DISABLED)

    textlassi.config(state=DISABLED)
    textpepsi.config(state=DISABLED)
    textbutmlk.config(state=DISABLED)
    textcofe.config(state=DISABLED)
    textmstea.config(state=DISABLED)
    textfaluda.config(state=DISABLED)
    textlmpni.config(state=DISABLED)
    textksmlk.config(state=DISABLED)
    textwtrbtl.config(state=DISABLED)
    textsting.config(state=DISABLED)
    textlmnsd.config(state=DISABLED)

    textglbjmn.config(state=DISABLED)
    textrsmli.config(state=DISABLED)
    textbsndi.config(state=DISABLED)
    textrsgula.config(state=DISABLED)
    textplnpl.config(state=DISABLED)
    textjlebi.config(state=DISABLED)
    texthlava.config(state=DISABLED)
    textkjktli.config(state=DISABLED)
    textghvar.config(state=DISABLED)
    textbrfi.config(state=DISABLED)
    textsrknd.config(state=DISABLED)
    





    





#function for send button
def send():
    def send_msg():
            message=textarea.get(1.0,END)
            number=numberfield.get()
            url = "https://www.fast2sms.com/dev/bulkV2"

            payload = f"sender_id=TXTIND&message={message}&route=p&language=english&numbers={number}"
            headers = {
                'authorization': 'Y7RSVm3chy0guZLNdUJHE1XrItOPCenM9F64xK2BGlDbi8qajWCDG2w1c53EidXpb6BTo7PWzsveSyf8',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Cache-Control': 'no-cache'
                
            }

            response = requests.request("POST", url=url, data=payload, headers=headers)
            print(response.text)
            dic=response.json()
            result=dic.get('return')
            if result==True:
                messagebox.showinfo('Send Successfully','Message sent succesfully')

            else:
                messagebox.showerror('Error','Something went wrong')
       


    root2=Toplevel()

    root2.title('SEND BILL')
    root2.config(bg='black')
    root2.geometry('485x620+50+50')

    logoimage=PhotoImage(file='128.png')
    label=Label(root2,image=logoimage)
    label.pack(pady=5)   

    numberlabel=Label(root2,text='Mobile Number',font=('ariel',18,'bold underline'),bg='black',fg='white')
    numberlabel.pack(pady=5)

    numberfield=Entry(root2,font=('helvetica',22,'bold'),bd=3,width=24)
    numberfield.pack(pady=5)

    billlabel=Label(root2,text='Bill Details',font=('ariel',18,'bold underline'),bg='black',fg='white')
    billlabel.pack(pady=5)

    textarea=Text(root2,font=('ariel',12,'bold'),bd=3,width=46,height=14)
    textarea.pack(pady=5)

    sendbutton=Button(root2,text='SEND',font=('ariel',19,'bold'),bg='white',fg='red4',bd=7,relief=GROOVE,command=send_msg)
    sendbutton.pack(pady=5)

    textarea.insert(END,'receipt Ref:\t'+billnumber+'\t\t\t'+'Date: '+ date +'\n\n')
    if costoffoodvar.get()!='0':
      textarea.insert(END,f'Cost of Food\t\t\tRs{price_of_food}\n')
    if costofdrinkvar.get()!='0':  
      textarea.insert(END,f'Cost Of Drinks\t\t\tRs{price_of_drinks}\n')
    if costofsweetvar.get()!='0':  
      textarea.insert(END,f'Cost of Sweets\t\t\tRs{price_of_sweets}\n') 

    textarea.insert(END,f'Subtotal of Item\t\t\tRs{sub_total_of_item}\n') 
    textarea.insert(END,f'Service Tax\t\t\tRs{10}\n\n') 
    textarea.insert(END,f'Total Cost\t\t\tRs{sub_total_of_item+10}\n')  

    root2.mainloop()

#function for save button
def save():
    url=filedialog.asksaveasfile(mode='w',defaultextension='.txt')
    bill_data=textreceipt.get(1.0,END)
    url.write(bill_data)
    url.close()
    messagebox.showinfo('Information','Your bill is Succesfully Saved ')


#function for receipt
def receipt():
    global billnumber,date
    textreceipt.delete(1.0,END)
    x=random.randint(100,20000)
    billnumber='BILL'+str(x)
    date=time.strftime('%d/%m/%Y')
    textreceipt.insert(END,'\t\t  RESTAURANT '+'\n')
    textreceipt.insert(END,'Receipt ref:'+'    '+  billnumber  +  ' \t\t\t\t\t'   +'date:  '+ date+'\n')
    textreceipt.insert(END,'**********************************************************************************\n')
    textreceipt.insert(END,'Item:\t\tCost of item(RS)'+'\n')
    textreceipt.insert(END,'*********************************************************************************\n')

    if e_roti.get()!='0':
        textreceipt.insert(END,f'Roti\t\t\t{int(e_roti.get())*10}\n\n')
    if e_daal.get()!='0':
        textreceipt.insert(END,f'Daal\t\t\t{int(e_daal.get())*70}\n\n')    
    if e_rice.get()!='0':
        textreceipt.insert(END,f'Rice\t\t\t{int(e_rice.get())*40}\n\n')
    if e_chilipaneer.get()!='0':
        textreceipt.insert(END,f'Chilipaneer\t\t\t{int(e_chilipaneer.get())*80}\n\n')
    if e_mixveg.get()!='0':
        textreceipt.insert(END,f'Mixveg\t\t\t{int(e_mixveg.get())*90}\n\n')  
    if e_alugobi.get()!='0':
        textreceipt.insert(END,f'Alu Gobi\t\t\t{int(e_alugobi.get())*90}\n\n')   
    if e_dalmakh.get()!='0':
        textreceipt.insert(END,f'Dalmakhni\t\t\t{int(e_dalmakh.get())*110}\n\n') 
    if e_gobimt.get()!='0':
        textreceipt.insert(END,f'Gobi mutter\t\t\t{int(e_gobimt.get())*90}\n\n')   
    if e_dumal.get()!='0':
        textreceipt.insert(END,f'Dum Aloo\t\t\t{int(e_dumal.get())*100}\n\n') 
    if e_chnam.get()!='0':
        textreceipt.insert(END,f'Chana Masala\t\t\t{int(e_chnam.get())*100}\n\n') 
    if e_pavbji.get()!='0':
        textreceipt.insert(END,f'Pav Bhaji\t\t\t{int(e_pavbji.get())*60}\n\n') 


    if e_lassi.get()!='0':
        textreceipt.insert(END,f'Lassi\t\t\t{int(e_lassi.get())*40}\n\n')
    if e_pepsi.get()!='0':
        textreceipt.insert(END,f'pepsi\t\t\t{int(e_pepsi.get())*20}\n\n') 
    if e_butmlk.get()!='0':
        textreceipt.insert(END,f'Butter milk\t\t\t{int(e_butmlk.get())*50}\n\n')
    if e_cofe.get()!='0':
        textreceipt.insert(END,f'Cofee\t\t\t{int(e_cofe.get())*20}\n\n')    
    if e_mstea.get()!='0':
        textreceipt.insert(END,f'Masala Tea\t\t\t{int(e_mstea.get())*20}\n\n') 
    if e_faluda.get()!='0':
        textreceipt.insert(END,f'Falooda\t\t\t{int(e_faluda.get())*40}\n\n')
    if e_lmpni.get()!='0':
        textreceipt.insert(END,f'Limbu Paani\t\t\t{int(e_lmpni.get())*30}\n\n')
    if e_ksmlk.get()!='0':
        textreceipt.insert(END,f'Kesar milk\t\t\t{int(e_ksmlk.get())*30}\n\n')
    if e_wtrbtle.get()!='0':
        textreceipt.insert(END,f'Water Bottle\t\t\t{int(e_wtrbtle.get())*20}\n\n')
    if e_sting.get()!='0':
        textreceipt.insert(END,f'Sting\t\t\t{int(e_sting.get())*20}\n\n')
    if e_lmnsoda.get()!='0':
        textreceipt.insert(END,f'Lemon soda\t\t\t{int(e_lmnsoda.get())*20}\n\n') 

    if e_glbjmn.get()!='0':
        textreceipt.insert(END,f'Gulab Jamun\t\t\t{int(e_glbjmn.get())*20}\n\n') 
    if e_rsmli.get()!='0':
        textreceipt.insert(END,f'Ras malai\t\t\t{int(e_rsmli.get())*20}\n\n')  
    if e_basundi.get()!='0':
        textreceipt.insert(END,f'Basundi\t\t\t{int(e_basundi.get())*25}\n\n')
    if e_rsgulla.get()!='0':
        textreceipt.insert(END,f'Ras gulla\t\t\t{int(e_rsgulla.get())*25}\n\n') 
    if e_pulanpli.get()!='0':
        textreceipt.insert(END,f'Puran Poli\t\t\t{int(e_pulanpli.get())*40}\n\n') 
    if e_jlebi.get()!='0':
        textreceipt.insert(END,f'Jalebi\t\t\t{int(e_jlebi.get())*20}\n\n') 
    if e_hlava.get()!='0':
        textreceipt.insert(END,f'Gajar ka Halva\t\t\t{int(e_hlava.get())*30}\n\n') 
    if e_kjtktli.get()!='0':
        textreceipt.insert(END,f'Kaju Katli\t\t\t{int(e_kjtktli.get())*20}\n\n')
    if e_ghevar.get()!='0':
        textreceipt.insert(END,f'Ghevar\t\t\t{int(e_ghevar.get())*30}\n\n')
    if e_barfi.get()!='0':
        textreceipt.insert(END,f'Barfi\t\t\t{int(e_barfi.get())*15}\n\n')
    if e_srknd.get()!='0':
        textreceipt.insert(END,f'Shrikhand\t\t\t{int(e_srknd.get())*30}\n\n')  

    textreceipt.insert(END,'*********************************************************************************\n')
    if costoffoodvar.get()!='Rs0':
      textreceipt.insert(END,f'Cost of Food\t\t\tRs{price_of_food}\n\n')
    if costofdrinkvar.get()!='Rs0':  
      textreceipt.insert(END,f'Cost Of Drinks\t\t\tRs{price_of_drinks}\n\n')
    if costofsweetvar.get()!='Rs0':  
      textreceipt.insert(END,f'Cost of Sweets\t\t\tRs{price_of_sweets}\n\n') 

    textreceipt.insert(END,f'Subtotal of Item\t\t\tRs{sub_total_of_item}\n\n') 
    textreceipt.insert(END,f'Service Tax\t\t\tRs{10}\n\n') 
    textreceipt.insert(END,f'Total Cost\t\t\tRs{sub_total_of_item+10}\n\n')  
    textreceipt.insert(END,'*********************************************************************************\n')                                                                         

       
    





    
def totalcost():
    global price_of_food,price_of_drinks,price_of_sweets,sub_total_of_item
    item1=int(e_roti.get())
    item2=int(e_daal.get())
    item3=int(e_rice.get())
    item4=int(e_chilipaneer.get())
    item5=int(e_mixveg.get())
    item6=int(e_alugobi.get())
    item7=int(e_dalmakh.get())
    item8=int(e_gobimt.get())
    item9=int(e_dumal.get())
    item10=int(e_chnam.get())
    item11=int(e_pavbji.get())

    item12=int(e_lassi.get())
    item13=int(e_pepsi.get())
    item14=int(e_butmlk.get())
    item15=int(e_cofe.get())
    item16=int(e_mstea.get())
    item17=int(e_faluda.get())
    item18=int(e_lmpni.get())
    item19=int(e_ksmlk.get())
    item20=int(e_wtrbtle.get())
    item21=int(e_sting.get())
    item22=int(e_lmnsoda.get())

    item23=int(e_glbjmn.get())
    item24=int(e_rsmli.get())
    item25=int(e_basundi.get())
    item26=int(e_rsgulla.get())
    item27=int(e_pulanpli.get())
    item28=int(e_jlebi.get())
    item29=int(e_hlava.get())
    item30=int(e_kjtktli.get())
    item31=int(e_ghevar.get())
    item32=int(e_barfi.get())
    item33=int(e_srknd.get())

    price_of_food=(item1*10)+(item2*70)+(item3*40)+(item4*80)+(item5*90)+(item6*90)+(item7*110)+(item8*90)+(item9*100)+(item10*100)+(item11*60)

    price_of_drinks=(item12*40)+(item13*30)+(item14*50)+(item15*20)+(item16*20)+(item17*40)+(item18*15)+(item19*30)+(item20*20)+(item21*20)+(item22*20) 

    price_of_sweets=(item23*20)+(item24*20)+(item25*25)+(item26*25)+(item27*40)+(item28*20)+(item29*30)+(item30*20)+(item31*30)+(item32*15)+(item33*30) 

    costoffoodvar.set('RS '+str( price_of_food))
    costofdrinkvar.set('RS '+str(price_of_drinks))
    costofsweetvar.set('RS '+str(price_of_sweets))

    sub_total_of_item=(price_of_food)+(price_of_drinks)+(price_of_sweets)
    subtotalvar.set('RS '+str(sub_total_of_item))

    servicetxvar.set('RS 10')
    totalcost=sub_total_of_item+10
    totalcostvar.set('RS '+str(totalcost))

    



    





#functions for food
def roti():
    if var1.get()==1:
           textroti.config(state=NORMAL)
           textroti.delete(0,END)
           textroti.focus()
    else:
        textroti.config(state=DISABLED)
        e_roti.set('0')
def daal():
    if var2.get()==1:
        textdaal.config(state=NORMAL)
        textdaal.delete(0,END)
        textroti.focus()
    else:
        textdaal.config(state=DISABLED)
        e_daal.set('0') 

def rice():
    if var3.get()==1:
        textrice.config(state=NORMAL)
        textrice.delete(0,END)
        textrice.focus()
    else:
        textrice.config(state=DISABLED)
        e_rice.set('0')   

def chilipaneer():
    if var4.get()==1:
        textchilipaneer.config(state=NORMAL)
        textchilipaneer.delete(0,END)
        textchilipaneer.focus()
    else:
        textchilipaneer.config(state=DISABLED)
        e_chilipaneer.set('0')           

def mixveg():
    if var5.get()==1:
        textmixveg.config(state=NORMAL)
        textmixveg.delete(0,END)
        textmixveg.focus()
    else:
        textmixveg.config(state=DISABLED)
        e_mixveg.set('0')           

def alugobi():
    if var6.get()==1:
        textalugobi.config(state=NORMAL)
        textalugobi.delete(0,END)
        textalugobi.focus()
    else:
        textalugobi.config(state=DISABLED)
        e_alugobi.set('0') 

def dalmakh():
    if var7.get()==1:
        textdaalmakh.config(state=NORMAL)
        textdaalmakh.delete(0,END)
        textdaalmakh.focus()
    else:
        textdaalmakh.config(state=DISABLED)
        e_dalmakh.set('0')

def gobimt():
    if var8.get()==1:
        textgobimt.config(state=NORMAL)
        textgobimt.delete(0,END)
        textgobimt.focus()
    else:
        textgobimt.config(state=DISABLED)
        e_gobimt.set('0')

def dumal():
    if var9.get()==1:
        textdumal.config(state=NORMAL)
        textdumal.delete(0,END)
        textdumal.focus()
    else:
        textdumal.config(state=DISABLED)
        e_dumal.set('0')                    

def chnam():
    if var10.get()==1:
        textchnam.config(state=NORMAL)
        textchnam.delete(0,END)
        textgobimt.focus()
    else:
        textchnam.config(state=DISABLED)
        e_chnam.set('0')

def pavbji():
    if var11.get()==1:
        textpavbji.config(state=NORMAL)
        textpavbji.delete(0,END)
        textpavbji.focus()
    else:
        textpavbji.config(state=DISABLED)
        e_pavbji.set('0')   

#functions of drinks
def lassi():
    if var12.get()==1:
        textlassi.config(state=NORMAL)
        textlassi.delete(0,END)
        textlassi.focus()
    else:
        textlassi.config(state=DISABLED)
        e_lassi.set('0')

def pepsi():
    if var14.get()==1:
        textpepsi.config(state=NORMAL)
        textpepsi.delete(0,END)
        textpepsi.focus()

    else:
        textpepsi.config(state=DISABLED)
        e_pepsi.set('0')

def butmlk():
    if var15.get()==1:
        textbutmlk.config(state=NORMAL)
        textbutmlk.delete(0,END)
        textbutmlk.focus()
    else:
        textbutmlk.config(state=DISABLED)
        e_butmlk.set('0')  

def cofe():
    if var16.get()==1:
        textcofe.config(state=NORMAL)
        textcofe.delete(0,END)
        textcofe.focus()
    else:
        textcofe.config(state=DISABLED)
        e_cofe.set('0')

def mstea():
    if var17.get()==1:
        textmstea.config(state=NORMAL)
        textmstea.delete(0,END)
        textmstea.focus()
    else:
        textmstea.config(state=DISABLED)
        e_mstea.set('0')

def faluda():
    if var18.get()==1:
        textfaluda.config(state=NORMAL)
        textfaluda.delete(0,END)
        textfaluda.focus()
    else:
        textfaluda.config(state=DISABLED)
        e_faluda.set('0') 

def lmpni():
    if var19.get()==1:
        textlmpni.config(state=NORMAL)
        textlmpni.delete(0,END)
        textlmpni.focus()
    else:
        textlmpni.config(state=DISABLED)
        e_lmpni.set('0')        

def ksmilk():
    if var20.get()==1:
        textksmlk.config(state=NORMAL)
        textksmlk.delete(0,END)
        textksmlk.focus()
    else:
        textksmlk.config(state=DISABLED)
        e_ksmlk.set('0')  

def wtrbtle():
    if var21.get()==1:
        textwtrbtl.config(state=NORMAL)
        textwtrbtl.delete(0,END)
        textwtrbtl.focus()
    else:
        textwtrbtl.config(state=DISABLED)
        e_wtrbtle.set('0')  

def sting():
    if var22.get()==1:
        textsting.config(state=NORMAL)
        textsting.delete(0,END)
        textsting.focus()
    else:
        textsting.config(state=DISABLED)
        e_sting.set('0')

def lemonsoda():
    if var23.get()==1:
        textlmnsd.config(state=NORMAL)
        textlmnsd.delete(0,END)
        textlmnsd.focus()
    else:
        textlmnsd.config(state=DISABLED)
        e_lmnsoda.set('0') 

#functions of sweet
def glbjmn():
    if var24.get()==1:
        textglbjmn.config(state=NORMAL)
        textglbjmn.delete(0,END)
        textglbjmn.focus()
    else:
        textglbjmn.config(state=DISABLED)
        e_glbjmn.set('0')

def rsmli():
    if var25.get()==1:
        textrsmli.config(state=NORMAL)
        textrsmli.delete(0,END)
        textrsmli.focus()
    else:
        textrsmli.config(state=DISABLED)
        e_rsmli.set('0')

def basundi():
    if var26.get()==1:
        textbsndi.config(state=NORMAL)
        textbsndi.delete(0,END)
        textbsndi.focus()
    else:
        textbsndi.config(state=DISABLED)
        e_basundi.set('0')

def rsgulla():
    if var27.get()==1:
        textrsgula.config(state=NORMAL)
        textrsgula.delete(0,END)
        textrsgula.focus()
    else:
        textrsgula.config(state=DISABLED)
        e_rsgulla.set('0') 

def pulanpli():
    if var28.get()==1:
        textplnpl.config(state=NORMAL)
        textplnpl.delete(0,END)
        textplnpl.focus()
    else:
        textplnpl.config(state=DISABLED)
        e_pulanpli.set('0') 

def jlebi():
    if var29.get()==1:
        textjlebi.config(state=NORMAL)
        textjlebi.delete(0,END)
        textjlebi.focus()
    else:
        textjlebi.config(state=DISABLED)
        e_basundi.set('0') 

def hlava():
    if var30.get()==1:
        texthlava.config(state=NORMAL)
        texthlava.delete(0,END)
        texthlava.focus()
    else:
        texthlava.config(state=DISABLED)
        e_hlava.set('0') 

def kjktli():
    if var31.get()==1:
        textkjktli.config(state=NORMAL)
        textkjktli.delete(0,END)
        textkjktli.focus()
    else:
        textkjktli.config(state=DISABLED)
        e_kjtktli.set('0') 

def ghevar():
    if var32.get()==1:
        textghvar.config(state=NORMAL)
        textghvar.delete(0,END)
        textghvar.focus()
    else:
        textghvar.config(state=DISABLED)
        e_ghevar.set('0') 

def barfi():
    if var33.get()==1:
        textbrfi.config(state=NORMAL)
        textbrfi.delete(0,END)
        textbrfi.focus()
    else:
        textbrfi.config(state=DISABLED)
        e_barfi.set('0') 

def srknd():
    if var34.get()==1:
        textsrknd.config(state=NORMAL)
        textsrknd.delete(0,END)
        textsrknd.focus()
    else:
        textsrknd.config(state=DISABLED)
        e_srknd.set('0') 


                 

           
root=Tk()
root.geometry('1500x800+0+0')
root.resizable(0,0)
root.title('Restarunt Management System ')
root.config(bg='gray')

topFrame=Frame(root,bd=10,relief=RIDGE,bg='lawngreen')
topFrame.pack(side=TOP)

labelTitle=Label(topFrame,text='Restaurant Management System',font=('arial',30,'bold'),fg='yellow',bd=9,bg='red4',width=40)

labelTitle.grid(row=0,column=0)

#frames
menuFrame=Frame(root,bd=10,relief=RIDGE,bg='coral')
menuFrame.pack(side=LEFT)

costFrame=Frame(menuFrame,bd=4,relief=RIDGE,bg='mediumturquoise',pady=10)
costFrame.pack(side=BOTTOM)

foodFrame=LabelFrame(menuFrame,text='Food',font=('arial',19,'bold'),bd=10,relief=RIDGE,fg='RED')
foodFrame.pack(side=LEFT)

drinksFrame=LabelFrame(menuFrame,text='Drinks',font=('arial',19,'bold'),bd=10,relief=RIDGE,fg='red')
drinksFrame.pack(side=LEFT)

sweetFrame=LabelFrame(menuFrame,text='Sweet',font=('arial',19,'bold'),bd=10,relief=RIDGE,fg='red')
sweetFrame.pack(side=LEFT)


rightFrame=Frame(root,bd=15,relief=RIDGE)
rightFrame.pack(side=RIGHT)

calculatorFrame=Frame(rightFrame,bd=1,relief=RIDGE)
calculatorFrame.pack()

receiptFrame=Frame(rightFrame,bd=4,relief=RIDGE)
receiptFrame.pack()


buttonFrame=Frame(rightFrame,bd=3,relief=RIDGE)
buttonFrame.pack()

#variable
var1=IntVar() #roti
var2=IntVar()#daal
var3=IntVar()#rice
var4=IntVar()#chilipaneer
var5=IntVar()#mixveg
var6=IntVar()#aloo-gobi
var7=IntVar()#dalmakni
var8=IntVar()#gobi mutter
var9=IntVar()#dum aloo
var10=IntVar()#chana masala
var11=IntVar()#pav bhaji

var12=IntVar()#lassi
var14=IntVar()#pepsi
var15=IntVar()#butter milk
var16=IntVar()#cofee
var17=IntVar()#masala tea
var18=IntVar()#falooda
var19=IntVar()#limbu paani
var20=IntVar()#keasr milk
var21=IntVar()#water bottle
var22=IntVar()#sting
var23=IntVar()#limbu paani

var24=IntVar()#gulab jamun
var25=IntVar()#ras malai
var26=IntVar()#basundi
var27=IntVar()#rasgulla
var28=IntVar()#puran poli
var29=IntVar()#jalebi
var30=IntVar()#gajar ka halava
var31=IntVar()#kaju ktli
var32=IntVar()#ghevar 
var33=IntVar()#barfi
var34=IntVar()#shrikhand

e_roti=StringVar()
e_daal=StringVar()
e_rice=StringVar()
e_chilipaneer=StringVar()
e_mixveg=StringVar()
e_alugobi=StringVar()
e_dalmakh=StringVar()
e_gobimt=StringVar()
e_dumal=StringVar()
e_chnam=StringVar()
e_pavbji=StringVar()

e_lassi=StringVar()
e_pepsi=StringVar()
e_butmlk=StringVar()
e_cofe=StringVar()
e_mstea=StringVar()
e_faluda=StringVar()
e_lmpni=StringVar()
e_ksmlk=StringVar()
e_wtrbtle=StringVar()
e_sting=StringVar()
e_lmnsoda=StringVar()
e_ampnna=StringVar()

e_glbjmn=StringVar()
e_rsmli=StringVar()
e_basundi=StringVar()
e_rsgulla=StringVar()
e_pulanpli=StringVar()
e_jlebi=StringVar()
e_hlava=StringVar()
e_kjtktli=StringVar()
e_ghevar=StringVar()
e_barfi=StringVar()
e_srknd=StringVar()

costoffoodvar=StringVar()
costofdrinkvar=StringVar()
costofsweetvar=StringVar()
subtotalvar=StringVar()
servicetxvar=StringVar()
totalcostvar=StringVar()

e_roti.set('0')
e_daal.set('0')
e_rice.set('0')
e_chilipaneer.set('0')
e_mixveg.set('0')
e_alugobi.set('0')
e_dalmakh.set('0')
e_gobimt.set('0')
e_dumal.set('0')
e_chnam.set('0')
e_chnam.set('0')
e_pavbji.set('0')

e_lassi.set('0')
e_pepsi.set('0')
e_butmlk.set('0')
e_cofe.set('0')
e_mstea.set('0')
e_faluda.set('0')
e_lmpni.set('0')
e_ksmlk.set('0')
e_wtrbtle.set('0')
e_sting.set('0')
e_lmnsoda.set('0')

e_glbjmn.set('0')
e_rsmli.set('0')
e_basundi.set('0')
e_rsgulla.set('0')
e_pulanpli.set('0')
e_jlebi.set('0')
e_hlava.set('0')
e_kjtktli.set('0')
e_ghevar.set('0')
e_barfi.set('0')
e_srknd.set('0')







#Food
roti=Checkbutton(foodFrame,text='Roti',font=('ariel',18,'bold'),onvalue=1,offvalue=0,variable=var1,command=roti)
roti.grid(row=0,column=0,sticky=W)

daal=Checkbutton(foodFrame,text="Daal",font=('ariel',18,'bold'),onvalue=1,offvalue=0,variable=var2,command=daal)
daal.grid(row=1,column=0,sticky=W)

rice=Checkbutton(foodFrame,text='Rice',font=('ariel',18,'bold'),onvalue=1,offvalue=0,variable=var3,command=rice)
rice.grid(row=2,column=0,sticky=W)

chilipaneer=Checkbutton(foodFrame,text='ChiliPaneer',font=('ariel',18,'bold'),onvalue=1,offvalue=0,variable=var4,command=chilipaneer)
chilipaneer.grid(row=3,column=0,sticky=W)

mixveg=Checkbutton(foodFrame,text='Mix Veg',font=('ariel',18,'bold'),onvalue=1,offvalue=0,variable=var5,command=mixveg)
mixveg.grid(row=4,column=0,sticky=W)

alugobi=Checkbutton(foodFrame,text='Aloo Gobi',font=('ariel',18,'bold'),onvalue=1,offvalue=0,variable=var6,command=alugobi)
alugobi.grid(row=5,column=0,sticky=W)

dalmakh=Checkbutton(foodFrame,text='Daal Makhni',font=('ariel',18,'bold'),onvalue=1,offvalue=0,variable=var7,command=dalmakh)
dalmakh.grid(row=6,column=0,sticky=W)

gobimt=Checkbutton(foodFrame,text='Gobi Mutter',font=('ariel',18,'bold'),onvalue=1,offvalue=0,variable=var8,command=gobimt)
gobimt.grid(row=7,column=0,sticky=W)

dumal=Checkbutton(foodFrame,text='Dum Aloo',font=('ariel',18,'bold'),onvalue=1,offvalue=0,variable=var9,command=dumal)
dumal.grid(row=8,column=0,sticky=W)

chnam=Checkbutton(foodFrame,text='Chana Masala',font=('ariel',18,'bold'),onvalue=1,offvalue=0,variable=var10,command=chnam)
chnam.grid(row=9,column=0,sticky=W)

pavbji=Checkbutton(foodFrame,text='Pav Bhaaji',font=('ariel',18,'bold'),onvalue=1,offvalue=0,variable=var11,command=pavbji)
pavbji.grid(row=10,column=0,sticky=W)




#entry fields for food

textroti=Entry(foodFrame,font=('ariel',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_roti)
textroti.grid(row=0,column=1)
textdaal=Entry(foodFrame,font=('ariel',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_daal)
textdaal.grid(row=1,column=1)
textrice=Entry(foodFrame,font=('ariel',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_rice)
textrice.grid(row=2,column=1)
textchilipaneer=Entry(foodFrame,font=('ariel',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_chilipaneer)
textchilipaneer.grid(row=3,column=1)
textmixveg=Entry(foodFrame,font=('ariel',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_mixveg)
textmixveg.grid(row=4,column=1)
textalugobi=Entry(foodFrame,font=('ariel',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_alugobi)
textalugobi.grid(row=5,column=1)
textdaalmakh=Entry(foodFrame,font=('ariel',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_dalmakh)
textdaalmakh.grid(row=6,column=1)
textgobimt=Entry(foodFrame,font=('ariel',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_gobimt)
textgobimt.grid(row=7,column=1)
textdumal=Entry(foodFrame,font=('ariel',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_dumal)
textdumal.grid(row=8,column=1)
textchnam=Entry(foodFrame,font=('ariel',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_chnam)
textchnam.grid(row=9,column=1)
textpavbji=Entry(foodFrame,font=('ariel',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_pavbji)
textpavbji.grid(row=10,column=1)

#Drinks
lassi=Checkbutton(drinksFrame,text='Lassi',font=('ariel',18,'bold'),onvalue=1,offvalue=0,variable=var12,command=lassi)
lassi.grid(row=0,column=1,sticky=W)
pepsi=Checkbutton(drinksFrame,text='Pepsi',font=('ariel',18,'bold'),onvalue=1,offvalue=0,variable=var14,command=pepsi)
pepsi.grid(row=1,column=1,sticky=W)
butmlk=Checkbutton(drinksFrame,text='Butter Milk',font=('ariel',18,'bold'),onvalue=1,offvalue=0,variable=var15,command=butmlk)
butmlk.grid(row=2,column=1,sticky=W)
cofe=Checkbutton(drinksFrame,text='Coffee',font=('ariel',18,'bold'),onvalue=1,offvalue=0,variable=var16,command=cofe)
cofe.grid(row=3,column=1,sticky=W)
mstea=Checkbutton(drinksFrame,text='Masala Tea',font=('ariel',18,'bold'),onvalue=1,offvalue=1,variable=var17,command=mstea)
mstea.grid(row=4,column=1,sticky=W)
faluda=Checkbutton(drinksFrame,text='Falooda',font=('ariel',18,'bold'),onvalue=1,offvalue=0,variable=var18,command=faluda)
faluda.grid(row=5,column=1,sticky=W)
lmpni=Checkbutton(drinksFrame,text='Limbu Paani',font=('ariel',18,'bold'),onvalue=1,offvalue=0,variable=var19,command=lmpni)
lmpni.grid(row=6,column=1,sticky=W)
ksmilk=Checkbutton(drinksFrame,text='Kesar Milk',font=('ariel',18,'bold'),onvalue=1,offvalue=1,variable=var20,command=ksmilk)
ksmilk.grid(row=7,column=1,sticky=W)
wtrbtle=Checkbutton(drinksFrame,text='Water Bottle',font=('ariel',18,'bold'),onvalue=1,offvalue=0,variable=var21,command=wtrbtle)
wtrbtle.grid(row=8,column=1,sticky=W)
sting=Checkbutton(drinksFrame,text='Sting',font=('ariel',18,'bold'),onvalue=1,offvalue=0,variable=var22,command=sting)
sting.grid(row=9,column=1,sticky=W)
lemonsoda=Checkbutton(drinksFrame,text='Lemon Soda',font=('ariel',18,'bold'),onvalue=1,offvalue=0,variable=var23,command=lemonsoda)
lemonsoda.grid(row=10,column=1,sticky=W)


#entry fields for drinks
textlassi=Entry(drinksFrame,font=('ariel',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_lassi)
textlassi.grid(row=0,column=2)
textpepsi=Entry(drinksFrame,font=('ariel',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_pepsi)
textpepsi.grid(row=1,column=2)
textbutmlk=Entry(drinksFrame,font=('ariel',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_butmlk)
textbutmlk.grid(row=2,column=2)
textcofe=Entry(drinksFrame,font=('ariel',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_cofe)
textcofe.grid(row=3,column=2)
textmstea=Entry(drinksFrame,font=('ariel',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_mstea)
textmstea.grid(row=4,column=2)
textfaluda=Entry(drinksFrame,font=('ariel',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_faluda)
textfaluda.grid(row=5,column=2)
textlmpni=Entry(drinksFrame,font=('ariel',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_lmpni)
textlmpni.grid(row=6,column=2)
textksmlk=Entry(drinksFrame,font=('ariel',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_ksmlk)
textksmlk.grid(row=7,column=2)
textwtrbtl=Entry(drinksFrame,font=('ariel',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_wtrbtle)
textwtrbtl.grid(row=8,column=2)
textsting=Entry(drinksFrame,font=('ariel',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_sting)
textsting.grid(row=9,column=2)
textlmnsd=Entry(drinksFrame,font=('ariel',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_lmnsoda)
textlmnsd.grid(row=10,column=2)



#sweet
glbjmn=Checkbutton(sweetFrame,text='Gulab Jamun',font=('ariel',18,'bold'),onvalue=1,offvalue=0,variable=var24,command=glbjmn)
glbjmn.grid(row=0,column=3,sticky=W)
rsmli=Checkbutton(sweetFrame,text='Ras Malai',font=('ariel',18,'bold'),onvalue=1,offvalue=0,variable=var25,command=rsmli)
rsmli.grid(row=1,column=3,sticky=W)
basundi=Checkbutton(sweetFrame,text='Basundi',font=('ariel',18,'bold'),onvalue=1,offvalue=0,variable=var26,command=basundi)
basundi.grid(row=2,column=3,sticky=W)
rsgulla=Checkbutton(sweetFrame,text='Rasgulla',font=('ariel',18,'bold'),onvalue=1,offvalue=0,variable=var27,command=rsgulla)
rsgulla.grid(row=3,column=3,sticky=W)
pulanpli=Checkbutton(sweetFrame,text='Puran Poli',font=('ariel',18,'bold'),onvalue=1,offvalue=0,variable=var28,command=pulanpli)
pulanpli.grid(row=4,column=3,sticky=W)
jlebi=Checkbutton(sweetFrame,text='Jalebi',font=('ariel',18,'bold'),onvalue=1,offvalue=0,variable=var29,command=jlebi)
jlebi.grid(row=5,column=3,sticky=W)
hlava=Checkbutton(sweetFrame,text='Gajar ka Halwa',font=('ariel',18,'bold'),onvalue=1,offvalue=0,variable=var30,command=hlava)
hlava.grid(row=6,column=3,sticky=W)
kjktli=Checkbutton(sweetFrame,text='Kaju Katli',font=('ariel',18,'bold'),onvalue=1,offvalue=0,variable=var31,command=kjktli)
kjktli.grid(row=7,column=3,sticky=W)
ghevar=Checkbutton(sweetFrame,text='Ghevar',font=('ariel',18,'bold'),onvalue=1,offvalue=0,variable=var32,command=ghevar)
ghevar.grid(row=8,column=3,sticky=W)
barfi=Checkbutton(sweetFrame,text='Barfi',font=('ariel',18,'bold'),onvalue=1,offvalue=0,variable=var33,command=barfi)
barfi.grid(row=9,column=3,sticky=W)
srknd=Checkbutton(sweetFrame,text='Shrikhand',font=('ariel',18,'bold'),onvalue=1,offvalue=0,variable=var34,command=srknd)
srknd.grid(row=10,column=3,sticky=W)

#entry fields for sweet
textglbjmn=Entry(sweetFrame,font=('ariel',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_glbjmn)
textglbjmn.grid(row=0,column=4)
textrsmli=Entry(sweetFrame,font=('ariel',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_rsmli)
textrsmli.grid(row=1,column=4)
textbsndi=Entry(sweetFrame,font=('ariel',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_basundi)
textbsndi.grid(row=2,column=4)
textrsgula=Entry(sweetFrame,font=('ariel',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_rsgulla)
textrsgula.grid(row=3,column=4)
textplnpl=Entry(sweetFrame,font=('ariel',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_pulanpli)
textplnpl.grid(row=4,column=4)
textjlebi=Entry(sweetFrame,font=('ariel',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_jlebi)
textjlebi.grid(row=5,column=4)
texthlava=Entry(sweetFrame,font=('ariel',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_hlava)
texthlava.grid(row=6,column=4)
textkjktli=Entry(sweetFrame,font=('ariel',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_kjtktli)
textkjktli.grid(row=7,column=4)
textghvar=Entry(sweetFrame,font=('ariel',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_ghevar)
textghvar.grid(row=8,column=4)
textbrfi=Entry(sweetFrame,font=('ariel',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_barfi)
textbrfi.grid(row=9,column=4)
textsrknd=Entry(sweetFrame,font=('ariel',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_srknd)
textsrknd.grid(row=10,column=4)

#cost tables and entry fees
labelcostoffood=Label(costFrame,text='Cost of Food',font=('ariel',16,'bold'),fg='white',bg='firebrick4')
labelcostoffood.grid(row=0,column=0)

textcostoffood=Entry(costFrame,font=('ariel',16,'bold'),bd=6,width=12,state='readonly',textvariable=costoffoodvar)
textcostoffood.grid(row=0,column=1,padx=45)

labelcostofdrink=Label(costFrame,text='Cost of Drinks',font=('ariel',16,'bold'),fg='white',bg='firebrick4')
labelcostofdrink.grid(row=1,column=0)

textcostofdrink=Entry(costFrame,font=('ariel',16,'bold'),bd=6,width=12,state='readonly',textvariable=costofdrinkvar)
textcostofdrink.grid(row=1,column=1,padx=45)

labelcostofsweet=Label(costFrame,text='Cost of Sweet',font=('ariel',16,'bold'),fg='white',bg='firebrick4')
labelcostofsweet.grid(row=2,column=0)

textcostofsweet=Entry(costFrame,font=('ariel',16,'bold'),bd=6,width=12,state='readonly',textvariable=costofsweetvar)
textcostofsweet.grid(row=2,column=1,padx=45)

labelsubtotal=Label(costFrame,text='Subtotal',font=('ariel',16,'bold'),fg='white',bg='firebrick4')
labelsubtotal.grid(row=0,column=2)

textsubtotal=Entry(costFrame,font=('ariel',16,'bold'),bd=6,width=12,state='readonly',textvariable=subtotalvar)
textsubtotal.grid(row=0,column=3,padx=45)

labelservicetx=Label(costFrame,text='Service Tax',font=('ariel',16,'bold'),fg='white',bg='firebrick4')
labelservicetx.grid(row=1,column=2)

textservicetx=Entry(costFrame,font=('ariel',16,'bold'),bd=6,width=12,state='readonly',textvariable=servicetxvar)
textservicetx.grid(row=1,column=3,padx=45)

labeltotalcst=Label(costFrame,text='Total Cost',font=('ariel',16,'bold'),fg='white',bg='firebrick4')
labeltotalcst.grid(row=2,column=2)

texttotalcst=Entry(costFrame,font=('ariel',16,'bold'),bd=6,width=12,state='readonly',textvariable=totalcostvar)
texttotalcst.grid(row=2,column=3,padx=50)

#butttons at bottom
buttontotal=Button(buttonFrame,text='Total',font=('ariel',14,'bold'),fg='white',bg='red4',bd=3,padx=5,command=totalcost)
buttontotal.grid(row=0,column=0)

buttonreceipt=Button(buttonFrame,text='Receipt',font=('ariel',14,'bold'),fg='white',bg='red4',bd=3,padx=5,command=receipt)
buttonreceipt.grid(row=0,column=1)
buttonsave=Button(buttonFrame,text='Save',font=('ariel',14,'bold'),fg='white',bg='red4',bd=3,padx=5,command=save)
buttonsave.grid(row=0,column=2)
buttonsend=Button(buttonFrame,text='Send',font=('ariel',14,'bold'),fg='white',bg='red4',bd=3,padx=5,command=send)
buttonsend.grid(row=0,column=3)
buttonreset=Button(buttonFrame,text='Reset',font=('ariel',14,'bold'),fg='white',bg='red4',bd=3,padx=5,command=reset)
buttonreset.grid(row=0,column=4)
#textarea for receipt
textreceipt=Text(receiptFrame,font=('ariel',12,'bold'),bd=3,width=54,height=25)
textreceipt.grid(row=0,column=0)








root.mainloop()
