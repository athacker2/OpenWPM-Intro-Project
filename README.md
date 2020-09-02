# OpenWPM Intro Project
## External Resources
The web crawls were conducted using the web privacy measurement framework OpenWPM. Further information about the framework can be found at the following repository: [https://github.com/mozilla/OpenWPM/blob/master/README.md](https://github.com/mozilla/OpenWPM/blob/master/README.md).

The top 100 websites were shortlisted and retrieved from [Tranco](https://tranco-list.eu/download_daily/56JN).
## Background
This project presents findings and analysis on data collected by crawling 100 websites using the OpenWPM framework. While conducting the crawls, three distinct metrics (HTTP Requests, Cookies, Javascript API Calls) were monitored in two different browser environments. The browsing environments were identical in all ways except the second browsing environment had an active ad-blocking extension (U Block Origin). The purpose of this project was to analyze the impacts this ad-blocking agent had on the three metrics that were being monitored.

## Third-Party HTTP Requets
![](Plots/http_plot.png)

### Most Popular Third Party Domains
Without Ad-Block Enabled:
|         Domain        | # of HTTP Requests |
|:---------------------:|:------------------:|
| ssl-images-amazon.com |         471        |
| alicdn.com            |         264        |
| doubleclick.net       |         262        |
| msocdn.com            |         249        |
| google.com            |         228        |
| pstatic.net           |         215        |
| cloudfront.net        |         204        |
| pinimg.com            |         200        |
| awsstatic.com         |         156        |
| qhimg.com             |         149        |

With Ad-Block Enabled:
|         Domain        | # of HTTP Requests |
|:---------------------:|:------------------:|
| ssl-images-amazon.com |         531        |
| msocdn.com            |         249        |
| alicdn.com            |         202        |
| cloudfront.net        |         199        |
| pinimg.com            |         190        |
| pstatic.net           |         173        |
| qhimg.com             |         150        |
| awsstatic.com         |         138        |
| twimg.com             |         121        |
| sinaimg.cn            |         119        |

## Third-Party Cookies
![](Plots/cookie_plot.png)

### Most Popular Third Party Domains
Without Ad-Block Enabled:
|       Domain       |    # of Cookies    |
|:------------------:|:------------------:|
| yahoo.com          |         310        |
| demdex.net         |         217        |
| pubmatic.com       |         203        |
| doubleclick.net    |         133        |
| rubiconproject.com |         131        |
| amazon.com         |         130        |
| adsrvr.org         |         117        |
| linkedin.com       |         92         |
| casalemedia.com    |         77         |
| rlcdn.com          |         72         |

With Ad-Block Enabled:
|     Domain    |    # of Cookies    |
|:-------------:|:------------------:|
| amazon.com    |         102        |
| microsoft.com |         24         |
| youtube.com   |         23         |
| aliexpress.ru |         20         |
| tmall.ru      |         19         |
| bbc.com       |         17         |
| live.com      |         16         |
| iscrv.com     |         14         |
| google.com    |         13         |
| sina.cn       |         11         |

## Third-Party JavaScript API Calls
![](Plots/api_plot.png)

### Most Popular Third Party Domains
Without Ad-Block Enabled:
|        Domain        | # of JavaScript API Calls |
|:--------------------:|:-------------------------:|
| forbesimg.com        |            6343           |
| media.net            |            2239           |
| google-analytics.com |            1297           |
| alicdn.com           |            1279           |
| youtube.com          |            1246           |
| segment.com          |            967            |
| adobedtm.com         |            919            |
| doubleclick.net      |            857            |
| itc.cn               |            838            |
| googletagmanager.com |            778            |

With Ad-Block Enabled:
|        Domain        | # of JavaScript API Calls |
|:--------------------:|:-------------------------:|
| forbesimg.com        |            6343           |
| media.net            |            2239           |
| google-analytics.com |            1297           |
| alicdn.com           |            1279           |
| youtube.com          |            1246           |
| segment.com          |            967            |
| adobedtm.com         |            919            |
| doubleclick.net      |            857            |
| itc.cn               |            838            |
| googletagmanager.com |            778            |

