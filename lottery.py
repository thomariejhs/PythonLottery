#Widgets:
from tkinter import *
window = Tk()
img = PhotoImage( file = 'lotto.gif' )
imgLbl = Label(window, image = img)
label1 = Label(window, relief = 'groove', width = 2,fg='red')
label2 = Label(window, relief = 'groove', width = 2,fg='red')
label3 = Label(window, relief = 'groove', width = 2,fg='red')
label4 = Label(window, relief = 'groove', width = 2,fg='red')
label5 = Label(window, relief = 'groove', width = 2,fg='red')
label6 = Label(window, relief = 'groove', width = 2,fg='red')
getBtn = Button(window)
resBtn = Button(window)

#Geometry:
imgLbl.grid(row = 1, column = 1, rowspan = 2)
label1.grid(row = 1, column = 2, padx = 10)
label2.grid(row = 1, column = 3, padx = 10)
label3.grid(row = 1, column = 4, padx = 10)
label4.grid(row = 1, column = 5, padx = 10)
label5.grid(row = 1, column = 6, padx = 10)
label6.grid(row = 1, column = 7, padx = 10)
getBtn.grid(row = 2, column = 2, columnspan = 4)
resBtn.grid(row = 2, column = 6, columnspan = 2)

#Static Properties:
window.title('Lottery Number Picker')
window.resizable(0, 0)
getBtn.configure(text = 'Get My Lucky Numbers')
resBtn.configure(text = 'Reset')


#Initial Properties:
label1.configure(text = '...')
label2.configure(text = '...')
label3.configure(text = '...')
label4.configure(text = '...')
label5.configure(text = '...')
label6.configure(text = '...')
resBtn.configure(state = DISABLED)


#Dynamic Properties:
from random import sample

def pick():
	nums = sample(range(1, 49), 6)
	label1.configure(text = nums[0])
	label2.configure(text = nums[1])
	label3.configure(text = nums[2])
	label4.configure(text = nums[3])
	label5.configure(text = nums[4])
	label6.configure(text = nums[5])
	getBtn.configure(state = NORMAL)
	resBtn.configure(state = DISABLED)
	



#delete me



#Sustain Window
window.mainloop()


