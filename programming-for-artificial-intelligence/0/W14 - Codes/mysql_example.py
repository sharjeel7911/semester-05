#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 15:44:01 2026

@author: awais
"""

import pymysql
from pymysql.constants import CLIENT

def run_mysql_northwind_crud_fixed():
    # PyMySQL handles modern authentication handshakes natively
    config = {
        'user': 'root',
        'password': '',
        'host': '127.0.0.1',
        'database': 'northwind',
        'cursorclass': pymysql.cursors.Cursor # Standard default cursor layout
    }
    
    try:
        # Establish the connection stream
        conn = pymysql.connect(**config)
        cursor = conn.cursor()
        print("Connected successfully using PyMySQL!")
        
        # --- [CREATE] Example ---
        insert_query = """
            INSERT INTO Suppliers (id, Company, last_name, address) 
            VALUES (%s, %s, %s, %s)
        """
        supplier_data = (30, "Lahore Software Tech", "Dr. Ahmad Kazmi", "Pakistan")
        
        cursor.execute(insert_query, supplier_data)
        conn.commit()
        print(f"Supplier Record Created successfully.")
        
        # Clean up local environment resources
        cursor.close()
        conn.close()

    except Exception as e:
        print(f"Critical Exception raised: {e}")

if __name__ == "__main__":
    run_mysql_northwind_crud_fixed()