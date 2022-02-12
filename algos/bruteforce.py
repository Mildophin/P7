from itertools import combinations
from builtins import list
import utils.dataset


def determine_all_combinations(shares_list):
    all_wallet_combinations = []
    for r in range(len(shares_list) + 1):
        combinations_obj = combinations(shares_list, r)
        combinations_list = list(combinations_obj)
        all_wallet_combinations += combinations_list
    return all_wallet_combinations


def bruteforce(budget, items, name, price, profit_percentage):

    # Premièrement, calcul le profit avec le prix et le pourcentage de rentabilité
    shares_list = utils.dataset.readable_data(name, price,
                                              profit_percentage,
                                              items)

    # Determine toutes les combinaisons de portefeuille possible
    all_wallet_combinations = determine_all_combinations(shares_list)
    del all_wallet_combinations[0]

    # Initialise la liste de tous les portefeuilles
    all_wallets = []

    # Calcul le profit total par combinaison
    for i in range(len(all_wallet_combinations)):
        current_combination = all_wallet_combinations[i]

        # Initialise Variables
        wallet_name = i
        wallet_price = 0
        wallet_profit = 0

        # Calcul le profit et prix
        for share in current_combination:
            wallet_price = wallet_price + share[1]
            wallet_profit = wallet_profit + share[2]

        # Garde seulement les portefeuilles où le prix total est inférieur à 500
        if wallet_price > (budget * 100):
            pass
        else:
            wallet = [wallet_name, wallet_price, wallet_profit]
            all_wallets.append(wallet)

    # Determine le meilleur portefeuille
    sorted_w = sorted(all_wallets, key=lambda w: w[2], reverse=True)
    res_wallet = sorted_w[0]
    best_wallet_shares = all_wallet_combinations[res_wallet[0]]

    # Montre le meilleur portefeuille dans la console
    print("Vous devriez acheter:")
    for item in range(len(best_wallet_shares)):
        share = best_wallet_shares[item]

        # Restore le prix correct aux actions
        c_s_price = share[1] / 100
        c_s_profit = share[2] / 100

        print(f"{share[0]} pour {c_s_price} € -> {c_s_profit} € de profit")

    # Restore le prix total du portefeuille et son profit
    w_price = res_wallet[1] / 100
    w_profit = res_wallet[2] / 100
    print(f"\nLe meilleur portefeuille coûte {w_price} € et vous permettra d'obtenir {w_profit} € de profit")
