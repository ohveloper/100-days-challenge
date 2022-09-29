import tkinter as tk

window = tk.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

my_label = tk.Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.pack()     # 자동으로 중간에 배치 시켜주는 함





window.mainloop()