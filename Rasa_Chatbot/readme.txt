=======================================
NLP Course Project - Building a Chatbot
=======================================
by - Rajesh Kumar S
Date: Apr 28 2020


******************************************************************************************
IMPORTANT NOTE: MODEL FILES EXCEEDING THE ALLOWED LIMIT OF 50MB, HENCE WE HAVE UPLOADED OUR MODEL FILES IN THE GOOGLE SHARE DRIVE AND SHARED IT WITH STUDENT MENTOR
******************************************************************************************


Version 1:
We added or defined more and more of the following to improve the accuracy and user experience of the chatbot:
Intents
entities
slots
responses

This ensure the bot identifies the intents of the user rightly.

Version 2:
ActionSearchRestaurants(Action)

We added user key to access the zomato API and initialized it. 
Using the initial actions file given to us, we started  developing it by capturing the entities from the user such as location, cuisine and price. And also email for action send email - more on this later.

Based on the problem statement, we filter the price as low, mid and high. Note the entity of price is not categorical but text.
We fetch the location details from the zomato api.
Using a dictionary we define the cuisines and key values.
Search for all the restaurants based in the cuisine dictorinary.
We created a dataframe with columns zomato rating, restaurant name, address and average budget for two.
We created another dataframe to store data temporarily.
As per the problem requirement, sorted the restaurants based on the aggreagate of zomato and user rating along with restaurant name, address and average price.
We display the top 5 results (subjective as per the search criteria) as response. And also offer a feature to send the top 10 restaurants details via an email if the user agrees.
For the above requirement we place the entire results with top 5 and top 10 in a dataframe separately and use it to display results and share it via email if required respectively.

Version 3:
ActionValidateLocation(Action)
We run the action validate location to validate the lcoation given by the user as per the problem statement. We validate it against the tier 1 and tier 2 cities of India. The bot will respond accordingly for an invalid location or any other smaller towns, villages.
We have reference the location using a lookup list location.txt

Version 4:
ActionValidateCuisine(Action)
We validate the cuisine specified by the user against the 6 cuisines described as per the problem statement. If the user enter any other cuisine, bot would respond that the cuisine is not available currently. For any invalid entry by user the bot will respond that it didn't understand the cuisine, try some other cuisine.

Version 5:
ActionValidateEmail(Action)
We have defined an entity for email. The email address submitted by the user is validated against a regular expression.
If the user specified entry fails, the bot will respond to enter a valid email address else for null submission it will respond as it didn't understand the email address provided.

