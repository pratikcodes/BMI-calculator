from tkinter import *
from tkinter import ttk
class Screen(Tk):
    def __init__(self):
        super().__init__()
        self.minsize(400, 250)
        #self.configure(background="#4d4d4d")
        self.title("BMI Calculator")
        self.create_widget()
    def clear_all(self):
        self.entry1.delete(0, END)
        self.entry2.delete(0, END)
        self.combobox1.current(0)
        self.combobox2.current(0)
        self.entry3.delete(0, END)
    def clear(self):
        self.entry3.delete(0, END)
    def clicked(self):
        self.weight = float(self.entry1.get())
        self.height = float(self.entry2.get())
        self.unit_w = self.combobox1.get()
        self.unit_h = self.combobox2.get()
        if self.unit_w == "kg":
            if self.unit_h == "cm":
                self.bmi = self.weight/(0.01*self.height)**2
            elif self.unit_h == "inch":
                self.bmi = self.weight/(2.54*0.01*self.height)**2
            else:
                self.bmi = "ERROR"
        elif self.unit_w == "lb":
            if self.unit_h == "cm":
                self.bmi = self.weight*0.4536/(0.01*self.height)**2
            elif self.unit_h == "inch":
                self.bmi = self.weight*0.4536/(2.54*0.01*self.height)**2
            else:
                self.bmi = "ERROR"
        else:
            self.bmi = "ERROR"
        if self.bmi == "ERROR":
            result_text = "ERR"
        else:
            result_text = str(round(self.bmi, 1))
        self.clear()
        self.entry3.insert(0, result_text)

    def create_widget(self):
        self.label1 = ttk.Label(self, text="Know your BMI", background="#4d4d4d", foreground="skyblue", font=("tahoma", 20))
        self.label1.grid(row=0, column=1, pady=5)
        self.label2 = ttk.Label(self, text="Enter your weight: ", background="#4d4d4d", foreground="#fe0")
        self.label2.grid(row=1, column=0)
        self.entry1 = ttk.Entry(self, width=10)
        self.entry1.grid(row=1, column=1)
        self.combobox1 = ttk.Combobox(self, width=5, values=["kg", "lb"])
        self.combobox1.grid(row=1, column=2)
        self.combobox1.current(0)
        self.label3 = ttk.Label(self, text="Enter your height: ", background="#4d4d4d", foreground="#fe0")
        self.label3.grid(row=2, pady=25, column=0)
        self.entry2 = ttk.Entry(self, width=10)
        self.entry2.grid(row=2, column=1)
        self.combobox2 = ttk.Combobox(self, width=5, values=["cm", "inch"])
        self.combobox2.grid(row=2, column=2)
        self.combobox2.current(0)
        self.submit = ttk.Button(self, text="Find your BMI!", command=self.clicked)
        self.submit.grid(row=3, column=1)
        self.label4 = ttk.Label(self, text="Your BMI is: ", background="#4d4d4d", foreground="#fe0")
        self.label4.grid(row=4, column=0)
        self.entry3 = ttk.Entry(self, width=5)
        self.entry3.grid(row=4, column=1, pady=25)
        self.clear_button = ttk.Button(self, text="Clear", command=self.clear_all)
        self.clear_button.grid(row=4, column=2)
        self.configure(background="#4d4d4d")
        self.wm_iconbitmap("health.ico")

screen = Screen()
screen.mainloop()