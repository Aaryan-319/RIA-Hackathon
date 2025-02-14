import os

def log():
    logCheck = os.listdir("C:\\Personal Files\\Programming\\Software Dev\\Python\\Data Science\\DBMS\\logs")
    if "dbms.log" in logCheck:
        file = open("C:\\Personal Files\\Programming\\Software Dev\\Python\\Data Science\\DBMS\\logs\\dbms.log", '')