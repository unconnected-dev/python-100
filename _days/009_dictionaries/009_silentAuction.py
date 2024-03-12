#Silent Auction
#Allow users to submit bids, then find highest bidder

import os
import logo


#Input bids
bidDict = {}
bidsOngoing = True
while bidsOngoing == True:
    print(logo.logo)
    print("")
    
    bidName = input(f"Please enter your name:\n")
    bidPrice = int(input(f"Please enter your bid:\n"))

    bidDict[bidName] = bidPrice


    checkOngoing = input("Are there any other users that would like to bid? y/n\n")
    if checkOngoing == "n":    
        bidsOngoing = False

    os.system('cls')


#Find highest bidder
highestBid = 0
highestBidder = "No one"

for name in bidDict:
    if(bidDict[name] > highestBid):
        highestBid = bidDict[name]
        highestBidder = name


print(logo.logo)
print("")
print(f"The highest bidder was {highestBidder} who bid ${highestBid}")
