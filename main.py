import tkinter as tk


class Main(tk.Tk):
    def __init__(self):
        super(Main, self).__init__()

        title_bar = tk.Canvas(self, width=1080, height=121, bg="#242424", highlightthickness=0)
        title_bar.pack()

        canva = tk.Canvas(self, width=314, height=533, bg="#D9D9D9", highlightthickness=0)
        canva.place(x=50, y=150)

    # Updating window
    def update(self):
        self.geometry("1080x720")
        self.config(bg="#9A9A9A")
        self.mainloop()


Main().update()
