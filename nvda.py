from secedgar import filings, FilingType
from datetime import date


# 10K filings for Nvidia (ticker "nvda")
my_filings = filings(cik_lookup="nvda",
                     filing_type=FilingType.FILING_10K,
                     start_date=date(2023, 1, 1),
                     user_agent="Bridget Leonard leonardbridget01@gmail.com")
my_filings.save('sec-edgar/filing_results')
