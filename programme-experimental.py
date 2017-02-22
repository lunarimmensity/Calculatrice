#programme experimental : la console sera ouverte lors du lancement du programme


from tkinter import *
import tkinter as tk
import turtle


# fonction pour boutons
# ATTETION ONT BESOIN DU PROGRAMME PRINCIPAL
def mode_calc():
    l_mode["text"] = "Calulatrice"


def mode_graph():
    l_mode["text"] = "Grapheur"


def key_off():
    calc.destroy()


def key_ac():
    l_expression["text"] = ""


def key_pi():
    l_expression["text"] += "π"


def key_virg():
    l_expression["text"] += ","


def key_plus():
    l_expression["text"] += "+"


def key_moins():
    l_expression["text"] += "-"


def key_fois():
    l_expression["text"] += "×"


def key_div():
    l_expression["text"] += "÷"


def key_pow():
    l_expression["text"] += "^("


def key_racine():
    l_expression["text"] += "√("


def key_exp():
    l_expression["text"] += "exp("


def key_ln():
    l_expression["text"] += "ln("


def key_log():
    l_expression["text"] += "log("


def key_e():
    l_expression["text"] += "×10^("


def key_cos():
    l_expression["text"] += "cos("


def key_sin():
    l_expression["text"] += "sin("


def key_tan():
    l_expression["text"] += "tan("


def key_par_ouvr():
    l_expression["text"] += "("


def key_par_ferm():
    l_expression["text"] += ")"


def key_egal():
    l_expression["text"] += "="


def key_0():
    l_expression["text"] += "0"


def key_1():
    l_expression["text"] += "1"


def key_2():
    l_expression["text"] += "2"


def key_3():
    l_expression["text"] += "3"


def key_4():
    l_expression["text"] += "4"


def key_5():
    l_expression["text"] += "5"


def key_6():
    l_expression["text"] += "6"


def key_7():
    l_expression["text"] += "7"


def key_8():
    l_expression["text"] += "8"


def key_9():
    l_expression["text"] += "9"


def key_x():
    l_expression["text"] += "x"


def key_a():
    l_expression["text"] += "a"

#déclaration noms de boutons et leurs commandes
boutons = [
    [["calc", mode_calc], ["graph", mode_graph], ["", ], ["", ], ["OFF", key_off]],
    [["x", key_x], ["a", key_a], ["", ], ["", ], ["", ]],
    [["sin", key_sin], ["cos", key_cos], ["tan", key_tan], ["(", key_par_ouvr], [")", key_par_ferm]],
    [["a²", key_pow], ["√", key_racine], ["exp", key_exp], ["ln", key_ln], ["log", key_log]],
    [["7", key_7], ["8", key_8], ["9", key_9], ["", ], ["AC", ]],
    [["4", key_4], ["5", key_5], ["6", key_6], ["+", key_plus], ["×", key_fois]],
    [["1", key_1], ["2", key_2], ["3", key_3], ["-", key_moins], ["÷", key_div]],
    [["0", key_0], [",", key_virg], ["E", key_e], ["π", key_pi], ["=", key_egal]]
]

# déclaration de la fenêtre
calc = tk.Tk()
calc.title("Calcultrice")

# déclaration des frames
f_commande = tk.Frame(calc, relief="ridge")
f_clavier = tk.Frame(f_commande, relief="ridge")
f_turtle = tk.Frame(calc, relief="ridge", bg="black")

# affichage des frames
f_commande.pack(side="left")
f_clavier.pack(side="bottom", padx=5, pady=5)
f_turtle.pack(side="right", padx=5, pady=5)

# déclaration du label mode
mode = "Calculatrice"
l_mode = Label(f_turtle, text=mode, bg="black", fg="white")
l_mode.pack()

# déclaratior et affichage de l'entrée
lf_expression = LabelFrame(f_commande, text="entrée")
lf_expression.pack()
l_expression = Label(lf_expression, text="")
l_expression.pack()

# déclaration et affichage de la tortue
fenTortue = turtle.Canvas(f_turtle, height=500, width=800)  # taille fenTortue
fenTortue.pack(padx=10, pady=10)
screen = turtle.TurtleScreen(fenTortue)
screen.screensize(200, 200)
t = turtle.RawTurtle(screen)
t.ht()

#affichage des boutons
for i in range(len(boutons)):
    for j in range(len(boutons[i])):
        try:
            Button(f_clavier, text=boutons[i][j][0], relief="flat", command=boutons[i][j][1]).grid(row=i, column=j,
                                                                                                   padx=2,
                                                                                                   pady=2)  # declaration des boutons(penser a leur assigen une fctn)
        except IndexError:
            Button(f_clavier, text=boutons[i][j][0], relief="flat").grid(row=i, column=j, padx=2, pady=2)
#bloque la taille min de la fenêtre à la taille actuelle
calc.minsize(calc.winfo_width(), calc.winfo_height())
#C'est parti!
calc.mainloop()

