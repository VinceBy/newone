
prices = {
    'ACME':45.23,
    'AAPL':612.78,
    'IBM':205.55,
    'HPQ':37.20,
    'FB':10.75
}

#make directonary of all prices
p1 = {key:value for key,value in prices.items() if value>200}
p1 = dict((key,value) for key,value in prices.items() if value>200)
print(p1)

#make a dictionary of tech stocks
tech_names = {'AAPL','IBM','HPQ','MSFT'}
tech_names = {key:value for key,value in prices.items() if key in tech_names}
p2 = {key:prices[key] for key in prices.keys()&tech_names }
print(tech_names,p2)

