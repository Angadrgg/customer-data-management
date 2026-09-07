# Customer Data Management & Verification System

This project is a complete **Extract, Transform, Load (ETL)** data pipeline built with Python, Pandas, and SQLite. It demonstrates the ability to ingest raw customer data (from Excel), apply data validation rules, store cleaned data in a relational database, and generate visual and tabular reports.

## Features
- **Data Extraction**: Reads messy customer data from `.xlsx`.
- **Data Validation**: Identifies duplicate records, validates email formatting using Regular Expressions, and flags missing essential information.
- **Data Loading**: Automatically provisions a SQLite database and inserts valid vs. flagged records into separate SQL tables.
- **Data Reporting & Visualization**: Generates SQL reports and uses Matplotlib to chart data validation results and customer status distributions.

## Tech Stack
- **Python**: Core logic, Regex, OS operations
- **Pandas**: Data manipulation, filtering, and Excel file handling
- **SQLite3**: Lightweight relational database for persistent storage
- **Matplotlib**: Data visualization (bar charts and pie charts)
- **SQL**: Querying cleaned data for reporting

## Setup and Execution

1. **Install Dependencies**
   ```bash
   pip install pandas openpyxl matplotlib
   ```

2. **Generate Mock Data**
   Creates a `raw_customers.xlsx` file with deliberate errors for testing.
   ```bash
   python generate_data.py
   ```

3. **Run the ETL Pipeline**
   Reads the raw data, applies validation rules, and saves to SQLite (`customers.db`).
   ```bash
   python data_pipeline.py
   ```

4. **Generate Visualizations**
   Creates PNG charts summarizing the cleaned data in the database.
   ```bash
   python visualize_data.py
   ```

## Project Structure
* `generate_data.py` - Script to generate the raw dataset.
* `data_pipeline.py` - The main ETL pipeline script.
* `visualize_data.py` - Generates analytical charts from the database.
* `reports.sql` - Sample SQL queries demonstrating data extraction.
