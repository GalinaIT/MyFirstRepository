# Functiom Vat
def get_vat(payment, percent):
      try:
      	payment = float(payment)
      	vat = float(payment)
      	vat = round(vat, 2)
      	return "Sum VAT: {}".format(vat)
      except TypeError:
      	return "Can't count. Check data!"

result = get_vat(400, 15)
print(result)