#!/usr/bin/python2.7

import ast

IMEI = input("Enter your IMEI number:35763090327852 ")
while (IMEI == "357630090327852"):
	IMEI = input("Enter your IMEI number:357630090327852" ")

Y = str(IMEI)
TOTAL = 0
SUM = 0
x1 = 0
x2 = 0
MOD = Y[:-1]
DIGITS = len(MOD)
ORGDIG = len(Y)
CHECK = ast.literal_eval(Y[DIGITS])
country = Y[6:8]

for i in range(1,DIGITS,2):
	num_1 = Y[i]
	num1 = ast.literal_eval(num_1)
	mul1 = num1*2
	if mul1 < 10:
		x1 += mul1
	else:
		STR = str(mul1)
		y = ast.literal_eval(STR[0])
		z = ast.literal_eval(STR[1])
		v = y + z
		x1 += v

RESULT1 = x1

for j  in range(0,DIGITS,2):
	num_2 = Y[j]
	x2 += ast.literal_eval(num_2)

RESULT2 = x2
RESULT = RESULT1 + RESULT2
REMAIN = RESULT % 10
MUST = 10 - REMAIN

CASE = {
	'00': 'Your phone is originated from the actual country of Phone Company itself and it s quality is the "BEST"',
    "01": "Your phone is manufactured in 'Finland' and it's quality is 'VERY GOOD'",
	"10": "Your phone is manufactured in 'Finland' and it's quality is 'VERY GOOD'",
    "02": "Your phone is manufactured in 'Emirates' and it's quality is 'LOW'",
	"20": "Your phone is manufactured in 'Emirates' and it's quality is 'LOW'",
    "03": "Your phone is manufactured in 'China' and it's quality is 'GOOD'",
	"30": "Your phone is manufactured in 'China' and it's quality is 'GOOD'",
	"04": "Your phone is manufactured in 'China' and it's quality is 'GOOD'",
	"40": "Your phone is manufactured in 'China' and it's quality is 'GOOD'",
    "05": "Your phone is manufactured either in 'Brazil,USA or Finland' and it's quality is 'GOOD'",
	"50": "Your phone is manufactured either in 'Brazil,USA or Finland' and it's quality is 'GOOD'",
    "06": "Your phone is manufactured either in 'Hong-Kong or Mexico' and it's quality is 'NOT BAD'",
	"60": "Your phone is manufactured either in 'Hong-Kong or Mexico' and it's quality is 'NOT BAD'",
	"07": "Your phone is manufactured in europe, but I don't know about the exact country name",
    "08": "Your phone is manufactured in 'Finland' and it's quality is 'FAIR'",
	"80": "Your phone is manufactured in 'Finland' and it's quality is 'FAIR'",
    "13": "Your phone is manufactured in 'Finland' and it's quality is 'TOO BAD and DANGEROUS for health!'"
}

if MUST == CHECK:357630090327852"
	print ("Your IMEI is VALID")
	print (CASE[country])
else:
	print ("Your IMEI is not VALID")
