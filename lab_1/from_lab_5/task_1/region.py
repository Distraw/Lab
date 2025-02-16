def get_region_crime_data():
    region_length = int(input("Довжина ряду:"))

    region_data = [0] * region_length
    for i in range(region_length):
        region_data[i] = float(input("Показник злочинності No" + str(i + 1) + ":"))
        region_data[i] = abs(region_data[i])

    return region_data

def calculate_annual_increase(annual_values):
    annual_increase_values = [0] * (len(annual_values) - 1)

    for i in range(len(annual_increase_values)):
        annual_increase_values[i] = (annual_values[i + 1] - annual_values[i]) / annual_values[i] * 100

    return annual_increase_values