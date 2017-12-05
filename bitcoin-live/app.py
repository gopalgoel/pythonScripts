import requests, time
buy_p = 0
sell_p = 0

while True:
	r = requests.get('https://api.zebpay.com/api/v1/ticker?currencyCode=INR')
	a = r.json()
	buy, sell = a["buy"], a["sell"]
	if(buy_p == buy and sell_p == sell):
		time.sleep(60)
	else:
		buy_p, sell_p = buy, sell
		print(buy, sell)