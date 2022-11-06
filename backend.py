#import os
from pyairtable import Table
from pyairtable import Api, Base, Table
import pandas as pd
import datetime
import time

pd.set_option('display.expand_frame_repr', False)

print("########################################################################################################################################")
#all data
global df

#total orders
global total_number_of_orders

#total orders this month 
global total_orders_this_month

#number of orders in progress
global number_of_orders_in_progress

#revenue
global total_revenue

#list of recent orders
global recent_orders_df

#Order frequency by product
global list2

#update time
global update_time
update_time = time.strftime("%Y-%m-%d %H:%M:%S")
print("update time: ")
print(update_time)
print("\n")



#api call to get data
#data can be imported directly into sqlite or other database and processed on server
#not all data needs to be requested, to make application more lightweight
#mutiple calls to request specifics can be used
#-----------------------------------------------------------------------------------------------------------------------
#api_key = os.environ["keyRB4GdffI7b0iS2"]
table = Table("keyRB4GdffI7b0iS2", 'app8wLQrrIMrnn673', 'Orders')#credentials can be in encrypted config.ini file in prod
data = table.all()
#print(data)
#-----------------------------------------------------------------------------------------------------------------------




#data tranferred into pandas dataframe for handling
#-----------------------------------------------------------------------------------------------------------------------
print("-----------------------------------------------------------------------------------------------------------------------")
print("All raw data from API: ")
df = pd.DataFrame.from_dict(data) # read into pandas dataframe
df = pd.concat([df.drop(['fields'], axis=1), df['fields'].apply(pd.Series)], axis=1) #fields dict mapped into remaining columns
print(df) # data output only for reference
print("-----------------------------------------------------------------------------------------------------------------------")
print("\n")
#-----------------------------------------------------------------------------------------------------------------------


#Total number of orders
#-----------------------------------------------------------------------------------------------------------------------
print("-----------------------------------------------------------------------------------------------------------------------")
print("Total number of orders: ")
total_number_of_orders = len(df. index)
print(total_number_of_orders)
print("-----------------------------------------------------------------------------------------------------------------------")
print("\n")
#-----------------------------------------------------------------------------------------------------------------------


#Total orders this month
#this is done assuming the month is october and year is 2021 as this is the timeframe of the data (10/2021) if records to appear here
#current month returns no records
#-----------------------------------------------------------------------------------------------------------------------
print("-----------------------------------------------------------------------------------------------------------------------")
df['order_placed'] = pd.to_datetime(df['order_placed']) # convert to pd.datetime
#df = df.sort_values(by='order_placed',ascending=False)
#print("date converted df")
date_time_month = datetime.datetime.now().month #current date month (change to 10 to see records)
date_time_year = datetime.datetime.now().year #current date year (change to 2021 to see records)
#print("This months orders: ")
df_this_month = df.loc[(df['order_placed'].dt.month==int(date_time_month))] #filter order date by current month
df_this_month  = df_this_month .loc[(df['order_placed'].dt.year==int(date_time_year))] # filter order date by current year
df_this_month  = df_this_month .sort_values(by='order_placed',ascending=False)
total_orders_this_month = len(df_this_month. index)
#print(df_this_month )
print("Total orders this month: ")
print(total_orders_this_month)
print("-----------------------------------------------------------------------------------------------------------------------")
print("\n")
#-----------------------------------------------------------------------------------------------------------------------


#Total number of orders in progress
#-----------------------------------------------------------------------------------------------------------------------
print("-----------------------------------------------------------------------------------------------------------------------")
print("Total number or orders in progress: ")
#print(df['order_status'].value_counts()) # method of getting counts of all values in column
number_of_orders_in_progress = len(df[df['order_status'] == 'in_progress'])
print(number_of_orders_in_progress)
print("-----------------------------------------------------------------------------------------------------------------------")
print("\n")
#-----------------------------------------------------------------------------------------------------------------------


#Total revenue
#-----------------------------------------------------------------------------------------------------------------------
print("-----------------------------------------------------------------------------------------------------------------------")
print("Total revenue: ")
total_revenue = df['price'].sum()
print(total_revenue)
print("-----------------------------------------------------------------------------------------------------------------------")
print("\n")
#-----------------------------------------------------------------------------------------------------------------------


#list of most recent orders
#-----------------------------------------------------------------------------------------------------------------------
print("-----------------------------------------------------------------------------------------------------------------------")
print("A list recent orders: ")
df= df.sort_values(by='order_placed',ascending=False)
#print(df)
recent_orders_df = df.head(n=10)
# recent_orders_df= recent_orders_df.reset_index(drop=True)
# recent_orders_df.reset_index(drop=True, inplace=True)
#recent_orders_df.reset_index(drop=True, inplace=True)
# recent_orders_df['id'] = recent_orders_df.index
#recent_orders_df= recent_orders_df.reset_index(drop=True, inplace=True)
#recent_orders_df = recent_orders_df.to_string(index=False)
print(recent_orders_df)
print("-----------------------------------------------------------------------------------------------------------------------")
print("\n")
#-----------------------------------------------------------------------------------------------------------------------


#Order frequency by product
#-----------------------------------------------------------------------------------------------------------------------
print("-----------------------------------------------------------------------------------------------------------------------")
print("Number of each product ordered")
orders_by_product = str(df['product_name'].value_counts())
#print(orders_by_product)
#print(df['product_name'].unique().tolist())
list1= df['product_name'].unique().tolist()
list2 = []

for x in list1:
    #print(str(x) +": " +str(df['product_name'].value_counts()[x]))
    y = str(x) +": " +str(df['product_name'].value_counts()[x])
    list2.append(y)

print(list2)
# orders_by_product = orders_by_product.splitlines()
#print(orders_by_product)
print("-----------------------------------------------------------------------------------------------------------------------")
print("\n")



print("########################################################################################################################################")