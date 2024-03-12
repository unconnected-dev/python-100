#Tip Calculator
#Calculate how much a group of people should pay from a total bill plus tip

print("Welcome to the tip calculator.")

totalBill = float(input("What was the total bill?\n"))
percentageTip = int(input("What percentage tip would you like to give? 10, 12, or 15?\n"))
splitBetween = int(input("How many people to split the bill?\n"))

eachPays = (totalBill + ((totalBill/100)*percentageTip)) / splitBetween
roundEachPays = round(eachPays, 2)
formatEachPays = "{:.2f}".format(roundEachPays)

print(f"Each person should pay: ${formatEachPays}")