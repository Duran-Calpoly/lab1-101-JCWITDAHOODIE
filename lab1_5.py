def check_multiple(num):
    if num % 3 ==0 and num % 5 ==0:
        return True
    else:
        return False
    """Check if a number is a multiple of 3, 5, or both."""
def check_password(password):
    if password == "Python123":
        return "access granted"
    else:
        return "access denied"
    """Check if the provided password is correct."""
def calculate_federal_tax(salary):
    if salary<=11000:
        return salary*0.1
    elif salary>11000 and salary<=44725:
        return salary * 0.12
    elif salary>44725 and salary<=95375:
        return salary*0.22
    elif salary>95375:
        return salary*0.24
    """Calculate federal tax based on the given salary."""