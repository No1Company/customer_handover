# **Main document**

## Table of contents
[1. Description of documents](#descriptiondocuments)   
[2. The bot's main functionality](#mainfunctionality)   
 
# 1. Description of documents <a name="descriptiondocuments"></a>

Several documents have been written to serve as a complement to the bot. In these documents there might exist links that do not work. This is because some links are intended for course staff and internal use. In Github, there are two branches named develop and ms-teams. The develop branch runs the bot in the emulator and the ms-teams branch runs it in Microsoft Teams. These are the attached documents:

- **[Rostbot guide](documents/RostbotGuide.md)** - This document includes a quickstart guide and relevant information about implementation and deployment.

- **[System requirements specification](documents/SystemRequirementsSpecification.md)** - The purpose of this document is to describe the features and behavior of the bot.

- **[Future development](documents/FutureDevelopment.md)** - This document details what we believe are the necessary steps in order to make our product into a complete solution.

- **[Market research](documents/MarketResearch.md)** - This document contains analysis of both internal and external aspects of market factors and how these aspects affect our solution. An analysis of the current market and how it affects the viability of our solution is also included.

- **[Design process](DesignProcess.md)** - A description of the design process and the use of prototypes and user tests.

- **[Automated testing](documents/AutomatedTesting.md)** - A document describing problems encountered with automated testing and possible solutions to these problems.

- **[Development decisions](documents/DevelopmentDecisions.md)** - This document briefly describes important decisions made by the development team. It is intended to give the customer insight into the development process as well as understanding why certain choices were made.

- **[Architecture overview](documents/ArchitectureOverview.md)** - The purpose of this document is to communicate how the system works to anyone who, after our development ends, will work with or read our code.

# 2. The bot's main functionality <a name="mainfunctionality"></a>

The user interacts with the bot through clickable buttons and text input. Note that the bot's range of interpretations is in some cases limited. The core features are listed below:

- **Register measurements** - It is possible to register measurements such as blood pressure with the bot. When registering measurements, the user can choose whether to be guided through the process or not. The bot also has the ability to keep track of which measurements have already been done and which are left to do.

- **Answer health forms regarding their general health** - The user can submit information about their health to the bot. This information is then used to keep track of the user's general health.

- **Ask questions** - The user has the option to ask questions by using the bot's FAQ. This includes questions about the bot and about the user's health. It is also possible to be redirected to 1177's website.

- **Manage booking of consultations** - Consultations can be booked with the bot by choosing from available dates. The user will only be suggested a consultation if the reported symptoms are severe enough.

- **Receive information about their symptoms** - By reporting their symptoms, the user can get information about their condition and the severity. 

- **Manage notifications** - By using the notification settings, it is possible to be notified about upcoming measurements and if the user has forgotten to measure any values in time.

