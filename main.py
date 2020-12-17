import pandas as pd

#UK holidays 2021

# Clean up steps into its own function
def holiday_table(table):
    # Returns a clean dataframe of holiday table.
    table = table.drop([0])
    table.columns = ["Date", "Day of Week", "Holiday Name", "Holiday Type", "Details"]
    table = table.reset_index(drop=True)
    return table


url = "https://www.timeanddate.com/holidays/uk/2021"

data = pd.read_html(url)

df = holiday_table(data[0])

print(df)


