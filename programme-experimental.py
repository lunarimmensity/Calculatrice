#programme experimental : la console sera ouverte lors du lancement du programme


# -*- coding:UTF-8 -*-

import time
import tkinter as tk
import turtle
from tkinter import *
import math
import R


# fonction pour boutons
# ATTENTION ONT BESOIN DU PROGRAMME PRINCIPAL


def mode_calc():
    t.clear()
    l_mode["text"] = "Calculatrice"
    R.Dyna = False


def mode_graph():
    t.clear()
    l_mode["text"] = "Grapheur"
    R.Dyna = False


def mode_dyna():
    t.clear()
    l_mode["text"] = "Dynamique"
    R.Dyna = True


def key_off():
    R.Dyna = False
    calc.destroy()


def key_ac():
    l_expression["text"] = ""
    R.Dyna = False
    t.clear()


def key_arrondi():
    print("Arrondi de " + l_expression["text"] + " …")


def key_effacer():
    chaine = ""
    for i in range(len(l_expression["text"]) - 1):
        chaine += l_expression["text"][i]
    l_expression["text"] = chaine


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


def key_carre():
    l_expression["text"] += "²"


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


def key_acos():
    l_expression["text"] += "cos⁻¹("


def key_sin():
    l_expression["text"] += "sin("


def key_asin():
    l_expression["text"] += "sin⁻¹("


def key_tan():
    l_expression["text"] += "tan("


def key_atan():
    l_expression["text"] += "tan⁻¹("


def key_parenthese_ouvr():
    l_expression["text"] += "("


def key_parenthese_ferm():
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


def test():
    var = -25
    print(var)
    print(xcoord_rep_t(xcoord_t_rep(var)))
    print(xcoord_t_rep(xcoord_rep_t(var)))


def executer():
    if l_mode["text"] == "Calculatrice":
        t.clear()
        clearT()
        t.up()
        t.goto(0, 0)
        t.write(l_expression["text"])
    elif l_mode["text"] == "Grapheur":
        tracer_graphe()
    elif l_mode["text"] == "Dynamique":
        while R.Dyna:
            a = R.aMin
            while a <= R.aMax and R.Dyna:
                tracer_graphe_d(a)
                time.sleep(R.pause)
                a += R.pas
    else:
        print("erreur mode")


# fen de param ds menu
def param_repere():
    def ok():
        R.xMin = float(xMin.get())
        R.xMax = float(xMax.get())
        R.yMin = float(yMin.get())
        R.yMax = float(yMax.get())
        R.xPas = float(xPas.get())
        R.yPas = float(yPas.get())
        R.actualiser()
        fen_repere.destroy()

    fen_repere = tk.Toplevel(calc)
    fen_repere.title("repère")
    l_xMin = tk.Label(fen_repere, text="x min")
    l_xMax = tk.Label(fen_repere, text="x max")
    l_yMin = tk.Label(fen_repere, text="y min")
    l_yMax = tk.Label(fen_repere, text="y max")
    l_xpas = tk.Label(fen_repere, text="pas x")
    l_ypas = tk.Label(fen_repere, text="pas y")

    xMin = StringVar()
    xMin.set(str(R.xMin))
    e_xMin = Entry(fen_repere, textvariable=xMin)

    xMax = StringVar()
    xMax.set(str(R.xMax))
    e_xMax = Entry(fen_repere, textvariable=xMax)

    yMin = StringVar()
    yMin.set(str(R.yMin))
    e_yMin = Entry(fen_repere, textvariable=yMin)

    yMax = StringVar()
    yMax.set(str(R.yMax))
    e_yMax = Entry(fen_repere, textvariable=yMax)

    xPas = StringVar()
    xPas.set(str(R.xPas))
    e_xPas = Entry(fen_repere, textvariable=xPas)

    yPas = StringVar()
    yPas.set(str(R.yPas))
    e_yPas = Entry(fen_repere, textvariable=yPas)

    l_xMin.grid(column=1, row=1, padx=2, pady=2)
    e_xMin.grid(column=1, row=2, padx=2, pady=2)
    l_yMin.grid(column=1, row=3, padx=2, pady=2)
    e_yMin.grid(column=1, row=4, padx=2, pady=2)
    l_xMax.grid(column=2, row=1, padx=2, pady=2)
    e_xMax.grid(column=2, row=2, padx=2, pady=2)
    l_yMax.grid(column=2, row=3, padx=2, pady=2)
    e_yMax.grid(column=2, row=4, padx=2, pady=2)
    l_xpas.grid(column=3, row=1, padx=2, pady=2)
    e_xPas.grid(column=3, row=2, padx=2, pady=2)
    l_ypas.grid(column=3, row=3, padx=2, pady=2)
    e_yPas.grid(column=3, row=4, padx=2, pady=2)
    tk.Button(fen_repere, text="ok", command=ok).grid(row=5, column=2, padx=2, pady=2)


