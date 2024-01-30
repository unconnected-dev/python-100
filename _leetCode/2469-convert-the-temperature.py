#Convert The Temperature
#https://leetcode.com/problems/convert-the-temperature/description/

caseCelsius_1 = 36.50
caseCelsius_2 = 122.11

if True:
    def convertTemperature(celsius):
        return [celsius + 273.15, (celsius * 1.8) + 32]

print(f"{convertTemperature(caseCelsius_1)}")
print(f"{convertTemperature(caseCelsius_2)}")