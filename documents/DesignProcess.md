# Design process

    Document Status: Finished
    Inspected by: Filip Nyberg (Quality Coordinator) on 2020-12-10
    Contact Person: Ola Friberg (Technical Writer)
    Written by: Ola Friberg (Technical Writer)
    Manager:

## Table of contents
[**1. Introduction**](#introduction)   
[**2. Design research**](#desinresearch)      
[**3. Prototype development**](#prototypedevelopment)   
&nbsp;&nbsp;[3.1 Phase 1](##phaseone)   
&nbsp;&nbsp;[3.2 Phase 2](##phasetwo)   
&nbsp;&nbsp;[3.3 Phase 3](##phasethree)   
&nbsp;&nbsp;[3.4 Phase 4](##phasefour)   
[**4. Future work**](#futurework)   
[**5. References**](#references)  

## 1. Introduction <a name="introduction"></a>

The design team started with researching the topic of bot design. This research laid the foundation of the first prototype but was also continuously referred to in order to guide the development of subsequent iterations. A summary of the findings of this research will be described, which will be followed by descriptions of the different prototypes with comments from user testing.

The tools used for prototyping are Botsociety, Figma and Botmock. Botsociety was used in the earlier prototypes (first and second prototypes), but because of its limitations this tool was later replaced by Botmock. One of these limitations is a max limit of 30 messages per prototype, which forced us to split our prototype up into multiple prototypes. There was also a lack of input formats available, which lead to the earlier prototypes having buttons where there was supposed to be text input.

## 2. Design research <a name="designresearch"></a>

Research indicates that it is helpful to have a welcome message accompanied by a menu in the beginning of the interaction with a bot. A menu makes it clear for the user what the bot is capable of, the bot’s limitations and how the user can interact with the bot. Communicating transparency in terms of what the bot can and cannot do with the user facilitates a higher degree of trust towards the bot. Additionally, it is important that it is made clear early on that the user is interacting with a bot. One way of doing so is having a suitable picture next to the bot’s message. Furthermore, the user’s trust in the bot is also affected by its language and grammar, which makes careful design of the message protocol important. Buttons have the advantage of promoting ease of use, since pressing a button is much faster than writing input manually. Buttons also have the advantage of reducing complexity in development, since there are fewer possibilities that the developers have to consider. [1]

## 3. Prototype development <a name="prototypedevelopment"></a>

Prototype development is divided into four phases. In each phase, except the first, user testing from the previous phase is used to iterate on and improve the prototype. For instance, the user feedback from the first round of user testing is used for the development of the second prototype. Similarly, the user feedback from round two of user testing lays the groundwork for the third prototype, and so on until the fourth and final prototype.

### 3.1 Phase 1 <a name="phaseone"></a>

The prototype for registering measurements, asking questions and booking consultations was created using Botsociety. The different features were designed quite similarly. The prototype was designed according to the sources described in the initial design research, and the registering measurements features was later user tested. The design consisted of a welcome message with a menu of clickable buttons that displays the available options to the user. After clicking the “register measurement” button, a procedure to measure blood pressure is initiated. This procedure guides you through each step of measuring blood pressure. When the user finally enters the blood pressure values, limited in the prototype to two specific blood pressures values, there is a request to double-check whether the user entered the correct values. All input is submitted via clickable buttons that send texts corresponding to the text on the button itself. Next to each message received from the bot, there is a small picture that clarifies to the user that it is communicating with the bot.

The prototype for notification settings was created with Figma. The design differed from the prototype using Botsociety. Both started with presenting a welcome message and a menu of available options to the user, but in this case only the functionality for the notification settings had been implemented. When clicking the button to show notification settings, the notification settings for each type of measurement are listed separately. This information includes how often notifications will be given before/after the measurements are due and if the notification is to be sent via a chat message, SMS or email. At the bottom there is a clickable button with the text “new notification”. When creating a new notification, the type of measurement and notification option are selected with the help of checkboxes, while the time for the notification is selected with the help of a scroll-function.


### 3.2 Phase 2 <a name="phasetwo"></a>

The second prototype for registering measurements, booking consultations and asking questions was also created in Botsociety. The user tests for registering measurements in phase one indicated that the bot was easy to use and it was not often that a tester felt lost in the process. People, for example, were content with the buttons, and so they remained mostly the same. However, there were some complaints about the overall process. Some testers reported a perceived lack of clarity in the texts. Changes were thus made to the texts in the second prototype. This includes a more detailed presentation about the bot in the welcome message.  The picture next to the bot’s messages was also changed to be more human-like. One version still retained the previous picture, however. Moreover, user feedback indicated the dialogue was too complicated with too many clicks. Some users also suggested that the bot should allow for registering measurements without a guide, so as to speed up the process. This resulted in two separate prototypes, one with the guide and one without. Additionally, the option to select either to measure weight or blood pressure was implemented.

When the user selects the option “ask questions” in the menu, the bot responds by asking what the user wants to know. When the user responds with their question, the bot answers by asking if the user wants to be redirected to another part of the bot which can answer the question. The user can then respond with yes or no by clicking on buttons. If the user responds with no, the bot asks if the user wants to ask another question and the user can again answer with buttons.

The prototype for notification settings is still created in Figma and there were almost no changes compared to the first prototype. The user testers on the first prototype were positive about that it was easy to use, though they sometimes clicked the wrong buttons. The user tests also indicated that users had problem using the scroll-function. The changes to the second prototype were that the ”add notification” button was higher up and that one button had its text changed.

### 3.3 Phase 3 <a name="phasethree"></a>

The third prototype was created in Botmock. This allowed us to test all features in the same prototype. A constant limitation of the previous prototype frameworks was the inability to write input. This new tool allowed us to do this. The structure of the bot was largely the same, but the design mimicked more closely a conversation one would have with a bot on Messenger. Because most testers in the previous rounds of user testing were positive towards being able to skip the guide for the measurements, this option was fully integrated into the third prototype. User feedback again indicated the measurement process had too many steps. Furthermore, users did not like that each measurement value had to be confirmed separately and suggested that it would suffice with just one final confirmation at the end of the measurement registration. Lastly, users were more positive towards the human-like picture, which is why it was used in the third prototype.

The functionality for booking consultations remained mostly the same, partly because it had not been tested in user tests yet. When choosing to book a consultation in the main menu, the bot asks for a reason for the booking. The user then provides a desired date, which the bot responds to with relevant time slots. The user can select one of these slots or request more options. In this prototype the booking confirmation now includes the booking details.

On the other hand, the functionality for asking questions had changed significantly. The structure has been revamped, and the bot now presents a menu with options “How does the chat-bot work?”, “My measurements” and “Other questions”. The first two options guide the user through a set of menus providing information, while the “Other questions” alternative lets the user ask the bot its own question.

### 3.4 Phase 4 <a name="phasefour"></a>

The fourth prototype was also implemented in Botmock, but the design is with Microsoft Teams in mind instead of Messenger. The most noticeable change between the third and fourth prototype is therefore the design. The functionality for registering measurements is the same for blood pressure. However, a new health form measurement has been added as an option. When registering a health form measurement, the user will answer 10 questions on a scale of 1 to 5 by clicking buttons. After all 10 questions have been answered, a verification message is sent by the bot. 

The booking consultation functionality was the same as in the previous prototype both according to functionality and text, the only difference was in the design. User feedback in the third round of user testing complimented the prototype’s ease of use, particularly the choice of buttons as primary communication tool. Something they thought could be improved though was the choice of widget for choosing a booking date. They preferred having a calendar to choose the date with rather than writing the date as text input. Therefore, a prototype of a calendar which displays all available bookings was created using Figma.

Finally, the functionality for asking questions also changed. There are new menus and changed texts. In the main question menu, the “My measurements” button has been split into two buttons, one called “Measured values” and another “Upcoming measurements”, both of which have new menus and new options. Another change in the main question menu is that settings now is a button.

## 4. Future work <a name="futurework"></a>

The fifth round of user testing was on the final product. The results of these are therefore a basis for future development. Most testers were positive about the registering of measurements. The amount of information and clicks necessary to measure blood pressure was appropriate and the option to skip having a guide was good. Although some of them wanted the measurement to be possible with even fewer steps, they generally expressed that the functionality was easy to use. They would have preferred the guide to be more easily added or removed directly when registering measurements, rather than configured through the settings which some of them found difficult to find.

They were also mostly positive about the functionality for changing notification settings. While all testers thought it was easy to use, one would have liked to have notifications at the exact time a measurement was due. 

Testers found the health form to be easy to use, but some would have liked to be able to edit answers to questions retroactively. Another possible improvement is numbering the questions so that the user knows how many are left. There was also some inconsistency in the scales used for the questions, which may lead to mistakes in filling the health form.

## 5 References <a name="references"></a>
[1]: Microsoft, Design a bot's first user interaction, https://docs.microsoft.com/en-us/azure/bot-service/bot-service-design-first-interaction?view=azure-bot-service-4.0 (2020-12-09)





