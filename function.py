import csv
import os
import pandas as pd

# Define the CSV file name
csv_file = 'user_data.csv'

def register_user(user_id, ic_number):
    file_exists = os.path.isfile(csv_file)
    
    with open(csv_file, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['UserID', 'ICNumber', 'Income', 'TaxRelief', 'TaxPayable'])
        if not file_exists:
            writer.writeheader()
        writer.writerow({'UserID': user_id, 'ICNumber': ic_number, 'Income': '', 'TaxRelief': '', 'TaxPayable': ''})
    print(f"User {user_id} registered successfully.")

def is_user_registered(user_id):
    if not os.path.isfile(csv_file):
        return False
    
    with open(csv_file, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['UserID'] == user_id:
                return True
    return False

def authenticate_user(user_id, ic_last_4_digits):
    if not os.path.isfile(csv_file):
        return False
    
    with open(csv_file, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['UserID'] == user_id and row['ICNumber'][-4:] == ic_last_4_digits:
                return True
    return False

def calculate_tax(income, tax_relief):
    taxable_income = income - tax_relief
    tax = 0

    if taxable_income <= 5000:
        tax = 0
    elif taxable_income <= 20000:
        tax = (taxable_income - 5000) * 0.01
    elif taxable_income <= 35000:
        tax = 150 + (taxable_income - 20000) * 0.03
    elif taxable_income <= 50000:
        tax = 600 + (taxable_income - 35000) * 0.06
    elif taxable_income <= 70000:
        tax = 1500 + (taxable_income - 50000) * 0.11
    elif taxable_income <= 100000:
        tax = 3700 + (taxable_income - 70000) * 0.19
    elif taxable_income <= 400000:
        tax = 9400 + (taxable_income - 100000) * 0.25
    elif taxable_income <= 600000:
        tax = 84400 + (taxable_income - 400000) * 0.26
    elif taxable_income <= 2000000:
        tax = 136400 + (taxable_income - 600000) * 0.28
    else:
        tax = 528400 + (taxable_income - 2000000) * 0.30
    
    return tax

def save_to_csv(user_id, income, tax_relief, tax_payable, filename):
    temp_rows = []
    
    if os.path.isfile(filename):
        with open(filename, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['UserID'] == user_id:
                    temp_rows.append({'UserID': user_id, 'ICNumber': row['ICNumber'], 'Income': income, 'TaxRelief': tax_relief, 'TaxPayable': tax_payable})
                else:
                    temp_rows.append(row)
    
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['UserID', 'ICNumber', 'Income', 'TaxRelief', 'TaxPayable'])
        writer.writeheader()
        for row in temp_rows:
            writer.writerow(row)

def read_from_csv(filename):
    if not os.path.isfile(filename):
        return None
    
    return pd.read_csv(filename)
