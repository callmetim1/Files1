import sys
from Tkinter import * 

array = []
onearray = []
zeroarray = []
number = str(10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000009111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111199999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)
number = list(number)

root = Tk()

def main():
    button = Button(root)
    button['text'] = 'Click to see hidden text!'
    button['command'] = quit_callback       
    button['width'] = 50 
    button.pack()
    newbutton = Button(root)
    newbutton['text'] = 'Quit this app!'
    newbutton['command'] = quit
    newbutton['width'] = 50
    newbutton.pack()
    
   #  text = Text(root)
    # text['text'] = "hi"
    # text.pack()
    # var = StringVar()
    # var.set("hi")
    root.mainloop()
    
def quit_callback():
    
    window = Toplevel(root)
    for items in number:
	    if items == `1` or `0` or `9`:
		    array.append(items)
    newlabel = Label(window, text="The amount of characters in array of elements displayed:", width=50)
    label = Label(window, text=len(array), width=50)
    text = Text(root)
    text.insert(INSERT, str(array))
    text.insert(END, " -End-")
    onebutton = Button(window)
    onebutton['text'] = "Find ", 1, " in the array."
    onebutton['command'] = one
    onebutton['width'] = 50 
    zerobutton = Button(window)
    zerobutton['text'] = "Find ", 0, " in the array."
    zerobutton['command'] = zero
    zerobutton['width'] = 50 
    newlabel.pack()
    label.pack()
    text.pack()
    onebutton.pack()
    zerobutton.pack()
    
def quit():
    sys.exit(0)
    
def one():
    newwindow = Toplevel(root)
    for newitems in number:
	    if newitems == `1`:
		    onearray.append(newitems)
    newerlabel = Label(newwindow, text=len(onearray), width=50)
    newerlabel.pack()
    
def zero():
    newnewwindow = Toplevel(root)
    for newnewitems in number:
	    if newnewitems == `0`:
		    zeroarray.append(newnewitems)
    newernewlabel = Label(newnewwindow, text=len(zeroarray), width=50)
    newernewlabel.pack()
    
    

main()