Version 6:
ActionSendEmail(Action)
We have implemented this action to share the results of restaurant list to the email address provided by the user.
We have used the smtplib.smtp ('smtp.gmail.com;) and by starting the tls and the port number is 587.
The subject is "Your Foodie Bot Query" inclusive of the search result as the message body.
We have imported relevant libraries to use this action.

Version 7:
ActionSlotReset(Action)
This action is implemented to reset the slots used by the entities. This is done to avoid the carry over of previous slot entries by the user during multiple sessions by the user before the session is expired.
We have imported relevant libraries to use this action.

Version 8:
ActionRestart(Action)
This action is triggered to restart the bot after a successful session.
We have imported relevant libraries to use this action.

Version 9:
config.yml
We altered the embeddings and policies which could help our bot performs better.
language: en
pipeline: supervised_embeddings
policies:
- name: MemoizationPolicy
  max_history: 1
- name: KerasPolicy
- name: MappingPolicy

Evaluation:
1. rasa data split nlu 
2. rasa test nlu -u train_test_split/test_data.md --model models/nlu-20200428-013037.tar.gz
3. rasa test core --stories data/stories.md --out results

Final result using rasa shell:
Your input ->  hi
Hey, How is it going. How may I help you Today
Your input ->  i am looking for restaurant in delhi
? what kind of cuisine would you like?  3: Italian (Italian)
? What price range are you looking at?  3: More than 700 (high)
1. Found "Nona's Kitchen" in A 224, Ground Floor, Supermart 1, DLF Phase 4, Gurgaon has been rated 4.6
Should I send you the details of all the restaurants on email?
Your input ->  yes please
To what email ID should I send it to?
Your input ->  rajasvim1617@gmail.com
Sent. Bon Appetit!
See you again!
Your input ->  dear sir
How are you doing today? How can I help you?
Your input ->  looking for restaurant around jabalpur
? what kind of cuisine would you like?  1: Chinese (Chinese)
? What price range are you looking at?  Type out your own message...
Your input ->  <300
1. Found "Best Choice" in Shop No 5& 6, Asha Complex, Napier Town, Jabalpur has been rated 4.6
2. Found "The Oven Classics" in 10 Carvas Comples, Station Road, South Civil Lines, Civil Lines, Jabalpur has been rated 4.5
3. Found "Naidu's Dilli Ki Gali Parathe Wali" in Shop 16, Block 7, Scheme 18, JDA, Marhathal, Civic Centre, Napier Town, Jabalpur has been rated 4.5
4. Found "Govinda's Fast Food Centre" in 10/11, Beside Dena Bank, Civic Center, Napier Town, Jabalpur has been rated 4.5
5. Found "Sai Chinese Point" in Opposite Samdariya Mall, Marhatal, Napier Town, Jabalpur has been rated 3.7
Should I send you the details of all the restaurants on email?
Your input ->  no thanks
Okay. Bon Appetit!
See you again!
Your input ->  hi bot
hey there! How may i help you
Your input ->  help me to search restaurant near panruti
Sorry! We aren't serving at the specified location yet. Please try some other location
Please provide a different location
Your input ->  how about vellore
? what kind of cuisine would you like?  Type out your own message...
Your input ->  i'll choose south indian
? What price range are you looking at?  Type out your own message...
Your input ->  cheaper
1. Found "Hotel You Think" in Arni Road, Virupachipuram, RN Palayam, Vellore has been rated 3.7
2. Found "Suvai Mess" in Katpadi Main Road, Gandhi Nagar, Vellore has been rated 3.6
3. Found "Nandhini Restaurant" in 40/3, Sripuram Main Road, Periya Allapuram, Thorapadi, Vellore has been rated 3.6
4. Found "Thangam Mess" in 18A, Ambigai Nivas, Arni Main Road, Kosapet, Vellore has been rated 3.4
5. Found "Baby Restaurant" in 7, Anna Salai, Kosapet, Vellore has been rated 3.4
Should I send you the details of all the restaurants on email?
Your input ->  yes please send it to v83@gmail.com
Sent. Bon Appetit!
See you again!
Your input ->  hi there
hey there! How may i help you
Your input ->  find me a restaurant near veppur
Sorry! We aren't serving at the specified location yet. Please try some other location
Please provide a different location
Your input ->  sorry, how about coimbatore
? what kind of cuisine would you like?  Type out your own message...
Your input ->  i'll prefer french
Sorry, the cuisine is not available yet. Please try again with the given options
? what kind of cuisine would you like?  Type out your own message...
Your input ->  okay. i will prefer north indian
? What price range are you looking at?  Type out your own message...
Your input ->  >700
1. Found "That's Y Food" in 24/49, TV Swamy Road East, Opposite Emeral Building, RS Puram, Coimbatore has been rated 4.5
2. Found "The Afghan Grill - The Residency Hotel" in The Residency Hotel, 1075/1076, Avinashi Road, Race Course, Coimbatore has been rated 4.1
3. Found "Func - #6 Hotels" in #6 Hotels, 257, Mettuppalayam Road, Tatabad, Saibaba Colony, Coimbatore has been rated 4.1
4. Found "The Great Kabab Factory - Radisson Blu" in Radisson Blu, 164-165, Avinashi Road, Peelamedu, Coimbatore has been rated 4.0
5. Found "Global Barbeque" in Hotel Vijay Elanza, Behind BP Petrol Bunk, Avinashi Road, Peelamedu, Coimbatore has been rated 3.9
Should I send you the details of all the restaurants on email?
Your input ->  no thats fine
Okay. Bon Appetit!
Bye-bye
Your input ->  hi are you there?
hey there! How may i help you
Your input ->  help me in finding some restaurant around vadalur
Sorry! We aren't serving at the specified location yet. Please try some other location
Please provide a different location
Your input ->  how about pondicherry
? what kind of cuisine would you like?  Type out your own message...
Your input ->  are there german cuisines available?
Sorry, I could not understand the cuisine. Please try again with the given options.
? what kind of cuisine would you like?  Type out your own message...
Your input ->  alright, i will go with american
? what kind of cuisine would you like?  2: Mexican (Mexican)
? What price range are you looking at?  2: Rs. 300 to 700 (mid)
1. Found "Yaa Mohaideen Briyani" in 336 & 338, Main Road, Pallavaram, Chennai has been rated 4.4
2. Found "SS Hyderabad Biryani" in 98/339, Arcot Road, Opposite Gokulam Chit Funds, Kodambakkam, Chennai has been rated 4.4
3. Found "Yaa Mohaideen Biryani" in 4/158, Church Road, Opposite Uzhavar Santhai & Tea Stall, Pallavaram, Chennai has been rated 4.4
4. Found "Mami Tiffen Stall" in 7, Pitchupillai Street, Near Kapaleeshwarar Temple, Mylapore, Chennai has been rated 4.3
5. Found "Kovai Alankar Vilas" in AC 3, 2nd Avenue, Anna Nagar East, Chennai . has been rated 4.2
Should I send you the details of all the restaurants on email?
Your input ->  no thanks
Okay. Bon Appetit!
Goodbye! See you again.
Your input ->  hi
hey there! How may i help you
Your input ->  looking for chinese restaurant
Certainly i can help you, let me know the location you prefer to dine?
Your input ->  bangalore
Please provide a different location
Your input ->  bengaluru
? what kind of cuisine would you like?  Type out your own message...
Your input ->  i'll prefer thai
Sorry, the cuisine is not available yet. Please try again with the given options
? what kind of cuisine would you like?  4: American (American)
? What price range are you looking at?  2: Rs. 300 to 700 (mid)
1. Found "Meghana Foods" in 124, KHB Colony, 1st Cross, Near Jyothi Nivas College, Koramangala 5th Block, Bangalore has been rated 4.4
2. Found "Muthashy's" in 3, Brindavan Complex, 20th Main, Maruthi Nagar Main Road, 1st Stage, BTM Layout has been rated 4.3
3. Found "eat.fit" in 96, 29th Main, 23rd Cross, 2nd Stage, BTM, Bangalore has been rated 4.3
4. Found "eat.fit" in 32/2G, NCPR Industrial Layout, Doddanakundi Industrial Area 2, Seetharampalya, Hoodi, Whitefield, Bangalore has been rated 4.3
5. Found "eat.fit" in 16, 1st Main Road, Muneswara Nagar, Sector 6, HSR, Bangalore has been rated 4.3
Should I send you the details of all the restaurants on email?
Your input ->  sure send it to v83@gmail.com
Sent. Bon Appetit!
See you again!
Your input ->  he
Your input ->  hi
Your input ->  there
Hey, How is it going. How may I help you Today
Your input ->  looking for mexican restaurant
Sure, i can find some nice restaurants, which location do you prefer?
Your input ->  ooty
Sorry, I could not understand the location. Try some other location
? what kind of cuisine would you like?  6: South Indian (South Indian)
Sure, i can find some nice restaurants, which location do you prefer?
Your input ->  madurai
Please provide a different location
Your input ->  bangalore
? what kind of cuisine would you like?  2: Mexican (Mexican)
? What price range are you looking at?  2: Rs. 300 to 700 (mid)
1. Found "Meghana Foods" in 124, KHB Colony, 1st Cross, Near Jyothi Nivas College, Koramangala 5th Block, Bangalore has been rated 4.4
2. Found "Muthashy's" in 3, Brindavan Complex, 20th Main, Maruthi Nagar Main Road, 1st Stage, BTM Layout has been rated 4.3
3. Found "eat.fit" in 96, 29th Main, 23rd Cross, 2nd Stage, BTM, Bangalore has been rated 4.3
4. Found "eat.fit" in 32/2G, NCPR Industrial Layout, Doddanakundi Industrial Area 2, Seetharampalya, Hoodi, Whitefield, Bangalore has been rated 4.3
5. Found "eat.fit" in 16, 1st Main Road, Muneswara Nagar, Sector 6, HSR, Bangalore has been rated 4.3
Should I send you the details of all the restaurants on email?
Your input ->  no thanks
Okay. Bon Appetit!
See you again!

Results received on email:

Vijay Venugopal
11:02 PM (0 minutes ago)
to me

FYI

---------- Forwarded message ---------
From: <foodiebot777@gmail.com>
Date: Tue, Apr 28, 2020 at 1:22 AM
Subject: Your Foodie Bot Query
To: <v83@gmail.com>

Hello, Please find the list of top 10 Italian restaurants around delhi in the mid price range.:

1. Found "Oishii Wok" in Behind Super Mart 2, DLF Phase 4, Gurgaon has been rated 4.9 average price for two people is Rs.700
2. Found "Punjabi Angithi" in 32-22, A 4, DDA Market, Paschim Vihar, New Delhi has been rated 4.5 average price for two people is Rs.400
3. Found "Gulab" in 5, Main Road, Pitampura, New Delhi has been rated 4.2 average price for two people is Rs.500
4. Found "Singla's" in A-139/140, Main Road, Madhu Vihar, Near Hasanpur Depot, IP Extension, New Delhi has been rated 4.2 average price for two people is Rs.500
5. Found "Bikanervala Angan" in 10181, 82, Arya Samaj Road, Karol Bagh, New Delhi has been rated 4.1 average price for two people is Rs.600
6. Found "Haldiram's" in 45, Ring Road, Lajpat Nagar 2, New Delhi has been rated 4.1 average price for two people is Rs.600
7. Found "Bikanervala" in Plot 3-5, Near Leisure Valley Park, Sector 29, Gurgaon has been rated 4.1 average price for two people is Rs.600
8. Found "Haldiram's" in C 9, Opposite ITI, Main Market, Malviya Nagar, New Delhi has been rated 4.1 average price for two people is Rs.600
9. Found "Om Sweets & Snacks" in SCO 17, Main Market, Sector 31, Gurgaon has been rated 4.1 average price for two people is Rs.500
10. Found "Bikanervala" in Suncity Business Tower, Golf Course Road, Gurgaon has been rated 4.1 average price for two people is Rs.600

Wish you have wonderful day ahead! See you soon!


TEST RESULTS:

(rasa) VIJAVENU-M-D0LL:Rasa_Chatbot_Assignment vijavenu$ rasa test core --stories data/stories.md --out results
//anaconda3/envs/rasa/lib/python3.7/site-packages/rasa/core/policies/keras_policy.py:265: FutureWarning: 'KerasPolicy' is deprecated and will be removed in version 2.0. Use 'TEDPolicy' instead.
  current_epoch=meta["epochs"],
Processed Story Blocks: 100%|██████████████████████████████████████████████████████████| 48/48 [00:00<00:00, 893.59it/s, # trackers=1]
2020-04-28 01:53:18 INFO     rasa.core.test  - Evaluating 45 stories
Progress:
100%|█████████████████████████████████████████████████████████████████████████████████████████████████| 45/45 [00:18<00:00,  1.97it/s]
2020-04-28 01:53:37 INFO     rasa.core.test  - Finished collecting predictions.
2020-04-28 01:53:37 INFO     rasa.core.test  - Evaluation Results on CONVERSATION level:
2020-04-28 01:53:37 INFO     rasa.core.test  - 	Correct:          3 / 45
2020-04-28 01:53:37 INFO     rasa.core.test  - 	F1-Score:         0.125
2020-04-28 01:53:37 INFO     rasa.core.test  - 	Precision:        1.000
2020-04-28 01:53:37 INFO     rasa.core.test  - 	Accuracy:         0.067
2020-04-28 01:53:37 INFO     rasa.core.test  - 	In-data fraction: 0.882
2020-04-28 01:53:37 INFO     rasa.core.test  - Evaluation Results on ACTION level:
2020-04-28 01:53:37 INFO     rasa.core.test  - 	Correct:          826 / 881
2020-04-28 01:53:37 INFO     rasa.core.test  - 	F1-Score:         0.918
2020-04-28 01:53:37 INFO     rasa.core.test  - 	Precision:        0.931
2020-04-28 01:53:37 INFO     rasa.core.test  - 	Accuracy:         0.938
2020-04-28 01:53:37 INFO     rasa.core.test  - 	In-data fraction: 0.882
2020-04-28 01:53:37 INFO     rasa.core.test  - 	Classification report:
                           precision    recall  f1-score   support

 action_validate_location       1.00      1.00      1.00        62
        utter_ask_emailID       0.97      0.97      0.97        34
            action_listen       0.86      1.00      0.92       255
          utter_ask_price       1.00      0.68      0.81        22
              utter_reply       1.00      1.00      1.00         3
           action_restart       1.00      1.00      1.00        45
action_search_restaurants       1.00      0.93      0.96        41
 utter_ask_location_again       1.00      1.00      1.00        21
        utter_ask_cuisine       1.00      1.00      1.00        33
         utter_email_sent       1.00      1.00      1.00        36
    action_validate_email       0.98      0.98      0.98        52
        action_send_email       1.00      1.00      1.00        36
              utter_greet       0.67      0.05      0.09        44
       utter_ask_location       1.00      1.00      1.00        16
            utter_goodbye       1.00      0.98      0.99        45
    utter_ask_about_email       1.00      1.00      1.00        36
  action_validate_cuisine       0.85      1.00      0.92        55
        action_slot_reset       1.00      1.00      1.00        40
     utter_email_not_sent       1.00      1.00      1.00         5

                 accuracy                           0.94       881
                macro avg       0.96      0.93      0.93       881
             weighted avg       0.93      0.94      0.92       881

2020-04-28 01:53:37 INFO     rasa.nlu.test  - Confusion matrix, without normalization:
[[255   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
    0]
 [  0  45   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
    0]
 [  0   0  38   0   0   3   0   0   0   0   0   0   0   0   0   0   0   0
    0]
 [  0   0   0  36   0   0   0   0   0   0   0   0   0   0   0   0   0   0
    0]
 [  0   0   0   0  40   0   0   0   0   0   0   0   0   0   0   0   0   0
    0]
 [  0   0   0   0   0  55   0   0   0   0   0   0   0   0   0   0   0   0
    0]
 [  0   0   0   0   0   0  51   0   0   0   1   0   0   0   0   0   0   0
    0]
 [  0   0   0   0   0   0   0  62   0   0   0   0   0   0   0   0   0   0
    0]
 [  0   0   0   0   0   0   0   0  36   0   0   0   0   0   0   0   0   0
    0]
 [  0   0   0   0   0   0   0   0   0  33   0   0   0   0   0   0   0   0
    0]
 [  0   0   0   0   0   0   1   0   0   0  33   0   0   0   0   0   0   0
    0]
 [  0   0   0   0   0   0   0   0   0   0   0  16   0   0   0   0   0   0
    0]
 [  0   0   0   0   0   0   0   0   0   0   0   0  21   0   0   0   0   0
    0]
 [  0   0   0   0   0   7   0   0   0   0   0   0   0  15   0   0   0   0
    0]
 [  0   0   0   0   0   0   0   0   0   0   0   0   0   0   5   0   0   0
    0]
 [  0   0   0   0   0   0   0   0   0   0   0   0   0   0   0  36   0   0
    0]
 [  0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0  44   1
    0]
 [ 42   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   2
    0]
 [  0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
