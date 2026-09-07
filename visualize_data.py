import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import os

def create_charts():
    # Connect to the local SQLite database
    conn = sqlite3.connect('customers.db')
    
    # --- Chart 1: Valid vs Flagged Customers (Pie Chart) ---
    # Query the counts from both tables
    valid_count = pd.read_sql("SELECT COUNT(*) as count FROM ValidCustomers", conn).iloc[0]['count']
    flagged_count = pd.read_sql("SELECT COUNT(*) as count FROM FlaggedCustomers", conn).iloc[0]['count']
    
    plt.figure(figsize=(6, 6))
    plt.pie([valid_count, flagged_count], 
            labels=['Valid Records', 'Flagged Records'], 
            autopct='%1.1f%%', 
            colors=['#4CAF50', '#F44336'], 
            startangle=90)
    plt.title('Data Validation Results')
    plt.savefig('validation_pie_chart.png')
    plt.close() # Close to prevent overlap with the next chart
    print("Success: Created validation_pie_chart.png")

    # --- Chart 2: Account Status Distribution (Bar Chart) ---
    # Query the grouping from the valid customers table
    status_df = pd.read_sql("SELECT AccountStatus, COUNT(*) as Count FROM ValidCustomers GROUP BY AccountStatus", conn)
    
    plt.figure(figsize=(8, 5))
    bars = plt.bar(status_df['AccountStatus'], status_df['Count'], color='#2196F3')
    plt.title('Valid Customers by Account Status')
    plt.xlabel('Account Status')
    plt.ylabel('Number of Customers')
    plt.yticks(range(0, int(status_df['Count'].max()) + 2)) # Keep Y-axis as whole numbers
    
    # Add the text counts above the bars
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 0.05, int(yval), ha='center', va='bottom')

    plt.savefig('account_status_bar.png')
    plt.close()
    print("Success: Created account_status_bar.png")

    conn.close()

if __name__ == "__main__":
    create_charts()
