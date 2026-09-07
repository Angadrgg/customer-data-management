import pandas as pd

def generate_mock_data():
    data = {
        'CustomerID': [101, 102, 103, 104, 105, 106, 101], # 101 is a duplicate
        'FullName': ['Alice Smith', 'Bob Jones', 'Charlie Brown', 'Diana Prince', 'Evan Wright', 'Fiona Gallagher', 'Alice Smith'],
        'Email': ['alice@example.com', 'bob.jones@email', 'charlie@example.com', None, 'evan@example.com', 'fiona@example.com', 'alice@example.com'], # Bob has invalid email format, Diana has no email
        'Phone': ['555-0101', '555-0102', None, '555-0104', '555-0105', '555-0106', '555-0101'], # Charlie has no phone
        'AccountStatus': ['Active', 'Active', 'Inactive', 'Active', 'Pending', 'Active', 'Active'],
        'JoinDate': ['2023-01-15', '2023-02-20', '2023-03-05', '2023-04-12', '2023-05-18', '2023-06-25', '2023-01-15']
    }

    df = pd.DataFrame(data)
    
    # Save to Excel
    file_path = 'raw_customers.xlsx'
    df.to_excel(file_path, index=False)
    print(f"Success: Created {file_path} with mock data.")

if __name__ == "__main__":
    generate_mock_data()
