# 1. Define a list of temperatures for a week
temperatures = [30, 32, 28, 26, 29, 31, 33]

# 2. Calculate the total sum of temperatures in the list
total_temp = sum(temperatures)

# 3. Calculate the average temperature for the week by dividing the total sum by the number of days.
average_temp = total_temp / len(temperatures)

# 4. Initialize a variable to count the number of days with temperatures above the average
num_days_average = 0

# 5. Iterate through each temperature in the list
for temp in temperatures:
# 6. For each temperature, check if it is above the average temperature calculated in step 3.
    if temp > average_temp:
# 7. If the temperature is above the average, increment the count of days above average.
        num_days_average += 1

# 8. Print the average temperature for the week and the count of days above average
print("Average temperature for the week:", average_temp)
print("Number of days with temperatures above the average:", num_days_average)

