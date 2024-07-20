"""Handle login functionaly"""

import os
import csv
from datetime import datetime

headers = ["username","password","balance","donations"]

def initate_db():
    """ Initiates db file if it doesn't exists"""

    db_file = os.path.exists("./user_db.csv")
    if not db_file:
        with open('./user_db.csv','w',newline='') as csvfile:
            writer = csv.DictWriter(csvfile,fieldnames=headers)
            writer.writeheader()
            writer.writerow({
                "username":"admin",
                "password":"password",
                "balance":0.0,
                "donations":''
                })

def get_db():
    # get database file and return dictionary
    database = []
    with open('./user_db.csv', newline='') as csvfile:
        file = csv.DictReader(csvfile,delimiter=',')
        for row in file:
            database.append(row)

    return database


def write_db(db):
    # write database
    with open('./user_db.csv','w',newline='') as csvfile:
        writer = csv.DictWriter(csvfile,fieldnames=headers)
        writer.writeheader()
        for row in db:
            writer.writerow({
                'username':row['username'],
                'password':row['password'],
                'balance':float(row['balance']),
                'donations':row['donations']
                })

def register(db):
    username = input("\nCreate username: ")
    while check_users(db,username):
        print("user already exists - try again")
        username = input("\nCreate username: ")
    password = input("Create a password: ")

    updated_db = db

    updated_db.append({'username':username,'password':password,'balance':0,'donations':[]})

    update_db(updated_db)
    print(f"\n{username} Successfully Registered!\n")

def update_db(db):
    # update database after an action
    with open('./user_db.csv','w',newline='') as csvfile:
        writer = csv.DictWriter(csvfile,fieldnames=headers)
        writer.writeheader()
        for row in db:
            writer.writerow({
                'username':row['username'],
                'password':row['password'],
                'balance':float(row['balance']),
                'donations':row['donations']
                })


def donate(db,username):
    for row in db:
        if username == row['username']:
            donation_amt = input("How much would you like to donate? ")
            balance = float(row['balance']) + float(donation_amt)
            row['balance'] = balance
            donations_list = list(row['donations'])
            print(donations_list)
            donations_list.append(donation_amt)
            row['donations'] = donations_list
    update_db(db)

def show_donations(user):
    print(f"\n Donation History: ")
    donations_ls = eval(user['donations'])

    for donation in donations_ls:
        print(f"\n* {datetime.now()} - You've donated on {donation}")

    print(f"\nYour total donation balance is: ${user['balance']}")


def login_user(db,uname,password):
    # login to db, and grab user info
    for row in db:
        if row['username'] == uname and row['password'] == password:
            print("\nUser Successfully Authenticated")
            print(f"\nHello {row['username']}!")
            return row

    print("\nNot a valid User")
    return False

def check_users(db,uname):
    # Check if user already exists in db
    for row in db:
        if row['username'] == uname:
            return True
    return False
