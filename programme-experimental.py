# -*- coding:UTF-8 -*-

import time
import tkinter as tk
import turtle
from tkinter import *
import math
import R
import operations

expression = []


# fonction pour boutons
# ATTENTION ONT BESOIN DU PROGRAMME PRINCIPAL


def key_off():
    R.Dyna = False
    calc.destroy()


def key_ac():
    l_expression["text"] = ""
    expression.clear()
    R.Dyna = False
    t.clear()
    time.sleep(0.5)
    t.clear()


def key_plus():
    boite_de_dialogue2(operations.somme, 'Nombre 1:', 'Nombre 2:', 'Somme')


def key_moins():
    boite_de_dialogue2(operations.soustraction, 'Nombre 1:', 'Nombre 2:', 'Soustraction')


def key_fois():
    boite_de_dialogue2(operations.produit, 'Nombre 1:', 'Nombre 2:', 'Multiplication')


def key_div():
    boite_de_dialogue2(operations.division, 'Nombre 1:', 'Nombre 2:', 'Division')


def key_pow():
    boite_de_dialogue2(math.pow, 'Nombre', 'Exposant', 'Puissance')


def key_sqrt():
    boite_de_dialogue1(math.sqrt, 'Nombre', 'Racine')


def key_exp():
    boite_de_dialogue1(math.exp, 'Nombre', 'Exponentielle')


def key_ln():
    # TODO ajouter ln
    print('à ajouter')


def key_log():
    boite_de_dialogue2(math.log, "Nombre", "Base", "logarithme")


def key_e():
    expression.append("×")
    expression.append("10")
    expression.append("^")
    l_expression["text"] = str_equation(expression)


def key_cos():
    boite_de_dialogue1(math.cos, "Nombre", "cosinus")


def key_acos():
    boite_de_dialogue1(math.acos, "Nombre", "arc cosinus")


def key_sin():
    boite_de_dialogue1(math.sin, "Nombre", "sinus")


def key_asin():
    boite_de_dialogue1(math.asin, "Nombre", "arc sinus")


def key_tan():
    boite_de_dialogue1(math.tan, "Nombre", "tangente")


def key_atan():
    boite_de_dialogue1(math.atan, "Nombre", "arc tangente")


def test():
    print(expression)


def executer():
    if l_mode["text"] == "Calculatrice":
        t.clear()
        # clearT()
        # t.up()
        t.speed(1)
        t.st()
        t.pu()
        t.goto(0, 0)
        t.pd()
        t.goto(coords(R.xMax, R.yMax, R.xMin, R.xMax, -R.xFenMax, R.xFenMax, R.yMin, R.yMax, -R.yFenMax, R.yFenMax))
        t.goto(coords(R.xMax, R.yMin, R.xMin, R.xMax, -R.xFenMax, R.xFenMax, R.yMin, R.yMax, -R.yFenMax, R.yFenMax))
        t.goto(coords(R.xMin, R.yMin, R.xMin, R.xMax, -R.xFenMax, R.xFenMax, R.yMin, R.yMax, -R.yFenMax, R.yFenMax))
        t.goto(coords(R.xMin, R.yMax, R.xMin, R.xMax, -R.xFenMax, R.xFenMax, R.yMin, R.yMax, -R.yFenMax, R.yFenMax))
        t.goto(coords(R.xMax, R.yMax, R.xMin, R.xMax, -R.xFenMax, R.xFenMax, R.yMin, R.yMax, -R.yFenMax, R.yFenMax))

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


def boite_de_dialogue2(func, nb1, nb2, titre):
    def ok():
        if e_nb_1.get() == 'x' or e_nb_1.get() == 'a':
            a = e_nb_1.get()
        else:
            a = int(e_nb_1.get())

        if e_nb_2.get() == 'x' or e_nb_2.get() == 'a':
            b = e_nb_2.get()
        else:
            b = int(e_nb_2.get())

        sequence.append([func, a, b])
        print(sequence)
        dialogue.destroy()

    dialogue = tk.Toplevel(calc)
    dialogue.title(titre)
    tk.Label(dialogue, text=nb1).pack()
    e_nb_1 = tk.StringVar()
    tk.Entry(dialogue, textvariable=e_nb_1).pack()
    tk.Button(dialogue, text='résultat précédant').pack()

    tk.Label(dialogue, text=nb2).pack()
    e_nb_2 = tk.StringVar()
    tk.Entry(dialogue, textvariable=e_nb_2).pack()
    tk.Button(dialogue, text='résultat précédant').pack()
    tk.Button(dialogue, text="OK", command=ok).pack()
    dialogue.mainloop()


