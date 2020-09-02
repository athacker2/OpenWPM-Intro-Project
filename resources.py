import sqlite3
import tldextract
import csv

DOMAIN_VISIT_ID = {}

#Create dictionary mapping visit_ids to domain names
def load_domain_dict():
    with open('/Users/abhaythacker/Desktop/top-1m.csv') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            DOMAIN_VISIT_ID.update({int(row[0]):tldextract.extract(row[1]).registered_domain})
            if row[0] == '100':
                break

def is_third_party(domain_url, url):
    return not(domain_url == url)

def print_top_domains(noblock_domains, block_domains):
    print("No Block:")
    for x in range (0,10):
        print(f"{x} {noblock_domains[x]}")
    print("Block:")
    for x in range(0,10):
        print(f"{x} {block_domains[x]}")


