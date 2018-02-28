from blockchain import exchangerates
import time
import os

ticker = exchangerates.get_ticker()

base = ticker['BRL'].sell
taxa_alerta = 0.04
tempo_base = 8 #minutos
flag = 'Comprar' #Comprar ou Vender
while True:
	try:
		ticker = exchangerates.get_ticker()
		sell = ticker['BRL'].sell
		buy = ticker['BRL'].buy
	except Exception as e:
		continue
	
	if flag == 'Comprar':
		valor = buy
	else:
		valor = sell
	msg = "Sell: R$ "+str(valor)+" Buy: R$ "+str(buy)

	if abs(1-(valor/base)) >= taxa_alerta:
		try:
			command = 'curl -X POST  https://rest.nexmo.com/sms/json -d api_key=KEY -d api_secret=SECRET -d to=55DDDSeuTELEFONE -d from="NEXMO" -d text="'+msg+'"'
			command = 'echo '+flag
			if flag == 'Comprar':
				flag = 'Vender'
			else:
				flag = 'Comprar'
			os.system(command)
			base = valor
		except Exception as e:
			raise e	
	print valor, abs(1-(valor/base)), (60*abs(tempo_base-abs((1-(valor/base))*100)))
	time.sleep(60*abs(tempo_base-abs((1-(valor/base))*100)))