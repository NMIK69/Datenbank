import json

def get_year_month(date):
    year, month = date.split('-')[0:2]
    month = int(month)
    
    return year, str(month)
    

def my_format(date, data_dict, coop):

    year, month = get_year_month(date)

    add = "("
    add += '"' + year + '", '
    add += '"' + month + '", '
    add += '"' + coop + '", '
    
    for value in data_dict.values():
        add += '"' + value + '", '

    add = add[:-2]
    add += ")"

    return add


def insert_into_stock(coop_symbol):
    big_insert = "INSERT INTO stocks (year, month, company, open, high, low, close, volume) values"

    filename = coop_symbol.lower() + "_monthly.json"

    with open(filename) as json_file:
        data = json.load(json_file)
        data = data["Monthly Time Series"]


        for x, y in data.items():
            big_insert += my_format(x, y, coop_symbol) + ","
    

    return big_insert[:-1]