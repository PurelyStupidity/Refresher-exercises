"""Write a function that takes in a price without GST, calculates the GST of 15% and returns the combined price.
"""
def calc_gst(price):
    price = price * 1.15
    # round price to 2 dp
    price = round(price, 2)
    return price

print(calc_gst(1067))