import tkinter as tk
class calculator:
    def _init_(self, master):
        self.master = master
        master.title("calculator")

        self.result_var = tk.StringVar()

        #Entry field for displaying the result
        self.result_entry = tk.Entry(master, textvariable=self.result_var, font=("Arial",30),bd=12, insertwidth=14, borderwidth=5)
        self.result_entry.grid(row=0, column=0, columnspan=5)

        #Button layout
        buttons = [
            '7','8','9','/',
            '4','5','6','*',
            '1','2','3','-',
            '0','C','=','+'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            if button == 'C':
                action = self.clear
            elif button == '=':
                action = self.calculate
            else:
                action = lambda x=button: self.append_to_result(x)
            tk.Button(master, text=button, padx=20, pady=20, font=("Arial",30), command=action).grid(row=row_val,column=col_val)

            col_val +=1
            if col_val >3:
                col_val = 0
                row_val += 1
                
def append_to_result(self, value):
       current_text = self.result_var.get()
       self.result_var.set(current_text + value)
def clear(self):
       self.result_var.set("")
def calculate(self):
       try:
           result = eval(self.result_var.get())
           self.reslt_var.set(result)
       except Exception as e:
           self.result_var.set(result)

       if _name_ =="_main_":
           root = tk.Tk()
           calculator = calculator(root)
           root.mainloop()


        
