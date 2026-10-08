#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 01:01:34 2026

@author: awais
"""

import threading
import time

# Threads share memory, so we can pass a list container to capture results safely
def calculate_performance_score(student_id, assignment_grades, results_pool):
    print(f"Thread processing metrics for Student {student_id}...")
    time.sleep(2)  # Simulating complex analytical calculation
    final_score = sum(assignment_grades) / len(assignment_grades)
    
    # Appending to a list is an atomic (thread-safe) operation in Python
    results_pool.append({"student_id": student_id, "score": final_score})

def main_synchronized_threads():
    start_time = time.time()
    shared_results_pool = []
    threads_list = []
    
    # Student mock dataset
    student_data = {
        "UCP-001": [12, 15, 14],
        "UCP-002": [18, 19, 17],
        "UCP-003": [8, 10, 9]
    }
    
    # 1. Spawn and start all threads
    for student_id, grades in student_data.items():
        t = threading.Thread(target=calculate_performance_score, 
                             args=(student_id, grades, shared_results_pool))
        threads_list.append(t)
        t.start()
        
    # 2. Enforce the BARRIER: Wait for all workers to join back up
    for t in threads_list:
        t.join()  # Main thread blocks here until thread 't' terminates
        
    print(f"\nAll operations synchronized in: {time.time() - start_time:.2f} seconds.")
    print(f"Collected Results Data: {shared_results_pool}")

if __name__ == "__main__":
    main_synchronized_threads()