import pandas as pd

#UK holidays 2021

url = "https://www.timeanddate.com/holidays/uk/2021"
filename = "~/uk_bank_holidays_2021.csv"

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

list = df['Date']
newlist = []

for item in list:
    item = item + " 2021"
    #print(item)
    newlist.append(item)

df['Date'] = newlist


print(df)
print("Exporting to CSV filename: " + filename)
df.to_csv(filename, index=False, header=True, encoding="utf-8")


