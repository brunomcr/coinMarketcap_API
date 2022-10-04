import csv


def json_to_csv(json_data):
    csv_file = open("coinMarketCap.csv", "w", newline="")
    csv_writer = csv.writer(csv_file)

    field_names = ["Name", "Symbol", "Price", "% 24h"]
    csv_writer.writerow(field_names)

    for coin in json_data:
        coin_row = [
            coin["name"],
            coin["symbol"],
            str(round(coin["quote"]["USD"]["price"], 2)),
            str(round(coin["quote"]["USD"]["percent_change_24h"], 2)),
        ]
        csv_writer.writerow(coin_row)

    csv_file.close()
