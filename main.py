import tkinter as tk
from tkinter import ttk
from tkinter.constants import *

class LoginToAccount(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self['borderwidth'] = 1
        self['relief'] = SOLID
        self.pack(padx=2, pady=2, fill=BOTH, expand=True)

        # contant
        self.label = ttk.Label(self, text='Login to account')
        self.label.pack()

class Registration(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self['borderwidth'] = 1
        self['relief'] = SOLID
        self.pack(padx=2, pady=2, fill=BOTH, expand=True)
        
        # contant
        self.label = ttk.Label(self, text='Registration')
        self.label.pack()

class SwitchWin(ttk.LabelFrame):
    def __init__(self, container):
        super().__init__(container)
        self['text'] = 'switch'
        self['borderwidth'] = 1
        self['relief'] = SOLID
        self.pack(padx=2, pady=2, fill=BOTH, expand=True)

        # contant
        options = {'padx':2, 'pady':2, 'anchor':W}
        # self.radio = tk.BooleanVar(value=True)
        self.radio = tk.BooleanVar()
        self.login_to_account = ttk.Radiobutton(self, variable=self.radio, text='login to account', value=True)
        #self.login_to_account['command'] = self.get_value_rb
        self.login_to_account.pack(**options)
        self.registration = ttk.Radiobutton(self, variable=self.radio, text='registration', value=False)
        #self.registration['command'] = self.get_value_rb
        self.registration.pack(**options)

    def get_value_rb(self):
        value_rb = self.radio.get()
        return value_rb


# класс для окон регистрации и входа в личный кабинет
class View(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self['borderwidth'] = 1
        self['relief'] = SOLID
        self.pack(padx=2, pady=2, fill=BOTH, expand=True)

        self.frame_2 = ttk.Frame(self, borderwidth=1, relief=SOLID)
        self.frame_2.pack(padx=2, pady=2, fill=BOTH, expand=True)

        self.frame_list = []
        self.frame_list.append(LoginToAccount(self.frame_2))
        self.frame_list.append(Registration(self.frame_2))
        self.frame_list[1].forget()

        self.switch_win = SwitchWin(self)
        self.switch_win.login_to_account['command'] = self.switch_frame
        self.switch_win.registration['command'] = self.switch_frame

    def switch_frame(self):
        value_radio_button = self.switch_win.get_value_rb()

        if value_radio_button:
            self.frame_list[1].forget()
            self.frame_list[0].pack(padx=2, pady=2, fill=BOTH, expand=True)
        else:
            self.frame_list[0].forget()
            self.frame_list[1].pack(padx=2, pady=2, fill=BOTH, expand=True)


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Hello world!')
        self.geometry('300x400')
        view = View(self)


if __name__ == '__main__':
    app = App()
    app.mainloop()
