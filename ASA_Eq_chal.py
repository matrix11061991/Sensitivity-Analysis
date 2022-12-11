import numpy as np

from scipy.solve_bvp import solve_bvp

from SALib.sample import latin

from SALib.analyze import sobol

# Définition des constantes

k = 0.5  # Conductivité thermique

h = 10   # Constant de transfert de chaleur

T_inf = 25  # Température ambiante

# Définition de la fonction de source de chaleur

def q(x, y):

    return np.sin(np.pi*x)*np.sin(np.pi*y)

# Définition des conditions aux limites

def bc(ya, yb):

    return ya[0] - T_inf, yb[0] - T_inf

# Génération d'un échantillon aléatoire pour l'analyse de sensibilité

param_values = latin.sample(2, 100)

# Résolution de l'équation de la chaleur pour chaque valeur de l'échantillon

solutions = []

for i in range(len(param_values)):

    # Récupération des valeurs des paramètres

    k_i = param_values[i][0]

    h_i = param_values[i][1]

    # Résolution de l'équation de la chaleur

    x = np.linspace(0, 1, 10)

    y = np.linspace(0, 1, 10)

    X, Y = np.meshgrid(x, y)

    T = solve_bvp(lambda x, y, T: k_i*(T[1] + T[2] - 2*T[0]) + h_i*q(x, y), bc, X, Y, T)

    # Stockage de la solution

    solutions.append(T)

# Analyse de sensibilité

problem = {

    'num_vars': 2,

    'names': ['k', 'h'],

    'bounds': [[0, 1], [0, 20]]

}

Si = sobol.analyze(problem, solutions, calc_second_order=True)

# Affichage des résultats

print(Si)

