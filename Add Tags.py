- Adding a column to excel sheet containing the output filter of drugs depending on their category first then their prices.
- i used pandas in python to create func to tag drugs to (A,B,C) using their category and prices


# Code
def categorize_price(row):
    category = row['Drug Category']
    price = row['Price']

    # Calculate the percentiles for the current category
    category_prices = df[df['Drug Category'] == category]['Price']   # all rowss prices of one category
    low = category_prices.quantile(0.33)
    high = category_prices.quantile(0.66)

    # Categorize based on percentiles
    if price <= low:
        return 'C'
    elif price <= high:
        return 'B'
    else:
        return 'A'

# Apply the function to each row in the DataFrame
df['Price Category'] = df.apply(categorize_price, axis=1)



# Output
df[df['Drug Category'] == 'Antibiotic']['Price']
3     406.58
28    165.62
30    201.60
55    270.59
61    380.77
75    385.17
78     47.34
83    113.49
98    349.24


df[df['Drug Category'] == 'Antibiotic']['Price'].quantile(0.33)
188.476
