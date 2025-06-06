# Initialize an empty list to store the temperatures for the week
temperatures = []

# Initialize variables for basic analysis
total_temperature = 0
highest_temperature = -float('inf')  # Start with negative infinity to ensure any temperature is higher
lowest_temperature = float('inf')   # Start with positive infinity to ensure any temperature is lower
warm_days_count = 0  # Days where temperature is above 25°C
cold_days_count = 0  # Days where temperature is below 10°C

# --- Input and Storage ---
print("Please enter the temperature for each of the 7 days (in Celsius).")
for i in range(7):
    while True:
        try:
            temp_input = input(f"Enter temperature for Day {i + 1}: ")
            temperature = float(temp_input)
            temperatures.append(temperature)
            total_temperature += temperature
            break # Exit loop if input is valid
        except ValueError:
            print("Invalid input. Please enter a numerical value for temperature.")

# --- Basic Analysis Calculations ---
for temp in temperatures:
    # Update highest temperature
    if temp > highest_temperature:
        highest_temperature = temp
    
    # Update lowest temperature
    if temp < lowest_temperature:
        lowest_temperature = temp
    
    # Count warm days
    if temp > 25:
        warm_days_count += 1
    
    # Count cold days
    if temp < 10:
        cold_days_count += 1

# Calculate average temperature
average_temperature = total_temperature / len(temperatures)

# --- Trend Analysis (Longest Heatwave and Cold Snap) ---
max_heatwave_streak = 0
current_heatwave_streak = 0
max_cold_snap_streak = 0
current_cold_snap_streak = 0

for temp in temperatures:
    # Heatwave analysis
    if temp > 25:
        current_heatwave_streak += 1
    else:
        current_heatwave_streak = 0 # Reset streak if condition is not met
    
    if current_heatwave_streak > max_heatwave_streak:
        max_heatwave_streak = current_heatwave_streak
    
    # Cold snap analysis
    if temp < 10:
        current_cold_snap_streak += 1
    else:
        current_cold_snap_streak = 0 # Reset streak if condition is not met
    
    if current_cold_snap_streak > max_cold_snap_streak:
        max_cold_snap_streak = current_cold_snap_streak

# --- Advanced Trend Analysis (Largest Temperature Fluctuation) ---
max_fluctuation = 0
day1_fluctuation = 0
day2_fluctuation = 0

# Use nested loops to compare every unique pair of days
for i in range(len(temperatures)):
    for j in range(i + 1, len(temperatures)): # Start from i + 1 to avoid duplicate pairs and comparing day with itself
        current_fluctuation = abs(temperatures[i] - temperatures[j])
        
        if current_fluctuation > max_fluctuation:
            max_fluctuation = current_fluctuation
            day1_fluctuation = i + 1 # Store day numbers (1-indexed)
            day2_fluctuation = j + 1 # Store day numbers (1-indexed)

# --- Display Results ---
print("\n--- Weekly Temperature Report ---")
print(f"Average Temperature: {average_temperature:.1f} C") # Format to one decimal place
print(f"Highest Temperature: {highest_temperature} C")
print(f"Lowest Temperature: {lowest_temperature} C")
print(f"Warm Days (above 25C): {warm_days_count}")
print(f"Cold Days (below 10C): {cold_days_count}")