def boite_de_dialogue1(func, nb1, titre):
    def ok():
        try:
            a = int(e_nb_1.get())
        except ValueError:
            if e_nb_1.get() == 'x' or e_nb_1.get() == 'a':
                a = e_nb_1.get()
            else:
                raise ValueError

        sequence.append([func, a])
        print(sequence)
        dialogue.destroy()

    dialogue = tk.Toplevel(calc)
    dialogue.title(titre)
    tk.Label(dialogue, text=nb1).pack()
    e_nb_1 = tk.StringVar()
    tk.Entry(dialogue, textvariable=e_nb_1).pack()
    tk.Button(dialogue, text='résultat précédant').pack()
    tk.Button(dialogue, text="OK", command=ok).pack()
    dialogue.mainloop()


# param ds menu
def menu_repere():
    def ok():
        R.xMin = float(xMin.get())
        R.xMax = float(xMax.get())
        R.yMin = float(yMin.get())
        R.yMax = float(yMax.get())
        R.xStep = float(xPas.get())
        R.yStep = float(yPas.get())
        R.actualiser()
        fen_repere.destroy()

    # déclaration de la fenêtre
    fen_repere = tk.Toplevel(calc)
    fen_repere.title("repère")

    # déclaration des labels
    l_xMin = tk.Label(fen_repere, text="x min")
    l_xMax = tk.Label(fen_repere, text="x max")
    l_yMin = tk.Label(fen_repere, text="y min")
    l_yMax = tk.Label(fen_repere, text="y max")
    l_xpas = tk.Label(fen_repere, text="pas x")
    l_ypas = tk.Label(fen_repere, text="pas y")

    # déclaration des entrées et de leurs labels
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
    xPas.set(str(R.xStep))
    e_xPas = Entry(fen_repere, textvariable=xPas)

    yPas = StringVar()
    yPas.set(str(R.yStep))
    e_yPas = Entry(fen_repere, textvariable=yPas)

    # affichage
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


def menu_dyna():
    def ok():
        R.aMin = float(amin.get())
        R.aMax = float(amax.get())
        R.pas = float(pas.get())
        R.pause = float(pause.get())
        fen_dyna.destroy()

    # déclaration de la fenêtre
    fen_dyna = tk.Toplevel(calc)
    fen_dyna.title("paramètres de la fenêtre dynamique")

    # déclaration des labels
    l_aMin = tk.Label(fen_dyna, text="a min")
    l_aMax = tk.Label(fen_dyna, text="a max")
    l_pas = tk.Label(fen_dyna, text="pas")
    l_pause = tk.Label(fen_dyna, text="pause")

    # déclaration des variables des entrées
    amin = StringVar()
    amin.set(str(R.aMin))
    amax = StringVar()
    amax.set(str(R.aMax))
    pas = StringVar()
    pas.set(str(R.pas))
    pause = StringVar()
    pause.set(R.pause)

    # déclaration des entrées
    e_aMin = tk.Entry(fen_dyna, textvariable=amin)
    e_aMax = tk.Entry(fen_dyna, textvariable=amax)
    e_pas = tk.Entry(fen_dyna, textvariable=pas)
    e_pause = tk.Entry(fen_dyna, textvariable=pause)

    # affichage
    l_aMin.grid(column=1, row=1)
    e_aMin.grid(column=1, row=2)
    l_aMax.grid(column=2, row=1)
    e_aMax.grid(column=2, row=2)
    l_pas.grid(column=1, row=3)
    e_pas.grid(column=1, row=4)
    l_pause.grid(column=2, row=3)
    e_pause.grid(column=2, row=4)
    Button(fen_dyna, text="ok", command=ok).grid(column=1, row=5)


