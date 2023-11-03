import os
import csv
import logging
from distutils.log import debug
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)
# Set up logging
logs_dir = os.path.join(os.getcwd(), 'logs')
os.makedirs(logs_dir, exist_ok=True)

# Load passwords from the CSV file into a dictionary
passwords = {}
with open('Passwords.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        passwords[row['Domain']] = {"userName":row['UserName'],"password": row['Password']}


@app.route('/get-password', methods=['POST'])
def get_password():
    print(request.data)
    data = request.get_json()
    domain = data.get('domain') 
    creds = passwords.get(domain)
    # Get the current date
    current_date = datetime.now().strftime('%Y-%m-%d')
    
    # Create a folder for the current date if it doesn't exist
    date_folder = os.path.join(logs_dir, current_date)
    os.makedirs(date_folder, exist_ok=True)
    
    # Create a log file within the respective date folder
    log_file = os.path.join(date_folder, f'requests_{current_date}.log')
    
    # Set up logging for the current log file
    logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(message)s')
    
    # Log the request to the file
    logging.info(f'Request - Domain: {domain}, Creds: {creds}')


    if creds:
        return jsonify(creds)
    else:
        return jsonify({'error': 'Domain not found'}), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000,debug='true')