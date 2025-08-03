from tkinter import *
class LoanCalculator:
    def __init__(self):
        window = Tk()
        window.title("Loan Calculator - Dark Mode")
        window.geometry("420x310")
        window.resizable(False, False)
        window.configure(bg="#1e1e1e")
        Label(window, text="💰 Loan Calculator 💰", 
              font=("Arial", 16, "bold"), 
              fg="#4fc3f7", bg="#1e1e1e").pack(pady=10)
        frame = Frame(window, bg="#1e1e1e")
        frame.pack(padx=20, pady=5)
        self.add_label_entry(frame, "Annual Interest Rate:", 0)
        self.add_label_entry(frame, "Number of Years:", 1)
        self.add_label_entry(frame, "Loan Amount:", 2)
        self.monthlyPaymentVar = StringVar()
        self.totalPaymentVar = StringVar()
        Label(frame, text="Monthly Payment:", font=("Arial", 10), fg="white", bg="#1e1e1e").grid(row=3, column=0, sticky=W, pady=5)
        Label(frame, textvariable=self.monthlyPaymentVar, font=("Arial", 10), fg="#90ee90", bg="#2e2e2e", width=20, anchor='e').grid(row=3, column=1)
        Label(frame, text="Total Payment:", font=("Arial", 10), fg="white", bg="#1e1e1e").grid(row=4, column=0, sticky=W, pady=5)
        Label(frame, textvariable=self.totalPaymentVar, font=("Arial", 10), fg="#90ee90", bg="#2e2e2e", width=20, anchor='e').grid(row=4, column=1)
        Button(window, text="Compute Payment", 
               command=self.computePayment, 
               bg="#007acc", fg="white", font=("Arial", 10, "bold"),
               activebackground="#005f9e", padx=10, pady=5).pack(pady=15)
        window.mainloop()
    def add_label_entry(self, frame, text, row):
        Label(frame, text=text, font=("Arial", 10), fg="white", bg="#1e1e1e").grid(row=row, column=0, sticky=W, pady=5)
        var = StringVar()
        entry = Entry(frame, textvariable=var, justify=RIGHT, width=22, bg="#2e2e2e", fg="white", insertbackground="white")
        entry.grid(row=row, column=1)
        if "Interest" in text:
            self.annualInterestRateVar = var
        elif "Years" in text:
            self.numberOfYearsVar = var
        elif "Loan" in text:
            self.loanAmountVar = var
    def computePayment(self):
        try:
            monthlyPayment = self.getMonthlyPayment(
                float(self.loanAmountVar.get()),
                float(self.annualInterestRateVar.get()) / 1200,
                int(self.numberOfYearsVar.get())
            )
            self.monthlyPaymentVar.set(format(monthlyPayment, '10.2f'))

            totalPayment = monthlyPayment * 12 * int(self.numberOfYearsVar.get())
            self.totalPaymentVar.set(format(totalPayment, '10.2f'))
        except ValueError:
            self.monthlyPaymentVar.set("Invalid Input")
            self.totalPaymentVar.set("Invalid Input")
    def getMonthlyPayment(self, loanAmount, monthlyInterestRate, numberOfYears):
        return loanAmount * monthlyInterestRate / (1 - 1 / (1 + monthlyInterestRate) ** (numberOfYears * 12))
LoanCalculator()
