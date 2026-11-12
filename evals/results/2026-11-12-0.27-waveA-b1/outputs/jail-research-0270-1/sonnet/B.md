I couldn't get an answer for you, and I don't want to put a guess in a client deck.

**What I tried**
- Two web searches returned only business directories, for-sale listings and company profiles. None gave a dated count of landscaping establishments in Suffolk County, so they can't show a trend.
- I tried to pull the official Census Bureau numbers directly. The shell command needs your approval, and the web fetch was refused by the proxy. So I have no verified figures.

**What the right source is**
Census County Business Patterns, NAICS 561730 (Landscaping Services), Suffolk County NY (state 36, county 103). It gives establishment counts by year, and it's citable on a slide.

**Ways to finish this**
1. **Approve the Census API calls.** I'd pull establishments and employees for roughly 2012–2023 and give you a trend table you can chart. The call is `https://api.census.gov/data/<year>/cbp?get=ESTAB,EMP,NAME&for=county:103&in=state:36&NAICS2017=561730`. Older years use a different NAICS vintage variable.
2. **Check it yourself.** On data.census.gov, search "CBP" and filter to NAICS 561730 and Suffolk County.
3. **Use NY State Department of Labor QCEW data.** It's a good cross-check, and it includes the employment trend.

One caveat for the deck: County Business Patterns counts only employer establishments. A lot of landscaping is sole proprietors and crews with no payroll, so the real number of businesses is higher. The Census "Nonemployer Statistics" series covers those. If the client cares about how many operators are really out there, show both series.

Do you want me to go ahead with option 1?