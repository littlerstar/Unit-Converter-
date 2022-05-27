from tkinter import *

root = Tk()
root.title("Unit Converter")

Units = ['km','hm','dam','m','dm','cm','mm']
menu = StringVar()
menu.set("m")

dropmenu1 = OptionMenu(root , menu , *Units)
dropmenu1.grid(row=1 , column=1)

menu2 = StringVar()
menu2.set("m")

dropmenu2 = OptionMenu(root , menu2, *Units)
dropmenu2.grid(row=1 , column=2)

input = Entry(root,font=(20))
input.grid(row=2, column=1)

output = Label(root,width = 20,borderwidth=3 , relief="solid")
output.grid(row=2 , column=2)

def Clear():
    input.delete(0,"end")
    output.config(text = "")

def Convert():
    
    unit1 = menu.get()
    unit2 = menu2.get()

    try:
        num = int(input.get())
        converted_num = num
        if unit1 == 'km' and unit2 == 'hm':
            converted_num = num*10

        elif unit1 == 'km' and unit2 == 'dam':
            converted_num = num*100
            
        elif unit1 == 'km' and unit2 == 'm':
            converted_num = num*1000
            
        elif unit1 == 'km' and unit2 == 'dm':
            converted_num = num*10000
            
        elif unit1 == 'km' and unit2 == 'cm':
            converted_num = num*100000
            
        elif unit1 == 'km' and unit2 == 'mm':
            converted_num = num*1000000
        elif unit1 == 'hm' and unit2 == 'km':
            converted_num = num/10
        elif unit1 == 'hm' and unit2 == 'dam':
            converted_num = num*10
        elif unit1 == 'hm' and unit2 == 'm':
            converted_num = num*100
        elif unit1 == 'hm' and unit2 == 'dm':
            converted_num = num*1000
        elif unit1 == 'hm' and unit2 == 'cm':
            converted_num = num*10000
        elif unit1 == 'hm' and unit2 == 'mm':
            converted_num = num*100000
        elif unit1 == 'dam' and unit2 == 'km':
            converted_num = num/100
        elif unit1 == 'dam' and unit2 == 'hm':
            converted_num = num/10
        elif unit1 == 'dam' and unit2 == 'm':
            converted_num = num*10
        elif unit1 == 'dam' and unit2 == 'dm':
            converted_num = num*100
        elif unit1 == 'dam' and unit2 == 'cm':
            converted_num = num*1000
        elif unit1 == 'dam' and unit2 == 'mm':
            converted_num = num*10000
        elif unit1 == 'm' and unit2 == 'km':
            converted_num = num/1000
        elif unit1 == 'm' and unit2 == 'hm':
            converted_num = num/100
        elif unit1 == 'm' and unit2 == 'dam':
            converted_num = num/10
        elif unit1 == 'm' and unit2 == 'dm':
            converted_num = num*10
        elif unit1 == 'm' and unit2 == 'cm':
            converted_num = num*100
        elif unit1 == 'm' and unit2 == 'mm':
            converted_num = num*1000
        #Dm
        elif unit1 == 'dm' and unit2 == 'km':
            converted_num = num/10000
        elif unit1 == 'dm' and unit2 == 'hm':
            converted_num = num/1000
        elif unit1 == 'dm' and unit2 == 'dam':
            converted_num = num/100
        elif unit1 == 'dm' and unit2 == 'm':
            converted_num = num/10
        elif unit1 == 'dm' and unit2 == 'cm':
            converted_num = num*10
        elif unit1 == 'dm' and unit2 == 'km':
            converted_num = num*100
        #Cm
        elif unit1 == 'cm' and unit2 == 'km':
            converted_num = num/100000
        elif unit1 == 'cm' and unit2 == 'hm':
            converted_num = num/10000
        elif unit1 == 'cm' and unit2 == 'dam':
            converted_num = num/1000
        elif unit1 == 'cm' and unit2 == 'm':
            converted_num = num/100
        elif unit1 == 'cm' and unit2 == 'dm':
            converted_num = num/10
        elif unit1 == 'cm' and unit2 == 'mm':
            converted_num = num*10
        
        #mm
        elif unit1 == 'mm' and unit2 == 'km':
            converted_num = num/1000000
        elif unit1 == 'mm' and unit2 == 'hm':
                converted_num = num/100000
        elif unit1 == 'mm' and unit2 == 'dam':
                converted_num = num/10000
        elif unit1 == 'mm' and unit2 == 'm':
                converted_num = num/1000
        elif unit1 == 'mm' and unit2 == 'dm':
                converted_num = num/100
        elif unit1 == 'mm' and unit2 == 'cm':
                converted_num = num/10
        
        output.config(text=str(converted_num))
    except:
        output.config(text="Invalid Input")

b_convert = Button(root , text = "Convert",command = Convert)
b_convert.grid(row=3 , column=1)

b_clear = Button(root, text="Clear" , command=Clear)
b_clear.grid(row=3,column=2)

root.mainloop()