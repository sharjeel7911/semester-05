#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 01:03:16 2026

@author: awais
"""

import anyio
import time


# Imagine this is legacy, synchronous code that you cannot modify or rewrite
def legacy_sync_logger(message):
    print(f"Writing to disk: {message}")
    time.sleep(2)  # High blocking latency disk operation
    return "SUCCESS_LOG"

async def async_application_wrapper():
    start_time = time.time()
    
    print("Starting modern async master loop application...")
    
    # anyio.to_thread.run_sync spins up a background thread dynamically under the hood,
    # converts the returning output into an awaitable task, and prevents loop blockages.
    async_wrapped_task1 = anyio.to_thread.run_sync(legacy_sync_logger, "User Login Event")
    async_wrapped_task2 = anyio.to_thread.run_sync(legacy_sync_logger, "Database Backup Event")
    
    # Drive execution loops concurrently using a task group context manager
    async with anyio.create_task_group() as tg:
        print("Dispatching wrapped legacy tasks concurrently...")
        # Tasks execute simultaneously without freezing the application runtime
        
    print(f"Asynchronous Wrapper complete in: {time.time() - start_time:.2f} seconds.")

if __name__ == "__main__":
    import asyncio
    import nest_asyncio
    nest_asyncio.apply()  # Patches the underlying IPython loop framework
    
    # --- The Spyder Fix ---
    # 1. Fetch the active background loop that Spyder is already running
    loop = asyncio.get_event_loop()
    
    # 2. Directly drop the anyio coroutine into Spyder's existing loop
    loop.run_until_complete(async_application_wrapper())