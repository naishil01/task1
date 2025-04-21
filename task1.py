import pandas as pd
import numpy as np
# Load the dataset
df = pd.read_csv(r"C:\Users\ADMIN\Downloads\archive\netflix_titles.csv")
# Check for missing values
df['director'] = df['director'].fillna("Na")
df['cast'] = df['cast'].fillna("Na")
df['country'] = df['country'].fillna("Na")
df['duration'] = df['duration'].fillna("Na")
df['date_added'] = df['date_added'].fillna("Na")
df['rating'] = df['rating'].fillna("Not Rated")
print(df.isnull().sum())
# Remove duplicate rows
duplicates = df.duplicated()
print(duplicates.sum())
df = df.drop_duplicates()
country_map={
    "Australia":"AUS",
    "Argentina":"ARG",
    "Austria":"AUT",
    "Bangladesh":"BAN",
    "Belarus":"BLR",
    "Belgium":"BEL",
    "Brazil":"BRA",
    "Bulgaria":"BGR",
    "Canada":"CAN",
    "Chile":"CHL",
    "Columbia":'COL',
    'Guatemala': 'GT',
    'Hungary': 'HU',
    'Iceland': 'IS',
    'India': 'IN',
    'Indonesia': 'ID',
    'Iran': 'IR',
    'Ireland': 'IE',
    'Israel': 'IL',
    "United States":"USA",
    "United Kingdom":"UK",
    "South Korea":"KOR",
    "Czech Republic":"CZE",
    "Cayman Islands":"CAY",
    "South Africa":"SA",
    "New Zealand":"NZ",
    "United Arab Emirates":"UAE",
    "Phillippines":"PH",
    "Luxembourg":"LUX",
    "Hong Kong":"HK",
    "South Africa":"SA",
    "Switzerland":"CHE",
    "Sweden":"SE",
    "Syria":"SY",
    "Taiwan":"TW",
    "Thailand":"TH",
    "Turkey":	"TR",
    "Ukraine"	:"UA",
    "Uruguay": "UY",
    "Venezuela": "VE",
    "Vietnam": "VN",
    "Germany": "GER",
    "Zimbabwe": "ZW"
}
df['country_cleaned'] = df['country'].str.split(',').str[0].str.strip()
df['country_code'] = df['country_cleaned'].map(country_map)
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
# Format as 'dd-mm-yyyy' (convert datetime to string format)
df['date_added'] = df['date_added'].dt.strftime('%d-%m-%Y')
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce',dayfirst=True)
print(df.dtypes)
print(df)


