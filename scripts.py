
import argparse
import algos.bruteforce as algo_a
import algos.optimized as algo_b


if __name__ == '__main__':

    options = {
        'bruteforce': algo_a.bruteforce,
        'optimized': algo_b.optimized
    }

    parser = argparse.ArgumentParser(
        description="Lancer l'algorithme pour AlgoInvest&Trade"
    )

    # Arguments pour la ligne de commande lançant le script
    parser.add_argument('-f', default='databases/dataset.csv',
                        metavar='filename',
                        help='Nom du fichier CSV (default: %(default)s'
                        'Format des data: nom, prix, valeur')
    parser.add_argument('-b', default=500,
                        metavar='wallet budget',
                        help='choisir le budget max pour le portefeuille')
    parser.add_argument('algo', choices=list(options.keys()),
                        help='Algo a choisir parmi: %(choices)s')

    args = parser.parse_args()
    data_filename = args.f
    budget = int(args.b)
    launch_algo = options[args.algo]

    # Initialise la liste
    name = []
    price = []
    profit_percentage = []
    items = 0
    item_removed_exceeded = 0
    item_removed_null = 0

    with open(data_filename, 'r') as file:
        data = file.read()
    for line in data.split('\n'):
        name_data, price_data, profit_percentage_data = line.split(',')

        # Check si le prix est inférieur ou égal à 0 ou dépasse le portefeuille
        price_int = int(float(price_data))
        if price_int > budget:
            item_removed_exceeded += 1
        elif price_int <= 0:
            item_removed_null += 1
        else:
            name.append(name_data)
            price.append(int(float(price_data) * 100))
            profit_percentage.append(int(float(profit_percentage_data) * 100))
            items += 1

    print(f"\n{item_removed_exceeded} actions supprimées (dépassant la taille du portefeuille)")
    print(f"\n{item_removed_null} actions supprimées (valeur nulle)\n")
    launch_algo(budget, items, name, price, profit_percentage)
