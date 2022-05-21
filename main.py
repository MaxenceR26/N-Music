import tkinter as tk
from ctypes import windll
from PIL import Image, ImageTk

from common_funcs import select_image, set_color


class Window(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("1080x720")
        self.config(bg=set_color('bg'))
        self.iconbitmap(select_image('icon.ico'))
        self.center()
        self.wm_overrideredirect(True)

        canvas = tk.Canvas(self, width=314, height=533, bg="#D9D9D9", highlightthickness=0)
        canvas.place(x=50, y=150)

        self.widget_title_bar()

    def widget_title_bar(self):
        self.title_frame = tk.Frame(self)
        title_bar = tk.Canvas(self.title_frame, width=self.winfo_width(), height=100,
                              bg=set_color('darkbg'), highlightthickness=0)
        title_bar.create_text(250, title_bar.winfo_reqheight() // 2, text="N-Music",
                              font=('Roboto', 40, 'bold'), fill=set_color('text'))

        icon_img = Image.open(select_image('icon.png'))
        icon_img = ImageTk.PhotoImage(icon_img.resize((title_bar.winfo_reqheight(), title_bar.winfo_reqheight())))

        icon = tk.Label(self.title_frame, image=icon_img, background=set_color('darkbg'), bd=0,
                        foreground=set_color('bg'))
        icon.photo = icon_img
        icon.place(x=0, y=0)

        image = tk.PhotoImage(file=select_image('exit_button.png')).subsample(6)
        quit_button = tk.Button(self, image=image, background=set_color('darkbg'), cursor='hand2',
                                bd=0, foreground=set_color('text'),
                                activebackground=set_color('darkbg'),
                                activeforeground=set_color('text'),
                                font=('Roboto', 20, 'bold'), command=exit)
        quit_button.photo = image
        quit_button.place(x=self.winfo_width() - 60, y=-1, width=50, height=50)
        title_bar.pack()
        self.title_frame.pack()

        self.apply_drag([title_bar, icon])

    def mouse_down(self, event):
        self.x, self.y = event.x, event.y

    def mouse_up(self, event):
        self.x, self.y = None, None

    def mouse_drag(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        x0 = self.winfo_x() + deltax
        y0 = self.winfo_y() + deltay
        self.geometry(f"+{x0}+{y0}")

    def apply_drag(self, elements):
        for element in elements:
            element.bind('<ButtonPress-1>', self.mouse_down)
            element.bind('<B1-Motion>', self.mouse_drag)
            element.bind('<ButtonRelease-1>', self.mouse_up)

    def center(self):
        self.update_idletasks()
        width = self.winfo_width()
        frm_width = self.winfo_rootx() - self.winfo_x()
        win_width = width + 2 * frm_width
        height = self.winfo_height()
        titlebar_height = self.winfo_rooty() - self.winfo_y()
        win_height = height + titlebar_height + frm_width
        x = self.winfo_screenwidth() // 2 - win_width // 2
        y = self.winfo_screenheight() // 2 - win_height // 2
        self.geometry(f'{width}x{height}+{x}+{y}')
        self.deiconify()

    def set_appwindow(self):  # Pour afficher l'icon dans la barre des taches

        GWL_EXSTYLE = -20
        WS_EX_APPWINDOW = 0x00040000
        WS_EX_TOOLWINDOW = 0x00000080
        # Magic
        hwnd = windll.user32.GetParent(self.winfo_id())
        stylew = windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
        stylew = stylew & ~WS_EX_TOOLWINDOW
        stylew = stylew | WS_EX_APPWINDOW
        windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, stylew)

        self.wm_withdraw()
        self.after(10, self.wm_deiconify)


window = Window().mainloop()