def menu_pen():
    def ok():
        R.couleur = R.set_couleur(rouge.get(), vert.get(), bleu.get())
        R.rouge = rouge.get()
        R.vert = vert.get()
        R.bleu = bleu.get()
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


def adapter():
    # aloue la taille dispo a la tortue
    R.xFen = calc.winfo_width() - f_clavier.winfo_width() - 30
    R.yFen = calc.winfo_height() - l_mode.winfo_height() - 30

    R.actualiser()
    fenTortue.destroy()
    global fenTortue
    global ecran
    global t
    fenTortue = turtle.Canvas(f_turtle, height=R.yFen, width=R.xFen)
    fenTortue.pack(padx=10, pady=10)
    ecran = turtle.TurtleScreen(fenTortue)
    t = turtle.RawTurtle(ecran)
    R.actualiser()
    t.ht()


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


def str_equation(expr):
    str_expr = ""
    for i in range(len(expr)):
        str_expr += expr[i]
    return str_expr


# fonctions de calcul
def calculer(x):
    return math.sin(x)


def calculer_d(x, a):
    return a / x


# fonctions de coordonées

def coord(x, de_min, de_max, a_min, a_max):
    de_diff = de_max - de_min
    a_diff = a_max - a_min
    assert de_diff != 0, "Les valeurs min et max doivent etres ≠"
    assert a_diff != 0, "Les valeurs min et max doivent etres ≠"
    return (a_diff / de_diff) * (x - de_min) - a_diff // 2


def coords(x, y, de_xmin, de_xmax, a_xmin, a_xmax, de_ymin,
           de_ymax, a_ymin, a_ymax):
    # retuorne les cocrdonnées de la fen à partir de celles du repère

    return coord(x, de_xmin, de_xmax, a_xmin, a_xmax), coord(y, de_ymin, de_ymax, a_ymin, a_ymax)


# paramètres de la tortue
def clearT():
    t.clear()
    t.pencolor("black")
    t.width(1)
    t.seth(0)
    t._tracer(20, 25)
    t.ht()
    t.fillcolor("black")


def setT():
    t.color(R.couleur)
    t.width(R.epaisseur)
    t.up()


# tracer graphiques

def tracer_axes():
    def graduation(a):
        if a % R.xStep == 0:
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

    def fleche():
        t.fd(5)
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

    def axex():
        a = R.xMin
        while t.xcor() < R.xUtilFen // 2:
            t.setx(coord(a, R.xMin, R.xMax, -R.xFenMax, R.xFenMax))
            graduation(a)
            a += 1
        # flèche bout axe
        fleche()
        t.up()

    def axey():
        a = R.yMin
        while t.ycor() < R.yUtilFen // 2:
            t.sety(coord(a, R.yMin, R.yMax, -R.yFenMax, R.yFenMax))
            graduation(a)
            a += 1
        # flèche bout axe
        fleche()
        t.up()

    clearT()
    t.up()

    # tracer axe des x
    if R.yMin > 0:
        t.goto(coords(R.xMin, R.yMin, de_xmin=R.xMin, de_xmax=R.xMax, a_xmin=-R.xFenMax, a_xmax=R.xFenMax,
                      de_ymin=R.yMin,
                      de_ymax=R.yMax, a_ymin=-R.yFenMax, a_ymax=R.yFenMax))
        t.down()
        axex()
    elif R.yMax < 0:
        t.goto(coords(R.xMin, R.yMax, de_xmin=R.xMin, de_xmax=R.xMax, a_xmin=-R.xFenMax, a_xmax=R.xFenMax,
                      de_ymin=R.yMin,
                      de_ymax=R.yMax, a_ymin=-R.yFenMax, a_ymax=R.yFenMax))
        t.down()
        axex()
    else:
        t.goto(
            coords(R.xMin, 0, de_xmin=R.xMin, de_xmax=R.xMax, a_xmin=-R.xFenMax, a_xmax=R.xFenMax, de_ymin=R.yMin,
                   de_ymax=R.yMax, a_ymin=-R.yFenMax, a_ymax=R.yFenMax))
        t.down()
        axex()

    # tracer axe des y
    if R.xMin > 0:
        t.goto(coords(R.xMin, R.yMin, de_xmin=R.xMin, de_xmax=R.xMax, a_xmin=-R.xFenMax, a_xmax=R.xFenMax,
                      de_ymin=R.yMin,
                      de_ymax=R.yMax, a_ymin=-R.yFenMax, a_ymax=R.yFenMax))
        t.down()
        axey()
    elif R.xMax < 0:
        t.goto(coords(R.xMax, R.yMin, de_xmin=R.xMin, de_xmax=R.xMax, a_xmin=-R.xFenMax, a_xmax=R.xFenMax,
                      de_ymin=R.yMin,
                      de_ymax=R.yMax, a_ymin=-R.yFenMax, a_ymax=R.yFenMax))
        t.down()
        axey()
    else:
        t.goto(
            coords(0, R.yMin, de_xmin=R.xMin, de_xmax=R.xMax, a_xmin=-R.xFenMax, a_xmax=R.xFenMax, de_ymin=R.yMin,
                   de_ymax=R.yMax, a_ymin=-R.yFenMax, a_ymax=R.yFenMax))
        t.down()
        axey()
    t.up()


