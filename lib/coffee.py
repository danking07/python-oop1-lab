#!/usr/bin/env python3

class Coffee:
    def __init__(self, size, price):
        self.size = size  # goes through the setter for validation
        self.price = price

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        # Only allow Small, Medium, or Large
        if size in ("Small", "Medium", "Large"):
            self._size = size
        else:
            print("size must be Small, Medium, or Large")

    def tip(self):
        # Simulates tipping: prints a thank-you and raises the price
        print("This coffee is great, here’s a tip!")
        self.price += 1