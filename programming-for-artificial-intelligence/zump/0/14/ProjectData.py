#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 08:53:04 2026

@author: awais
"""

import os
import sqlite3
import pandas as pd

def create_project_database(db_path):
    """Creates a SQLite database at the given path and initializes the

    Advisor, Project, and ProjectMember tables.
    """
    # Ensure the directory path exists before creating the database
    dir_name = os.path.dirname(db_path)
    if dir_name and not os.path.exists(dir_name):
        os.makedirs(dir_name)

    conn = None
    try:
        # Connect to the database (it will be created if it doesn't exist)
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # CRITICAL: Enable foreign key support in SQLite
        cursor.execute("PRAGMA foreign_keys = ON;")

        # 1. Create Advisor Table
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS Advisor (
                aid INTEGER PRIMARY KEY AUTOINCREMENT,
                AdvisorName TEXT NOT NULL,
                AdvisorEmail TEXT NOT NULL
            );
        """
        )

        # 2. Create Project Table
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS Project (
                pid INTEGER PRIMARY KEY AUTOINCREMENT,
                ProjectId TEXT NOT NULL UNIQUE,
                ProjectName TEXT NOT NULL,
                aid INTEGER,
                FOREIGN KEY (aid) REFERENCES Advisor(aid) 
                    ON DELETE SET NULL ON UPDATE CASCADE
            );
        """
        )

        # 3. Create ProjectMember Table
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS ProjectMember (
                sid INTEGER PRIMARY KEY AUTOINCREMENT,
                RollNo TEXT NOT NULL UNIQUE,
                StudentName TEXT NOT NULL,
                StudentEmail TEXT NOT NULL,
                pid INTEGER,
                FOREIGN KEY (pid) REFERENCES Project(pid) 
                    ON DELETE CASCADE ON UPDATE CASCADE
            );
        """
        )

        # Commit the changes to the database
        conn.commit()
        print(f"Database and tables successfully created at: {db_path}")

    except sqlite3.Error as e:
        print(f"An error occurred while creating the database: {e}")

    finally:
        # Ensure the connection is closed properly
        if conn:
            conn.close()

