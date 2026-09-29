#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 01:14:56 2026

@author: awais
"""

import threading
import queue
import time
import random

# 1. Initialize a thread-safe FIFO Queue
# Setting a maxsize prevents memory overflow if producers outpace the consumer
data_pipeline = queue.Queue(maxsize=10)

def producer_worker(producer_id, item_count):
    """Simulates background data collectors (e.g., scraping index grids)."""
    for i in range(item_count):
        # Simulate variable network latency
        time.sleep(random.uniform(0.1, 0.8))
        
        item_data = f"Product_ID_{producer_id}_{i}"
        
        # .put() blocks automatically if the queue is full (maxsize reached)
        # This naturally throttles the producers to cooperate with the consumer
        data_pipeline.put(item_data)
        print(f"[PRODUCER {producer_id}] Successfully queued: {item_data} | Pipeline Size: {data_pipeline.qsize()}")
    
    print(f"--- [PRODUCER {producer_id}] Finished gathering all items. ---")

def consumer_logger():
    """Simulates a single, dedicated database writer thread."""
    while True:
        try:
            # .get() will BLOCK the consumer thread automatically if the queue is empty,
            # putting it to sleep until a producer drops a fresh item in.
            # We set a timeout so the consumer knows when to shut down if no data arrives.
            item = data_pipeline.get(timeout=4)
            
            # Simulate transactional processing latency (e.g., writing to SQLite)
            time.sleep(0.3)
            print(f"\t[CONSUMER DB WRITER] Extracted & Processed: {item}")
            
            # Signals back to the queue architecture that the item processing is fully completed
            data_pipeline.task_done()
            
        except queue.Empty:
            # If the queue remains completely empty for the timeout duration, assume producers are done
            print("\n--- [CONSUMER] Pipeline empty timeout reached. Shutting down writer thread. ---")
            break

# --- Thread Orchestration Pipeline ---
if __name__ == "__main__":
    start_time = time.time()
    print("Initializing Cooperative Multithreading Pipeline...\n")
    
    # 1. Spawn and start the Consumer Thread
    consumer_thread = threading.Thread(target=consumer_logger, name="DB-Writer")
    consumer_thread.start()
    
    # 2. Spawn and start a pool of distinct Producer Threads
    producer_pool = []
    for p_id in range(3): # 3 distinct scrapers running in parallel
        t = threading.Thread(target=producer_worker, args=(p_id, 4)) # Each collects 4 items
        producer_pool.append(t)
        t.start()
        
    # 3. Synchronize: Wait for all PRODUCERS to finish their collection loops
    for t in producer_pool:
        t.join()
        
    # 4. Synchronize the Queue: Wait until all items inside the queue are processed (task_done matches counts)
    data_pipeline.join()
    
    # 5. Wait for consumer thread to exit its timeout loop gracefully
    consumer_thread.join()
    
    print(f"\nPipeline successfully drained. Total execution time: {time.time() - start_time:.2f} seconds.")