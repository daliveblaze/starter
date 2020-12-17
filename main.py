import pandas as pd
import datetime

#UK holidays by year
year = datetime.date.today().year

url = "https://www.timeanddate.com/holidays/uk/" + str(year)
filename = "~/uk_bank_holidays_" + str(year) + ".csv"

# Clean up steps into its own function
def holiday_table(table):
    # Returns a clean dataframe of holiday table.
    table.columns = ["Date", "Day of Week", "Holiday Name", "Holiday Type", "Details"]
    table = table.reset_index(drop=True)
    # Only get the ones with Bank Holidays
    table = table.loc[table['Holiday Type'] == "Bank holiday"]
    return table


data = pd.read_html(url)
# Get clean table
df = holiday_table(data[0])

myDates = df['Date']

# Date is missing the year, add it in
df['Date'] = myDates.apply(lambda x: x+' '+str(year))

print(df)
print("Exporting to CSV filename: " + filename)
df.to_csv(filename, index=False, header=True, encoding="utf-8")


