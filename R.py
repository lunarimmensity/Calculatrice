def actualiser():
    global xDiff
    global yDiff
    global xUtilFen
    global yUtilFen
    xDiff = xMax - xMin
    yDiff = yMax - yMin
    xUtilFen = xFen - 2 * marges
    yUtilFen = yFen - 2 * marges


def set_couleur(r, v, b):
    r = hex(r)
    v = hex(v)
    b = hex(b)
    s = "#"
    try:
        s += r[2] + r[3]
    except IndexError:
        s += "0" + r[2]

    try:
        s += v[2] + v[3]
    except IndexError:
        s += "0" + v[2]
    try:
        s += b[2] + b[3]
    except IndexError:
        s += "0" + b[2]
    return s


# param fen
xFen = 800
yFen = 500
marges = 20
xUtilFen = xFen - 2 * marges
xFenMax = xFen//2-marges
yUtilFen = yFen - 2 * marges
yFenMax = yFen//2-marges
Dyna = False

# paramètres du repère
xMin = -5
xMax = 5
xStep = 1
xDiff = xMax - xMin

yMin = -5
yMax = 5
yStep = 1
yDiff = yMax - yMin

# paramètre du tracer

rouge = 25
vert = 75
bleu = 235
couleur = set_couleur(rouge, vert, bleu)
epaisseur = 5
précision = 0.005

# paramètres dyna
aMin = -5
aMax = 5
pause = 1
pas = 1


