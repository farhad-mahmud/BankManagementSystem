import tkinter as tk
from tkinter import messagebox as MessageBox
import mysql.connector as mysql
from tkinter import *

class Appli:
    def __init__(self, master):
        self.master = master

        def go_back():
            self.master.destroy()

        def apply_loan():
            acc_no = e_acc_no.get().strip()
            try:
                loan_amt = float(loan_amount.get())
                interest_rate = float(interest.get())
                duration_val = int(duration.get())
            except ValueError:
                MessageBox.showinfo("Input Error", "All fields must be filled with valid numeric values.")
                return

            if not acc_no:
                MessageBox.showinfo("Input Error", "Account number is required.")
                return
            if loan_amt <= 0 or interest_rate <= 0 or duration_val <= 0:
                MessageBox.showinfo("Input Error", "Loan amount, interest rate, and duration must be positive.")
                return

            try:
                con = mysql.connect(host="localhost", user="root", password="donotrootfarhad", database="bank_data")
                cursor = con.cursor()

                # Calculate the total repayment amount (loan balance)
                total_repayment = loan_amt * (1 + (interest_rate / 100) * (duration_val / 12))

                # Insert loan details into the database
                cursor.execute(
                    """
                    INSERT INTO loans (acc_no, loan_amount, interest_rate, duration, loan_balance)
                    VALUES (%s, %s, %s, %s, %s)
                    """,
                    (acc_no, loan_amt, interest_rate, duration_val, total_repayment),
                )
                con.commit()
                MessageBox.showinfo("Loan Application", "Loan applied successfully.")

            except mysql.Error as e:
                MessageBox.showerror("Database Error", f"An error occurred: {str(e)}")
            finally:
                if 'con' in locals() and con.is_connected():
                    con.close()

        def repay_loan():
            acc_no = e_acc_no.get().strip()

            if not acc_no:
                MessageBox.showinfo("Input Error", "Account number is required.")
                return

            try:
                con = mysql.connect(host="localhost", user="root", password="donotrootfarhad", database="bank_data")
                cursor = con.cursor()

                # Fetch loan details
                cursor.execute("SELECT loan_amount, interest_rate, duration, loan_balance FROM loans WHERE acc_no = %s", (acc_no,))
                loan_data = cursor.fetchone()

                if loan_data:
                    loan_amt, interest_rate, duration_val, current_balance = loan_data

                    # Calculate EMI
                    monthly_rate = interest_rate / 100 / 12
                    emi = (loan_amt * monthly_rate * (1 + monthly_rate) ** duration_val) / ((1 + monthly_rate) ** duration_val - 1)

                    if emi > current_balance:
                        MessageBox.showinfo("Error", "Monthly payment exceeds loan balance.")
                        return

                    # Deduct EMI from loan balance
                    new_balance = current_balance - emi
                    cursor.execute("UPDATE loans SET loan_balance = %s WHERE acc_no = %s", (new_balance, acc_no))
                    con.commit()

                    MessageBox.showinfo("Repayment Success", f"Loan repaid successfully. New balance: {new_balance:.2f}")
                else:
                    MessageBox.showinfo("Loan Not Found", "No loan found for this account number.")

            except mysql.Error as e:
                MessageBox.showerror("Database Error", f"An error occurred: {str(e)}")
            finally:
                if 'con' in locals() and con.is_connected():
                    con.close()

        def check_loan_balance():
            acc_no = e_acc_no.get().strip()

            if not acc_no:
                MessageBox.showinfo("Input Error", "Account number is required.")
                return

            try:
                con = mysql.connect(host="localhost", user="root", password="donotrootfarhad", database="bank_data")
                cursor = con.cursor()

                # Fetch loan balance
                cursor.execute("SELECT loan_balance FROM loans WHERE acc_no = %s", (acc_no,))
                loan_data = cursor.fetchone()

                if loan_data:
                    lb.delete(0, tk.END)
                    lb.insert(0, f"{loan_data[0]:.2f}")
                else:
                    MessageBox.showinfo("Loan Not Found", "No loan found for this account number.")

            except mysql.Error as e:
                MessageBox.showerror("Database Error", f"An error occurred: {str(e)}")
            finally:
                if 'con' in locals() and con.is_connected():
                    con.close()

        self.top = tk.Frame(master, height=100, bg="#f4f5f5")
        self.top.pack(fill=tk.X)

        self.bottom = tk.Frame(master, height=800, bg="#8e9b96")
        self.bottom.pack(fill=tk.X)

        # Heading
        self.heading = tk.Label(self.top, text="Loan System", font="helvetica 18 bold", bg="#f4f5f5")
        self.heading.place(x=265, y=30)

        # Labels
        labels = [
            ("Account Number", 55),
            ("Loan Amount", 110),
            ("Interest Rate (%)", 165),
            ("Duration (months)", 220),
            ("Monthly Payment", 275),
            ("Loan Balance", 330),
        ]

        for text, y_pos in labels:
            tk.Label(self.bottom, text=text, font="helvetica 14 bold", bg="#8e9b96").place(x=40, y=y_pos)

        # Entry Fields
        e_acc_no = tk.Entry(self.bottom, width="45")
        e_acc_no.place(x=320, y=55)

        loan_amount = tk.Entry(self.bottom, width="60")
        loan_amount.place(x=320, y=110)

        interest = tk.Entry(self.bottom, width="60")
        interest.place(x=320, y=165)

        duration = tk.Entry(self.bottom, width="60")
        duration.place(x=320, y=220)

        repayment = tk.Entry(self.bottom, width="60")
        repayment.place(x=320, y=275)

        lb = tk.Entry(self.bottom, width="60")
        lb.place(x=320, y=330)

        # Buttons
        buttons = [
            ("Apply Loan", apply_loan, 380),
            ("Monthly Payment", repay_loan, 420),
            ("Check Loan Balance", check_loan_balance, 460),
        ]

        self.back_btn = Button(self.bottom, text="Back", bg="red", font="helvetica 15 bold", width="10", command=go_back)
        self.back_btn.place(x=35, y=415)

        for text, command, y_pos in buttons:
            tk.Button(self.bottom, text=text, font="helvetica 15 bold", width="20", command=command).place(x=235, y=y_pos)


def main():
    root = tk.Tk()
    app = Appli(root)
    root.geometry("700x600+200+20")
    root.resizable(height=0, width=0)
    root.mainloop()


if __name__ == "__main__":
    main()
