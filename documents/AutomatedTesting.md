# Automated testing 


    Document Status: Finished
    Inspected by: Jonathan Snäll (Test Leader) and Filip Nyberg (Quality Coordinator) on 2020-12-10
    Contact Person: Ola Friberg (Technical Writer)
    Written by: Ola Friberg (Technical Writer)
## Table of contents
[**1. Introduction**](#introduction)   
[**2. Unit testing**](#unittesting)   
[2.1 Possible solution](##unitsolution)   
[**3. UI testing**](#uitesting)   
[3.1 Possible solution](##uisolution)   
[**4. Client API testing**](#clientapitesting)   
 
## 1. Introduction <a name="introduction"></a>

Multiple ways of creating automated tests have been explored, but there has not been much success implementing them. Due to time limitations, not all options have been fully examined. While the options tried so far have not worked, a few options do remain. This document will detail both what has been tested and possible solutions that would have been explored if there was more time.

## 2. Unit testing <a name="unittesting"></a>

Initially, there was some success making a few sample test cases. The next step was to move on to automating the creation of test cases. However, the development team decided on another approach which utilizes Microsoft composer. The framework generates files with all the required codes that client communication with the bot has to be able to respond to. This saves them the work of creating manual response codes. This change made the old test cases obsolete. In a meeting with the development team, they suggested looking at other testing options provided by Microsoft and the framework Selenium.

Microsoft’s testing options were investigated first. The issue with the sample codes was that they were adapted for programming purposes such as C# or Node.js but not for Microsoft composer. At this point there was not enough time to code a solution from scratch. A more thorough study of the composer was conducted, but no solution was found. Eventually, testing management decided on a different approach.

### 2.1 Possible solution <a name="unitsolution"></a>

If the bot was not developed using Microsoft Composer, it may have been possible to develop automated test cases using test driven development. However, trying to implement automated test cases in conjunction with Microsoft Composer would have required a great deal of research and time, which was not feasible given the strict deadline of the project.

## 3. UI testing <a name="uitesting"></a>

Selenium was the next approach. Selenium works for creating UI tests, but the core issue is that it has certain limitations when operating on Microsoft Teams. Selenium scripting was successful in opening the browser, redirecting to the chat URL and logging in, but it was incompatible with the user interface of Microsoft Teams. Textboxes and buttons did not respond appropriately. We tried using the IDE tool of the Selenium framework, but it was still not possible to gain sufficient access to the Microsoft Teams environment to conduct automated tests. The same approach was implemented against a website, where it did work, leading us to believe Selenium is simply unable to access the chat system on Microsoft Teams.

### 3.1 Possible solution <a name="uisolution"></a>

A possible solution is to host the bot on a website instead of Microsoft Teams. This would allow us to implement automated testing using Selenium.

## 4. Client API testing <a name="clientapitesting"></a>

Lastly, we looked into creating a client API and smoke testing. Because there was not enough time to implement anything, our goal was to find out as much as possible about the two approaches. The findings were promising. There needs to be more research into the subject, but it is likely that an automation of test cases might be successful using either of these two approaches.
