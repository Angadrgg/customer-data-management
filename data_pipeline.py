import pandas as pd
import sqlite3
import re

def validate_email(email):
    """Simple regex to validate email format."""
    if pd.isna(email):
        return False
    # Check for basic email pattern (e.g., name@domain.com)
    return bool(re.match(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,4}$", str(email)))

def run_pipeline():
    print("1. Loading raw data from Excel...")
    try:
        df = pd.read_excel('raw_customers.xlsx')
    except FileNotFoundError:
        print("Error: raw_customers.xlsx not found. Run generate_data.py first.")
        return
    
    print("\n2. Validating Data (Python/Pandas)...")
    # Rule 1: Identify duplicates (keep the first occurrence)
    df['IsDuplicate'] = df.duplicated(subset=['CustomerID'], keep='first')
    
    # Rule 2: Validate Emails
    df['HasValidEmail'] = df['Email'].apply(validate_email)
    
    # Rule 3: Check for missing critical fields (Name)
    df['HasMissingName'] = df['FullName'].isna()
    
    # Create a mask for invalid records
    invalid_mask = df['IsDuplicate'] | ~df['HasValidEmail'] | df['HasMissingName']
    
    # Split the dataset
    invalid_records = df[invalid_mask].copy()
    valid_records = df[~invalid_mask].copy()
    
    # Clean up validation helper columns from valid records before saving
    cols_to_drop = ['IsDuplicate', 'HasValidEmail', 'HasMissingName']
    valid_records = valid_records.drop(columns=cols_to_drop)
    
    print(f"   -> Found {len(valid_records)} valid records and {len(invalid_records)} flagged records.")
    print(f"   -> Flagged reasons: Duplicates ({df['IsDuplicate'].sum()}), Invalid Emails ({(~df['HasValidEmail']).sum()})")
    
    print("\n3. Storing data in SQL Database (SQLite)...")
    # Connect to local SQLite database (creates file if it doesn't exist)
    conn = sqlite3.connect('customers.db')
    
    # Save valid and invalid records to separate SQL tables
    valid_records.to_sql('ValidCustomers', conn, if_exists='replace', index=False)
    invalid_records.to_sql('FlaggedCustomers', conn, if_exists='replace', index=False)
    
    print("   -> Data successfully inserted into SQL tables 'ValidCustomers' and 'FlaggedCustomers'.")
    
    print("\n4. Generating clean reports...")
    # Export the clean dataset back to Excel for stakeholders
    valid_records.to_excel('clean_customers.xlsx', index=False)
    print("   -> Exported clean records to 'clean_customers.xlsx'.")
    
    # Example SQL Query inside Python to generate a quick report
    print("\n--- Quick SQL Report: Customer Count by Status ---")
    cursor = conn.cursor()
    cursor.execute("SELECT AccountStatus, COUNT(*) as Count FROM ValidCustomers GROUP BY AccountStatus")
    rows = cursor.fetchall()
    for row in rows:
        print(f"Status: {row[0]} | Count: {row[1]}")
    
    conn.close()
    print("\nPipeline execution complete!")

if __name__ == "__main__":
    run_pipeline()
