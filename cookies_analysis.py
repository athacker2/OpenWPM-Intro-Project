import sqlite3
import tldextract
import matplotlib.pyplot as plt
from resources import *

NO_BLOCK_COOKIES = []
BLOCK_COOKIES = []

THIRD_PARTY_DOMAIN_COUNTS = {}
SORTED_THIRD_PARTY_DOMAINS_NO_BLOCK = []
SORTED_THIRD_PARTY_DOMAINS_BLOCK = []

def count_third_pary_cookies(c):
    third_party_cookies = []
    for x in range(1,101):
        cookies_count = 0
        for row in c.execute(f"SELECT host FROM javascript_cookies WHERE visit_id = {x}"):
            cookie_domain = tldextract.extract(row[0]).registered_domain
            if(is_third_party(DOMAIN_VISIT_ID[x], cookie_domain)):
                cookies_count += 1
                if(cookie_domain in THIRD_PARTY_DOMAIN_COUNTS):
                    THIRD_PARTY_DOMAIN_COUNTS[cookie_domain] += 1
                else:
                    THIRD_PARTY_DOMAIN_COUNTS.update({cookie_domain:1})
        third_party_cookies.append((x, cookies_count))
    return third_party_cookies


#Load Dictionary Mapping Visit IDs with Domains
load_domain_dict()

#Load in data from vanilla browsing database
conn = sqlite3.connect('./Crawls/crawl-data-noblock.sqlite')
c = conn.cursor()

NO_BLOCK_COOKIES = count_third_pary_cookies(c)
SORTED_THIRD_PARTY_DOMAINS_NO_BLOCK = sorted(THIRD_PARTY_DOMAIN_COUNTS.items(), key=lambda x: x[1], reverse=True)
THIRD_PARTY_DOMAIN_COUNTS.clear()

conn.close()


#Load in data from ad-block browsing database
conn = sqlite3.connect('./Crawls/crawl-data-block.sqlite')
c = conn.cursor()

BLOCK_COOKIES = count_third_pary_cookies(c)
SORTED_THIRD_PARTY_DOMAINS_BLOCK = sorted(THIRD_PARTY_DOMAIN_COUNTS.items(), key=lambda x: x[1], reverse=True)
THIRD_PARTY_DOMAIN_COUNTS.clear()

conn.close()

print_top_domains(SORTED_THIRD_PARTY_DOMAINS_NO_BLOCK, SORTED_THIRD_PARTY_DOMAINS_BLOCK)

no_block_mean = sum([x[1] for x in NO_BLOCK_COOKIES])/len([x[1] for x in NO_BLOCK_COOKIES])
block_mean = sum([x[1] for x in BLOCK_COOKIES])/len([x[1] for x in BLOCK_COOKIES])

print(f"Mean NoBlock - {no_block_mean}")
print(f"Mean Block - {block_mean}")

plt.figure(figsize=(12,7))

#Plot for Cookies in vanilla vs ad block browsing
no_block = plt.subplot(121)
no_block.set_title('Ad-Block Disabled')
no_block.set(xlabel = 'Top 100 Websites', ylabel = "Number of Third-Party Cookies")
plt.ylim(0,550)
no_block.bar([x[0] for x in NO_BLOCK_COOKIES], [x[1] for x in NO_BLOCK_COOKIES])
no_block.axhline(block_mean, color='red')
no_block.tick_params(axis=u'both', which=u'both',length=0)

with_block = plt.subplot(122)
with_block.set_title('Ad-Block Enabled')
with_block.set(xlabel = 'Top 100 Websites', ylabel = "")
plt.ylim(0,550)
with_block.bar([x[0] for x in BLOCK_COOKIES], [x[1] for x in BLOCK_COOKIES])
with_block.axhline(block_mean, color='red')
with_block.tick_params(axis=u'both', which=u'both',length=0)

plt.show()