#DBMS made easier to use and understand.

import os
import time
import openpyxl

dirCheck = os.listdir("C:/Personal Files/Programming/Software Dev/Python/Data Science/DBMS")
localtime = str(time.asctime(time.localtime(time.time())))

#creating new dataset files:
def create(filename):
    try:
        if filename in dirCheck:
            print("ERR-001")
            print("ERR-NOTICE: THE DATASET ALREADY EXISTS.")

        elif filename not in dirCheck:
            wb = openpyxl.Workbook()
            wb.save(f'C:/Personal Files/Programming/Software Dev/Python/Data Science/DBMS/{filename}.xlsx')
            wb = openpyxl.load_workbook(f'C:/Personal Files/Programming/Software Dev/Python/Data Science/DBMS/{filename}.xlsx')
            wb.properties.title = filename
            wb.properties.category = filename
            wb.properties.keywords = filename
            wb.save(f'C:/Personal Files/Programming/Software Dev/Python/Data Science/DBMS/{filename}.xlsx')
            wb.close()

    except Exception as e:
        print("ERR-101")
        print("ERR-NOTICE: UNKNOWN ERROR OCCURRED")

#searching the database for datasets:
def search(dataset):
    if dataset in dirCheck:
        searchResult = dirCheck
        print(searchResult)
        print(f"RECORDS FOUND AT C:/Personal Files/Programming/Software Dev/Python/Data Science/DBMS/{searchResult}")
    else:
        print("ERR-010")
        print("ERR-NOTICE: NO SUCH FILE FOUND!")

if __name__ == '__main__':
    while True:
        query = input(str("> "))
        query = query.split(" ")
        if "create" == query[0] or "-c" == query[0]:
            if "new" == query[1] or "-n" == query[1]:
                if "database" == query[3] or "dataset" == query[3] or "-db" == query[3]:
                    filename = input(str("TOPIC: "))
                    create(filename)
                    print("STATUS: A NEW DATA ENTRY CREATED")