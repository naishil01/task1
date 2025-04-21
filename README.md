# task1
internship(task1: data cleaning and preprocessing
Includes the First task: Data Cleaning and Preprocessing Objective: Clean and prepare a raw dataset (with nulls, duplicates, inconsistent formats). Converted the Date_Added column for fixing datatypes to datetime format using pd.to_datetime(), handling invalid entries with errors='coerce' for consistent date format.

Filled missing values in the Date_Added column with a default date (2023-01-01) to ensure consistency in time-based analysis.

Standardized country names, including handling multiple countries in a single row, by splitting entries, mapping them to short codes (e.g., 'India' → 'IN'), and rejoining them.

Removed duplicate rows using .drop_duplicates() to maintain data integrity.

Dropped unnecessary columns like country_cleaned and country_code after standardization.

Formatted Date_Added for display as YYYY-MM-DD using .dt.strftime('%Y-%m-%d').

THE SOURCE FILE IS IN:Task-1.py
