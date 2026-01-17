def calculate_average(num1,num2,num3) :
    """Calculate the average of three numbers."""
    total = num1 + num2 + num3
    average = total / 3
    return average
def add_tax(bill_total) :
    """Add 10% tax to the bill total."""
    tax_rate = 0.10
    total_with_tax = bill_total + (bill_total * tax_rate)
    return total_with_tax
def greet_user(Jacob) :
    """Return a greeting message for the user."""
    return "Hello " + Jacob
