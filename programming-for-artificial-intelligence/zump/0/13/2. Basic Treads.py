#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 01:00:51 2026

@author: awais
"""

import threading
import time

def heavy_io_task(worker_name, duration):
    print(f"[START] Worker {worker_name} running in background thread...")
    time.sleep(duration)
    print(f"[COMPLETE] Worker {worker_name} finished.")

def main_threads_naive():
    start_time = time.time()
    
    # Instantiate background thread workers
    # args must be passed as a tuple: (worker_name, duration)
    thread1 = threading.Thread(target=heavy_io_task, args=("Alpha", 3))
    thread2 = threading.Thread(target=heavy_io_task, args=("Beta", 2))
    
    # Fire off execution streams asynchronously
    thread1.start()
    thread2.start()
    
    # PITFALL: The main thread does not wait. It finishes instantly!
    print(f"Main Thread reached the end in: {time.time() - start_time:.2f} seconds.")

if __name__ == "__main__":
    main_threads_naive()