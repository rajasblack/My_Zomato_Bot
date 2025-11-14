from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import zomatopy
import json
import pandas as pd
import smtplib
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import re
from rasa_sdk.events import AllSlotsReset
from rasa_sdk.events import Restarted

class ActionValidateLocation(Action):
	def name(self):
		return 'action_validate_location'
		
	def run(self, dispatcher, tracker, domain):
		loc = tracker.get_slot('location')
		list_loc = ["ahmedabad","bangalore","chennai","delhi","hyderabad","kolkata","mumbai","pune","agra", "ajmer", "aligarh", "amravati", "amritsar", "asansol", "aurangabad", "bareilly", "belgaum", "bhavnagar", "bhiwandi", "bhopal", "bhubaneswar", "bikaner", "bilaspur", "bokaro steel city", "chandigarh", "coimbatore", "cuttack", "dehradun", "dhanbad", "bhilai", "durgapur", "erode", "faridabad", "firozabad", "ghaziabad", "gorakhpur", "gulbarga", "guntur", "gwalior", "gurgaon", "guwahati", "hamirpur", "hubli", "dharwad", "indore", "jabalpur", "jaipur", "jalandhar", "jammu", "jamnagar", "jamshedpur", "jhansi", "jodhpur", "kakinada", "kannur", "kanpur", "kochi", "kolhapur", "kollam", "kozhikode", "kurnool", "ludhiana", "lucknow", "madurai", "malappuram", "mathura", "goa", "mangalore", "meerut", "moradabad", "mysore", "nagpur", "nanded", "nashik", "nellore", "noida", "patna", "pondicherry", "purulia prayagraj", "prayagraj", "raipur", "rajkot", "rajahmundry", "ranchi", "rourkela", "salem", "sangli", "shimla", "siliguri", "solapur", "srinagar", "surat", "thiruvananthapuram", "thrissur", "tiruchirappalli", "tiruppur", "ujjain", "bijapur", "vadodara", "varanasi", "vasai-virar city", "vijayawada", "visakhapatnam", "vellore", "warangal"]

		if loc is not None:
			if loc.lower() in list_loc:
				return[SlotSet('location',loc)]
			else:
				dispatcher.utter_message("Sorry! We aren't serving at the specified location yet. Please try some other location")
				return[SlotSet('location',None)]
		else:
			dispatcher.utter_message("Sorry, I could not understand the location. Try some other location")
			return[SlotSet('location', None)]

class ActionValidateCuisine(Action):
	def name(self):
		return 'action_validate_cuisine'
		
	def run(self, dispatcher, tracker, domain):
		list_cuisine = ["chinese","mexican","american","italian","south indian","north indian"]
		cuisine = tracker.get_slot('cuisine')
		if cuisine is not None:
			if cuisine.lower() in list_cuisine:
				return[SlotSet('cuisine',cuisine)]
			else:
				dispatcher.utter_message("Sorry, the cuisine is not available yet. Please try again with the given options")
				return[SlotSet('cuisine',None)]
		else:
			dispatcher.utter_message("Sorry, I could not understand the cuisine. Please try again with the given options.")
			return[SlotSet('cuisine', None)]			
	
