
def readable_data(name, price, profit_percentage, items):

    shares_list = []

    for i in range(items):
        profit_value = int(price[i] * (profit_percentage[i] / 10000))
        share = [name[i], price[i], profit_value]
        shares_list.append(share)

    return shares_list
