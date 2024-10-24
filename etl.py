import pandas as pd
from datetime import datetime
from sqlalchemy import create_engine

# Step 1: Extract data from file
file_path = 'customer_data.csv'  # Your input data file
data = pd.read_csv(file_path, sep='|', skiprows=1, header=None)

# Assigning column names as per file structure
data.columns = ['Record_Type', 'Customer_Name', 'Customer_Id', 'Open_Date', 'Last_Consulted_Date',
                'Vaccination_Id', 'Doctor_Name', 'State', 'Country', 'DOB', 'Is_Active']

# Step 2: Transform - Process Data
# Convert dates to appropriate format
data['Open_Date'] = pd.to_datetime(data['Open_Date'], format='%Y%m%d')
data['Last_Consulted_Date'] = pd.to_datetime(data['Last_Consulted_Date'], format='%Y%m%d', errors='coerce')
data['DOB'] = pd.to_datetime(data['DOB'], format='%d%m%Y', errors='coerce')

# Calculate age (Derived Column)
data['Age'] = data['DOB'].apply(lambda dob: datetime.now().year - dob.year if pd.notnull(dob) else None)

# Calculate days since last consultation (Derived Column)
data['Days_Since_Last_Consult'] = (datetime.now() - data['Last_Consulted_Date']).dt.days

# Filter customers from India
india_data = data[data['Country'] == 'IND']

# Step 3: Load - Insert into corresponding country tables (Here: Table_India)
# SQLAlchemy engine to connect to the database
engine = create_engine('postgresql://username:password@localhost/dbname')

# Insert data into the India table
india_data[['Customer_Name', 'Customer_Id', 'Open_Date', 'Last_Consulted_Date', 'Vaccination_Id',
            'Doctor_Name', 'State', 'Country', 'DOB', 'Is_Active', 'Age', 'Days_Since_Last_Consult']].to_sql(
    'Table_India', engine, if_exists='append', index=False)

print("Data loaded successfully into Table_India.")
