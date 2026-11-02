# ============================== imports ==============================
import csv
import time
from collections.abc import Iterator
from functools import wraps

# ====================================================================================================


# ============================== TASK 1: THE SCP DECODER ==============================
def get_mi_mapping(mapping_csv_path: str) -> dict:
    """
    Reads scp_statements.csv and returns a dictionary mapping
    codes to descriptions for 'Myocardial Infarction' only.
    """
    mi_map = {}
    # TODO: Implement CSV reading and dictionary building
    with open(mapping_csv_path, mode="r", newline="") as file:
        reader = csv.DictReader(file)
        scp_code_col = reader.fieldnames[0]  # gets the first col header
        # print(f"Column headers: {reader.fieldnames} ")  # Debug
        for row in reader:
            if row.get("Statement Category") == "Myocardial Infarction":
                mi_map[row[scp_code_col].strip().upper().replace(" ", "_")] = (
                    row["description"].strip().lower().replace(" ", "_")
                )
                # print(f"Added MI mapping: {row[scp_code_col]} -> {row['description']}")  # Debug
    return mi_map


# mi_mapping = get_mi_mapping("data/scp_statements.csv")  # Debug

# ====================================================================================================


# ============================== TASK 2: THE PATIENT GENERATOR ==============================
def mi_patient_generator(database_csv_path: str, mi_mapping: dict) -> dict:
    """
    A generator that yields patient records matching MI criteria.
    """
    # TODO: Use csv.DictReader to iterate through database_csv_path
    # TODO: Check if scp_codes contains any key from mi_mapping
    # TODO: Yield a dictionary with the required fields
    with open(database_csv_path, mode="r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            scp_codes = row["scp_codes"]
            # print(scp_codes)  # Debug
            for code, description in mi_mapping.items():
                if f"'{code}'" in scp_codes:
                    # print(f"{code} -> {description} -> {scp_codes}") # Debug
                    yield {
                        "patient_id": int(float(row["patient_id"])),
                        "age": int(float(row["age"])),
                        "sex": int(float(row["sex"])),
                        "record_date": row["recording_date"],
                        "diagnosis": description,
                        "filename": row["filename_hr"],
                    }
                    break


# patient_gen = mi_patient_generator("data/ptbxl_database.csv", mi_mapping)  # Debug
# print(next(patient_gen))  # Debug
# print(next(patient_gen))  # Debug


# ====================================================================================================


# ============================== TASK 3: TIMING ==============================
def timer(func: callable) -> callable:
    """
    Decorator that reports how long the wrapped function takes.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = (
            time.perf_counter()
        )  # perf_counter() captures the most precise time available
        result = func(*args, **kwargs)
        end_time = time.perf_counter() - start_time
        print(f"\nTime taken to find records: {end_time:.4f} seconds")
        return result

    return wrapper


@timer
def print_matches(patient_gen: Iterator[dict], n: int = 25) -> None:
    count = 0
    for idx, record in enumerate(patient_gen):
        print(f"{idx + 1}. {record}")
        count += 1
        if count == n:
            break
    print(f"\nPrinted {count} records.")


# ====================================================================================================


def main():
    db_path = "data/ptbxl_database.csv"
    statements_path = "data/scp_statements.csv"

    print(
        "============================== Initializing MI Mapping =============================="
    )
    mi_mapping = get_mi_mapping(statements_path)
    for idx, val in enumerate(mi_mapping.items()):
        print(f"{idx + 1}. {val[0]} -> {val[1]}")
    print(f"\nLoaded {len(mi_mapping)} MI-related diagnostic codes.\n")

    print(
        "============================== Starting Patient Stream =============================="
    )
    patient_gen = mi_patient_generator(db_path, mi_mapping)
    print_matches(patient_gen, 25)


if __name__ == "__main__":
    main()