def param_dyna():
    def ok():
        R.aMin = float(amin.get())
        R.aMax = float(amax.get())
        R.pas = float(pas.get())
        R.pause = float(pause.get())
        fen_dyna.destroy()

    fen_dyna = tk.Toplevel(calc)
    fen_dyna.title("paramètres de la fenêtre dynamique")

    l_aMin = tk.Label(fen_dyna, text="a min")
    l_aMax = tk.Label(fen_dyna, text="a max")
    l_pas = tk.Label(fen_dyna, text="pas")
    l_pause = tk.Label(fen_dyna, text="pause")

    amin = StringVar()
    amin.set(str(R.aMin))
    amax = StringVar()
    amax.set(str(R.aMax))
    pas = StringVar()
    pas.set(str(R.pas))
    pause = StringVar()
    pause.set(R.pause)

    e_aMin = tk.Entry(fen_dyna, textvariable=amin)
    e_aMax = tk.Entry(fen_dyna, textvariable=amax)
    e_pas = tk.Entry(fen_dyna, textvariable=pas)
    e_pause = tk.Entry(fen_dyna, textvariable=pause)

    l_aMin.grid(column=1, row=1)
    e_aMin.grid(column=1, row=2)
    l_aMax.grid(column=2, row=1)
    e_aMax.grid(column=2, row=2)
    l_pas.grid(column=1, row=3)
    e_pas.grid(column=1, row=4)
    l_pause.grid(column=2, row=3)
    e_pause.grid(column=2, row=4)
    Button(fen_dyna, text="ok", command=ok).grid(column=1, row=5)


def parm_pen():
    def ok():
        R.couleur = R.set_couleur(rouge.get(), vert.get(), bleu.get())
        R.epaisseur = float(epaiseur.get())
        R.précision = float(precision.get())
        fen_pen.destroy()

    def voir():
        b_voir["bg"] = R.set_couleur(rouge.get(), vert.get(), bleu.get())

    fen_pen = tk.Toplevel(calc)
    fen_pen.title("paramètres du crayon")

    f_couleur = tk.Frame(fen_pen)
    f_reste = tk.Frame(fen_pen)
    f_couleur.pack(side="left")
    f_reste.pack(side="right")

    l_epaisseur = tk.Label(f_reste, text="épaisseur")
    l_couleur = tk.Label(f_couleur, text="couleur")
    l_precision = tk.Label(f_reste, text="l_precision")

    epaiseur = StringVar()
    epaiseur.set(str(R.epaisseur))
    precision = StringVar()
    precision.set(str(R.précision))

    rouge = IntVar()
    rouge.set(R.rouge)
    vert = IntVar()
    vert.set(R.vert)
    bleu = IntVar()
    bleu.set(R.bleu)

    e_epaisseur = tk.Entry(f_reste, textvariable=epaiseur)
    e_precision = tk.Entry(f_reste, textvariable=precision)

    scl_rouge = tk.Scale(f_couleur, variable=rouge, from_=0, to=255, label="rouge", orient="horizontal")
    scl_vert = tk.Scale(f_couleur, variable=vert, from_=0, to=255, label="vert", orient="horizontal")
    scl_bleu = tk.Scale(f_couleur, variable=bleu, from_=0, to=255, label="bleu", orient="horizontal")
    b_voir = Button(f_couleur, text="prévisualiser", command=voir)

    l_couleur.pack()
    scl_rouge.pack()
    scl_vert.pack()
    scl_bleu.pack()
    b_voir.pack()
    voir()

    l_epaisseur.pack()
    e_epaisseur.pack()
    l_precision.pack()
    e_precision.pack()
    tk.Button(fen_pen, text="OK", command=ok).pack(side="bottom")


def get_equation():
    return l_expression["text"]


# fonctions de calcul
calculer = lambda x: math.expm1(x)
calculer_d = lambda x, a: a / x


# fonctions de coordonées

