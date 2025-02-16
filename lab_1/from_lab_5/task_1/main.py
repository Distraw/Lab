import sys
import lab_5

try:
    region_data = lab_5.get_region_crime_data()
except Exception as exception:
    print(exception)
    sys.exit()

annual_increase = lab_5.calculate_annual_increase(region_data)

for element, i in zip(annual_increase, range(len(annual_increase))):
    print(str(i) + "-" + str(i) + ": " + str(element))