class ActionValidateEmail(Action):
	def name(self):
		return 'action_validate_email'
		
	def run(self, dispatcher, tracker, domain):
		email = tracker.get_slot('email')		
		email_check = re.match('^[_a-zA-Z0-9-]+(\.[_a-zA-Z0-9-]+)*@[a-z]+(\.[a-z]+)*(\.[a-z]{2,3})$', email)
		if email is not None:
			if email_check is not None:
				return[SlotSet('email',email)]
			else:
				dispatcher.utter_message("Email address appears to be invalid, Kindly enter a valid email address.")
				return[SlotSet('email',None)]
		else:
			dispatcher.utter_message("Sorry, I could not understand the email address which you provided. Please provide again")
			return[SlotSet('email', None)]

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_restaurants'
		
	def run(self, dispatcher, tracker, domain):
		config={ "user_key":"a98349b9986d1d6518c0605e73564f03"}
		zomato = zomatopy.initialize_app(config)
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		price = tracker.get_slot('price')
		if price == 'low':
			min_cost= 0
			max_cost = 300
		elif price == 'mid':
			min_cost = 301
			max_cost = 700
		elif price == 'high':
			min_cost = 701
			max_cost = 9999
		location_detail=zomato.get_location(loc, 1)
		d1 = json.loads(location_detail)
		lat=d1["location_suggestions"][0]["latitude"]
		lon=d1["location_suggestions"][0]["longitude"]

		cuisines_dict={"american":1,"chinese":25,"mexican":73,"italian":55,"north indian":50,"south indian":85}

		results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), limit="")

		d = json.loads(results)

		response=""
		response_10=""

		col_names = ["zomato rating", "restaurant name", "address", "avg. budget for two"]
		res = pd.DataFrame(columns = col_names)
		temp_res = pd.DataFrame(columns = col_names)

		if d["results_found"] == 0:
			response= "Found 0 restaurants in given price range"
		else:
			for restaurant in d["restaurants"]:
				temp_res = {"zomato rating":restaurant["restaurant"]["user_rating"]["aggregate_rating"],"restaurant name":restaurant["restaurant"]["name"],"address": restaurant["restaurant"]["location"]["address"], "avg. budget for two": restaurant["restaurant"]["average_cost_for_two"]}                         
				if temp_res['avg. budget for two'] >= min_cost:
					if temp_res['avg. budget for two'] <= max_cost:
						res.loc[len(res)] = temp_res

		#res_budget = res[(res["avg. budget for two"] >= min_cost) & (res["avg. budget for two"] <= max_cost)]

		# sorting the restaurant list
		res_sorted = res.sort_values(['zomato rating'], ascending=False)
		res_top5 = res_sorted.reset_index(drop=True).head(5)
		res_top10 = res_sorted.reset_index(drop=True).head(10)
		res_sorted = res_sorted.reset_index(drop=True)
		res_sorted.index = res_sorted.index.map(str)

		# print restaurant list
		if len(res_top5) != 0:
			for index, row in res_top5.iterrows():
				response = response + str(index+1) + ". Found \""+ row['restaurant name']+ "\" in "+ row['address']+" has been rated "+ row['zomato rating']+"\n"
		else:
			response = 'Found 0 restaurants in given price range'
		dispatcher.utter_message(response)
        
        # print restaurant list
		if len(res_top10)!=0:
			response_10 = "Hello, Please find the list of top " + str(len(res_top10)) +" "+ cuisine +" restaurants around " + loc + " in the " + price + " price range." + ": \n\n"
			for index, row in res_top10.iterrows():
				response_10 = response_10 + str(index+1) + ". Found \""+ row['restaurant name']+ "\" in "+ row['address']+" has been rated "+ row['zomato rating']+ " average price for two people is Rs." + str(row['avg. budget for two']) + "\n"
			response_10 = response_10 +"\n"+ "Wish you have wonderful day ahead! See you soon!"
		else:
			response_10 = 'Found 0 restaurants in given price range'
			
		return [SlotSet('body',response_10)]
    
class ActionSendEmail(Action):

    def name(self):
        return 'action_send_email'

    def run(self, dispatcher, tracker, domain):
        from_user = 'foodiebot777@gmail.com'
        to_user = tracker.get_slot('email')
        password = '<password>'
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(from_user, password)
        subject = 'Your Foodie Bot Query'
        msg = MIMEMultipart()
        msg['From'] = from_user
        msg['TO'] = to_user
        msg['Subject'] = subject
        
        emailbody = tracker.get_slot('body')
            
        msg.attach(MIMEText(emailbody,'plain'))
        text = msg.as_string()
        server.sendmail(from_user,to_user,text)
        server.close()

class ActionSlotReset(Action): 	
    def name(self): 		
        return 'action_slot_reset' 	
    def run(self, dispatcher, tracker, domain): 		
        return[AllSlotsReset()]

class ActionRestart(Action): 	
    def name(self): 		
        return 'action_restart' 	
    def run(self, dispatcher, tracker, domain): 
        return[Restarted()] 
