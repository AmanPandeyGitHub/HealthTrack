from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from database import FullDatabase
from styles import Styles
import re


class SingUp:

    #! ******************************** Properties *******************************

    def __init__(self, master):

        # ******************************** Main Window *******************************

        self.master = master
        self.master.title('HealthTrack')
        self.master.resizable(False, False)
        self.master.geometry("950x600")

        # Main Background Image

        self.background_image = PhotoImage(file='assets/background_main.png')
        self.background_image = self.background_image.subsample(4, 4)
        self.background_label = ttk.Label(
            self.master, image=self.background_image, borderwidth=0)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # ******************************** Define Styles *******************************

        self.s = Styles()

        # ******************************** LogIn Frame *******************************

        # *Login Frame Construction
        self.frame_login = ttk.Frame(
            self.master, relief=FLAT, style='Maron.TFrame')
        self.frame_login.config(padding=(40, 10))
        self.frame_login.place(x=590, y=0)

        # Logo Display in the Login Section
        self.login_logo = PhotoImage(file='assets/logo_main-01.png')
        self.login_logo = self.login_logo.subsample(3, 3)
        self.top_logo = ttk.Label(
            self.frame_login, image=self.login_logo, style='BlackOnMaron.TLabel')

        # Name Label
        self.name_label = ttk.Label(
            self.frame_login, text='Name:', style='BlackOnMaron.TLabel')

        # Entry for Name
        self.entry_name = ttk.Entry(
            self.frame_login, width=40, font=('Arial', 10))

        # Last Name Label
        self.lastname_label = ttk.Label(
            self.frame_login, text='Last Name:', style='BlackOnMaron.TLabel')

        # Entry for Last Name
        self.entry_lastname = ttk.Entry(
            self.frame_login, width=40, font=('Arial', 10))

        # Username Label
        self.username_label = ttk.Label(
            self.frame_login, text='Email:', style='BlackOnMaron.TLabel')

        # Entry for Username
        self.entry_username = ttk.Entry(
            self.frame_login, width=40, font=('Arial', 10))

        # Password Label
        self.password_label = ttk.Label(
            self.frame_login, text='Password:', style='BlackOnMaron.TLabel')

        # Entry for Password
        self.entry_password = ttk.Entry(
            self.frame_login, width=40, font=('Arial', 10), show='*')

        # Button Sign Up
        self.login_button = ttk.Button(self.frame_login,
                                       text='Sign Up!',
                                       style='PinkButton.TButton',
                                       command=self.submit)

        # Geometrtic Distribution
        self.top_logo.grid(row=0, column=0, columnspan=3)
        self.name_label.grid(row=1, column=0, columnspan=3, sticky='w')
        self.entry_name.grid(row=2, column=0, columnspan=3, ipady=8)
        self.lastname_label.grid(row=3, column=0, columnspan=3, sticky='w')
        self.entry_lastname.grid(row=4, column=0, columnspan=3, ipady=8)
        self.username_label.grid(row=5, column=0, columnspan=3, sticky='w')
        self.entry_username.grid(row=6, column=0, columnspan=3, ipady=8)
        self.password_label.grid(row=7, column=0, columnspan=3, sticky='w')
        self.entry_password.grid(row=8, column=0, columnspan=3, ipady=8)
        self.login_button.grid(row=15, column=0, columnspan=3, ipady=3,
                               pady=20, sticky='nsew')

        # ******************************** Footer Frame *******************************

        # *Footer Frame Construction
        self.frame_footer = ttk.Frame(self.master, relief=FLAT, style='TFrame')
        self.frame_footer.config(padding=(0, 15))
        self.frame_footer.pack(fill=X, side=BOTTOM)

        # Button Sign Up
        ttk.Button(self.frame_footer, text='Back to LogIn!', style='PinkButton.TButton',
                   command=self.load_Login).grid(row=0, column=2)

        # Copyright

        # Error Message
        self.error_label = ttk.Label(self.frame_footer,
                                     text='Login to see your profile!',
                                     style='BoldTextOnWhite.TLabel')
        self.error_label.grid(row=0, column=1, padx=350)

        # ******************************** Actions *******************************

    #! ******************************** Methods *******************************

    def load_Login(self):
        ''' This method return the user to the LogIn portal'''

        from main import Welcome
        self.frame_login.destroy()
        self.frame_footer.destroy()
        self.background_label.destroy()

        # * LOAD NEW CLASS (SIGNUP) TO ROOT
        self.another = Welcome(self.master)

    def submit(self):
        '''This function registers a new user. All critirias must be met.'''

        # Get all values from form
        self.name = self.entry_name.get()
        self.lastname = self.entry_lastname.get()
        self.username = self.entry_username.get()
        self.password = self.entry_password.get()

        # Set special values
        calendar_map = {'Jan': 1, 'Feb': 2, 'Mar': 3,
                        'Apr': 4, 'May': 5, 'Jun': 6,
                        'Jul': 7, 'Aug': 8, 'Sep': 9,
                        'Oct': 10, 'Nov': 11, 'Dec': 12}

        self.user_fullname = self.name + ' ' + self.lastname

        # Set dicionarties
        user_info = {
            "username": self.username,
            "name": self.name,
            "lastname": self.lastname,
            "fullname": self.user_fullname,
            
            "work_habits": [[1, "Drink Water"], [5, "Stand Up"]],

            "work_habits_data": [],

            "user_habits": [

                ["Drink Water", 8.0, [
                    "Monday", "Tuesday", "Wednesday", "Thursday",
                    "Friday", "Saturday", "Sunday"], "all_time", 0],

                ["Exericise", 1.0, [
                 "Monday", "Tuesday", "Wednesday", "Thursday",
                 "Friday", "Saturday", "Sunday"], "morning", 0]

            ],
            "user_habits_data": [],
            "user_habits_streak": [],
            "password": self.password
        }

        user_credentials = {
            "username": self.username,
            "password": self.password,
            "name": self.name,
            "lastname": self.lastname,
        }

        valid_submission = True

        # Check for empty values
        for k, v in user_info.items():
            if v == '':
                messagebox.showinfo(title='Error',
                                    message='Error: Please fill ALL fields',
                                    icon='warning')

                self.error_label.config(style='Error.TLabel',
                                        text="Error: Please fill ALL fields.")
                valid_submission = False
                break

        # Check for valid email format
        if valid_submission == True:
            if not re.match(r"[^@\s]+@[^@\s]+\.[a-zA-Z0-9]+$", self.username):
                messagebox.showinfo(title='Error',
                                    message='Error: Please enter a valid email.',
                                    icon='warning')

                self.error_label.config(style='Error.TLabel',
                                        text="Error: Please enter a valid email!.")
                valid_submission = False

        # Check if email exists already
        if valid_submission == True:

            # Load Databases
            self.full_database = FullDatabase()
            credentials = self.full_database.load_credentials()
            user = self.full_database.load_users_info()

            for i, v in enumerate(credentials):
                if credentials[i]['username'] == self.username:

                    messagebox.showinfo(title='Error',
                                        message='Error: Email Exists Already.',
                                        icon='warning')

                    self.error_label.config(style='Error.TLabel',
                                            text="Error: Please enter a NEW email!.")
                    valid_submission = False

        # Proceed with signin up process
        if valid_submission == True:

            # Delete password from USER_INFO dictionary
            del user_info['password']

            credentials.append(user_credentials)
            user.append(user_info)

            # Update DataBase
            self.full_database.update_database(credentials, user)

            from habits import Habits
            self.frame_login.destroy()
            self.frame_footer.destroy()
            self.background_label.destroy()

            # * LOAD NEW CLASS (SIGNUP) TO ROOT
            self.another = Habits(self.master, self.username)
