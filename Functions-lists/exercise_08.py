import random


def create_random_int_list(count):
    result = []
    for _ in range(count):
        result.append(random.randrange(100))
    return result


# 1. Use the create_random_int_list function to build
# a random 25 element integer list.
result = create_random_int_list(25)

# 2. Calculate the sum. (Results will vary because of randomness.)
def calculate_sum(list):
    sum = 0
    for value in list:
        sum+=value
    return sum

# 3. Challenge: calculate the average.
def calculate_avg(list):
    sum = calculate_sum(list)
    return (sum/len(list))
    

# 4. Challenge, Challenge: calculate the standard deviation.
def standard_deviation(list):
    # Find the Mean (Average):
    mean = calculate_avg(list)
    # Calculate the Deviations from the Mean:
    deviation_list = []
    for value in list:
        deviation = value - mean
        squared_deviation = deviation ** 2
        deviation_list.append(squared_deviation)
    # Find the Average of the Squared Deviations:
    avg_deviation = calculate_avg(deviation_list)
    # Return the Square Root:
    return avg_deviation**0.5
    


# Test
test_list = [1,2,3,4,5,6,7,8,9,10]
print(calculate_sum(test_list))
print(calculate_avg(test_list))
print(standard_deviation(test_list))
