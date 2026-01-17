import numpy as np
import matplotlib.pyplot as plt

# Demander un entier
def demander_int(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("⚠️ Entrée invalide, veuillez entrer un entier.")

# Demander un float
def demander_float(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("⚠️ Entrée invalide, veuillez entrer un nombre.")

# Fonction pour obtenir les coefficients de polynômes
def coeff_polynome(N):
    coeffs = []
    for i in range(N):
        print(f"\nPolynôme {i+1}")
        a = demander_float("Coefficient de x² : ")
        b = demander_float("Coefficient de x : ")
        c = demander_float("Constante : ")
        coeffs.append([a, b, c])

    return coeffs

# Fonction pour creer intervalle
def intervalle():
    # Les bornes
    while True:
        xmin = demander_float("\nBorne inférieure : ")
        xmax = demander_float("Borne supérieure : ")
        if xmin >= xmax : print("Bornes Invalide !")
        else : break
    # Le Pas
    while True:
        pas = demander_float("Pas : ")
        if pas <= 0 or pas >= xmax - xmin : print("Pas invalide !")
        else : break

    return xmin,xmax,pas

# Fonction pour calculer les valeurs 
def calculer_valeurs(xmin,xmax,pas,coeffs):
    x_values = np.arange(xmin, xmax, pas)
    y_values = []
    for c in coeffs:
        y_values.append(np.polyval(c, x_values))

    return x_values,y_values

# Affichage de polynomes
def afficher_polynome(coeffs):
    a, b, c = coeffs
    expression = ""

    if a != 0:
        expression += f"{a}x^2"

    if b != 0:
        if b > 0:
            expression += f" + {b}x"
        else:
            expression += f" - {abs(b)}x"

    if c != 0:
        if c > 0:
            expression += f" + {c}"
        else:
            expression += f" - {abs(c)}"

    return f"${expression}$"


# =========================
# Nombre de polynômes
while True :
    N = demander_int("Entrez le nombre de polynomes : ")
    if N<=0 or N>3 : print("Nombre invalide !")
    else : break

# =========================
# Coefficients
coeffs = coeff_polynome(N)

# =========================
# Intervalle
xmin,xmax,pas = intervalle()

# =========================
# Calcul des valeurs
x_values,y_values = calculer_valeurs(xmin,xmax,pas,coeffs)

# =========================
# Couleurs
colors = ["blue", "green", "red"]

# =========================
# Tracé
for i in range(N):
    label = afficher_polynome(coeffs[i])
    plt.plot(x_values, y_values[i], color=colors[i], label=label)

plt.title("Tracé de polynômes")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()
plt.show()