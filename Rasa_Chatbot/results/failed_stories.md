## interactive_story_2_1
* greet
    - utter_greet   <!-- predicted: action_listen -->
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_validate_location
    - slot{"location": null}
    - utter_ask_location_again
* restaurant_search{"location": "Warangal"}
    - slot{"location": "Warangal"}
    - slot{"location": "Warangal"}
    - action_validate_location
    - slot{"location": "Warangal"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_validate_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - utter_ask_about_email
* email_affirm{"email": "xyz@sth.edu"}
    - slot{"email": "xyz@sth.edu"}
    - slot{"email": "xyz@sth.edu"}
    - action_validate_email
    - slot{"email": "xyz@sth.edu"}
    - action_send_email
    - utter_email_sent
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - action_restart


## interactive_story_2_1a
* greet
    - utter_greet   <!-- predicted: action_listen -->
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_validate_location
    - slot{"location": null}
    - utter_ask_location_again
* restaurant_search{"location": "Warangal"}
    - slot{"location": "Warangal"}
    - slot{"location": "Warangal"}
    - action_validate_location
    - slot{"location": "Warangal"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_validate_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - utter_ask_about_email
* email_affirm
    - utter_ask_emailID
* emailID{"email": "jddk.2jmd@kdl.co.in"}
    - slot{"email": "jddk.2jmd@kdl.co.in"}
    - slot{"email": "jddk.2jmd@kdl.co.in"}
    - action_validate_email
    - slot{"email": "jddk.2jmd@kdl.co.in"}
    - action_send_email
    - utter_email_sent
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - action_restart


## interactive_story_2_2
* greet
    - utter_greet   <!-- predicted: action_listen -->
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - action_validate_location
    - slot{"location": "kolkata"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - action_validate_cuisine
    - slot{"cuisine": "american"}
    - utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - slot{"price": "low"}
    - action_search_restaurants
    - slot{"body": "Hello, Please find the list of top 6 american restaurants around kolkata in the low price range.: \n\n1. Found \"The Bahubelly\" in 67, Natabar Paul Road, Tikiapara, Kadamtala, Howrah has been rated 4.1 average price for two people is Rs.400\n2. Found \"Forkstruck\" in 188/13, Jodhpur Garden, Lake Gardens, Kolkata has been rated 4.1 average price for two people is Rs.400\n3. Found \"The Chicken House\" in 29/1, Hare Krishna Kunal Road, Entally, Kolkata has been rated 4.0 average price for two people is Rs.250\n4. Found \"Crossroads\" in 345, Prince Anwar Shah Road, Kolkata has been rated 4.0 average price for two people is Rs.300\n5. Found \"The Fried Factory\" in 8B, Ibrahimpur Road, Bidhan Pally, Jadavpur, Kolkata has been rated 2.9 average price for two people is Rs.300\n6. Found \"Street Cafe\" in 7, Haridutt Rai Chamaria Road, Near Howrah AC Market, Dobson Road, Howrah has been rated 2.9 average price for two people is Rs.300\n\nWish you have wonderful day ahead! See you soon!"}
    - utter_ask_about_email
* email_affirm
    - utter_ask_emailID
* emailID{"email": "jddk.2jmd@kdl.co.in"}
    - slot{"email": "jddk.2jmd@kdl.co.in"}
    - slot{"email": "jddk.2jmd@kdl.co.in"}
    - action_validate_email
    - slot{"email": "jddk.2jmd@kdl.co.in"}
    - action_send_email
    - utter_email_sent
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - action_restart


## interactive_story_2_3
* greet
    - utter_greet   <!-- predicted: action_listen -->
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mubaim"}
    - slot{"location": "mubaim"}
    - slot{"location": "mubaim"}
    - action_validate_location
    - slot{"location": null}
    - utter_ask_location_again
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_validate_location
    - slot{"location": "Mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - action_validate_cuisine
    - slot{"cuisine": "american"}
    - utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - slot{"price": "low"}
    - action_search_restaurants
    - slot{"body": "Hello, Please find the list of top 1 american restaurants around Mumbai in the low price range.: \n\n1. Found \"Bruciato Food Factory\" in Shop 17, Rainbow Tower, Sector 20, Airoli, Navi Mumbai has been rated 4.2 average price for two people is Rs.500\n\nWish you have wonderful day ahead! See you soon!"}
    - utter_ask_about_email
* email_affirm
    - utter_ask_emailID
* emailID{"email": "jddk.2jmd@kdl.co.in"}
    - slot{"email": "jddk.2jmd@kdl.co.in"}
    - slot{"email": "jddk.2jmd@kdl.co.in"}
    - action_validate_email
    - slot{"email": "jddk.2jmd@kdl.co.in"}
    - action_send_email
    - utter_email_sent
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - action_restart


## interactive_story_2_4
* greet
    - utter_greet   <!-- predicted: action_listen -->
* restaurant_search{"cuisine": "chinese", "location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigarh"}
    - action_validate_location
    - slot{"location": "chandigarh"}
    - action_validate_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - slot{"price": "mid"}
    - action_search_restaurants
    - slot{"body": "Hello, Please find the list of top 4 chinese restaurants around chandigarh in the mid price range.: \n\n1. Found \"Kathmandu Chinese Fast Food\" in Booth 223, Sector 15 D, Near Sector 15, Chandigarh has been rated 3.9 average price for two people is Rs.300\n2. Found \"Sandhya\" in Booth 37 & 40, Rehri Market, Sector 7, Panchkula has been rated 3.9 average price for two people is Rs.250\n3. Found \"Chinese Food Xpress\" in Booth 334, Sector 44D, Near Sector 44, Chandigarh has been rated 3.7 average price for two people is Rs.500\n4. Found \"Crazy Dumplings\" in Shop 1, Elante Mall, Chandigarh Industrial Area, Chandigarh has been rated 3.5 average price for two people is Rs.300\n\nWish you have wonderful day ahead! See you soon!"}
    - utter_ask_about_email
* email_deny
    - utter_email_not_sent
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - action_restart


## interactive_story_2_5
* greet
    - utter_greet   <!-- predicted: action_listen -->
* restaurant_search{"cuisine": "italian", "location": "kochi", "price": "mid"}
    - slot{"cuisine": "italian"}
    - slot{"location": "kochi"}
    - slot{"price": "mid"}
    - slot{"cuisine": "italian"}
    - slot{"location": "kochi"}
    - slot{"price": "mid"}
    - action_validate_location
    - slot{"location": "kochi"}
    - action_validate_cuisine
    - slot{"cuisine": "italian"}
    - action_search_restaurants
    - slot{"body": "Hello, Please find the list of top 6 italian restaurants around kochi in the mid price range.: \n\n1. Found \"Cafe Stories\" in HMT Road, Kalamassery, Kochi, Kochi has been rated 4.0 average price for two people is Rs.500\n2. Found \"Domino's Pizza\" in Ground Floor, Shop G-1 & G-2, Vadakumthala Elanjikal Arcade, Opposite Police Station, Palarivattom, Kochi has been rated 3.6 average price for two people is Rs.400\n3. Found \"Upstairs Italian Pizzeria\" in 1/453 ,Bastian Street , Fortkochi, Kochi Circle, Ernakulam, Kochi has been rated 3.1 average price for two people is Rs.450\n4. Found \"Domino's Pizza\" in 39/4153, 1st Floor, Ravipuram, Kochi Ravipuram has been rated 3.1 average price for two people is Rs.400\n5. Found \"Pizzeria\" in The Woods Manor Hotel, Woodlands Junction, MG Road, Kochi has been rated 2.7 average price for two people is Rs.500\n6. Found \"Domino's Pizza\" in Carnival Food Court, Kakkanad, Kochi has been rated 2.6 average price for two people is Rs.400\n\nWish you have wonderful day ahead! See you soon!"}
    - utter_ask_about_email
* email_affirm
    - utter_ask_emailID
* emailID{"email": "vvijay83@gmail.com"}
    - slot{"email": "vvijay83@gmail.com"}
    - slot{"email": "vvijay83@gmail.com"}
    - action_validate_email
    - slot{"email": "vvijay83@gmail.com"}
    - action_send_email
    - utter_email_sent
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - action_restart


## interactive_story_2_6
* greet
    - utter_greet   <!-- predicted: action_listen -->
* restaurant_search{"price": "high", "cuisine": "mexican", "location": "chennai", "email": "vvijay83@gmail.com"}
    - slot{"cuisine": "mexican"}
    - slot{"email": "vvijay83@gmail.com"}
    - slot{"location": "chennai"}
    - slot{"price": "high"}
    - slot{"cuisine": "mexican"}
    - slot{"email": "vvijay83@gmail.com"}
    - slot{"location": "chennai"}
    - slot{"price": "high"}
    - action_validate_location
    - slot{"location": "chennai"}
    - action_validate_cuisine
    - slot{"cuisine": "mexican"}
    - action_validate_email
    - slot{"email": "vvijay83@gmail.com"}
    - action_search_restaurants
    - slot{"body": "Hello, Please find the list of top 5 mexican restaurants around chennai in the high price range.: \n\n1. Found \"Fusilli Reasons\" in 2/64, Ormes Main Road, Kilpauk, Chennai has been rated 4.6 average price for two people is Rs.400\n2. Found \"Pasta Square\" in 6th Street, Gopalapuram, Chennai has been rated 3.8 average price for two people is Rs.350\n3. Found \"Yummy Bowls @fs\" in Badma Avenue Balaraman Road, Thailavaram has been rated 3.6 average price for two people is Rs.400\n4. Found \"The Pirates Barbeque\" in Plot 5, Sholinganalur Road, Kailash Nagar, Medavakkam, Chennai has been rated 3.3 average price for two people is Rs.200\n5. Found \"Cafe Gangsta\" in 48/20, Abdul Asees Street, T. Nagar, Chennai has been rated 2.9 average price for two people is Rs.300\n\nWish you have wonderful day ahead! See you soon!"}
    - action_send_email
    - utter_email_sent
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - action_restart


## interactive_story_2_6a
* greet
    - utter_greet   <!-- predicted: action_listen -->
* restaurant_search{"price": "high", "cuisine": "mexican", "location": "chennai", "email": "vvijay83@gmail..com"}
    - slot{"cuisine": "mexican"}
    - slot{"email": "vvijay83@gmail..com"}
    - slot{"location": "chennai"}
    - slot{"price": "high"}
    - slot{"cuisine": "mexican"}
    - slot{"email": "vvijay83@gmail..com"}
    - slot{"location": "chennai"}
    - slot{"price": "high"}
    - action_validate_location
    - slot{"location": "chennai"}
    - action_validate_cuisine
    - slot{"cuisine": "mexican"}
    - action_validate_email
    - slot{"email": null}
    - utter_ask_emailID
* emailID{"email": "vvijay83@gmail.com"}
    - slot{"email": "vvijay83@gmail.com"}
    - slot{"email": "vvijay83@gmail.com"}
    - action_validate_email
    - slot{"email": "vvijay83@gmail.com"}
    - action_search_restaurants
    - slot{"body": "Hello, Please find the list of top 5 mexican restaurants around chennai in the high price range.: \n\n1. Found \"Fusilli Reasons\" in 2/64, Ormes Main Road, Kilpauk, Chennai has been rated 4.6 average price for two people is Rs.400\n2. Found \"Pasta Square\" in 6th Street, Gopalapuram, Chennai has been rated 3.8 average price for two people is Rs.350\n3. Found \"Yummy Bowls @fs\" in Badma Avenue Balaraman Road, Thailavaram has been rated 3.6 average price for two people is Rs.400\n4. Found \"The Pirates Barbeque\" in Plot 5, Sholinganalur Road, Kailash Nagar, Medavakkam, Chennai has been rated 3.3 average price for two people is Rs.200\n5. Found \"Cafe Gangsta\" in 48/20, Abdul Asees Street, T. Nagar, Chennai has been rated 2.9 average price for two people is Rs.300\n\nWish you have wonderful day ahead! See you soon!"}
    - action_send_email
    - utter_email_sent
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - action_restart


## interactive_story_2_6a_a
* greet
    - utter_greet   <!-- predicted: action_listen -->
* restaurant_search{"price": "high", "cuisine": "mexican", "location": "chennai", "email": "vvijay83@gmail..com"}
    - slot{"cuisine": "mexican"}
    - slot{"email": "vvijay83@gmail..com"}
    - slot{"location": "chennai"}
    - slot{"price": "high"}
    - slot{"cuisine": "mexican"}
    - slot{"email": "vvijay83@gmail..com"}
    - slot{"location": "chennai"}
    - slot{"price": "high"}
    - action_validate_location
    - slot{"location": "chennai"}
    - action_validate_cuisine
    - slot{"cuisine": "mexican"}
    - action_validate_email
    - slot{"email": null}
    - utter_ask_emailID
* email_affirm{"email": "xyz@sth.edu"}
    - slot{"email": "xyz@sth.edu"}
    - slot{"email": "xyz@sth.edu"}
    - action_validate_email
    - slot{"email": "xyz@sth.edu"}
    - action_search_restaurants
    - slot{"body": "Hello, Please find the list of top 5 mexican restaurants around chennai in the high price range.: \n\n1. Found \"Fusilli Reasons\" in 2/64, Ormes Main Road, Kilpauk, Chennai has been rated 4.6 average price for two people is Rs.400\n2. Found \"Pasta Square\" in 6th Street, Gopalapuram, Chennai has been rated 3.8 average price for two people is Rs.350\n3. Found \"Yummy Bowls @fs\" in Badma Avenue Balaraman Road, Thailavaram has been rated 3.6 average price for two people is Rs.400\n4. Found \"The Pirates Barbeque\" in Plot 5, Sholinganalur Road, Kailash Nagar, Medavakkam, Chennai has been rated 3.3 average price for two people is Rs.200\n5. Found \"Cafe Gangsta\" in 48/20, Abdul Asees Street, T. Nagar, Chennai has been rated 2.9 average price for two people is Rs.300\n\nWish you have wonderful day ahead! See you soon!"}
    - action_send_email
    - utter_email_sent
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - action_restart


## interactive_story_2_6b
* greet
    - utter_greet   <!-- predicted: action_listen -->
* restaurant_search{"price": "low", "cuisine": "chinese", "location": "conoor", "email": "vvijay83@gmail.com"}
    - slot{"cuisine": "chinese"}
    - slot{"email": "vvijay83@gmail.com"}
    - slot{"location": "conoor"}
    - slot{"price": "low"}
    - slot{"cuisine": "chinese"}
    - slot{"email": "vvijay83@gmail.com"}
    - slot{"location": "conoor"}
    - slot{"price": "low"}
    - action_validate_location
    - slot{"location": null}
    - utter_ask_location_again
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_validate_location
    - slot{"location": "Mumbai"}
    - action_validate_cuisine
    - slot{"cuisine": "chinese"}
    - action_validate_email
    - slot{"email": "vvijay83@gmail.com"}
    - action_search_restaurants
    - slot{"body": "Hello, Please find the list of top 5 mexican restaurants around chennai in the high price range.: \n\n1. Found \"Fusilli Reasons\" in 2/64, Ormes Main Road, Kilpauk, Chennai has been rated 4.6 average price for two people is Rs.400\n2. Found \"Pasta Square\" in 6th Street, Gopalapuram, Chennai has been rated 3.8 average price for two people is Rs.350\n3. Found \"Yummy Bowls @fs\" in Badma Avenue Balaraman Road, Thailavaram has been rated 3.6 average price for two people is Rs.400\n4. Found \"The Pirates Barbeque\" in Plot 5, Sholinganalur Road, Kailash Nagar, Medavakkam, Chennai has been rated 3.3 average price for two people is Rs.200\n5. Found \"Cafe Gangsta\" in 48/20, Abdul Asees Street, T. Nagar, Chennai has been rated 2.9 average price for two people is Rs.300\n\nWish you have wonderful day ahead! See you soon!"}
    - action_send_email
    - utter_email_sent
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - action_restart


## interactive_story_2_6c
* greet
    - utter_greet   <!-- predicted: action_listen -->
* restaurant_search{"price": "high", "cuisine": "japanese", "location": "delhi", "email": "vvijay83@gmail.com"}
    - slot{"cuisine": "japanese"}
    - slot{"email": "vvijay83@gmail.com"}
    - slot{"location": "delhi"}
    - slot{"price": "high"}
    - slot{"cuisine": "japanese"}
    - slot{"email": "vvijay83@gmail.com"}
    - slot{"location": "delhi"}
    - slot{"price": "high"}
    - action_validate_location
    - slot{"location": "delhi"}
    - action_validate_cuisine
    - slot{"cuisine": null}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_validate_cuisine
    - slot{"cuisine": "South Indian"}
    - action_validate_email
    - slot{"email": "vvijay83@gmail.com"}
    - action_search_restaurants
    - slot{"body": "Hello, Please find the list of top 5 mexican restaurants around chennai in the high price range.: \n\n1. Found \"Fusilli Reasons\" in 2/64, Ormes Main Road, Kilpauk, Chennai has been rated 4.6 average price for two people is Rs.400\n2. Found \"Pasta Square\" in 6th Street, Gopalapuram, Chennai has been rated 3.8 average price for two people is Rs.350\n3. Found \"Yummy Bowls @fs\" in Badma Avenue Balaraman Road, Thailavaram has been rated 3.6 average price for two people is Rs.400\n4. Found \"The Pirates Barbeque\" in Plot 5, Sholinganalur Road, Kailash Nagar, Medavakkam, Chennai has been rated 3.3 average price for two people is Rs.200\n5. Found \"Cafe Gangsta\" in 48/20, Abdul Asees Street, T. Nagar, Chennai has been rated 2.9 average price for two people is Rs.300\n\nWish you have wonderful day ahead! See you soon!"}
    - action_send_email
    - utter_email_sent
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - action_restart


## interactive_story_2_8
* greet
    - utter_greet   <!-- predicted: action_listen -->
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "yercaud"}
    - slot{"location": "yercaud"}
    - slot{"location": "yercaud"}
    - action_validate_location
    - slot{"location": null}
    - utter_ask_location_again
* restaurant_search{"location": "warangal"}
    - slot{"location": "warangal"}
    - slot{"location": "warangal"}
    - action_validate_location
    - slot{"location": "warangal"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - action_validate_cuisine
    - slot{"cuisine": null}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - action_validate_cuisine
    - slot{"cuisine": "north indian"}
    - utter_ask_price
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - slot{"price": "mid"}
    - action_search_restaurants
    - slot{"body": "Hello, Please find the list of top 6 north indian restaurants around warangal in the mid price range.: \n\n1. Found \"Hotel Shreya\" in Near Kalyan Jewellers, New Bus Stand road, Kakaji Colony, Hanamkonda, Hanamakonda, Warangal has been rated 3.8 average price for two people is Rs.400\n2. Found \"Hangout\" in Mandi Bazar, Girmajipet, Warangal has been rated 3.8 average price for two people is Rs.400\n3. Found \"Arabian Knights\" in 11-25-27/1, Jakotia Mall, Pochamma Maidan, Girmajipet, Warangal has been rated 3.8 average price for two people is Rs.350\n4. Found \"Telangana Biryani Point\" in House :24-7-186, Near Sub Station, Kazipet, Warangal has been rated 3.6 average price for two people is Rs.400\n5. Found \"Dolphin Restaurant\" in Punjab National Bank Lane, Sherpura, Mathwada, Warangal has been rated 3.5 average price for two people is Rs.500\n6. Found \"Hotel Vaishnavi Grand\" in Fatima Complex, Fatima Nagar, NH 163, Kazipet, Warangal has been rated 3.4 average price for two people is Rs.500\n\nWish you have wonderful day ahead! See you soon!"}
    - utter_ask_about_email
* email_affirm
    - utter_ask_emailID
* emailID{"email": "vijay@google"}
    - slot{"email": "vijay@google"}
    - slot{"email": "vijay@google"}
    - action_validate_email
    - slot{"email": null}
    - utter_ask_emailID
* emailID{"email": "vvijay83@gmail.com"}
    - slot{"email": "vvijay83@gmail.com"}
    - slot{"email": "vvijay83@gmail.com"}
    - action_validate_email
    - slot{"email": "vvijay83@gmail.com"}
    - action_send_email
    - utter_email_sent
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - action_restart


## interactive_story_3_1
* greet
    - utter_greet   <!-- predicted: action_listen -->
* restaurant_search{"location": "Chikmagalur"}
    - slot{"location": "Chikmagalur"}
    - slot{"location": "Chikmagalur"}
    - action_validate_location
    - slot{"location": null}
    - utter_ask_location_again
* restaurant_search{"location": "madurai"}
    - slot{"location": "madurai"}
    - slot{"location": "madurai"}
    - action_validate_location
    - slot{"location": "madurai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "bakery"}
    - slot{"cuisine": "bakery"}
    - slot{"cuisine": "bakery"}
    - action_validate_cuisine
    - slot{"cuisine": null}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_validate_cuisine
    - slot{"cuisine": "North Indian"}
    - utter_ask_price
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - slot{"price": "mid"}
    - action_search_restaurants
    - slot{"body": "Hello, Please find the list of top 10 North Indian restaurants around madurai in the mid price range.: \n\n1. Found \"Zaitoon\" in 32, 80 Feet Road, Anna Nagar, Sathamangalam, Madurai has been rated 4.8 average price for two people is Rs.450\n2. Found \"Kumar Mess\" in 57, Alagar Kovil Road, Tallakulam, KK Nagar, Madurai has been rated 4.6 average price for two people is Rs.350\n3. Found \"KFC\" in 61/4B, Pattu Arcade, Bypass Road, Opposite World Of Titan, SS Colony, Madurai has been rated 4.4 average price for two people is Rs.450\n4. Found \"KFC\" in 64, 80 Feet Road, Anna Nagar, Sathamangalam, Madurai has been rated 4.4 average price for two people is Rs.450\n5. Found \"Mukku Kadai K Subbu Moongil Thottam\" in Bharathi Street, KK Nagar, Madurai has been rated 4.3 average price for two people is Rs.350\n6. Found \"Dindigul Thalappakatti\" in Bypass Road, Kalavasal, SS Colony, Madurai has been rated 4.2 average price for two people is Rs.450\n7. Found \"Domino's Pizza\" in Ground Floor, Sivasakthi Plaza, 80 Feet Road, Managairi, KK Nagar, Madurai has been rated 4.1 average price for two people is Rs.400\n8. Found \"Dindigul Thalappakatti\" in 1, Melur Main Road, Opposite to District Court, KK Nagar, Madurai has been rated 4.1 average price for two people is Rs.650\n9. Found \"Al Ahad Muslim Biriyani\" in 5 /12, Subburaman Street, Gandhi Nagar, Anna Bus Stand, Anna Nagar, Sathamangalam, Madurai has been rated 4.1 average price for two people is Rs.400\n10. Found \"Domino's Pizza\" in Near Aristo Hospital, Bypass Main Road, SS Colony, Madurai has been rated 4.0 average price for two people is Rs.400\n\nWish you have wonderful day ahead! See you soon!"}
    - utter_ask_about_email
* email_affirm{"email_affirm": "please do"}
    - utter_ask_emailID
* emailID{"email": "chatbot@gmail.com"}
    - slot{"email": "chatbot@gmail.com"}
    - slot{"email": "chatbot@gmail.com"}
    - action_validate_email
    - slot{"email": "chatbot@gmail.com"}
    - action_send_email
    - utter_email_sent
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - action_restart


## interactive_story_3_4
* greet
    - utter_greet   <!-- predicted: action_listen -->
* restaurant_search{"location": "noida"}
    - slot{"location": "noida"}
    - slot{"location": "noida"}
    - action_validate_location
    - slot{"location": "noida"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "spanish"}
    - slot{"cuisine": "spanish"}
    - slot{"cuisine": "spanish"}
    - action_validate_cuisine
    - slot{"cuisine": null}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_validate_cuisine
    - slot{"cuisine": "South Indian"}
    - utter_ask_price
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - slot{"price": "mid"}
    - action_search_restaurants
    - slot{"body": "Hello, Please find the list of top 10 South Indian restaurants around noida in the mid price range.: \n\n1. Found \"Oishii Wok\" in Behind Super Mart 2, DLF Phase 4, Gurgaon has been rated 4.9 average price for two people is Rs.700\n2. Found \"Punjabi Angithi\" in 32-22, A 4, DDA Market, Paschim Vihar, New Delhi has been rated 4.5 average price for two people is Rs.400\n3. Found \"Gulab\" in 5, Main Road, Pitampura, New Delhi has been rated 4.2 average price for two people is Rs.500\n4. Found \"Singla's\" in A-139/140, Main Road, Madhu Vihar, Near Hasanpur Depot, IP Extension, New Delhi has been rated 4.2 average price for two people is Rs.500\n5. Found \"Bikanervala Angan\" in 10181, 82, Arya Samaj Road, Karol Bagh, New Delhi has been rated 4.1 average price for two people is Rs.600\n6. Found \"Haldiram's\" in 45, Ring Road, Lajpat Nagar 2, New Delhi has been rated 4.1 average price for two people is Rs.600\n7. Found \"Bikanervala\" in Plot 3-5, Near Leisure Valley Park, Sector 29, Gurgaon has been rated 4.1 average price for two people is Rs.600\n8. Found \"Haldiram's\" in C 9, Opposite ITI, Main Market, Malviya Nagar, New Delhi has been rated 4.1 average price for two people is Rs.600\n9. Found \"Om Sweets & Snacks\" in SCO 17, Main Market, Sector 31, Gurgaon has been rated 4.1 average price for two people is Rs.500\n10. Found \"Bikanervala\" in Suncity Business Tower, Golf Course Road, Gurgaon has been rated 4.1 average price for two people is Rs.600\n\nWish you have wonderful day ahead! See you soon!"}
    - utter_ask_about_email
* email_affirm
    - utter_ask_emailID
* emailID{"email": "noreply#yahoo.com"}
    - slot{"email": "noreply#yahoo.com"}
    - slot{"email": "noreply#yahoo.com"}
    - action_validate_email
    - slot{"email": null}
    - utter_ask_emailID
* emailID{"email": "rajasvim1617@gmail.com"}
    - slot{"email": "rajasvim1617@gmail.com"}
    - slot{"email": "rajasvim1617@gmail.com"}
    - action_validate_email
    - slot{"email": "rajasvim1617@gmail.com"}
    - action_send_email
    - utter_email_sent
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - action_restart


## interactive_story_3_5
* greet
    - utter_greet   <!-- predicted: action_listen -->
* restaurant_search{"location": "savanur"}
    - slot{"location": "savanur"}
    - slot{"location": "savanur"}
    - action_validate_location
    - slot{"location": null}
    - utter_ask_location_again
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_validate_location
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - action_validate_cuisine
    - slot{"cuisine": "Mexican"}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"body": "Hello, Please find the list of top 10 Mexican restaurants around bangalore in the high price range.: \n\n1. Found \"Empire Restaurant\" in Next To BSNL, HAL 2nd Stage, 80 Feet Road, Indiranagar, Bangalore has been rated 4.6 average price for two people is Rs.800\n2. Found \"Empire Restaurant\" in 148/1, Bilekhahalli Village, Near IIM Bangalore, Arekere Gate, Bannerghatta Road, Bangalore has been rated 4.6 average price for two people is Rs.800\n3. Found \"Empire Restaurant\" in 701, Sri Lakshmi Narayana Arcade, West of Chord Road 2nd Stage, Modi Hospital Road, Mahalakshimipuram, Rajajinagar, Bangalore has been rated 4.5 average price for two people is Rs.800\n4. Found \"Empire Restaurant\" in 103, Industrial Area, 5th Block, Near Jyothi Nivas College, Koramangala 5th Block, Bangalore has been rated 4.5 average price for two people is Rs.800\n5. Found \"Empire Restaurant\" in 4, Opposite NMKRV College, 21st C Cross Road, 3rd Block, Jayanagar, Bangalore has been rated 4.5 average price for two people is Rs.800\n6. Found \"Empire Restaurant\" in 83, Nehru Main Road, Kammanahalli, Bangalore has been rated 4.4 average price for two people is Rs.800\n7. Found \"Empire Restaurant\" in 24th Main Road, 5th Phase, JP Nagar, Bangalore has been rated 4.4 average price for two people is Rs.800\n8. Found \"Imperio Restaurant\" in 429, 7th Main Road, HRBR Layout, 1st Block, Kalyan Nagar, Bangalore has been rated 4.3 average price for two people is Rs.900\n9. Found \"Empire Restaurant\" in 161, 80 Feet Road, Ganganagar, Matadahalli, RT Nagar, Bangalore has been rated 4.3 average price for two people is Rs.800\n10. Found \"Le Arabia\" in 11th Main Road, Bimajyothi LIC Colony, Basaveshwara Nagar, Bangalore has been rated 4.3 average price for two people is Rs.800\n\nWish you have wonderful day ahead! See you soon!"}
    - utter_ask_about_email
* email_affirm{"email": "google123$gmail.com"}
    - slot{"email": "google123$gmail.com"}
    - slot{"email": "google123$gmail.com"}
    - action_validate_email
    - slot{"email": null}
    - utter_ask_emailID
* emailID{"email": "rajasvim1617@gmail.com"}
    - slot{"email": "rajasvim1617@gmail.com"}
    - slot{"email": "rajasvim1617@gmail.com"}
    - action_validate_email
    - slot{"email": "rajasvim1617@gmail.com"}
    - action_send_email
    - utter_email_sent
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - action_restart


## interactive_story_3_6
* greet
    - utter_greet   <!-- predicted: action_listen -->
* restaurant_search{"cuisine": "Turkish"}
    - slot{"cuisine": "Turkish"}
    - slot{"cuisine": "Turkish"}
    - action_validate_cuisine
    - slot{"cuisine": null}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - action_validate_cuisine
    - slot{"cuisine": "Mexican"}
    - utter_ask_location
* restaurant_search{"location": "krishnagiri"}
    - slot{"location": "krishnagiri"}
    - slot{"location": "krishnagiri"}
    - action_validate_location
    - slot{"location": null}
    - utter_ask_location_again
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
    - slot{"location": "pune"}
    - action_validate_location
    - slot{"location": "pune"}
    - utter_ask_price   <!-- predicted: action_validate_cuisine -->
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - slot{"price": "low"}
    - action_search_restaurants
    - slot{"body": "Hello, Please find the list of top 2 Chinese restaurants around pune in the low price range.: \n\n1. Found \"Arabian Bites\" in Shop 2, Bulding 69, Opposite Kausar Baugh Masjid, Kondhwa, Pune has been rated 4.2 average price for two people is Rs.250\n2. Found \"Teri Rajput\" in Shop 4, Survey 32A/1b, Plot 325, Sukhwani Park, Koregaon Park, Pune has been rated 4.1 average price for two people is Rs.300\n\nWish you have wonderful day ahead! See you soon!"}
    - utter_ask_about_email
* emailID{"email": "invalidemail.com"}
    - slot{"email": "invalidemail.com"}
    - slot{"email": "invalidemail.com"}
    - action_validate_email
    - slot{"email": null}
    - utter_ask_emailID
* emailID{"email": "vvijay83@gmail.com"}
    - slot{"email": "vvijay83@gmail.com"}
    - slot{"email": "vvijay83@gmail.com"}
    - action_validate_email
    - slot{"email": "vvijay83@gmail.com"}
    - action_send_email
    - utter_email_sent
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - action_restart


## interactive_story_3_7
* greet
    - utter_greet   <!-- predicted: action_listen -->
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - action_validate_cuisine
    - slot{"cuisine": "Mexican"}
    - utter_ask_location
* restaurant_search{"location": "ooty"}
    - slot{"location": "ooty"}
    - slot{"location": "ooty"}
    - action_validate_location
    - slot{"location": null}
    - utter_ask_location_again
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
    - slot{"location": "pune"}
    - action_validate_location
    - slot{"location": "pune"}
    - utter_ask_price   <!-- predicted: action_validate_cuisine -->
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - slot{"price": "low"}
    - action_search_restaurants
    - slot{"body": "Hello, Please find the list of top 2 Chinese restaurants around pune in the low price range.: \n\n1. Found \"Arabian Bites\" in Shop 2, Bulding 69, Opposite Kausar Baugh Masjid, Kondhwa, Pune has been rated 4.2 average price for two people is Rs.250\n2. Found \"Teri Rajput\" in Shop 4, Survey 32A/1b, Plot 325, Sukhwani Park, Koregaon Park, Pune has been rated 4.1 average price for two people is Rs.300\n\nWish you have wonderful day ahead! See you soon!"}
    - utter_ask_about_email
* emailID{"email": "invalidemail.com"}
    - slot{"email": "invalidemail.com"}
    - slot{"email": "invalidemail.com"}
    - action_validate_email
    - slot{"email": null}
    - utter_ask_emailID
* emailID{"email": "vvijay83@gmail.com"}
    - slot{"email": "vvijay83@gmail.com"}
    - slot{"email": "vvijay83@gmail.com"}
    - action_validate_email
    - slot{"email": "vvijay83@gmail.com"}
    - action_send_email
    - utter_email_sent
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - action_restart


## greet_goodbye
* greet
    - utter_greet   <!-- predicted: action_listen -->
* goodbye
    - utter_goodbye
    - action_restart


## interactive_story_3_8
* greet
    - utter_greet   <!-- predicted: action_listen -->
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_validate_cuisine
    - slot{"cuisine": "Italian"}
    - utter_ask_location
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - action_validate_location
    - slot{"location": "kolkata"}
    - utter_ask_price   <!-- predicted: action_validate_cuisine -->
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - slot{"price": "mid"}
    - action_search_restaurants
    - slot{"body": "Hello, Please find the list of top 2 Chinese restaurants around pune in the low price range.: \n\n1. Found \"Arabian Bites\" in Shop 2, Bulding 69, Opposite Kausar Baugh Masjid, Kondhwa, Pune has been rated 4.2 average price for two people is Rs.250\n2. Found \"Teri Rajput\" in Shop 4, Survey 32A/1b, Plot 325, Sukhwani Park, Koregaon Park, Pune has been rated 4.1 average price for two people is Rs.300\n\nWish you have wonderful day ahead! See you soon!"}
    - utter_ask_about_email
* email_affirm
    - utter_ask_emailID
* emailID{"email": "vvijay83@gmail.com"}
    - slot{"email": "vvijay83@gmail.com"}
    - slot{"email": "vvijay83@gmail.com"}
    - action_validate_email
    - slot{"email": "vvijay83@gmail.com"}
    - action_send_email
    - utter_email_sent
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - action_restart


## interactive_story_4_1
* greet
    - utter_greet   <!-- predicted: action_listen -->
* restaurant_search{"price": "high", "cuisine": "mexican", "location": "kottayam"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "kottayam"}
    - slot{"price": "high"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "kottayam"}
    - slot{"price": "high"}
    - action_validate_location
    - slot{"location": null}
    - utter_ask_location_again
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_validate_location
    - slot{"location": "Mumbai"}
    - action_search_restaurants   <!-- predicted: action_validate_cuisine -->
    - slot{"body": "Hello, Please find the list of top 4 mexican restaurants around Mumbai in the high price range.: \n\n1. Found \"Soul Curry\" in Crystal Building, Ground Floor, Near Gopal Sharma School, Powai Vihar Complex, Powai, Mumbai has been rated 4.4 average price for two people is Rs.1800\n2. Found \"Froozo\" in 3, King Palace Building, Opposite Link House, Link Road, Malad West, Mumbai has been rated 4.3 average price for two people is Rs.800\n3. Found \"Maiz Mexican Kitchen\" in Shop 6, Mahavir Apartments, Javji Dadaji Marg, Near Bharat Petroleum, Tardeo, Mumbai has been rated 4.1 average price for two people is Rs.800\n4. Found \"Maiz Mexican Kitchen\" in Shop 45, Ground Floor, Hari Market Building, 4th Road, Ram Krishna Nagar, Khar West, Mumbai has been rated 4.0 average price for two people is Rs.800\n\nWish you have wonderful day ahead! See you soon!"}
    - utter_ask_about_email
* email_affirm
    - utter_ask_emailID
* emailID{"email": "vvijay83@gmail.com"}
    - slot{"email": "vvijay83@gmail.com"}
    - slot{"email": "vvijay83@gmail.com"}
    - action_validate_email
    - slot{"email": "vvijay83@gmail.com"}
    - action_send_email
    - utter_email_sent
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - action_restart


## interactive_story_4_2
* greet
    - utter_greet   <!-- predicted: action_listen -->
* restaurant_search{"price": "low", "cuisine": "korean", "location": "karaikal"}
    - slot{"cuisine": "korean"}
    - slot{"location": "karaikal"}
    - slot{"price": "low"}
    - slot{"cuisine": "korean"}
    - slot{"location": "karaikal"}
    - slot{"price": "low"}
    - action_validate_location
    - slot{"location": null}
    - utter_ask_location_again
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_location
    - slot{"location": "delhi"}
    - action_validate_cuisine
    - slot{"cuisine": null}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - action_validate_cuisine
    - slot{"cuisine": "American"}
    - action_search_restaurants
    - slot{"body": "Hello, Please find the list of top 3 American restaurants around delhi in the low price range.: \n\n1. Found \"Pandit Ji Parantha Hut\" in 10, Community Centre, Ashok Vihar Phase 2, New Delhi has been rated 4.0 average price for two people is Rs.200\n2. Found \"Radha Krishna Chole Bhature\" in 115, Priya Enclave, Karkardooma, New Delhi has been rated 3.8 average price for two people is Rs.300\n3. Found \"Sunil Momos.com\" in 14, Block GH, Paschim Vihar, New Delhi has been rated 3.7 average price for two people is Rs.300\n\nWish you have wonderful day ahead! See you soon!"}
    - utter_ask_about_email
* email_affirm
    - utter_ask_emailID
* emailID{"email": "vvijay4u@gmail.com"}
    - slot{"email": "vvijay4u@gmail.com"}
    - slot{"email": "vvijay4u@gmail.com"}
    - action_validate_email
    - slot{"email": "vvijay4u@gmail.com"}
    - action_send_email
    - utter_email_sent
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - action_restart


## interactive_story_4_3
* greet
    - utter_greet   <!-- predicted: action_listen -->
* restaurant_search{"price": "mid", "cuisine": "vietnamese", "location": "panruti"}
    - slot{"cuisine": "vietnamese"}
    - slot{"location": "panruti"}
    - slot{"price": "mid"}
    - slot{"cuisine": "vietnamese"}
    - slot{"location": "panruti"}
    - slot{"price": "mid"}
    - action_validate_location
    - slot{"location": null}
    - utter_ask_location_again
* restaurant_search{"location": "pondicherry"}
    - slot{"location": "pondicherry"}
    - slot{"location": "pondicherry"}
    - action_validate_location
    - slot{"location": "pondicherry"}
    - action_validate_cuisine
    - slot{"cuisine": null}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_validate_cuisine
    - slot{"cuisine": "North Indian"}
    - action_search_restaurants
    - slot{"body": "Hello, Please find the list of top 10 North Indian restaurants around pondicherry in the mid price range.: \n\n1. Found \"Yaa Mohaideen Briyani\" in 336 & 338, Main Road, Pallavaram, Chennai has been rated 4.4 average price for two people is Rs.500\n2. Found \"SS Hyderabad Biryani\" in 98/339, Arcot Road, Opposite Gokulam Chit Funds, Kodambakkam, Chennai has been rated 4.4 average price for two people is Rs.500\n3. Found \"Yaa Mohaideen Biryani\" in 4/158, Church Road, Opposite Uzhavar Santhai & Tea Stall, Pallavaram, Chennai has been rated 4.4 average price for two people is Rs.600\n4. Found \"Mami Tiffen Stall\" in 7, Pitchupillai Street, Near Kapaleeshwarar Temple, Mylapore, Chennai has been rated 4.3 average price for two people is Rs.400\n5. Found \"Bakya Veg Restaurant\" in 20, Jaishankar Street, Near Ayodhya Mandapam, West Mambalam, Chennai has been rated 4.2 average price for two people is Rs.400\n6. Found \"Kovai Alankar Vilas\" in AC 3, 2nd Avenue, Anna Nagar East, Chennai . has been rated 4.2 average price for two people is Rs.700\n7. Found \"Hotel Paramount\" in 12/5, Ormes Road, Kilpauk, Chennai has been rated 4.2 average price for two people is Rs.500\n8. Found \"KFC\" in Number 5, GST Road, Tambaram Sanatorium, Chromepet, Chennai has been rated 4.1 average price for two people is Rs.500\n9. Found \"Yaa Mohaideen Biryani\" in 13, Kailash Nagar, Perumbakkam, Medavakkam, Chennai has been rated 4.0 average price for two people is Rs.700\n10. Found \"SS Hyderabad Biryani\" in 152, Paper Mills Road, Near Vasan Eye Care, Perambur, Chennai has been rated 4.0 average price for two people is Rs.500\n\nWish you have wonderful day ahead! See you soon!"}
    - utter_ask_about_email
* email_affirm{"email": "vijay.123"}
    - slot{"email": "vijay.123"}
    - slot{"email": "vijay.123"}
    - utter_ask_emailID   <!-- predicted: action_validate_email -->
* emailID{"email": "vvijay83@gmail.com"}
    - slot{"email": "vvijay83@gmail.com"}
    - slot{"email": "vvijay83@gmail.com"}
    - action_validate_email
    - slot{"email": "vvijay83@gmail.com"}
    - action_send_email
    - utter_email_sent
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - action_restart


## interactive_story_4_4
* greet
    - utter_greet   <!-- predicted: action_listen -->
* restaurant_search{"price": "low", "cuisine": "spanish", "location": "kochi"}
    - slot{"cuisine": "spanish"}
    - slot{"location": "kochi"}
    - slot{"price": "low"}
    - slot{"cuisine": "spanish"}
    - slot{"location": "kochi"}
    - slot{"price": "low"}
    - action_validate_location
    - slot{"location": "kochi"}
    - action_validate_cuisine
    - slot{"cuisine": null}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_validate_cuisine
    - slot{"cuisine": "Italian"}
    - action_search_restaurants
    - slot{"body": "Hello, Please find the list of top 5 Italian restaurants around kochi in the low price range.: \n\n1. Found \"Westleys Restocafe\" in Ground Floor, Kalliyath Building, Mamangalam, Palarivattom, Kochi has been rated 4.3 average price for two people is Rs.300\n2. Found \"Biriyani Chembu\" in 33 Ayisha Buluding Changampuzha Nagar South Kalamessry, Kalamassery, Kochi has been rated 4.2 average price for two people is Rs.300\n3. Found \"Real Arabia\" in 39/6648(61/1796) M G Road, Revipuram, Ernakulam, Ravipuram, Kochi has been rated 4.1 average price for two people is Rs.300\n4. Found \"Hotel Paradise - Palarivattom\" in Janatha Junction, Palarivattom, Palarivattom, Kochi has been rated 3.9 average price for two people is Rs.200\n5. Found \"Thaal Kitchen\" in Infopark Expressway, Near Rajagiri College, Kakkanad, Kochi has been rated 3.7 average price for two people is Rs.300\n\nWish you have wonderful day ahead! See you soon!"}
    - utter_ask_about_email
* email_affirm{"email": "vvijay@yahoo.com"}
    - slot{"email": "vvijay@yahoo.com"}
    - slot{"email": "vvijay@yahoo.com"}
    - action_validate_email
    - slot{"email": "vvijay@yahoo.com"}
    - action_send_email
    - utter_email_sent
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - action_restart


## interactive_story_4_5
* greet
    - utter_greet   <!-- predicted: action_listen -->
* restaurant_search{"price": "high", "cuisine": "french", "location": "salem"}
    - slot{"cuisine": "french"}
    - slot{"location": "salem"}
    - slot{"price": "high"}
    - slot{"cuisine": "french"}
    - slot{"location": "salem"}
    - slot{"price": "high"}
    - action_validate_location
    - slot{"location": "salem"}
    - action_validate_cuisine
    - slot{"cuisine": null}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_validate_cuisine
    - slot{"cuisine": "South Indian"}
    - action_search_restaurants
    - slot{"body": "Hello, Please find the list of top 1 South Indian restaurants around salem in the high price range.: \n\n1. Found \"Barbeque Nation\" in 3rd Floor, Jayakumar Plaza, Saradha College Main Road, Alagapuram Pudur, Salem has been rated 4.9 average price for two people is Rs.1200\n\nWish you have wonderful day ahead! See you soon!"}
    - utter_ask_about_email
* email_affirm
    - utter_ask_emailID
* emailID{"email": "12345.com"}
    - slot{"email": "12345.com"}
    - slot{"email": "12345.com"}
    - action_validate_email
    - slot{"email": null}
    - utter_ask_emailID
* emailID{"email": "vvijay83@gmail.com"}
    - slot{"email": "vvijay83@gmail.com"}
    - slot{"email": "vvijay83@gmail.com"}
    - action_validate_email
    - slot{"email": "vvijay83@gmail.com"}
    - action_send_email
    - utter_email_sent
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - action_restart


## interactive_story_4_6
* greet
    - utter_greet   <!-- predicted: action_listen -->
* restaurant_search{"price": "low", "cuisine": "Chinese", "location": "Chennai"}
    - slot{"cuisine": "Chinese"}
    - slot{"location": "Chennai"}
    - slot{"price": "low"}
    - slot{"cuisine": "Chinese"}
    - slot{"location": "Chennai"}
    - slot{"price": "low"}
    - action_validate_location
    - slot{"location": "Chennai"}
    - action_validate_cuisine
    - slot{"cuisine": "Chinese"}
    - action_search_restaurants
    - slot{"body": "Hello, Please find the list of top 1 Chinese restaurants around Chennai in the low price range.: \n\n1. Found \"Tasty Kitchen\" in 135B,SRP Colony, Peravallur, Perambur, Chennai has been rated 4.1 average price for two people is Rs.300\n\nWish you have wonderful day ahead! See you soon!"}
    - utter_ask_about_email
* email_affirm{"email": "vijay#gmai..co.om"}
    - slot{"email": "vijay#gmai..co.om"}
    - slot{"email": "vijay#gmai..co.om"}
    - action_validate_email
    - slot{"email": null}
    - utter_ask_emailID
* emailID{"email": "vvijay4u@gmail.com"}
    - slot{"email": "vvijay4u@gmail.com"}
    - slot{"email": "vvijay4u@gmail.com"}
    - action_validate_email
    - slot{"email": "vvijay4u@gmail.com"}
    - action_send_email
    - utter_email_sent
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - action_restart


## interactive_story_4_7
* greet
    - utter_greet   <!-- predicted: action_listen -->
* restaurant_search{"price": "mid", "cuisine": "north indian", "location": "villupuram"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "villupuram"}
    - slot{"price": "mid"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "villupuram"}
    - slot{"price": "mid"}
    - action_validate_location
    - slot{"location": null}
    - utter_ask_location_again
* restaurant_search{"location": "Chennai"}
    - slot{"location": "Chennai"}
    - slot{"location": "Chennai"}
    - action_validate_location
    - slot{"location": "Chennai"}
    - action_validate_cuisine
    - slot{"cuisine": "north indian"}
    - action_search_restaurants
    - slot{"body": "Hello, Please find the list of top 7 north indian restaurants around Chennai in the mid price range.: \n\n1. Found \"V4 Midnight Dhabba\" in 16, 2nd Floor, Rajee Complex, CTH Main Road, Near Vivekanandha School, Ambattur, Chennai has been rated 4.5 average price for two people is Rs.600\n2. Found \"V4 Midnight Dhabba\" in 22, Nolambur Service Road, Opposite KG Signature City, Mogappair West, Chennai has been rated 4.4 average price for two people is Rs.550\n3. Found \"Arabian Kebab Center\" in 17/5, Station View Road, Kodambakkam, Chennai has been rated 4.4 average price for two people is Rs.400\n4. Found \"Shri Rajasthani Dhaba\" in C 40, 3rd Floor, 2nd Avenue, Opposite KFC, Anna Nagar West, Chennai has been rated 4.3 average price for two people is Rs.500\n5. Found \"Masaledaar Desi Rasoi\" in 24, Wellington Estate, Ethiraj Salai, Egmore, Chennai has been rated 4.2 average price for two people is Rs.500\n6. Found \"Velidis\" in 3/88, Mount Poonamallee Road, Ramapuram, Chennai has been rated 4.1 average price for two people is Rs.500\n7. Found \"Behrouz Biryani - Royal & Safe\" in Thuraipakkam, Chennai has been rated 4.0 average price for two people is Rs.700\n\nWish you have wonderful day ahead! See you soon!"}
    - utter_ask_about_email
* email_affirm
    - utter_ask_emailID
* emailID{"email": "aasfasfd%asdf.c.c."}
    - slot{"email": "aasfasfd%asdf.c.c."}
    - slot{"email": "aasfasfd%asdf.c.c."}
    - action_validate_email
    - slot{"email": null}
    - utter_ask_emailID
* emailID{"email": "vvijay83@gmail.com"}
    - slot{"email": "vvijay83@gmail.com"}
    - slot{"email": "vvijay83@gmail.com"}
    - action_validate_email
    - slot{"email": "vvijay83@gmail.com"}
    - action_send_email
    - utter_email_sent
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - action_restart


## interactive_story_4_8
* greet
    - utter_greet   <!-- predicted: action_listen -->
* restaurant_search{"price": "mid", "cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - slot{"price": "mid"}
    - slot{"cuisine": "north indian"}
    - slot{"price": "mid"}
    - action_validate_cuisine
    - slot{"cuisine": "north indian"}
    - utter_ask_location
* restaurant_search{"location": "bilaspur"}
    - slot{"location": "bilaspur"}
    - slot{"location": "bilaspur"}
    - action_validate_location
    - slot{"location": "bilaspur"}
    - action_search_restaurants   <!-- predicted: action_validate_cuisine -->
    - slot{"body": "Hello, Please find the list of top 8 north indian restaurants around bilaspur in the mid price range.: \n\n1. Found \"Krishna Veg Restaurant\" in Main Road, Telephone Exchange Road, Old Bus Stand, Telipara, Bilaspur has been rated 4.1 average price for two people is Rs.350\n2. Found \"The Punjabi Restaurant (hotel Anand)\" in C/O Anand Hotel, Anand Hotel Road, Bilaspur H O, Bilaspur-Chhattisgarh - 495001, Near Old Bus Stand, Shiv Takiz Chowk, Telipara, Bilaspur has been rated 4.0 average price for two people is Rs.500\n3. Found \"Tandoori Nights Restaurant\" in Beside Gaytri Hospital, Sarkanda, Bilaspur has been rated 3.9 average price for two people is Rs.400\n4. Found \"Tandoori Club\" in Tarbahar Chowk, Tarbahar Indra Gandhi Chowk, Tikrapara, Bilaspur has been rated 3.9 average price for two people is Rs.500\n5. Found \"Hotel 786\" in Satyam Complex, Satyam Chowk, Civil LineBilaspur, Link Road, Bilaspur-Chhattisgarh - 495001, Beside Satyam Talkies Infront Of Hotel Chandrika, Masanganj, Bilaspur has been rated 3.8 average price for two people is Rs.450\n6. Found \"New Santusht Thali Rajisthani And Gujrati Restaurant\" in Santusht Restaurant, Agrasen Chowk, Bilaspur H O, Bilaspur-Chhattisgarh - 495001, Near Hotel East Park, Masanganj, Bilaspur has been rated 3.6 average price for two people is Rs.500\n7. Found \"Masala Curry\" in Second Floor Shop No 105, Bilaspur H O, Bilaspur-Chhattisgarh - 495001, Near Rama Magneto Mall, Narmada Nagar, Bilaspur has been rated 3.5 average price for two people is Rs.450\n8. Found \"Maze The Cafe ( Hotel Grand Amba)\" in Hotel Grand Amba Building, Bilaspur, Telephone Exchange Road, Bilaspur-Chhattisgarh - 495001, Telipara, Bilaspur has been rated 3.3 average price for two people is Rs.600\n\nWish you have wonderful day ahead! See you soon!"}
    - utter_ask_about_email
* email_deny
    - utter_email_not_sent
    - utter_goodbye
    - action_restart


## interactive_story_4_9
* greet
    - utter_greet   <!-- predicted: action_listen -->
* restaurant_search{"price": "low", "cuisine": "irish"}
    - slot{"cuisine": "irish"}
    - slot{"price": "low"}
    - slot{"cuisine": "irish"}
    - slot{"price": "low"}
    - action_validate_cuisine
    - slot{"cuisine": null}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - action_validate_cuisine
    - slot{"cuisine": "American"}
    - utter_ask_location
* restaurant_search{"location": "chitoor"}
    - slot{"location": "chitoor"}
    - slot{"location": "chitoor"}
    - action_validate_location
    - slot{"location": null}
    - utter_ask_location_again
* restaurant_search{"location": "hyderabad"}
    - slot{"location": "hyderabad"}
    - slot{"location": "hyderabad"}
    - action_validate_location
    - slot{"location": "hyderabad"}
    - action_search_restaurants   <!-- predicted: action_validate_cuisine -->
    - slot{"body": "Hello, Please find the list of top 4 American restaurants around hyderabad in the low price range.: \n\n1. Found \"4M Biryani House\" in Badi Masjid, Bholakpur, Musheerabad, Hyderabad has been rated 4.4 average price for two people is Rs.300\n2. Found \"Azam Hotel\" in 2-3-1 to 7, Ram Gopalpet, Near Nallagutta Masjid, M.G. Road, Secunderabad has been rated 4.1 average price for two people is Rs.300\n3. Found \"Cafe 555\" in Shop 5, Maheswari Complex, Owaisi Pura, Masab Tank, Hyderabad has been rated 4.1 average price for two people is Rs.300\n4. Found \"Krupa Mess & Tiffins\" in 4-1-827/3, Beside Ramakrishna Theater, Abids, Hyderabad has been rated 3.9 average price for two people is Rs.250\n\nWish you have wonderful day ahead! See you soon!"}
    - utter_ask_about_email
* email_affirm
    - utter_ask_emailID
* emailID{"email": "vijay@#gmaol.com"}
    - slot{"email": "vijay@#gmaol.com"}
    - slot{"email": "vijay@#gmaol.com"}
    - action_validate_email
    - slot{"email": null}
    - utter_ask_emailID
* emailID{"email": "vvijay83@gmail.com"}
    - slot{"email": "vvijay83@gmail.com"}
    - slot{"email": "vvijay83@gmail.com"}
    - action_validate_email
    - slot{"email": "vvijay83@gmail.com"}
    - action_send_email
    - utter_email_sent
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - action_restart


## greet_exit
* greet
    - utter_greet   <!-- predicted: action_listen -->
* greet
    - utter_greet
* greet
    - utter_greet
* greet
    - utter_goodbye   <!-- predicted: utter_greet -->
    - action_restart


## interactive_story_5_0
* greet
    - utter_greet   <!-- predicted: action_listen -->
* restaurant_search{"price": "mid", "location": "kochi"}
    - slot{"location": "kochi"}
    - slot{"price": "mid"}
    - slot{"location": "kochi"}
    - slot{"price": "mid"}
    - action_validate_location
    - slot{"location": "kochi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_validate_cuisine
    - slot{"cuisine": "Italian"}
    - action_search_restaurants
    - slot{"body": "Hello, Please find the list of top 10 Italian restaurants around kochi in the mid price range.: \n\n1. Found \"The Burger Junction\" in 68, B-1, Atlantis Road, Above Corporation Bank, Panampilly Nagar, Kochi has been rated 4.6 average price for two people is Rs.450\n2. Found \"The Burger Junction\" in NH 47, Toll Junction, Edappally, Kochi has been rated 4.4 average price for two people is Rs.500\n3. Found \"Al- Sheba Kuzhimandhi\" in Near BMC, Seaport Airport Road, Kakkanad, Kochi has been rated 4.3 average price for two people is Rs.400\n4. Found \"The Grill Lab\" in Namaskar Building, S.N. Junction, Sonia Nagar, Palarivattom, Kochi has been rated 4.3 average price for two people is Rs.700\n5. Found \"Ifthar\" in KK Building, Opposite Pittappillil, Edappally Toll, Kochi has been rated 4.2 average price for two people is Rs.350\n6. Found \"Slice of Spice\" in Market Road, Opposite Saritha Savitha Theatre, Kacheripady, Kochi has been rated 4.2 average price for two people is Rs.400\n7. Found \"The Voyager\" in MM Tower 2, Ecchamukku Junction, Seaport Airport Road, Kakkanad, Kochi has been rated 4.1 average price for two people is Rs.600\n8. Found \"Hotel Paradise - Karukappilly\" in 44/2708-C, Desabhimani Road, Palarivattom, Karukappilly, Mamangalam, Kaloor, Kochi has been rated 4.0 average price for two people is Rs.400\n9. Found \"Chiyang\" in Mariyambika Building, Madhava Pharmacy Junction, Kacheripady, Kochi has been rated 4.0 average price for two people is Rs.450\n10. Found \"Ceylon Bake House\" in 67/8336(40/1891), Broadway, Near Guest House, Broadway, Marine Drive, Kochi has been rated 4.0 average price for two people is Rs.500\n\nWish you have wonderful day ahead! See you soon!"}
    - utter_ask_about_email
* email_deny
    - utter_email_not_sent
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - action_restart


## interactive_story_5_1
* greet
    - utter_greet   <!-- predicted: action_listen -->
* restaurant_search{"price": "high", "location": "vadalur"}
    - slot{"location": "vadalur"}
    - slot{"price": "high"}
    - slot{"location": "vadalur"}
    - slot{"price": "high"}
    - action_validate_location
    - slot{"location": null}
    - utter_ask_location_again
* restaurant_search{"location": "coimbatore"}
    - slot{"location": "coimbatore"}
    - slot{"location": "coimbatore"}
    - action_validate_location
    - slot{"location": "coimbatore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "swedish"}
    - slot{"cuisine": "swedish"}
    - slot{"cuisine": "swedish"}
    - action_validate_cuisine
    - slot{"cuisine": null}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_validate_cuisine
    - slot{"cuisine": "North Indian"}
    - action_search_restaurants
    - slot{"body": "Hello, Please find the list of top 4 North Indian restaurants around coimbatore in the high price range.: \n\n1. Found \"Barbeque Nation\" in 6th Floor, Metro Park Inn, 1000, Raja Street, Near Clock Tower, Town Hall, Coimbatore has been rated 4.8 average price for two people is Rs.1200\n2. Found \"Zucca Pizzeria\" in 24A, Suganya Complex, Thudiyalur Road, Saravanampatti, Saravanampatty, Coimbatore has been rated 4.2 average price for two people is Rs.750\n3. Found \"Zucca Pizzeria\" in GRG College Road, Opposite Rajasree Ford Showroom, Peelamedu, Coimbatore has been rated 4.1 average price for two people is Rs.750\n4. Found \"Bazaar - Zone By The Park\" in 33, Kamaraj Road, Lakshmi Mills, Coimbatore has been rated 4.0 average price for two people is Rs.1300\n\nWish you have wonderful day ahead! See you soon!"}
    - utter_ask_about_email
* email_affirm{"email": "vija^edu.com"}
    - slot{"email": "vija^edu.com"}
    - slot{"email": "vija^edu.com"}
    - action_validate_email
    - slot{"email": null}
    - action_validate_email   <!-- predicted: utter_ask_emailID -->
    - utter_ask_emailID
* emailID{"email": "vvijay83@gmail.com"}
    - slot{"email": "vvijay83@gmail.com"}
    - slot{"email": "vvijay83@gmail.com"}
    - action_validate_email
    - slot{"email": "vvijay83@gmail.com"}
    - action_send_email
    - utter_email_sent
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - action_restart


## interactive_story_5_2
* greet
    - utter_greet   <!-- predicted: action_listen -->
* restaurant_search{"cuisine": "south indian", "location": "jaipur"}
    - slot{"cuisine": "south indian"}
    - slot{"location": "jaipur"}
    - slot{"cuisine": "south indian"}
    - slot{"location": "jaipur"}
    - action_validate_location
    - slot{"location": "jaipur"}
    - action_validate_cuisine
    - slot{"cuisine": "south indian"}
    - utter_ask_price
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - slot{"price": "mid"}
    - action_search_restaurants
    - slot{"body": "Hello, Please find the list of top 7 south indian restaurants around jaipur in the mid price range.: \n\n1. Found \"Dosaka - Taste of South\" in Shop 5, Opposite Mahaveer School, Gate 2, Mahavir Marg, C Scheme, Jaipur has been rated 4.1 average price for two people is Rs.500\n2. Found \"Hey Dosa!\" in 180, Rathod Nagar, Amrapali Marg, Opposite Talwalkars Gym, Vaishali Nagar, Jaipur has been rated 4.0 average price for two people is Rs.500\n3. Found \"Sankalp\" in 32 & 33, 1st Floor, Vidhyut Nagar A, Near Subh Hospital, Prince Road, Vaishali Nagar, Jaipur has been rated 3.7 average price for two people is Rs.650\n4. Found \"Hey Dosa!\" in G-8, Ganpati Paradise, Central Spine, Vidhyadhar Nagar, Jaipur has been rated 3.7 average price for two people is Rs.400\n5. Found \"Vaango!\" in World Trade Park, 3rd Floor, JLN Marg, Malviya Nagar, Jaipur has been rated 3.7 average price for two people is Rs.400\n6. Found \"Raman Dosawala\" in 8, Masala Chowk, Near Albert Hall, Ram Niwas Baag, Adarsh Nagar, Jaipur has been rated 3.6 average price for two people is Rs.350\n7. Found \"Andhra Vilas - South Indian Foods\" in Ground Floor, Kamla Tower, Opposite Kumbha Marg, Sector 5, Sanganer, Tonk Road, Jaipur has been rated 3.6 average price for two people is Rs.350\n\nWish you have wonderful day ahead! See you soon!"}
    - utter_ask_about_email
* email_affirm
    - utter_ask_emailID
* emailID{"email": "vvijay4u@gmail.com"}
    - slot{"email": "vvijay4u@gmail.com"}
    - slot{"email": "vvijay4u@gmail.com"}
    - action_validate_email
    - slot{"email": "vvijay4u@gmail.com"}
    - action_send_email
    - utter_email_sent
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - action_restart


## interactive_story_5_3
* greet
    - utter_greet   <!-- predicted: action_listen -->
* restaurant_search{"cuisine": "korean", "location": "veppur"}
    - slot{"cuisine": "korean"}
    - slot{"location": "veppur"}
    - slot{"cuisine": "korean"}
    - slot{"location": "veppur"}
    - action_validate_location
    - slot{"location": null}
    - utter_ask_location_again
* restaurant_search{"location": "guntur"}
    - slot{"location": "guntur"}
    - slot{"location": "guntur"}
    - action_validate_location
    - slot{"location": "guntur"}
    - action_validate_cuisine
    - slot{"cuisine": null}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_validate_cuisine
    - slot{"cuisine": "North Indian"}
    - utter_ask_price
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - slot{"price": "mid"}
    - action_search_restaurants
    - slot{"body": "Hello, Please find the list of top 10 North Indian restaurants around guntur in the mid price range.: \n\n1. Found \"Hotel Subani\" in Nallapadu Road, Sai Nagar, Near Mirchi Yard, GT Road, Srinivasarao Pet, Guntur has been rated 4.0 average price for two people is Rs.600\n2. Found \"Pizza World\" in Laxmipuram Main Road, Below Hollywood Bollywood Theatre, Lakshmipuram, Guntur has been rated 4.0 average price for two people is Rs.350\n3. Found \"Venkatesh Grand\" in 2/2 Arundelpet, 2nd Lane 2 Cross Road, Near Rail Way Station, Brodipet, Guntur has been rated 3.9 average price for two people is Rs.350\n4. Found \"KFC\" in Plot 5, 87/92, Laxmipuram Main Road, Lakshmipuram, Guntur has been rated 3.8 average price for two people is Rs.450\n5. Found \"Viceroy Biryani Point\" in 1, Ground Floor, Swarnalok Complex 7-4-78 4, Behind Andhra Bank Lane, Arundelpet, Brodipet, Guntur has been rated 3.8 average price for two people is Rs.350\n6. Found \"Pizza World\" in 4/5, 4th Lane, Beside Help Hospital, Arundelpet, Brodipet, Guntur has been rated 3.8 average price for two people is Rs.350\n7. Found \"Sweet Magic\" in Beside Reliance Smart, Laxmipuram Main Road, Laxmipuram, Guntur has been rated 3.8 average price for two people is Rs.600\n8. Found \"V Royal Park\" in 6-7-72, Arundelpet, 2nd Lane 2 Cross Road, Near Rail Way Station, Brodipet, Guntur has been rated 3.8 average price for two people is Rs.500\n9. Found \"Sri Sankara Vilas\" in 4th Ln, Brodipet, Guntur has been rated 3.8 average price for two people is Rs.400\n10. Found \"Chennai Thalapakatti Biryani\" in Near Kanna School, Lane Beside Rail Bridge, Rail Pet, Old Guntur, Guntur has been rated 3.7 average price for two people is Rs.550\n\nWish you have wonderful day ahead! See you soon!"}
    - utter_ask_about_email
* email_affirm
    - utter_ask_emailID
* emailID{"email": "vijay@brava_com"}
    - slot{"email": "vijay@brava_com"}
    - slot{"email": "vijay@brava_com"}
    - action_validate_email
    - slot{"email": null}
    - utter_ask_emailID
* emailID{"email": "vvijay83@gmail.com"}
    - slot{"email": "vvijay83@gmail.com"}
    - slot{"email": "vvijay83@gmail.com"}
    - action_validate_email
    - slot{"email": "vvijay83@gmail.com"}
    - action_send_email
    - utter_email_sent
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - action_restart


## interactive_story_5_4
* greet
    - utter_greet   <!-- predicted: action_listen -->
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - slot{"price": "mid"}
    - utter_ask_location
* restaurant_search{"location": "chandigarh"}
    - slot{"location": "chandigarh"}
    - slot{"location": "chandigarh"}
    - action_validate_location
    - slot{"location": "chandigarh"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_validate_cuisine
    - slot{"cuisine": "South Indian"}
    - action_search_restaurants
    - slot{"body": "Hello, Please find the list of top 10 South Indian restaurants around chandigarh in the mid price range.: \n\n1. Found \"Subway\" in SCF 30, Phase 10, Sector 64, Mohali has been rated 4.6 average price for two people is Rs.500\n2. Found \"Subway\" in Shop 1 & 2, Upper Ground Floor, Raksha Business Centre, Chandigarh Road, Zirakpur has been rated 4.6 average price for two people is Rs.500\n3. Found \"Biryani By Kilo\" in SCO 71, Ground Floor, Sector 30 C, Near Sector 30, Chandigarh has been rated 4.3 average price for two people is Rs.700\n4. Found \"Subway\" in SCO 501, Ground Floor, Sector 70, Mohali has been rated 4.3 average price for two people is Rs.500\n5. Found \"Khalsa Dhaba\" in SCF 81, Phase 5, Mohali has been rated 4.1 average price for two people is Rs.400\n6. Found \"Amrit Sweets\" in SCF 78, Phase 5, Mohali has been rated 4.1 average price for two people is Rs.500\n7. Found \"JnJ's\" in Plot 5, Sector 28, Chandigarh has been rated 4.0 average price for two people is Rs.400\n8. Found \"New Panna Sweets\" in SCF 218, Near Fun Republic Cinema, Manimajra, Chandigarh has been rated 4.0 average price for two people is Rs.500\n9. Found \"KFC\" in SCO 328, Sector 9, Panchkula has been rated 4.0 average price for two people is Rs.450\n10. Found \"Captain Sam's\" in SCO 533, Main Road, Sector 70, Mohali has been rated 3.9 average price for two people is Rs.500\n\nWish you have wonderful day ahead! See you soon!"}
    - utter_ask_about_email
* email_affirm{"email": "vvijay4u@gmail.com"}
    - slot{"email": "vvijay4u@gmail.com"}
    - slot{"email": "vvijay4u@gmail.com"}
    - action_validate_email
    - slot{"email": "vvijay4u@gmail.com"}
    - action_send_email
    - utter_email_sent
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - action_restart


## interactive_story_5_5
* greet
    - utter_greet   <!-- predicted: action_listen -->
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - slot{"price": "low"}
    - utter_ask_location
* restaurant_search{"location": "dalian"}
    - slot{"location": "dalian"}
    - slot{"location": "dalian"}
    - action_validate_location
    - slot{"location": null}
    - utter_ask_location_again
* restaurant_search{"location": "Chennai"}
    - slot{"location": "Chennai"}
    - slot{"location": "Chennai"}
    - action_validate_location
    - slot{"location": "Chennai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "japanese"}
    - slot{"cuisine": "japanese"}
    - slot{"cuisine": "japanese"}
    - action_validate_cuisine
    - slot{"cuisine": null}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - action_validate_cuisine
    - slot{"cuisine": "American"}
    - action_search_restaurants
    - slot{"body": "Hello, Please find the list of top 1 American restaurants around Chennai in the low price range.: \n\n1. Found \"Tasty Kitchen\" in 135B,SRP Colony, Peravallur, Perambur, Chennai has been rated 4.1 average price for two people is Rs.300\n\nWish you have wonderful day ahead! See you soon!"}
    - utter_ask_about_email
* email_affirm{"email": "vijay@g_gle..com"}
    - slot{"email": "vijay@g_gle..com"}
    - slot{"email": "vijay@g_gle..com"}
    - action_validate_email
    - slot{"email": null}
    - utter_ask_emailID
* emailID{"email": "vvijay83@gmail.com"}
    - slot{"email": "vvijay83@gmail.com"}
    - slot{"email": "vvijay83@gmail.com"}
    - action_validate_email
    - slot{"email": "vvijay83@gmail.com"}
    - action_send_email
    - utter_email_sent
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - action_restart


## interactive_story_1
* greet
    - utter_greet   <!-- predicted: action_listen -->
* restaurant_search{"cuisine": "hungarian"}
    - slot{"cuisine": "hungarian"}
    - slot{"cuisine": "hungarian"}
    - action_validate_cuisine
    - slot{"cuisine": null}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_validate_cuisine
    - slot{"cuisine": "Italian"}
    - utter_ask_location
* restaurant_search{"location": "krishnagiri"}
    - slot{"location": "krishnagiri"}
    - slot{"location": "krishnagiri"}
    - action_validate_location
    - slot{"location": null}
    - utter_ask_location_again
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_location
    - slot{"location": "delhi"}
    - utter_ask_price   <!-- predicted: action_validate_cuisine -->
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - slot{"price": "mid"}
    - action_search_restaurants
    - slot{"body": "Hello, Please find the list of top 10 Italian restaurants around delhi in the mid price range.: \n\n1. Found \"Oishii Wok\" in Behind Super Mart 2, DLF Phase 4, Gurgaon has been rated 4.9 average price for two people is Rs.700\n2. Found \"Punjabi Angithi\" in 32-22, A 4, DDA Market, Paschim Vihar, New Delhi has been rated 4.5 average price for two people is Rs.400\n3. Found \"Gulab\" in 5, Main Road, Pitampura, New Delhi has been rated 4.2 average price for two people is Rs.500\n4. Found \"Singla's\" in A-139/140, Main Road, Madhu Vihar, Near Hasanpur Depot, IP Extension, New Delhi has been rated 4.2 average price for two people is Rs.500\n5. Found \"Bikanervala Angan\" in 10181, 82, Arya Samaj Road, Karol Bagh, New Delhi has been rated 4.1 average price for two people is Rs.600\n6. Found \"Haldiram's\" in 45, Ring Road, Lajpat Nagar 2, New Delhi has been rated 4.1 average price for two people is Rs.600\n7. Found \"Bikanervala\" in Plot 3-5, Near Leisure Valley Park, Sector 29, Gurgaon has been rated 4.1 average price for two people is Rs.600\n8. Found \"Haldiram's\" in C 9, Opposite ITI, Main Market, Malviya Nagar, New Delhi has been rated 4.1 average price for two people is Rs.600\n9. Found \"Om Sweets & Snacks\" in SCO 17, Main Market, Sector 31, Gurgaon has been rated 4.1 average price for two people is Rs.500\n10. Found \"Bikanervala\" in Suncity Business Tower, Golf Course Road, Gurgaon has been rated 4.1 average price for two people is Rs.600\n\nWish you have wonderful day ahead! See you soon!"}
    - utter_ask_about_email
* email_affirm{"email": "vvijay83@@gmail.com"}
    - slot{"email": "vvijay83@@gmail.com"}
    - slot{"email": "vvijay83@@gmail.com"}
    - action_validate_email
    - slot{"email": null}
    - utter_ask_emailID
* email_affirm{"email": "vvijay83@gmail.com"}
    - slot{"email": "vvijay83@gmail.com"}
    - slot{"email": "vvijay83@gmail.com"}
    - action_validate_email
    - slot{"email": "vvijay83@gmail.com"}
    - action_send_email
    - utter_email_sent
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - action_restart


## interactive_story_2
* greet
    - utter_greet   <!-- predicted: action_listen -->
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - action_validate_cuisine
    - slot{"cuisine": "american"}
    - utter_ask_location
* restaurant_search{"location": "ooty"}
    - slot{"location": "ooty"}
    - slot{"location": "ooty"}
    - action_validate_location
    - slot{"location": null}
    - utter_ask_location_again
* restaurant_search{"location": "hyderabad"}
    - slot{"location": "hyderabad"}
    - slot{"location": "hyderabad"}
    - action_validate_location
    - slot{"location": "hyderabad"}
    - utter_ask_price   <!-- predicted: action_validate_cuisine -->
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - slot{"price": "low"}
    - action_search_restaurants
    - slot{"body": "Found 0 restaurants in given price range"}
    - utter_ask_about_email
* email_deny
    - utter_email_not_sent
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - action_restart


## interactive_story_3
* greet
    - utter_greet   <!-- predicted: action_listen -->
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_validate_cuisine
    - slot{"cuisine": "south indian"}
    - utter_ask_location
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - action_validate_location
    - slot{"location": "kolkata"}
    - utter_ask_price   <!-- predicted: action_validate_cuisine -->
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"body": "Hello, Please find the list of top 1 south indian restaurants around kolkata in the high price range.: \n\n1. Found \"Surfiré The Coastal Café\" in 24, Rajani Sen Road, Near Menoka Cinema, Southern Avenue, Kolkata has been rated 3.9 average price for two people is Rs.800\n\nWish you have wonderful day ahead! See you soon!"}
    - utter_ask_about_email
* email_affirm{"email": "vvijay83@gmail.com"}
    - slot{"email": "vvijay83@gmail.com"}
    - slot{"email": "vvijay83@gmail.com"}
    - action_validate_email
    - slot{"email": "vvijay83@gmail.com"}
    - action_send_email
    - utter_email_sent
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - action_restart


## interactive_story_1_0
* greet
    - utter_greet   <!-- predicted: action_listen -->
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - action_validate_location
    - slot{"location": "kolkata"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - action_validate_cuisine
    - slot{"cuisine": "American"}
    - utter_ask_price
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - slot{"price": "mid"}
    - action_search_restaurants
    - slot{"body": "Hello, Please find the list of top 10 American restaurants around kolkata in the mid price range.: \n\n1. Found \"Balaram Mullick & Radharaman Mullick Sweets\" in 367, Lake Gardens, Kolkata has been rated 4.4 average price for two people is Rs.100\n2. Found \"Mama Mia!\" in 59, Ballygunge Circular Road, Ballygunge, Kolkata has been rated 4.3 average price for two people is Rs.500\n3. Found \"Balaram Mullick & Radharaman Mullick Sweets\" in 2A, Paddapukur Road, Bhawanipur, Kolkata has been rated 4.3 average price for two people is Rs.100\n4. Found \"Haji Saheb\" in 476, Diamond Harbour Road, Near Tram Depot Bazaar, Behala, Kolkata has been rated 4.2 average price for two people is Rs.300\n5. Found \"Haldiram's Prabhuji\" in P420, Kazi Nazrul Islam Avenue, V.I.P. Road, Kaikhali, Kolkata has been rated 4.1 average price for two people is Rs.300\n6. Found \"KFC\" in 20K, Park Street, Park Street Area, Kolkata has been rated 4.1 average price for two people is Rs.450\n7. Found \"Haldiram's Prabhuji\" in 7, Jagmohan Mullick Lane, Bara Bazar, Kolkata has been rated 4.0 average price for two people is Rs.300\n8. Found \"Kankurgachi Dhaba\" in P-5, CIT Road, Scheme 7M, Kankurgachi, Kolkata has been rated 3.9 average price for two people is Rs.500\n9. Found \"Mezban\" in 6, Ripon Street, Near Triangular Park, Wellesley, Kolkata has been rated 3.8 average price for two people is Rs.500\n10. Found \"Al Baik Fast Food Corner\" in 54, Phears Lane, Bara Bazar, Kolkata has been rated 3.8 average price for two people is Rs.250\n\nWish you have wonderful day ahead! See you soon!"}
    - utter_ask_about_email
* email_affirm
    - utter_ask_emailID
* emailID{"email": "vvijay83@gmail.com"}
    - slot{"email": "vvijay83@gmail.com"}
    - slot{"email": "vvijay83@gmail.com"}
    - action_validate_email
    - slot{"email": "vvijay83@gmail.com"}
    - action_send_email
    - utter_email_sent
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - action_restart


## interactive_story_1_1
* greet
    - utter_greet   <!-- predicted: action_listen -->
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - action_validate_location
    - slot{"location": "kolkata"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - action_validate_cuisine
    - slot{"cuisine": "American"}
    - utter_ask_price
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - slot{"price": "mid"}
    - action_search_restaurants
    - slot{"body": "Hello, Please find the list of top 10 American restaurants around kolkata in the mid price range.: \n\n1. Found \"Balaram Mullick & Radharaman Mullick Sweets\" in 367, Lake Gardens, Kolkata has been rated 4.4 average price for two people is Rs.100\n2. Found \"Mama Mia!\" in 59, Ballygunge Circular Road, Ballygunge, Kolkata has been rated 4.3 average price for two people is Rs.500\n3. Found \"Balaram Mullick & Radharaman Mullick Sweets\" in 2A, Paddapukur Road, Bhawanipur, Kolkata has been rated 4.3 average price for two people is Rs.100\n4. Found \"Haji Saheb\" in 476, Diamond Harbour Road, Near Tram Depot Bazaar, Behala, Kolkata has been rated 4.2 average price for two people is Rs.300\n5. Found \"Haldiram's Prabhuji\" in P420, Kazi Nazrul Islam Avenue, V.I.P. Road, Kaikhali, Kolkata has been rated 4.1 average price for two people is Rs.300\n6. Found \"KFC\" in 20K, Park Street, Park Street Area, Kolkata has been rated 4.1 average price for two people is Rs.450\n7. Found \"Haldiram's Prabhuji\" in 7, Jagmohan Mullick Lane, Bara Bazar, Kolkata has been rated 4.0 average price for two people is Rs.300\n8. Found \"Kankurgachi Dhaba\" in P-5, CIT Road, Scheme 7M, Kankurgachi, Kolkata has been rated 3.9 average price for two people is Rs.500\n9. Found \"Mezban\" in 6, Ripon Street, Near Triangular Park, Wellesley, Kolkata has been rated 3.8 average price for two people is Rs.500\n10. Found \"Al Baik Fast Food Corner\" in 54, Phears Lane, Bara Bazar, Kolkata has been rated 3.8 average price for two people is Rs.250\n\nWish you have wonderful day ahead! See you soon!"}
    - utter_ask_about_email
* email_affirm{"email": "vvijay83@gmail.com"}
    - slot{"email": "vvijay83@gmail.com"}
    - slot{"email": "vvijay83@gmail.com"}
    - action_validate_email
    - slot{"email": "vvijay83@gmail.com"}
    - action_send_email
    - utter_email_sent
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - action_restart


## interactive_story_1_3
* greet
    - utter_greet   <!-- predicted: action_listen -->
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "neyveli"}
    - slot{"location": "neyveli"}
    - slot{"location": "neyveli"}
    - action_validate_location
    - slot{"location": null}
    - utter_ask_location_again
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_location
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_price   <!-- predicted: action_validate_cuisine -->
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"body": "Hello, Please find the list of top 10 Italian restaurants around delhi in the high price range.: \n\n1. Found \"Punjabi Angithi\" in 32-22, A 4, DDA Market, Paschim Vihar, New Delhi has been rated 4.5 average price for two people is Rs.400\n2. Found \"Gulab\" in 5, Main Road, Pitampura, New Delhi has been rated 4.2 average price for two people is Rs.500\n3. Found \"Singla's\" in A-139/140, Main Road, Madhu Vihar, Near Hasanpur Depot, IP Extension, New Delhi has been rated 4.2 average price for two people is Rs.500\n4. Found \"Om Sweets & Snacks\" in 84-85, Shopping Complex, Sector 14, Gurgaon has been rated 4.1 average price for two people is Rs.500\n5. Found \"Om Sweets & Snacks\" in SCO 17, Main Market, Sector 31, Gurgaon has been rated 4.1 average price for two people is Rs.500\n6. Found \"McDonald's\" in 41, Block UA, Bungalow Road, Jawahar Nagar, Kamla Nagar, New Delhi has been rated 4.1 average price for two people is Rs.500\n7. Found \"Hira Sweets\" in E-60, Vikas Marg, Laxmi Nagar, New Delhi has been rated 4.0 average price for two people is Rs.500\n8. Found \"Pandit Ji Parantha Hut\" in 10, Community Centre, Ashok Vihar Phase 2, New Delhi has been rated 4.0 average price for two people is Rs.200\n9. Found \"Burger King\" in F-15, Vijay Block, Laxmi Nagar, New Delhi has been rated 4.0 average price for two people is Rs.500\n10. Found \"Radha Krishna Chole Bhature\" in 115, Priya Enclave, Karkardooma, New Delhi has been rated 3.8 average price for two people is Rs.300\n\nWish you have wonderful day ahead! See you soon!"}
    - utter_ask_about_email
* email_affirm
    - utter_ask_emailID
* emailID{"email": "vvijay83@gmail.com"}
    - slot{"email": "vvijay83@gmail.com"}
    - slot{"email": "vvijay83@gmail.com"}
    - action_validate_email
    - slot{"email": "vvijay83@gmail.com"}
    - action_send_email
    - utter_email_sent
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - action_restart


## interactive_story_1_4
* greet
    - utter_greet   <!-- predicted: action_listen -->
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "pollachi"}
    - slot{"location": "pollachi"}
    - slot{"location": "pollachi"}
    - action_validate_location
    - slot{"location": null}
    - utter_ask_location_again
* affirm{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - action_validate_location
    - slot{"location": "kolkata"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "cake"}
    - slot{"cuisine": "cake"}
    - slot{"cuisine": "cake"}
    - action_validate_cuisine
    - slot{"cuisine": null}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - action_validate_cuisine
    - slot{"cuisine": "American"}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"body": "Hello, Please find the list of top 10 American restaurants around kolkata in the high price range.: \n\n1. Found \"Balaram Mullick & Radharaman Mullick Sweets\" in 367, Lake Gardens, Kolkata has been rated 4.4 average price for two people is Rs.100\n2. Found \"Mama Mia!\" in 59, Ballygunge Circular Road, Ballygunge, Kolkata has been rated 4.3 average price for two people is Rs.500\n3. Found \"Balaram Mullick & Radharaman Mullick Sweets\" in 2A, Paddapukur Road, Bhawanipur, Kolkata has been rated 4.3 average price for two people is Rs.100\n4. Found \"Haji Saheb\" in 476, Diamond Harbour Road, Near Tram Depot Bazaar, Behala, Kolkata has been rated 4.2 average price for two people is Rs.300\n5. Found \"Haldiram's Prabhuji\" in P420, Kazi Nazrul Islam Avenue, V.I.P. Road, Kaikhali, Kolkata has been rated 4.1 average price for two people is Rs.300\n6. Found \"KFC\" in 20K, Park Street, Park Street Area, Kolkata has been rated 4.1 average price for two people is Rs.450\n7. Found \"Haldiram's Prabhuji\" in 7, Jagmohan Mullick Lane, Bara Bazar, Kolkata has been rated 4.0 average price for two people is Rs.300\n8. Found \"Kankurgachi Dhaba\" in P-5, CIT Road, Scheme 7M, Kankurgachi, Kolkata has been rated 3.9 average price for two people is Rs.500\n9. Found \"Mezban\" in 6, Ripon Street, Near Triangular Park, Wellesley, Kolkata has been rated 3.8 average price for two people is Rs.500\n10. Found \"Al Baik Fast Food Corner\" in 54, Phears Lane, Bara Bazar, Kolkata has been rated 3.8 average price for two people is Rs.250\n\nWish you have wonderful day ahead! See you soon!"}
    - utter_ask_about_email
* email_affirm
    - utter_ask_emailID
* emailID{"email": "vvijay83@gmail.com"}
    - slot{"email": "vvijay83@gmail.com"}
    - slot{"email": "vvijay83@gmail.com"}
    - action_validate_email
    - slot{"email": "vvijay83@gmail.com"}
    - action_send_email
    - utter_email_sent
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - action_restart


