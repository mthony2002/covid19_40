country = {
 	"name": "Germany",
 	"population": "83 million",
 	"capital": "Berlin",
 	"currency": "Euro"
 }

out = "{name} {population} {capital} {currency} "
print(out.format(**country))