def tracer_graphe():
    clearT()
    tracer_axes()
    setT()

    g = R.xMin
    while g <= R.xMax:

        try:
            t.goto(coords(g, calculer(g), de_xmin=R.xMin, de_xmax=R.xMax, a_xmin=-R.xFenMax, a_xmax=R.xFenMax,
                          de_ymin=R.yMin,
                          de_ymax=R.yMax, a_ymin=-R.yFenMax, a_ymax=R.yFenMax))
            t.pd()
        except ValueError:
            t.up()

        g += R.précision


def tracer_graphe_d(a):
    clearT()

    tracer_axes()

    setT()
    g = R.xMin
    while g <= R.xMax:

        try:
            t.goto(
                coords(g, calculer_d(g, a), de_xmin=R.xMin, de_xmax=R.xMax, a_xmin=-R.xFenMax, a_xmax=R.xFenMax,
                       de_ymin=R.yMin,
                       de_ymax=R.yMax, a_ymin=-R.yFenMax, a_ymax=R.yFenMax))
            t.pd()
        except ValueError:
            t.up()

        g += R.précision
    t.up()
    t.goto(R.xUtilFen // 2 - 100, -R.yUtilFen // 2)
    t.write("a= " + str(a))


boutons = [
    [["pow", key_pow], ["OFF", key_off]],
    [["tan⁻¹", key_atan], ["log", key_log], ],
    [["sin⁻¹", key_acos], ["cos⁻¹", key_asin]],
    [["sin", key_sin], ["cos", key_cos]],
    [["exp", key_exp], ["tan", key_tan]],
    [["sqrt", key_sqrt], ["ln", key_ln]],
    [["AC", key_ac], ["TEST", test], ],
    [["+", key_plus], ["×", key_fois]],
    [["-", key_moins], ["÷", key_div]],
    [["E", key_e], ["⏎", executer]]
]

sequence = []

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
f_clavier.pack(side="bottom")
f_turtle.pack(side="right")

# déclaration et affichage du label modedans le label tortue
mode = "Calculatrice"
l_mode = Label(f_turtle, text=mode, bg="grey", fg="white")
l_mode.pack()

# déclaratior et affichage de l'entrée et du label entée
lf_expression = LabelFrame(f_commande, text="entrée", bg="white")
lf_expression.pack(padx=2, pady=2)
l_expression = Label(lf_expression, text="", bg="white")
l_expression.pack(padx=2, pady=2)

# déclaration et affichage de la tortue
fenTortue = turtle.Canvas(f_turtle, height=R.yFen, width=R.xFen)
fenTortue.pack(padx=10, pady=10)
ecran = turtle.TurtleScreen(fenTortue)
t = turtle.RawTurtle(ecran)
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
parametres.add_command(label="Fenêtre graphique", command=menu_repere)
parametres.add_command(label="Dynamique", command=menu_dyna)
parametres.add_command(label="Crayon", command=menu_pen)
parametres.add_separator()
parametres.add_command(label="adapter fenêtre", command=adapter)
menu.add_cascade(label="pamètres", menu=parametres)

calc.config(menu=menu)

# afichage de la fenetre
calc.mainloop()

# Début fenêtre
