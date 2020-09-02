import sqlite3
import tldextract
import matplotlib.pyplot as plt
from resources import *

NO_BLOCK_HTTP_REQUESTS = []
BLOCK_HTTP_REQUESTS = []

THIRD_PARTY_DOMAINS_COUNTS = {}
SORTED_THIRD_PARTY_DOMAINS_NO_BLOCK = []
SORTED_THIRD_PARTY_DOMAINS_BLOCK = []

def count_third_party_http_requests(c):
    http_requests = []
    for x in range(1,101):
        http_requests_count = 0
        for row in c.execute(f'SELECT url FROM http_requests WHERE visit_id = {x}'):
            third_party_domain = str(tldextract.extract(row[0]).registered_domain)
            if(is_third_party(DOMAIN_VISIT_ID[x], third_party_domain)):
                http_requests_count += 1
                if(third_party_domain in THIRD_PARTY_DOMAINS_COUNTS):
                    THIRD_PARTY_DOMAINS_COUNTS[third_party_domain] += 1
                else:
                    THIRD_PARTY_DOMAINS_COUNTS.update({third_party_domain:1})      
        http_requests.append((x, http_requests_count))
    return http_requests

#Load Dictionary Mapping Visit IDs with Domains
load_domain_dict()

#Load in data from vanilla browsing database
conn = sqlite3.connect('./Crawls/crawl-data-noblock.sqlite')
c = conn.cursor()

NO_BLOCK_HTTP_REQUESTS = count_third_party_http_requests(c)
SORTED_THIRD_PARTY_DOMAINS_NO_BLOCK = sorted(THIRD_PARTY_DOMAINS_COUNTS.items(), key=lambda x: x[1], reverse=True)
THIRD_PARTY_DOMAINS_COUNTS.clear()

conn.close()

#Load in data from ad-block browsing database
conn = sqlite3.connect('./Crawls/crawl-data-block.sqlite')
c = conn.cursor()

BLOCK_HTTP_REQUESTS = count_third_party_http_requests(c)
SORTED_THIRD_PARTY_DOMAINS_BLOCK = sorted(THIRD_PARTY_DOMAINS_COUNTS.items(), key=lambda x: x[1], reverse=True)
THIRD_PARTY_DOMAINS_COUNTS.clear()

conn.close()

print_top_domains(SORTED_THIRD_PARTY_DOMAINS_NO_BLOCK, SORTED_THIRD_PARTY_DOMAINS_BLOCK)

no_block_mean = sum([x[1] for x in NO_BLOCK_HTTP_REQUESTS])/len([x[1] for x in NO_BLOCK_HTTP_REQUESTS])
block_mean = sum([x[1] for x in BLOCK_HTTP_REQUESTS])/len([x[1] for x in BLOCK_HTTP_REQUESTS])

print(f"Mean NoBlock - {no_block_mean}")
print(f"Mean Block - {block_mean}")

plt.figure(figsize=(12,7))

#Plot for HTML REQUESTS in vanilla vs ad block browsing
no_block = plt.subplot(121)
no_block.set_title('Ad-Block Disabled')
no_block.set(xlabel = 'Top 100 Websites', ylabel = "Number of Third-Party HTTP Requests")
plt.ylim(0,500)
no_block.bar([x[0] for x in NO_BLOCK_HTTP_REQUESTS], [x[1] for x in NO_BLOCK_HTTP_REQUESTS])
no_block.axhline(no_block_mean, color='red')
no_block.tick_params(axis=u'both', which=u'both',length=0)

with_block = plt.subplot(122)
with_block.set_title('Ad-Block Enabled')
with_block.set(xlabel = 'Top 100 Websites', ylabel = "")
plt.ylim(0,500)
with_block.bar([x[0] for x in BLOCK_HTTP_REQUESTS], [x[1] for x in BLOCK_HTTP_REQUESTS])
with_block.axhline(block_mean, color='red')
with_block.tick_params(axis=u'both', which=u'both',length=0)

plt.show()
