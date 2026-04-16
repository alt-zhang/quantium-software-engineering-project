#!/usr/bin/env python3

# CSV file format:
#   product,price,quantity,date,region
#   pink morsel,$3.00,546,2018-02-06,north
#   pink morsel,$3.00,549,2018-02-06,south
#   pink morsel,$3.00,577,2018-02-06,east
#   pink morsel,$3.00,519,2018-02-06,west
#   gold morsel,$9.99,580,2018-02-06,north
#   gold morsel,$9.99,530,2018-02-06,south
#   gold morsel,$9.99,576,2018-02-06,east
#   gold morsel,$9.99,580,2018-02-06,west
#   magenta morsel,$2.50,522,2018-02-06,north

import csv

def process_csv(reader, writer):
    for row in reader:
        product, price, quantity, date, region = row

        if product != "pink morsel":
            continue

        sales = float(price[1:]) * int(quantity)
        writer.writerow([sales, date, region])

output_file = "combined_output.csv"
csv_files = [
    "data/daily_sales_data_0.csv",
    "data/daily_sales_data_2.csv",
    "data/daily_sales_data_1.csv"
]

with open(output_file, "w") as outfile:
    writer = csv.writer(outfile)
    writer.writerow(["sales", "date", "region"])

    for csv_file in csv_files:
        with open(csv_file, "r") as infile:
            reader = csv.reader(infile)
            process_csv(reader, writer)

