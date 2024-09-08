import math
import matplotlib.pyplot as plt

# Constants (could be inputs or defined for specific UAVs)
g = 9.81  # gravitational acceleration (m/s^2)
rho = 1.225  # air density at sea level (kg/m^3)

# Function to calculate Lift-to-Drag ratio (L/D)
def calculate_ld_ratio(cl, cd):
    """Calculates Lift-to-Drag Ratio."""
    return cl / cd

# Function to calculate Stall Speed (Vs)
def calculate_stall_speed(weight, wing_area, cl_max):
    """Calculates Stall Speed (Vs) in m/s."""
    vs = math.sqrt((2 * weight) / (rho * wing_area * cl_max))
    return vs

# Function to calculate Range
def calculate_range(ld_ratio, fuel_weight, specific_fuel_consumption):
    """Calculates Range (R) in meters."""
    return (ld_ratio / specific_fuel_consumption) * math.log(1 + (fuel_weight / 1000))

# Function to calculate Endurance
def calculate_endurance(ld_ratio, fuel_weight, specific_fuel_consumption):
    """Calculates Endurance (E) in seconds."""
    return ld_ratio / specific_fuel_consumption * fuel_weight

# Function to plot performance data
def plot_data(altitudes, stall_speeds, ranges):
    plt.figure(figsize=(10, 6))

    # Plot Stall Speed
    plt.subplot(1, 2, 1)
    plt.plot(altitudes, stall_speeds, label='Stall Speed (m/s)', color='blue', marker='o')
    plt.xlabel('Altitude (m)')
    plt.ylabel('Stall Speed (m/s)')
    plt.title('Stall Speed vs Altitude')
    plt.grid(True)

    # Plot Range
    plt.subplot(1, 2, 2)
    plt.plot(altitudes, ranges, label='Range (km)', color='green', marker='o')
    plt.xlabel('Altitude (m)')
    plt.ylabel('Range (km)')
    plt.title('Range vs Altitude')
    plt.grid(True)

    plt.tight_layout()
    plt.show()

# Main Program
if __name__ == "__main__":
    # UAV Inputs
    weight = float(input("Enter the UAV weight (in N): "))
    wing_area = float(input("Enter the wing area (in m^2): "))
    cl_max = float(input("Enter the maximum lift coefficient (Cl_max): "))
    cd = float(input("Enter the drag coefficient (Cd): "))
    fuel_weight = float(input("Enter the fuel weight (in kg): "))
    specific_fuel_consumption = float(input("Enter the specific fuel consumption (kg/N/s): "))

    # List of altitudes for simulation (could be extended)
    altitudes = [0, 1000, 2000, 3000, 4000, 5000]  # in meters

    # Lists to store results
    stall_speeds = []
    ranges = []

    # Perform calculations for each altitude
    for altitude in altitudes:
        # Update air density based on altitude (simplified for now)
        rho_alt = rho * math.exp(-altitude / 10000)

        # Calculate performance metrics
        vs = calculate_stall_speed(weight, wing_area, cl_max)
        ld_ratio = calculate_ld_ratio(cl_max, cd)
        r = calculate_range(ld_ratio, fuel_weight, specific_fuel_consumption) / 1000  # convert to km

        # Store results
        stall_speeds.append(vs)
        ranges.append(r)

    # Display the results
    plot_data(altitudes, stall_speeds, ranges)

    print("Flight Performance Analysis Complete!")
