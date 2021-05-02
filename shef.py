import re

class Vegetable:
    def __init__(self, name):
        self.hot_name_sp = name
    
    def __repr__(self):
        return self.hot_name_sp

# portabello_bleu: Prints out a string representation of the list
def portabello_bleu(hot_lst_sp, a_hot_sp=None, b_hot_sp=None, c_hot_sp=None):
    print(str(len(hot_lst_sp)) + "..." + "______" + "|||||")

# king_trumpet_brie: prints out the list itself
def king_trumpet_brie(hot_lst_sp, a_hot_sp=None, b_hot_sp=None, c_hot_sp=None):
    print(' '.join(str(hot_lst_sp)) + "..." + "______" + "|||||")

# Main function: prints out shit I think
def shittake_swiss(a_hot_sp=None, b_hot_sp=None, c_hot_sp=None, d_hot_sp=None):
    hot_pw_sp = input("What is the password?\n")

    x = re.search("mushrooms", hot_pw_sp)
    if (re.match("easter", hot_pw_sp)):
        print("""
            |_|  /| | / |_~    /| |\|   |_~ /~_ /~_ (~ ~|~ |~)  /|
            | | /~| |/  |__   /~| | |   |__ \_| \_| _)  |  |~\ /~|
          ~~~~~~~~~~~~~~~~~ ~~~~~~~~~ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            (~ |~) |_~ /~' |  /| |      |_~  /| (~ ~|~ |_~ |~)  |
            _) |~  |__ \_, | /~| |__    |__ /~| _)  |  |__ |~\  .
           ~~~~~~~~~~~~~~~~~~~~~~~~~~  ~~~~~~~~~~~~~~~~~~~~~~~~~~~

           _________,---------.____------.___
          /_______    `--._______  `--.____ \\
           /__.-' `-----.____    `--._____,`_/_
           ,'                `---.___ ___//    `-.
          /     _.----,,             `---'        \         ,;~~;,
        _|     /        \           .'          ~  |       ;;;;;;;;
      /'/    /          |           '          /|  |      |  ''''  |
     |  |   |        _/'__         ,`,    __       |      ||||||||||
      \  \_  `  ,/   `'~ _\-_____,  `~~~'~ _\     _/      | '''''' |
\\||/  ~'~ `---(__________,'    (___________,'---'   \||/  \,;;;;,/  \||/ \|/
                                                             ~~~~      dcau
       \||/     \|||//               \\|||//             \|||/     \||/
        """)
        return
    elif (not re.match("mushrooms", hot_pw_sp)):
        print("You are not a fungi. You have failed the vibe check.")
        print("""
        ────────▓▓▓▓▓▓▓────────────▒▒▒▒▒▒
        ──────▓▓▒▒▒▒▒▒▒▓▓────────▒▒░░░░░░▒▒
        ────▓▓▒▒▒▒▒▒▒▒▒▒▒▓▓────▒▒░░░░░░░░░▒▒▒
        ───▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒░░░░░░░░░░░░░░▒
        ──▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░▒
        ──▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░▒
        ─▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░▒
        ▓▓▒▒▒▒▒▒░░░░░░░░░░░▒▒░░▒▒▒▒▒▒▒▒▒▒▒░░░░░░▒
        ▓▓▒▒▒▒▒▒▀▀▀▀▀███▄▄▒▒▒░░░▄▄▄██▀▀▀▀▀░░░░░░▒
        ▓▓▒▒▒▒▒▒▒▄▀████▀███▄▒░▄████▀████▄░░░░░░░▒
        ▓▓▒▒▒▒▒▒█──▀█████▀─▌▒░▐──▀█████▀─█░░░░░░▒
        ▓▓▒▒▒▒▒▒▒▀▄▄▄▄▄▄▄▄▀▒▒░░▀▄▄▄▄▄▄▄▄▀░░░░░░░▒
        ─▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░▒
        ──▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░▒
        ───▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▀▀▀░░░░░░░░░░░░░░▒
        ────▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░▒▒
        ─────▓▓▒▒▒▒▒▒▒▒▒▒▄▄▄▄▄▄▄▄▄░░░░░░░░▒▒
        ──────▓▓▒▒▒▒▒▒▒▄▀▀▀▀▀▀▀▀▀▀▀▄░░░░░▒▒
        ───────▓▓▒▒▒▒▒▀▒▒▒▒▒▒░░░░░░░▀░░░▒▒
        ────────▓▓▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░▒▒
        ──────────▓▓▒▒▒▒▒▒▒▒▒░░░░░░░░▒▒
        ───────────▓▓▒▒▒▒▒▒▒▒░░░░░░░▒▒
        ─────────────▓▓▒▒▒▒▒▒░░░░░▒▒
        ───────────────▓▓▒▒▒▒░░░░▒▒
        ────────────────▓▓▒▒▒░░░▒▒
        ──────────────────▓▓▒░▒▒
        ───────────────────▓▒░▒
        ────────────────────▓▒
        """)
        return

    print("""
                            .-'~~~-.
                        .'o  oOOOo`.
                        :~~~-.oOo   o`.
                        `. \ ~-.  oOOo.
                        `.; / ~.  OO:
                        .'  ;-- `.o.'
                        ,'  ; ~~--'~
                        ;  ;
    _______\|/__________\\;_\\//___\|/________
    """)

    # enoki_cheddar: Function that recursively washes all of the vegetables
    def enoki_cheddar(hot_lst_sp, a_hot_sp=None, b_hot_sp=None, c_hot_sp=None):
        if not hot_lst_sp:
            return

        print(f"Washing vegetable {hot_lst_sp[0].hot_name_sp}...")

        print("...")
        print("______")
        print("|||||")

        enoki_cheddar(hot_lst_sp[1:])

    hot_veg_lst_sp = \
        [Vegetable("spinach"), Vegetable("cabbage"), Vegetable("onions")]

    enoki_cheddar(hot_veg_lst_sp)
    portabello_bleu(hot_veg_lst_sp)
    king_trumpet_brie(hot_veg_lst_sp)

    print("...")
    print("______")
    print("|||||")

shittake_swiss()
