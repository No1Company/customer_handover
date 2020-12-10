# Development decisions  

    Document Status: Finished
    Inspected by: Filip Nyberg (Quality Coordinator) & Ola Friberg (Technical Writer) on 2020-12-09
    Contact Person: Victor Lindholm (Lead developer)
    Written by: Development team
    Manager: Albin Ekenhagen

## Table Of Content 
[1. Background](#background)   

[2. Microsoft Bot Framework](#microsoftbotframework)   

[3. Composer](#composer)

[4. Adaptive cards](#adaptivecards)

[5. Extra server](#extraserver) 

[6. OpenEHR](#openehr)

[7. Teams](#teams)

[8. Different branches for Teams and emulator](#differentbranchesforteamsandemulator)

[9. Dialogue design](#dialoguedesign) 

# 1. Background <a name="background"></a>
This document briefly describes important decisions made by the development team. It is intended to give the customer insight in the development process as well as understanding why certain choices were made. It discusses our choice of framework and development tools, backend and server usage, which platform the chatbot is deployed to and some discussion about functionality and dialogue design.

# 2. Microsoft Bot Framework <a name="microsoftbotframework"></a>
The first major decision to be made by the developers was the tools and frameworks to use in the implementation of the solution. We wanted to use a framework to get started with the work early and be able to produce deliverables every sprint instead of starting from nothing. During the process of determining the correct tools for the job the three major frontrunners up for consideration were wit.ai (Facebook-owned), Dialogflow (Google-owned) and Microsoft Bot Framework. 

Major factors that played into the choice of Microsoft Bot Framework included it having a relatively large community of users that could be used for troubleshooting, an array of YouTube-tutorial videos, examples of bots implementing certain features and a quite fleshed out documentation. 

Ultimately the contenders came out quite even and what tipped the scales in Microsoft Bot Framework's favor was that it was recommended by the customer. Furthermore, the client preffered us to not use neither facebook-owned nor google-owned software. Since none of the developers had prior experience with any of the potential frameworks we had the luxury of using the one preferred by the client.

# 3. Composer <a name="composer"></a>
As the Microsoft Bot Framework was complicated to get started with using examples of other bots, editing pre-made conversation in JavaScript, we searched through the documentation of the framework. We found that Microsoft supplies a GUI for creating bots called Microsoft Bot Composer. This was tempting as we couldn't quite proceed with trial and error, when we felt like we didn't make any progress. This made the choice of Composer as editor for the bot quite natural. Using this, we could make great advancements, a lot faster than before. We did however encounter bugs in Composer, but we felt as if it was a trade-off worthwhile. This made the step out of the framework and composer quite big and we became locked to the framework relatively early in the process. With that said, it still works most of the time, but it is harder to get logs of what went wrong than using a regular compiler. Composer is however fairly straightforward to use, and the "rostbotguide" will guide you through the foundations of it. There's also quite a bit of documentation, but for the functionality included in the bot, creating conversations, using variables and such, it is simple to get started using the guide. Had we done the project with the knowledge we have in the end of the project, we'd probably have used a lighter framework. The functionality we have right now isn't logically complex and would probably be easier and more robust to develop with a framework with less overhead. 

# 4. Adaptive cards <a name="adaptivecards"></a>
Microsoft Bot Framework supports the use of something called an Adaptive Card. An example of what this is can be seen as soon as the bot is started - the first interaction sent from the bot is a card with a picture, some text and a couple of buttons. We found this quite early and decided that this was something that we would want to use as it was quite esthetically pleasing and it was possible to show suggestions for possible actions to the user.

These cards could easily be replaced by normal text so it was more of a design-oriented decision since we wanted to show not only the possible functionality in Microsoft Bot Framework but also what it could look like. This is why not all dialog flows make use of this as it is more time consuming than plain text. Later we also found out that the cards are not fully compatible with all platforms such as Messenger and Whatsapp.

# 5. Extra server <a name="extraserver"></a>
Composer hosts a server that the chat clients connect to when they initiate a conversation. This server is supplemented by an additional server that serves two purposes. 

1. The developers needed some way to simulate external resources, such as RÖs scheduling system. This required some kind of external server that could provide external data. This was the main reason for creating the extra server. 

2. Composer has limited communication capabilities. It has the ability to make HTTP requests, but they are very awkward to make and they require great care to get right. Thus, communicating with OpenEHR using the built in HTTP requests, while probably possible, was something that we wanted to avoid. The extra server allows the developers to make simplified requests in a format that is easy to implement in Composer. These requests are sent to the extra server that then makes more complicated requests to OpenEHR.

# 6. OpenEHR <a name="openehr"></a>
The decision to use OpenEHR was an easy decision to make. The customer required us to use it for storing patient data.

# 7. Teams <a name="teams"></a>
As the company uses Microsoft Teams as its communications platform, the decision to deploy the bot to the platform was made. The customer also uses Teams, so they approved of this decision. Teams is owned by Microsoft, and was mentioned in the documentation as a platform which was able to handle a lot of chat bot functions, which were additional reasons to use Teams as its platform. Other platforms such as Messenger and Whatsapp isn't compatible with all functions that we are using.

# 8. Different branches for Teams and emulator <a name="differentbranchesforteamsandemulator"></a>
During the final iterations of the project, it became apparent that there were some compatibility issues between the developed bot and Microsoft Teams. Due to limited time and resources to spare, the decision to work on the Teams implementation of the bot on a separate branch was made in order to save time. The underlying reason behind the compatibility issue turned out to be the formatting of the cards that the bot send to the user. In order to avoid having to rewrite our whole conversation flow structure to support both the emulator channel and the Teams channel we decided to split. 

# 9. Dialogue design <a name="dialoguedesign"></a>
The dialogues are not considered to be complete, neither being one of our main priorities during development. They are simple and intended to show the functionality of the chat bot, not to express correct sentences from a health and medical perspective. Consider the dialogues as a simple suggestion for RÖ to build upon. Furthermore, the dialogues lack a common thread, where the way the bot expresses itself may vary in style (tempus and even grammar in some points).

There are mainly two reasons to why the dialogues were less prioritized than other aspects of the bot. First, we are well aware of the fact that in a finished product, the dialogues and sentences must be written carefully with a great attention to details, to be sure that the right type of message is sent. We don't consider us to be able to create these dialogues. Additionaly, RÖ told us to value quantity over quality in terms of possible functions of the chat bot, and spending time creating better dialogues would interfere with this prioritization.

To summarize - the dialogues are ment to be a first idea of the capabilities of a finished product and are intended to be improved by RÖ.
