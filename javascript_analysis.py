import sqlite3
import tldextract
import matplotlib.pyplot as plt
from resources import *

NO_BLOCK_APIS = []
BLOCK_APIS = []

THIRD_PARTY_DOMAIN_COUNTS = {}
SORTED_THIRD_PARTY_DOMAINS_NO_BLOCK = []
SORTED_THIRD_PARTY_DOMAINS_BLOCK = []

def count_third_pary_apis(c):
    third_party_apis = []
    for x in range(1,101):
        apis_count = 0
        for row in c.execute(f"SELECT script_url FROM javascript WHERE visit_id = {x}"):
            api_domain = tldextract.extract(row[0]).registered_domain
            if(is_third_party(DOMAIN_VISIT_ID[x], api_domain)):
                apis_count += 1
                if(api_domain in THIRD_PARTY_DOMAIN_COUNTS):
                    THIRD_PARTY_DOMAIN_COUNTS[api_domain] += 1
                else:
                    THIRD_PARTY_DOMAIN_COUNTS.update({api_domain:1})
        third_party_apis.append((x, apis_count))
    return third_party_apis

#Load Dictionary Mapping Visit IDs with Domains
load_domain_dict()

#Load in data from vanilla browsing database
conn = sqlite3.connect('./Crawls/crawl-data-noblock.sqlite')
c = conn.cursor()

NO_BLOCK_APIS = count_third_pary_apis(c)
SORTED_THIRD_PARTY_DOMAINS_NO_BLOCK = sorted(THIRD_PARTY_DOMAIN_COUNTS.items(), key=lambda x: x[1], reverse=True)
THIRD_PARTY_DOMAIN_COUNTS.clear()

conn.close()

#Load in data from ad-block browsing database
conn = sqlite3.connect('./Crawls/crawl-data-block.sqlite')
c = conn.cursor()

BLOCK_APIS = count_third_pary_apis(c)
SORTED_THIRD_PARTY_DOMAINS_BLOCK = sorted(THIRD_PARTY_DOMAIN_COUNTS.items(), key=lambda x: x[1], reverse=True)
THIRD_PARTY_DOMAIN_COUNTS.clear()

conn.close()

#Print top 10 Third Party Domains 
print_top_domains(SORTED_THIRD_PARTY_DOMAINS_NO_BLOCK, SORTED_THIRD_PARTY_DOMAINS_BLOCK)

plt.figure(figsize=(12,7))

#Plot for Javascript APIs in vanilla vs ad block browsing
no_block = plt.subplot(121)
no_block.set_title('Ad-Block Disabled')
no_block.set(xlabel = 'Top 100 Websites', ylabel = "Number of Third-Party JavaScript API Calls")
plt.ylim(0,10000)
no_block.bar([x[0] for x in NO_BLOCK_APIS], [x[1] for x in NO_BLOCK_APIS])
no_block.tick_params(axis=u'both', which=u'both',length=0)

with_block = plt.subplot(122)
with_block.set_title('Ad-Block Enabled')
with_block.set(xlabel = 'Top 100 Websites', ylabel = "")
plt.ylim(0,10000)
with_block.bar([x[0] for x in BLOCK_APIS], [x[1] for x in BLOCK_APIS])
with_block.tick_params(axis=u'both', which=u'both',length=0)
plt.suptitle('Javascript APIs')

plt.show()