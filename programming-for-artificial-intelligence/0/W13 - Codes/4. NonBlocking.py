#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 01:02:42 2026

@author: awais
"""

import asyncio
import time

# import nest_asyncio
# nest_asyncio.apply()  # Patches the running IPython loop to allow nesting

# 'async' keyword turns a regular function into a Coroutine
async def async_network_scraper(portal_name, duration):
    print(f"[ASYNC START] Fetching metrics from {portal_name}...")
    
    # CRITICAL: time.sleep() is synchronous and will block the entire event loop!
    # We must use asyncio.sleep() to yield control back to the loop engine.
    await asyncio.sleep(duration) 
    
    print(f"[ASYNC COMPLETE] Captured data from {portal_name}.")
    return f"{portal_name}_data_payload"

async def main_async_engine():
    start_time = time.time()
    
    # Schedule multiple coroutines concurrently using a task gather bundle
    task_bundle = asyncio.gather(
        async_network_scraper("Daraz Portal", 3),
        async_network_scraper("OLX Portal", 2),
        async_network_scraper("AliExpress", 4)
    )
    
    # Await the bundle execution block to harvest all returning records
    results = await task_bundle
    
    print(f"\nAsync pipeline completed in: {time.time() - start_time:.2f} seconds.")
    print(f"Returned Payloads: {results}")

if __name__ == "__main__":
    # Initialize and drive the core execution loop runtime
    asyncio.run(main_async_engine())