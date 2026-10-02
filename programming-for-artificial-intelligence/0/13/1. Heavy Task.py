#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 00:59:40 2026

@author: awais
"""

import time

def heavy_io_task(worker_name, duration):
    print(f"[START] Worker {worker_name} is processing a heavy operation...")
    time.sleep(duration)  # Simulating a heavy network call or database query
    print(f"[COMPLETE] Worker {worker_name} finished after {duration}s.")

def main_sync():
    start_time = time.time()
    
    # Executing tasks sequentially on the main thread
    heavy_io_task("Alpha", 3)
    heavy_io_task("Beta", 2)
    
    print(f"Total Main Thread Execution Time: {time.time() - start_time:.2f} seconds.")

# --- Execution ---
if __name__ == "__main__":
    main_sync()