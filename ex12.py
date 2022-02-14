"""
Create a program for a movie cinema. It will be used to
keep track of ticket sales throughout the day. The
program should do the following:
Keep asking for tickets until the end of the day
(maybe ask the user "Do you want to sell
another ticket? (Y/N) ")
Tickets sold are either Adult, Student, Child, or
they use a Gift Voucher.
When a ticket is sold, print the price of
the ticket to the user:
• Adult $12.50
• Student $9.00
• Child $7.00
Gift Voucher is free
When a ticket is sold, keep track of how
many are sold of each type.
At the end of the day, print out the total tickets
sold/used, how many tickets were sold of each
type, and the total value of tickets.
Advanced challenge: Allow the user to cancel
buying a ticket
"""
adult_price = 12.50
student_price = 9.00
child_price = 7.00
gift_price = 0

def get_ticket():
    ticket = input("What type of ticket would you like to buy?\n (A)dult, (S)tudent, (C)hild, or (G)ift Voucher? ").lower()
    if ticket == "a":
        return "Adult"
    elif ticket == "s":
        return "Student"
    elif ticket == "c":
        return "Child"
    elif ticket == "g":
        return "Gift Voucher"
    else:
        print("Invalid ticket type. Please try again.")
        get_ticket()