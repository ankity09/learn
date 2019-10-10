#Given customer bank saving data customer-savings.txt, please answer the following questions using Python #programming.
#What’s the average balance for male and female?
#What’s the average balance for while collar and blue collar in England?
#Data columns in customer-savings.txt (separated by comma):
#Customer ID, Customer Name, Customer Surname, Gender, Age, Region, Job Classification, Date joined, Balance #100000001,Simon,Walsh,Male,21,England,White Collar,05.Jan.15,113810.15 #100000003,Liam,Brown,Male,46,England,White Collar,07.Jan.15,101536.83

import pandas as pd

customer_data = pd.read_csv("customer-savings.txt", sep = ",")
customer_data.columns = ["Customer ID", "Customer Name", "Customer Surname","Gender", "Age", "Region", "Job Classification", "Date joined", "Balance"]
gender_mean = customer_data.groupby('Gender')['Balance'].mean()
collar = customer_data[customer_data['Region'] == 'England'].groupby('Job Classification')['Balance'].mean()
print(gender_mean,"\n")
print(collar)

#Combine multiple files
#Use Python programming to combine two text files: customer-status.txt and sales.txt
#Data columns in customer-status.txt (separated by comma):
#Account Number, Name, Status 527099,Sanford and Sons,bronze
#Data columns in sales.txt (separated by comma):
#Account Name, Name, SKU, Quantity, Unit Price, Ext Price, Date
#163416,Purdy-Kunde,S1-30248,19,65.03,1235.57,2014-03-01 16:07:40 527099,Sanford and #Sons,S2-82423,3,76.21,228.63,2014-03-01 17:18:01
#After you combine, you will see the following:
#527099,Sanford and Sons,S2-82423,3,76.21,228.63,2014-03-01 17:18:01,bronze

import pandas as pd

customer_status = pd.read_csv('customer-status.csv')
sales = pd.read_csv('sales.csv')

combined = customer_status.merge(sales)
export_csv = combined.to_csv (r'/Users/ankityadav/Desktop/Fall_2019/PDA/combined.csv', index = None, header=True)
