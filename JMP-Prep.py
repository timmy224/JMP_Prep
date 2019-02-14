"""
Description: duplicates each row according to number of individuals and creates a new 
spreadsheet for JMP database (reads and creates CSV files only)

Requirements: make sure this script and the file you want to duplicate are in 
the same folder (directory level) 

Author: Timmy 
"""

import csv


with open('Prep-1_FG 95_Platypodinae.csv', 'r') as original:
    """change the 'source file' you want to copy in line 6 above"""
    """insert source file: file_name.csv between parentheses"""

    csv_reader = csv.reader(original)

    with open('JMP-Prep_Prep-1_FG 95_Platypodinae.csv', 'w') as new:
        """place output file name between parentheses"""
        csv_writer = csv.writer(new)

        csv_writer.writerow(next(csv_reader)) # copies header

        next(csv_reader, None) # skips header before iteration (for loop)

        for row in csv_reader:
            
            if int(row[4]) > 1: 
                """replace row[n] with n as the cell row position for 
                individuals (start counting with 0)"""

                for i in range(0, int(row[4])):
                    csv_writer.writerow(row)
            else: 
                csv_writer.writerow(row)
        
        

 

        


        