def import_advisors(db_path, excel_path, sheet_name):
    """Reads advisor data from a specific Excel sheet and inserts it into

    the Advisor table in the SQLite database.
    """
    try:
        # 1. Read the specific sheet from the Excel file
        # 'usecols' ensures we only pull the columns we actually care about
        df = pd.read_excel(
            excel_path,
            sheet_name=sheet_name,
            usecols=["Faculty Member", "Email ID"],
        )

        # 2. Clean data: Drop rows where the essential data might be missing
        df = df.dropna(subset=["Faculty Member", "Email ID"])

        # 3. Rename columns to match your SQLite Advisor table schema
        df = df.rename(
            columns={
                "Faculty Member": "AdvisorName",
                "Email ID": "AdvisorEmail",
            }
        )

        # 4. Connect to the SQLite database
        conn = sqlite3.connect(db_path)

        # 5. Append the data to the Advisor table
        # if_exists='append' ensures we don't overwrite existing data
        # index=False prevents pandas from inserting its own row index as a column
        df.to_sql("Advisor", conn, if_exists="append", index=False)

        # Close the connection
        conn.close()

        print(
            f"Successfully imported {len(df)} advisors from sheet '{sheet_name}' into the database."
        )

    except FileNotFoundError:
        print(f"Error: The file at {excel_path} was not found.")
    except ValueError as e:
        print(
            f"Error: Sheet '{sheet_name}' or specified columns not found. Detailed error: {e}"
        )
    except sqlite3.Error as e:
        print(f"Database error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        

def import_projects(db_path, excel_path, sheet_name):
    """Reads project data from an Excel sheet, looks up the advisor IDs

    from the Advisor table, and inserts the records into the Project table.
    """
    try:
        # 1. Read the specific sheet from the Excel file
        df_excel = pd.read_excel(
            excel_path,
            sheet_name=sheet_name,
            usecols=["Group ID", "PROJECT", "Advisor"],
        )

        # Clean Excel data: strip trailing whitespaces from names for accurate matching
        df_excel["Advisor"] = df_excel["Advisor"].astype(str).str.strip()

        # 2. Connect to the database to fetch Advisor mapping
        conn = sqlite3.connect(db_path)

        # Load Advisor table into a DataFrame to use as a lookup map
        df_advisors = pd.read_sql_query(
            "SELECT aid, AdvisorName FROM Advisor", conn
        )
        df_advisors["AdvisorName"] = (
            df_advisors["AdvisorName"].astype(str).str.strip()
        )

        # 3. Merge (Lookup) aid based on Advisor Name
        # This acts like a SQL JOIN or Excel VLOOKUP
        df_merged = pd.merge(
            df_excel,
            df_advisors,
            left_on="Advisor",
            right_on="AdvisorName",
            how="left",
        )

        # Check for any advisors that couldn't be found in the DB
        missing_advisors = df_merged[df_merged["aid"].isna()][
            "Advisor"
        ].unique()
        if len(missing_advisors) > 0 and missing_advisors != ["nan"]:
            print(
                f"Warning: The following advisors were not found in the Advisor table: {missing_advisors}"
            )
            print("Rows with missing advisors will be inserted with 'NULL' for aid.")

        # 4. Filter and rename columns to match the 'Project' table schema
        # Schema: pid (auto), ProjectId, ProjectName, aid
        df_final = df_merged[["Group ID", "PROJECT", "aid"]].rename(
            columns={"Group ID": "ProjectId", "PROJECT": "ProjectName"}
        )

        # 5. Insert data into Project table
        # index=False ensures the Pandas DataFrame index isn't written as a column
        df_final.to_sql("Project", conn, if_exists="append", index=False)

        # Close the connection
        conn.close()

        print(
            f"Successfully imported {len(df_final)} projects from sheet '{sheet_name}' into the database."
        )

    except FileNotFoundError:
        print(f"Error: The file at {excel_path} was not found.")
    except ValueError as e:
        print(
            f"Error: Sheet '{sheet_name}' or specified columns not found. Detailed error: {e}"
        )
    except sqlite3.Error as e:
        print(f"Database error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def import_project_members(db_path, excel_path, sheet_name):
    """Reads student data from an Excel sheet, looks up the corresponding pid

    from the Project table using Group ID, and populates ProjectMember.
    """
    try:
        # 1. Read the specific sheet from the Excel file
        df_excel = pd.read_excel(
            excel_path,
            sheet_name=sheet_name,
            usecols=["Group. ID", "REGISTRATION#", "STUDENT NAME"],
        )

        # Clean string inputs to prevent lookup misses due to accidental spaces
        df_excel["Group. ID"] = df_excel["Group. ID"].astype(str).str.strip()
        df_excel["REGISTRATION#"] = (
            df_excel["REGISTRATION#"].astype(str).str.strip()
        )

        # 2. Connect to the SQLite database
        conn = sqlite3.connect(db_path)

        # Load existing Project records to map ProjectId to internal pid
        df_projects = pd.read_sql_query(
            "SELECT pid, ProjectId FROM Project", conn
        )
        df_projects["ProjectId"] = df_projects["ProjectId"].astype(str).str.strip()

        # 3. Lookup pid by merging on the Excel Group ID matching DB ProjectId
        df_merged = pd.merge(
            df_excel,
            df_projects,
            left_on="Group. ID",
            right_on="ProjectId",
            how="left",
        )

        # Check if any Group IDs failed to match a project in the database
        missing_projects = df_merged[df_merged["pid"].isna()][
            "Group. ID"
        ].unique()
        if len(missing_projects) > 0 and missing_projects != ["nan"]:
            print(
                f"Warning: The following Group IDs were not found in the Project table: {missing_projects}"
            )
            print("Members tied to these groups will be skipped or set to NULL.")

        # 4. Data Transformations
        # Map columns: REGISTRATION# -> RollNo, STUDENT NAME -> StudentName
        df_merged = df_merged.rename(
            columns={"REGISTRATION#": "RollNo", "STUDENT NAME": "StudentName"}
        )

        # Generate StudentEmail dynamic string: concat(RollNo, "@ucp.edu.pk")
        df_merged["StudentEmail"] = df_merged["RollNo"] + "@ucp.edu.pk"

        # 5. Filter down to the final target schema for ProjectMember
        # Schema: sid (auto-handled), RollNo, StudentName, StudentEmail, pid
        df_final = df_merged[["RollNo", "StudentName", "StudentEmail", "pid"]]

        # Clean up any NaN/Null errors in core identifier fields if necessary
        df_final = df_final.dropna(subset=["RollNo"])

        # 6. Bulk insert into ProjectMember table
        df_final.to_sql("ProjectMember", conn, if_exists="append", index=False)

        # Close database connection
        conn.close()

        print(
            f"Successfully imported {len(df_final)} project members from sheet '{sheet_name}'."
        )

    except FileNotFoundError:
        print(f"Error: The file at {excel_path} was not found.")
    except ValueError as e:
        print(
            f"Error: Excel parsing failed. Verify column names. Details: {e}"
        )
    except sqlite3.Error as e:
        print(f"Database error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    database_location = "Projects Data.sqlite"

    create_project_database(database_location)
    import_advisors(database_location, "Projects Data.xlsx", "Evaluators")
    import_projects(database_location, "Projects Data.xlsx", "Projects")
    import_project_members(database_location, "Projects Data.xlsx", "All Data")
