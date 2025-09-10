import csv
import json
import os
import xml.etree.ElementTree as ET
import sqlite3
import sqlite3

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect("portfolio.db")
        print("Connection successful")
    except sqlite3.Error as e:
        print(f"Error: {e}")
    return conn

create_connection("portfolio.db")

#portfolio_sample.csv

# def lire_portfolio_csv(nom_fichier):
#     portfolio = []
#     with open(nom_fichier, newline='', encoding='utf-8') as csvfile:
#         reader = csv.reader(csvfile, delimiter=',')  # or delimiter=';' depending on your file
#         for row in reader:
#             portfolio.append(row)
#     return portfolio

def lire_portfolio_csv(nom_fichier):
    portfolio = []
    with open(nom_fichier, newline='', encoding='utf-8') as csvfile:
        lecteur_csv = csv.DictReader(csvfile, delimiter=',')  # adjust delimiter if needed
        for line in lecteur_csv:
            position = {
                'symbol': line.get('symbol'),
                'quantity': int(line.get('quantity', 0)),
                'purchase_price': float(line.get('purchase_price', 0.0)),
                'purchase_date': line.get('purchase_date')
            }
            portfolio.append(position)
    return portfolio

print("\n====== Lire portfolio csv ========")
data = lire_portfolio_csv("portfolio_sample.csv")
print(data)


#portfolio_sample.json
def lire_portfolio_json(nom_fichier):
    with open(nom_fichier, encoding='utf-8') as json_file:
        json_data = json.load(json_file)

        positions = json_data.get("positions", [])  # list of dicts
        cleaned_positions = []
        for pos in positions:
            cleaned_positions.append({
                "symbol": pos.get("symbol"),
                "quantity": int(pos.get("quantity", 0)),
                "purchase_price": float(pos.get("purchase_price", 0.0)),
                "purchase_date": pos.get("purchase_date")
            })

    return cleaned_positions

print("\n======== Lire portfolio json ===========")

# csv_data = lire_portfolio_csv("portfolio_sample.csv")
json_data = lire_portfolio_json("portfolio_sample.json")
#
# print(csv_data)
print(json_data)

print("\n========= Lire portfolio xml ===========")

def lire_portfolio_xml(nom_fichier):
    tree = ET.parse(nom_fichier)
    root = tree.getroot()
    portfolio = []

    for pos in root.findall(".//position"):
        entry = {child.tag: child.text for child in pos}
        portfolio.append(entry)

    return portfolio

xml_data = lire_portfolio_xml("portfolio_sample.xml")
print(xml_data)




# afficher_portfolio(portfolio) # affiche un résumé lisible du portfolio
def afficher_portfolio(portfolio):
    if portfolio.endswith(".csv"):
        csv_data = lire_portfolio_csv(portfolio)
        print("\ncsv Portfolio:")
        print(csv_data)
    elif portfolio.endswith(".json"):
        json_data = lire_portfolio_json(portfolio)
        print("\njson Portfolio:")
        print(json_data)
    elif portfolio.endswith(".xml"):
        tree = ET.parse(portfolio)
        root = tree.getroot()
        print("\nXML Portfolio:")
        for pos in root.findall(".//position"):
            entry = {child.tag: child.text for child in pos}
            print(entry)
    else:
        print("\nUnknown format")

afficher_portfolio("portfolio_sample.csv")
afficher_portfolio("portfolio_sample.json")
afficher_portfolio("portfolio_sample.xml")


def recherche_par_symbole(filename, symbole):
    results = []
    if filename.endswith(".csv"):
        # read CSV as list of rows
        csv_data = lire_portfolio_csv(filename)
        headers = csv_data[0]
        for row in csv_data[1:]:
            row_dict = dict(zip(headers, row))
            if row_dict.get("symbol") == symbole:
                results.append(row_dict)

    elif filename.endswith(".json"):
        # read JSON as Python dictimport xml.etree.ElementTree as ET
        positions = lire_portfolio_json(filename)
        for pos in positions:
            if pos.get("symbol") == symbole:
                results.append(pos)
    elif filename.endswith(".xml"):
        tree = ET.parse(filename)
        root = tree.getroot()
        for pos in root.findall(".//position"):
            entry = {child.tag: child.text for child in pos}
            if entry.get("symbol") == symbole:
                results.append(entry)
    else:
        print("Unknown format")
    return results


matches = recherche_par_symbole("portfolio_sample.csv", "AAPL")
print(matches)

print(recherche_par_symbole("portfolio_sample.json", "AAPL"))
print(recherche_par_symbole("portfolio_sample.xml", "MSFT"))


def recherche_par_symbole_db(db_file, symbole):
    conn = sqlite3.connect(db_file)
    cur = conn.cursor()
    sql = "SELECT * FROM sample WHERE symbol = ?"
    cur.execute(sql, (symbole,))
    rows = cur.fetchall()
    conn.close()
    return rows

# Now this works:
rows = recherche_par_symbole_db("portfolio.db", "AAPL")
print(rows)





