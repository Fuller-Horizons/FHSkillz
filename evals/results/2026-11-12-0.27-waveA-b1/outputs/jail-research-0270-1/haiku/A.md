I couldn't find a reliable answer for Suffolk County specifically. The web doesn't give a county-level trend, so I'd leave "growing or shrinking" out of the client deck until we have official numbers.

**What I found**

- **National direction (weak, and the sources conflict):** IBISWorld shows US landscaping services businesses up 1.8% in 2026 and up 4.8% in 2025, but its two pages give very different totals (556,238 vs. 692,777). Treat this as directional at most. [IBISWorld (2026 count)](https://img2.ibisworld.com/united-states/number-of-businesses/landscaping-services/1497/) · [IBISWorld (number of businesses, 2005–2031)](https://img3.ibisworld.com/united-states/number-of-businesses/landscaping-services/1497)
- **New York State:** A summary of 2023 County Business Patterns data puts New York at 7,725 landscaping employer establishments, third nationally. I found no prior-year figure, so it doesn't show a trend. [Startbusinessbystate](https://startbusinessbystate.com/landscaping-industry-statistics/)
- **Suffolk County:** No establishment count or time series turned up. The Suffolk results were sale listings and company directories, which don't measure total businesses or change over time. [BizBuySell, Suffolk County](https://www.bizbuysell.com/new-york/suffolk-county/landscaping-and-yard-service-businesses-for-sale/) · [Procore, New Suffolk](https://network.procore.com/us/ny/new-suffolk/landscaping)

**How to get a real answer**

The authoritative source is Census County Business Patterns for Suffolk County (FIPS 36103), NAICS 561730, for 2019 through 2023. Comparing those years gives an establishment-count trend. Sole proprietors with no employees are excluded from CBP, so Nonemployer Statistics for the same codes would be a useful complement.

I tried to pull those figures from the Census API, but the sandbox required approval for the calls and I didn't run them. If you approve, I can pull the five years and calculate the trend. Or you can run the query at data.census.gov.