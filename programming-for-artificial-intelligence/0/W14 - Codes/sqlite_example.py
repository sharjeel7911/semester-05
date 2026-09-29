#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 15:29:55 2026

@author: awais
"""

import sqlite3

def run_sqlite_crud_pipeline():
    # 1. CONNECT & INITIALIZE
    # If 'academic_records.db' doesn't exist, SQLite handles creation automatically
    conn = sqlite3.connect('new_academic_records.db')
    cursor = conn.cursor()
    
    print("--- 1. [CREATE] Setting up Schema and Inserting Records ---")
    # Initialize a sample relational table structure
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS target_students (
            roll_no TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            cgpa REAL,
            department TEXT
        )
    """)
    
    # Secure Parametric Insertion using '?' placeholders to prevent injection
    new_students = [
        ("UCP-101", "Hamza Ali", 3.42, "CS"),
        ("UCP-102", "Zainab Fatima", 3.85, "SE"),
        ("UCP-103", "Bilal Khan", 2.10, "EE")
    ]
    cursor.executemany("INSERT OR IGNORE INTO target_students VALUES (?, ?, ?, ?)", new_students)
    conn.commit() # Save changes structurally to disk
    print(f"Successfully inserted {len(new_students)} student profiles.")

    print("\n--- 2. [READ] Fetching Dynamic Data Profiles ---")
    # Fetch students with a CGPA above a safe threshold parameter
    threshold_cgpa = 3.0
    cursor.execute("SELECT name, cgpa FROM target_students WHERE cgpa > ?", (threshold_cgpa,))
    
    # fetchall() extracts the remaining rows as a clean Python list of tuples
    high_achievers = cursor.fetchall()
    for student in high_achievers:
        print(f"High Achiever Student Record -> Name: {student[0]} | CGPA: {student[1]}")

    print("\n--- 3. [UPDATE] Modifying Active Field Matrix Values ---")
    # Grade update processing step
    target_roll = "UCP-103"
    updated_cgpa = 2.45
    cursor.execute("UPDATE target_students SET cgpa = ? WHERE roll_no = ?", (updated_cgpa, target_roll))
    conn.commit()
    print(f"Updated status profile for student {target_roll}. Rows modified: {cursor.rowcount}")

    print("\n--- 4. [DELETE] Purging Database Records ---")
    # Clean up an unwanted entry trace profile
    purge_target = "UCP-101"
    cursor.execute("DELETE FROM target_students WHERE roll_no = ?", (purge_target,))
    conn.commit()
    print(f"Purged profile target {purge_target}. Active rows dropped: {cursor.rowcount}")

    # Explicit resource closing lifecycle pipeline step
    cursor.close()
    conn.close()

if __name__ == "__main__":
    run_sqlite_crud_pipeline()