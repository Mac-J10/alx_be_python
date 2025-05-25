principal= 1000  # Principal amount
rate = 0.05  # Interest rate
time = 3  # Time in years

def calculate_simple_interest(principal, rate, time):
    interest = principal * rate * time
    return interest

interest = calculate_simple_interest(principal, rate, time)  # Calculate simple interest

print("The simple interest is: " + str(interest))
