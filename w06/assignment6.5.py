text = "X-DSPAM-Confidence:    0.8475";

spacePos = text.find(" ")
number = text[spacePos::1]
strippedNumber = number.lstrip();
result = float(strippedNumber)
	
def reprint(printed):
 print (printed);
	
reprint(result)
/*отступ должен быть в 9 строке ровно в 1 пробел*/

