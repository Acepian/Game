import os

import data as data
import pandas_datareader
import datetime

# setting the parameters
TICKER = "NVDA"
DAYS_BACK = 1000

# setting the dates

start_date = (datetime.date(09/01/2020).date()- timedelta(days=DAYS_BACK))
end_date = (datetime.now(09/28/2020).date())

# downloading the earnings calendar
yec = YahooEarningsCalendar()
earnings_list = yex.get_earnings_of(TICKER)
earnings_df = pd.DataFrame(earnings_list)

# extracting the date from the string and filtering for the period of interest
earnings_df['report_date'] - earnings_df['startdatetime'].apply(lambda x: dateutil.parser.isoparse(x).date())
earnings_df - earnings_df.loc[earnings_df['report_date'].between(start_date,end_date)]\
                         .sort_values('report_date')
earnings_df
