import csv
import random
from datetime import datetime, timedelta
import string

class Deposit:
    def __init__(self, deposit_id, interest_rate_id, deposit_date, amount, account_number, bank_id, worker_id):
        self.deposit_id = deposit_id
        self.interest_rate_id = interest_rate_id
        self.deposit_date = deposit_date
        self.amount = amount
        self.account_number = account_number
        self.bank_id = bank_id
        self.worker_id = worker_id

def generate_unique_deposit_id(used_deposit_ids):
    while True:
        deposit_id = str(random.randint(1000, 9999))  # Generate a random 4-digit number
        if deposit_id not in used_deposit_ids:
            used_deposit_ids.add(deposit_id)
            break
    return deposit_id

def read_interest_rates(filename):
    interest_rates = []
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header
        for row in reader:
            interest_rates.append(row[0])
    return interest_rates

def generate_unique_interest_rate_id(interest_rates):
    return random.choice(interest_rates)

def generate_random_date(start_date, end_date):
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return start_date + timedelta(days=random_days)

def generate_random_amount():
    return round(random.uniform(100, 10000), 2)

def generate_random_account_number():
    return ''.join(random.choices(string.digits, k=10))

def read_bank_ids(filename):
    bank_ids = []
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header
        for row in reader:
            bank_ids.append(row[0])
    return bank_ids

def generate_random_worker_id(used_worker_ids):
    while True:
        worker_id = str(random.randint(1000, 9999))
        if worker_id not in used_worker_ids:
            used_worker_ids.add(worker_id)
            break
    return worker_id

def generate_random_deposit(bank_ids, interest_rates, used_deposit_ids, used_account_numbers, used_worker_ids):
    deposit_id = generate_unique_deposit_id(used_deposit_ids)
    interest_rate_id = generate_unique_interest_rate_id(interest_rates)
    deposit_date = generate_random_date(datetime(2020, 1, 1), datetime(2023, 12, 31))
    amount = generate_random_amount()

    account_number = random.choice(used_account_numbers)
    bank_id = random.choice(bank_ids)
    worker_id = generate_random_worker_id(used_worker_ids)

    return Deposit(deposit_id, interest_rate_id, deposit_date, amount, account_number, bank_id, worker_id)

def write_to_csv(deposits):
    with open("deposit.csv", 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        # Write headers
        writer.writerow(['Deposit_ID', 'Interest_Rate_ID', 'Deposit_Date', 'Amount', 'Account_Number', 'Bank_ID', 'Worker_ID'])

        # Write deposit data
        for deposit in deposits:
            writer.writerow([deposit.deposit_id, deposit.interest_rate_id, deposit.deposit_date.strftime('%Y-%m-%d'), deposit.amount, 
                             deposit.account_number, deposit.bank_id, deposit.worker_id])

def main():
    # Read existing data or generate if necessary
    bank_ids = read_bank_ids('bank.csv')
    interest_rates = read_interest_rates('interest_rate.csv')
    used_deposit_ids = set()
    used_account_numbers = [generate_random_account_number() for _ in range(100)]  # Assuming 100 existing accounts
    used_worker_ids = set()  # Initialize set to store used worker IDs

    # Generate 200 random deposits
    deposits = [generate_random_deposit(bank_ids, interest_rates, used_deposit_ids, used_account_numbers, used_worker_ids) for _ in range(200)]

    # Write deposits to CSV file
    write_to_csv(deposits)

if __name__ == "__main__":
    main()
