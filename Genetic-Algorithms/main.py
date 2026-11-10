# imports
import time
import random
import math
import sys


#vars
people = [('Lisbon','LIS'),
          ('Madrid','MAD'),
          ('Paris','CDG'),
          ('Dublin','DUB'),
          ('Brussels','BRI'),
          ('London','LHR')] # it's a cities list

destiny = 'FCO' # Rome airport it's the destiny, all of them want to go to Rome

#example
flights = {('BRU', 'FCO'): ['15:44', '18:55', 382]} # dictionary

print(f"Fligths hour and gate: { flights[('BRU', 'FCO')] }") # just to show it


flights = {}
for row in open ('./flights.txt'):
    print(row.split(','))
    origin, destiny, departure, arrival, price = row.split(',')
    print(f"origin: {origin}, destiny: {destiny}, departure: {departure}, arrival: {arrival}, price: {price}")
    flights.setdefault((origin, destiny), []) #creating keys according the variables origin and destiny
    flights[(origin, destiny)].append((departure,arrival,int(price)))
    
print(f"Arrival: \n{flights}")
print(f"Arrival2: \n{flights[('LIS','FCO')]}")
print(f"Arrival3: \n{flights[('FCO','LIS')]}")

#we're going to select the best flights into our genetic-algorithm