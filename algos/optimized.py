import numpy as np
import utils.dataset


def optimized(initial_budget, items, name, price, profit_percentage):

    # Budget mis à jour, car le prix et le pourcentage était multiplié par 100
    budget = initial_budget * 100

    # Premièrement, calcul le profit avec le prix et le pourcentage de profit
    shares_list = utils.dataset.readable_data(name, price,
                                              profit_percentage,
                                              items)

    # Deuxièmement, on obtient le profit des shares_list :
    profit_int = []
    for share in shares_list:
        share_profit = share[2]
        profit_int.append(share_profit)

    # Phase 1 : Création d'une grille avec la meilleure solution

    # Initialisation de la Matrice
    matrice = np.empty((items + 1, budget + 1), dtype=int)
    matrice[0] = 0

    # Remplissage de la matrice
    for item in range(items):
        this_price = price[item]
        this_value = profit_int[item]
        matrice[item+1, :this_price] = matrice[item, :this_price]
        temp = matrice[item, :-this_price] + this_value
        matrice[item + 1, this_price:] = np.where(
            temp > matrice[item, this_price:], temp, matrice[item, this_price:]
            )

    # Phase 2 : Backtracking pour obtenir les meilleures actions
    wallet_price = 0
    taken = []

    # Backtracking pour la taken list
    for item in range(items, 0, -1):
        if matrice[item][budget] != matrice[item - 1][budget]:
            taken.append(item - 1)
            budget -= price[item - 1]
            wallet_price += price[item - 1]

    # Montre le meilleur portefeuille dans la console
    print("Vous devriez acheter:")
    profit_total = []
    for item in taken:
        share = shares_list[item]
        # Restore le prix correct aux actions
        c_s_price = share[1] / 100
        c_s_profit = share[2] / 100

        # Rajoute le profit total avec le profit
        profit_total.append(c_s_profit)

        print(f"{share[0]} pour {c_s_price} € -> {c_s_profit} € de profit")

    # Restore le prix total du portefeuille et son profit
    w_price = wallet_price / 100
    w_profit = sum(profit_total)
    print(f"\nLe meilleur portefeuille coûte {w_price} € et vous permettra d'obtenir {w_profit} € de profit")
