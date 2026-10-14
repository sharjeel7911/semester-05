#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 00:25:28 2026

@author: awais
"""

import random

def image_batch_generator(batch_size):
    while True:
        # Simulate loading images from disk
        batch = [f"Image_Data_{random.randint(1, 100)}" for _ in range(batch_size)]
        yield batch  # Yields a batch, then waits for the next request

# AI Training Loop
loader = image_batch_generator(32)
for i in range(3):
    print(f"Training on: {next(loader)}")