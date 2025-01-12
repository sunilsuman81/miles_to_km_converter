from tkinter import *

window = Tk()
window.title("Mile To Km Converter")
#window.minsize(width=100, height=100)
window.config(padx=20, pady=20)

def mile_to_km():
    #print("calculate button clicked")
    mValue = float(milesEntryBox.get())
    #print(mValue)
    kmValue = mValue * 1.609
    kmEntryLabel.config(text=f"{kmValue}")

#Label Is equal to
my_label = Label(text="Is equal to")
my_label.grid(column=0, row=1)

#Entry - Miles
milesEntryBox = Entry(width=10)
milesEntryBox.grid(column=1, row=0)

#Label - Km
kmEntryLabel = Label(text=0)
kmEntryLabel.grid(column=1, row=1)


# Label Mile
milesLabel = Label(text="Miles")
milesLabel.grid(column=2, row=0)

#Label KM
kmLabel = Label(text="Km")
kmLabel.grid(column=2, row=1)

#Button calculate
calculateButton = Button(text="Calculate", command=mile_to_km)
calculateButton.grid(column=1, row=2)





window.mainloop()
