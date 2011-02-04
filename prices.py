#!/usr/bin/env python
from prices1 import name as name1
from prices1 import price as price1
from prices2 import name as name2
from prices2 import price as price2
from operator import itemgetter
from sys import argv
import traceback

differences = {}
abs_difs = {}
max_profit = {}
best_buy = {}
for item in price1.keys():
	differences[item] = price1[item][1] - price2[item][1]
	abs_difs[item] = abs(differences[item])
	max_profit[item] = price1[item][0] * abs_difs[item]
	best_buy[item] = name1 if differences[item] > 0 else name2

#now for some results
print '%-20s\t%-7s\t%-20s' % ("Item", "Profit", "Where?")
for (k, v) in sorted(max_profit.iteritems(), key=itemgetter(1), reverse=True):
	print '%-20s\t%-7d\t%-20s' % (str(k), max_profit[k], best_buy[k])

#also, given cash and a location, what should we buy?
if len(argv) == 3:
	try:
		cash = int(argv[1])
		prices = {}
		if argv[2] == "1":
			location = name1
			prices = price1
		elif argv[2] == "2":
			location = name2
			prices = price2
		else:
			location = None
		if location != None and cash > 0:
			buy = {}
			for (k, v) in [(k, v) for (k, v) in sorted(max_profit.iteritems(), key=itemgetter(1), reverse=True) if best_buy[k] == location and abs_difs[k] != 0]:
				if cash > 0:
					if cash / prices[k][1] <= prices[k][0]:
						buy[k] = cash / prices[k][1] #amount of items to buy here
					else:
						buy[k] = prices[k][0]
					cash -= buy[k] * prices[k][1]
		print "\nItems to buy in %s:\n%17s %-4s %-7s %-7s" % (location, "Item", "#", "$", "Total")
		for (k,v) in buy.iteritems():
			if v != 0 :
				print "%17s %-4d %-7d %-7d" % (k, v, prices[k][1], v * prices[k][1])
		print "%17s%14s%-7d" % ("Total", "", int(argv[1]) - cash)
		print "%17s%14s%-7d" % ("Cash left", "", cash)
			
	except:
		traceback.print_exc()
		print "No valid cash or location, aborting"
else:
	print "Cities:"
	print "1 : " + name1
	print "2 : " + name2
