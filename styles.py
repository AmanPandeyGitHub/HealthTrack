from tkinter import *
from tkinter import ttk
from platform import system


class Styles:

    def __init__(self):
            self.style = ttk.Style()
            self.style.theme_use('clam')

            # General frame styles
            self.style.configure('TFrame', background='white')
            self.style.configure('TLabel', background='white')
            self.style.configure('Yellow.TFrame', background='#c2d4ba')
            self.style.configure('Maron.TFrame', background='#e1edd5')
            self.style.configure('Pink.TFrame', background='#294a00')
            self.style.configure('Blue.TFrame', background='#e1edd5')

            # Welcome frame styless
            self.style.configure('Header.TLabel',
                                 foreground='#6d6e71',
                                 font=(('Century Gothic', 19, '')))

            self.style.configure('Sub.Header.TLabel',
                                 foreground='#6d6e71',
                                 font=(('Century Gothic', 12, '')))

            self.style.configure('GreenButton.TButton',
                                 foreground='white',
                                 background='#5ba600',
                                 highlightthickness='0',
                                 font=('Century Gothic', 8, 'bold'))

            self.style.map('GreenButton.TButton',
                           foreground=[('disabled', 'white'),
                                       ('active', 'black'),
                                       ('pressed', 'black')],
                           background=[('disabled', '#294a00'),
                                       ('pressed', '#fced1c'),
                                       ('active', '#fced1c')])
            
            self.style.configure('GreenButton2.TButton',
                                 foreground='white',
                                 background='#497d2d',
                                 highlightthickness='0',
                                 font=('Century Gothic', 8, 'bold'),
                                 relief=FLAT)

            self.style.map('GreenButton2.TButton',
                           foreground=[('disabled', 'white'),
                                       ('active', 'black'),
                                       ('pressed', 'black')],
                           background=[('disabled', '#294a00'),
                                       ('pressed', '#fced1c'),
                                       ('active', '#fced1c')])

            self.style.configure('BlueButton.TButton',
                                 foreground='white',
                                 background='#8ea3ae',
                                 highlightthickness='0',
                                 font=('Century Gothic', 8, 'bold'),
                                 relief=FLAT)

            self.style.map('BlueButton.TButton',
                           foreground=[('disabled', 'white'),
                                       ('pressed', 'white'),
                                       ('active', 'white')],
                           background=[('disabled', '#808184'),
                                       ('pressed', '#f37b75'),
                                       ('active', '#f37b75')])

            self.style.configure('PinkButton.TButton',
                                 foreground='white',
                                 background='#294a00',
                                 highlightthickness='0',
                                 font=('Century Gothic', 8, 'bold'))

            self.style.map('PinkButton.TButton',
                           foreground=[('disabled', 'white'),
                                       ('pressed', 'black'),
                                       ('active', 'black')],
                           background=[('disabled', '#294a00'),
                                       ('pressed', '#fced1c'),
                                       ('active', '#fced1c')],)

            self.style.configure('WhiteButton.TButton',
                                 foreground='white',
                                 background='white',
                                 highlightthickness='0',
                                 font=('Century Gothic', 8, 'bold'),
                                 relief=FLAT)

            self.style.map('WhiteButton.TButton',
                           foreground=[('disabled', 'white'),
                                       ('pressed', 'white'),
                                       ('active', 'white')],
                           background=[('disabled', 'white'),
                                       ('pressed', 'white'),
                                       ('active', 'white')])

            self.style.configure('YellowButton.TButton',
                                 foreground='black',
                                 background='#c2d4ba',
                                 highlightthickness='0',
                                 font=('Century Gothic', 8, 'bold'),
                                 relief=FLAT)

            self.style.map('YellowButton.TButton',
                           foreground=[('disabled', 'white'),
                                       ('pressed', 'white'),
                                       ('active', 'white')],
                           background=[('disabled', '#c2d4ba'),
                                       ('pressed', '#c2d4ba'),
                                       ('active', '#c2d4ba')])

            self.style.configure('YellowButton2.TButton',
                                 foreground='black',
                                 background='#c2d4ba',
                                 highlightthickness='0',
                                 font=('Century Gothic', 8, 'bold'),
                                 relief=RAISED)

            self.style.map('YellowButton2.TButton',
                           foreground=[('disabled', 'white'),
                                       ('pressed', 'white'),
                                       ('active', 'white')],
                           background=[('disabled', '#efefe1'),
                                       ('pressed', '#efefe1'),
                                       ('active', '#efefe1')])

            self.style.configure('WhiteOnPink.TLabel',
                                 foreground='white',
                                 background='#294a00',
                                 font=('Century Gothic', 10, 'bold'))

            self.style.configure('PinkOnYellow.TLabel',
                                 background='#c2d4ba',
                                 foreground='black',
                                 font=('Century Gothic', 9, 'bold'))

            self.style.configure('WhiteOnGreen.TLabel',
                                 background='#bbceb2',
                                 foreground='white',
                                 font=('Century Gothic', 11, 'bold'))

            self.style.configure('WhiteOnGreenSmall.TLabel',
                                 background='#bbceb2',
                                 foreground='white',
                                 font=('Century Gothic', 9, 'bold'))

            self.style.configure('Stopwatch.TLabel',
                                 background='#c2d4ba',
                                 foreground='#58595b',
                                 font=('Century Gothic', 28, 'bold'))

            self.style.configure('TextOnYellow.TLabel',
                                 background='#c2d4ba',
                                 foreground='#6d6e71',
                                 justify=CENTER,
                                 font=('Century Gothic', 9,))

            self.style.configure('BoldTextOnYellow.TLabel',
                                 background='#c2d4ba',
                                 foreground='#294a00',
                                 justify=CENTER,
                                 font=('Century Gothic', 9, 'bold'))

            self.style.configure('BoldTextOnWhite.TLabel',
                                 background='white',
                                 foreground='black',
                                 justify=LEFT,
                                 font=('Century Gothic', 9, 'bold'))

            self.style.configure('BoldTextOnGreen.TLabel',
                                 background='#bbceb2',
                                 foreground='#6d6e71',
                                 justify=LEFT,
                                 font=('Century Gothic', 9, 'bold'))

            self.style.configure('PinkOnWhiteLarge.TLabel',
                                 background='white',
                                 foreground='#3e8500',
                                 font=('Century Gothic', 30, 'bold'))

            self.style.configure('BlackOnWhite.TLabel',
                                 background='white',
                                 foreground='black',
                                 font=('Century Gothic', 8, 'bold'))

            self.style.configure('WhiteOnBlueLarge.TLabel',
                                 background='#e1edd5',
                                 foreground='#3e8500',
                                 font=('Century Gothic', 30, 'bold'))

            self.style.configure('WhiteOnBlue.TLabel',
                                 background='#e1edd5',
                                 foreground='black',
                                 font=('Century Gothic', 8, 'bold'))

            self.style.configure('PinkOnMaronLarge.TLabel',
                                 background='#e1edd5',
                                 foreground='#294a00',
                                 font=('Century Gothic', 30, 'bold'))

            self.style.configure('PinkOnMaronMedium.TLabel',
                                 background='#e1edd5',
                                 foreground='#294a00',
                                 font=('Century Gothic', 15, 'bold'))

            self.style.configure('BlackOnMaronMedium.TLabel',
                                 background='#e1edd5',
                                 foreground='black',
                                 font=('Century Gothic', 11, 'bold'))

            self.style.configure('BlackOnMaron.TLabel',
                                 foreground='black',
                                 background='#e1edd5')

            self.style.configure('TextOnWhite.TLabel',
                                 foreground='black',
                                 background='white')

            self.style.configure('PinkOnWhite.TLabel',
                                 background='white',
                                 font=(('Century Gothic', 9, 'bold')),
                                 foreground='#294a00')

            self.style.configure('PinkOnWhite.TLabel',
                                 background='white',
                                 foreground='#294a00',
                                 font=('Century Gothic', 10, 'bold'))

            self.style.configure('TCheckbutton',
                                 background='#c2d4ba',
                                 font=('Century Gothic', 8, 'bold'),
                                 foreground='#6d6e71')

            self.style.map('TCheckbutton',
                           foreground=[('disabled', 'white'),
                                       ('pressed', 'black'),
                                       ('active', 'black')],
                           background=[('disabled', '#f9f9f9'),
                                       ('pressed', '#c2d4ba'),
                                       ('active', '#c2d4ba')])

            self.style.configure('Pink.Horizontal.TProgressbar',
                                 background='#a0c90a', troughcolor='#295200')

            # Footer Style

            self.style.configure('FooterHabits.TLabel',
                                 background='#efefe1',
                                 foreground='#808184',
                                 font=('Century Gothic', 8, ''))