def xcoord_t_rep(x):
    # retuorne les abs de la fen à partir de celles du repère
    try:
        return (R.xUtilFen / R.xDiff) * (x - R.xMin) - R.xUtilFen // 2
    except ZeroDivisionError:
        tk.messagebox.showerror("erreur ", "les valeurs entrées e x doivent être differntes")


def ycoord_t_rep(y):
    # retuorne les ordonnées de la fen à partir de celles du repère
    try:
        return (R.yUtilFen / R.yDiff) * (y - R.yMin) - R.yUtilFen // 2
    except ZeroDivisionError:
        tk.messagebox.showerror("erreur ", "les valeurs entrées e y doivent être differntes")


def coord_t_rep(x, y):
    # retuorne les cocrdonnées de la fen à partir de celles du repère

    return xcoord_t_rep(x), ycoord_t_rep(y)


def xcoord_rep_t(x):
    try:
        return -(R.xMin - (R.xDiff / R.xUtilFen) * (-R.xUtilFen // 2 + x))
    except ZeroDivisionError:
        tk.messagebox.showerror("erreur ", "les valeurs entrées e y doivent être differntes")


def ycoord_rep_t(y):
    try:
        return -(R.yMin - (R.yDiff / R.yUtilFen) * (-R.yUtilFen // 2 + y))
    except ZeroDivisionError:
        tk.messagebox.showerror("erreur ", "les valeurs entrées e y doivent être differntes")


def coord_rep_t(x, y):
    return xcoord_rep_t(x), ycoord_rep_t()


def clearT():
    t.clear()
    t.pencolor("black")
    t.width(1)
    t.seth(0)
    t._tracer(20, 25)
    t.ht()
    t.fillcolor("black")


# tracer graphiques

def tracer_axes():
    def axex():
        a = R.xMin
        while t.xcor() < R.xUtilFen // 2:
            t.setx(xcoord_t_rep(a))
            if a % R.xPas == 0:
                t.right(90)
                t.fd(2)
                if a != 0:
                    t.up()
                    t.fd(20)
                    t.write(a, align='center')
                    t.bk(20)
                    t.pd()
                t.bk(4)
                t.fd(2)
                t.left(90)
            a += 1
        # flèche bout axe
        t.fd(3)
        t.begin_fill()
        t.left(90)
        t.fd(4)
        t.right(135)
        t.fd(4 * 2 ** 0.5)
        t.right(90)
        t.fd(4 * 2 ** 0.5)
        t.right(135)
        t.fd(4)
        t.end_fill()
        t.up()

    def axey():
        a = R.yMin
        while t.ycor() < R.yUtilFen // 2:
            t.sety(ycoord_t_rep(a))
            if a % R.yPas == 0:
                t.right(90)
                t.fd(2)
                if a != 0:
                    t.up()
                    t.fd(10)
                    t.write(a, align='center')
                    t.bk(10)
                    t.pd()
                t.bk(4)
                t.fd(2)
                t.left(90)
            a += 1
        # flèche bout axe
        t.fd(3)
        t.begin_fill()
        t.left(90)
        t.fd(4)
        t.right(135)
        t.fd(4 * 2 ** 0.5)
        t.right(90)
        t.fd(4 * 2 ** 0.5)
        t.right(135)
        t.fd(4)
        t.end_fill()
        t.up()

    clearT()
    t.up()

    # tracer axe des x
    if R.yMin > 0:
        t.goto(coord_t_rep(R.xMin, R.yMin))
        t.down()
        axex()
    elif R.yMax < 0:
        t.goto(coord_t_rep(R.xMin, R.yMax))
        t.down()
        axex()
    else:
        t.goto(coord_t_rep(R.xMin, 0))
        t.down()
        axex()

    # tracer axe des y
    if R.xMin > 0:
        t.goto(coord_t_rep(R.xMin, R.yMin))
        t.down()
        axey()
    elif R.xMax < 0:
        t.goto(coord_t_rep(R.xMax, R.yMin))
        t.down()
        axey()
    else:
        t.goto(coord_t_rep(0, R.yMin))
        t.down()
        axey()
    t.up()


def tracer_graphe():
    clearT()

    tracer_axes()

    t.color(R.couleur)
    t.width(R.epaisseur)
    t.up()
    g = R.xMin
    while g <= R.xMax:

        try:
            t.goto(coord_t_rep(g, calculer(g)))
            t.pd()
        except ValueError:
            t.up()

        g += R.précision


def tracer_graphe_d(a):
    clearT()

    tracer_axes()

    t.color(R.couleur)
    t.width(R.epaisseur)
    t.up()
    g = R.xMin
    while g <= R.xMax:

        try:
            t.goto(coord_t_rep(g, calculer_d(g, a)))
            t.pd()
        except ValueError:
            t.up()

        g += R.précision
    t.up()
    t.goto(R.xUtilFen // 2 - 50, -R.yUtilFen // 2)
    t.write("a= " + str(a))


boutons = [
    [["(", key_parenthese_ouvr], [")", key_parenthese_ferm], ["log", key_log], ["pow", key_pow], ["OFF", key_off]],
    [["x", key_x], ["a", key_a], ["=", key_egal], ["ln", key_ln], ["TEST", test]],
    [["sin⁻¹", key_acos], ["cos⁻¹", key_asin], ["tan⁻¹", key_atan], ["", ], ["arnd", key_arrondi]],
    [["sin", key_sin], ["cos", key_cos], ["tan", key_tan], ["", ], ["", ]],
    [["a²", key_carre], ["√", key_racine], ["exp", key_exp], ["", ], ["", ]],
    [["7", key_7], ["8", key_8], ["9", key_9], ["⌫", key_effacer], ["AC", key_ac]],
    [["4", key_4], ["5", key_5], ["6", key_6], ["+", key_plus], ["×", key_fois]],
    [["1", key_1], ["2", key_2], ["3", key_3], ["-", key_moins], ["÷", key_div]],
    [["0", key_0], [",", key_virg], ["E", key_e], ["π", key_pi], ["⏎", executer]]
]


# déclaration de la fenêtre #


# déclaration de la fenêtre
calc = tk.Tk()
calc.title("Calcultrice")
calc.configure(bg="white")

# déclaration des frames
f_commande = tk.Frame(calc, relief="ridge", bg="white")
f_clavier = tk.Frame(f_commande, relief="ridge", bg="white")
f_turtle = tk.Frame(calc, relief="ridge", bg="grey")

# affichage des frames
f_commande.pack(side="left")
f_clavier.pack(side="bottom", padx=5, pady=5)
f_turtle.pack(side="right", padx=5, pady=5)

# déclaration et affichage du label mode
mode = "Calculatrice"
l_mode = Label(f_turtle, text=mode, bg="grey", fg="white")
l_mode.pack()

# déclaratior et affichage de l'entrée et du label entée
lf_expression = LabelFrame(f_commande, text="entrée", bg="white")
lf_expression.pack(padx=2, pady=2)
l_expression = Label(lf_expression, text="", bg="white")
l_expression.pack(padx=2, pady=2)

# déclaration et affichage de la tortue
fenTortue = turtle.Canvas(f_turtle, height=R.yFen, width=R.xFen)  # taille fenTortue
fenTortue.pack(padx=10, pady=10)
screen = turtle.TurtleScreen(fenTortue)
t = turtle.RawTurtle(screen)
t.ht()

# affichage des boutons
for i in range(len(boutons)):
    for j in range(len(boutons[i])):
        try:
            Button(f_clavier, text=boutons[i][j][0], relief="flat", command=boutons[i][j][1], height=1, width=4).grid(
                row=i, column=j,
                padx=2,
                pady=2)  # declaration des boutons(penser a leur donner une fctn)
        except IndexError:
            Button(f_clavier, text=boutons[i][j][0], relief="flat", height=1, width=4).grid(row=i, column=j, padx=2,
                                                                                            pady=2)

# barre de menu
menu = tk.Menu(calc)

mode = tk.Menu(menu, tearoff=0)
mode.add_command(label="Calculatrice", command=mode_calc)
mode.add_command(label="Grapheur", command=mode_graph)
mode.add_command(label="Grapheur Dynamique", command=mode_dyna)
menu.add_cascade(label='Mode', menu=mode)

parametres = tk.Menu(menu, tearoff=0)
parametres.add_command(label="Fenêtre graphique", command=param_repere)
parametres.add_command(label="Dynamique", command=param_dyna)
parametres.add_command(label="Crayon", command=parm_pen)
parametres.add_separator()
parametres.add_command(label="adapter fenêtre")
menu.add_cascade(label="pamètres", menu=parametres)

calc.config(menu=menu)

# afichage de la fenetre
calc.minsize(calc.winfo_width(), calc.winfo_height())
calc.mainloop()


# Début fenêtre #

