import pandas as pd
import seaborn as sns
import matplotlib as plt
import matplotlib.pyplot as plt
import os

data = pd.read_csv(r'C:\Users\hp\Downloads\Walmart.csv')

output_folder = 'visualizations'
os.makedirs(output_folder, exist_ok=True)

def save_plot(filename):
    """Save the current figure with the given filename."""
    plt.savefig(f'{output_folder}/{filename}', bbox_inches='tight')
    print(f"Figure saved as {output_folder}/{filename}")


data.head(7) #Display the first and last few rows for confirmation
data.tail(7)

data.describe()   #Quick overview of the dataset
data.shape  

dup_data = data.duplicated().any()
print('Are there any duplicated values in the data? =', dup_data) 


data.isnull()  #Check for null values
data.isnull().sum()

data['Date'] = data['Date'].ffill()  #Since we have nulls fill missing dates with the last known valid date


#1. What are the Top 5 stores with the highest sales? How do stores differ in their overall performance?

data1 = data.groupby('Store')['Weekly_Sales'].agg(Total_Weekly_Sales='sum', Average_Weekly_Sales='mean').reset_index()


top_5_stores = data1.sort_values(by='Total_Weekly_Sales', ascending=False).head(5)  #Top 5 stores by total weekly sales

#Bar plot for Top 5 stores
plt.figure(figsize=(10, 6))
sns.barplot(x=top_5_stores['Store'], y=top_5_stores['Total_Weekly_Sales'], palette="Blues_d")
plt.title('Top 5 Stores by Total Weekly Sales', fontsize=16)
plt.xlabel('Store', fontsize=12)
plt.ylabel('Total Weekly Sales', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
save_plot('top_5_stores.png')  
plt.show()

#Contribution of top 5 stores to overall sales
top_5_contribution = top_5_stores['Total_Weekly_Sales'].sum() / data1['Total_Weekly_Sales'].sum() * 100
print(f"The top 5 stores contribute {top_5_contribution:.2f}% of total weekly sales.")

#Box plot for overall performance (distribution of weekly sales across stores)
plt.figure(figsize=(12, 6))
sns.boxplot(data=data, x='Store', y='Weekly_Sales', palette='Set2')
plt.title('Weekly Sales Distribution Across Stores', fontsize=16)
plt.xlabel('Store', fontsize=12)
plt.ylabel('Weekly Sales', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
save_plot('weekly_sales_boxplot.png')  
plt.show()



#2. What is the distribution of sales over time, and are there any noticeable seasonal trends?
data['Date'] = pd.to_datetime(data['Date'], format='mixed', dayfirst=True) 
data['Year_Month'] = data['Date'].dt.to_period('M') #Extract Year and Month from the Date


monthly_sales = data.groupby('Year_Month')['Weekly_Sales'].sum() #Aggregate weekly sales by Year-Month

plt.figure(figsize=(16, 6))  #Distribution of Sales over time visualised
sns.lineplot(x=monthly_sales.index.astype(str), y=monthly_sales.values)
plt.title('Monthly Sales over Time')
plt.xlabel('Month')
plt.ylabel('Total Weekly Sales')
plt.xticks(rotation=45)
save_plot('monthly_sales_over_time.png')
plt.show()

"""
The line plot reveals that weekly sales peak in December for both 2011 and 2012, 
indicating a strong seasonal trend. This suggests that December is a critical sales 
period, likely driven by holiday demand, and stores should plan for increased sales 
by adjusting inventory and launching targeted marketing campaigns during this time.
"""



#3. What factors contribute to the highest sales?

monthly_sales = data.groupby('Year_Month')['Weekly_Sales'].sum().reset_index()  #Aggregate Weekly Sales by Year_Month to get Total Monthly Sales

monthly_sales.rename(columns={'Weekly_Sales': 'Total_Monthly_Sales'}, inplace=True)  #Rename column to 'Total_Monthly_Sales'

data_with_monthly_sales = data.merge(monthly_sales, on='Year_Month', how='left') #Merge monthly sales data back into original dataframe

print(data_with_monthly_sales.head())

#Visualisation of Total Monthly Sales over Time
plt.figure(figsize=(16, 6))
sns.lineplot(x=monthly_sales['Year_Month'].astype(str), y=monthly_sales['Total_Monthly_Sales'])
plt.title('Total Monthly Sales over Time')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
save_plot('total_monthly_sales_over_time.png')
plt.show()


#Now use Total Monthly Sales for factor analysis
data_with_monthly_sales = data.merge(monthly_sales, on='Year_Month')

#Group by Year_Month and calculate means for factor analysis
monthly_combined = data_with_monthly_sales.groupby('Year_Month').mean()

#CPI vs Total Monthly Sales
plt.figure(figsize=(10, 6))
sns.scatterplot(data=monthly_combined, x='CPI', y='Total_Monthly_Sales', s=100)
plt.title('CPI vs Total Monthly Sales')
plt.xlabel('CPI')
plt.ylabel('Total Monthly Sales')
save_plot('CPI_vs_total_monthly_sales.png')
plt.show()

#Temperature vs Total Monthly Sales
plt.figure(figsize=(10, 6))
sns.scatterplot(data=monthly_combined, x='Temperature', y='Total_Monthly_Sales', s=100)
plt.title('Temperature vs Total Monthly Sales')
plt.xlabel('Temperature')
plt.ylabel('Total Monthly Sales')
save_plot('temperature_vs_total_monthly_sales.png')
plt.show()

#Fuel Price vs Total Monthly Sales
plt.figure(figsize=(10, 6))
sns.scatterplot(data=monthly_combined, x='Fuel_Price', y='Total_Monthly_Sales', s=100)
plt.title('Fuel Price vs Total Monthly Sales')
plt.xlabel('Fuel Price')
plt.ylabel('Total Monthly Sales')
save_plot('fuel_price_vs_total_monthly_sales.png')
plt.show()


"""
The analysis of scatter plots reveals that CPI does not have a consistent or strong impact on weekly sales, with sales 
fluctuating at various CPI levels. Temperature shows a more noticeable trend, with sales rising between 50-60°F, slightly 
declining between 60-70°F, and increasing significantly in the 70-80°F range, suggesting a positive correlation with higher 
temperatures. Fuel price exhibits a more variable relationship with sales, where higher fuel prices sometimes correspond with 
increased sales, but this pattern is inconsistent across different price levels. Overall, while temperature appears to influence
sales more clearly, CPI and fuel price do not show strong, predictable effects on weekly sales.
"""
 


#4. What is the average sales per store, and how does it compare across different stores?

average_sales_per_store = data.groupby('Store')['Weekly_Sales'].mean()
print(average_sales_per_store)

plt.figure(figsize=(16, 6))  #Visualise data using lineplot
sns.lineplot(x=average_sales_per_store.index.astype(str), y=average_sales_per_store)
plt.title('Average Weekly Sales Across Stores')
plt.xlabel('Store')
plt.ylabel('Average Weekly Stores')
plt.xticks(rotation=45)
save_plot('average_weekly_sales_across_stores.png')
plt.show()

"""
The line plot of weekly sales across different stores shows some interesting patterns. 
Stores 13 and 14 exhibit identical sales, while stores 34 and 35 are closely matched as well. 
Additionally, store 2 shows a noticeable dip in sales compared to others, and store 10 stands out with relatively higher sales. 
Most stores have a consistent range of weekly sales, with some slight fluctuations, suggesting overall stability in their performance. 
However, there are a few stores, like store 1 and store 6, that show more variability, indicating that their sales performance 
might be more sensitive to external factors or inconsistencies.
"""



#5. How do holiday weeks impact sales compared to non-holiday weeks?

holiday_sales_avg = data[data['Holiday_Flag'] == 1]['Weekly_Sales'].mean()
non_holiday_sales_avg = data[data['Holiday_Flag'] == 0]['Weekly_Sales'].mean()

sales_data_avg = {
    'Week Type': ['Holiday', 'Non-Holiday'],
    'Average Weekly Sales': [holiday_sales_avg, non_holiday_sales_avg]
}

sales_avg_df = pd.DataFrame(sales_data_avg)

#Plot average weekly sales
plt.figure(figsize=(8, 5))
sns.barplot(x='Week Type', y='Average Weekly Sales', data=sales_avg_df, palette='Blues_d')
plt.title('Average Weekly Sales: Holiday vs Non-Holiday Weeks')
plt.xlabel('Week Type')
plt.ylabel('Average Weekly Sales')
save_plot('avg_sales_holiday_vs_non_holiday.png')
plt.show()

'''
Sales during holiday weeks are higher than non-holiday weeks, highlighting the importance of holidays in driving revenue. 
The difference underscores the need to allocate resources and prepare for increased demand during holidays.
'''

#6. Is there any correlation between unemployment rates and weekly sales?

data2 = data.groupby('Unemployment')['Weekly_Sales'].sum().reset_index()
data2

sns.regplot(data=data, x='Unemployment', y='Weekly_Sales', ci=None, scatter_kws={'alpha':0.6}, line_kws={'color':'red'})
plt.title("Relationship Between Unemployment and Weekly Sales")
plt.xlabel("Unemployment Rate")
plt.ylabel("Weekly Sales")
save_plot('relationship_between_unemployment_and_weekly_sales.png')
plt.show()  #Visualise the data with a scatter plot with trendline


'''
The scatter plot shows a negative correlation between unemployment and weekly sales, with higher unemployment rates generally corresponding to 
sales. The downward slope of the red trendline suggests that as unemployment increases, weekly sales tend to decrease, indicating that economic 
hardship may reduce consumer spending.
'''

import time

#Add a delay to allow rendering
time.sleep(2)



data_with_monthly_sales.to_csv('updated_data.csv', index=False)  #Saves without the index column
data_with_monthly_sales.to_csv(r'C:\Users\hp\OneDrive\Desktop\updated_data.csv', index=False)


