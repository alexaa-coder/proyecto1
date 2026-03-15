SOFTWARE VALIDATION REPORT










Function:
Prepared by:
Reviewed by:
Approved by:




Department:
Development
Development
Quality Assurance


Name:
Daniel Cámara
Javier Vico
Ivan Perez


Signature:





Date:
09/08/2024
09/08/2024
09/08/2024




# Content

[1.](#introduction) [Introduction](#introduction) [4](#introduction)

[2.](#scope) [Scope](#scope) [4](#scope)

[3.](#definitions) [Definitions](#definitions) [4](#definitions)

[4.](#validation-plan) [Validation plan](#validation-plan)
[4](#validation-plan)

[4.1.](#goals) [Objectives](#goals) [4](#goals)

[4.2.](#validation-methods) [Validation methods](#validation-methods)
[5](#validation-methods)

[4.3.](#acceptance-criteria) [Acceptance criteria](#acceptance-criteria)
[5](#acceptance-criteria)

[4.4.](#validated-software-version) [Validated software
version](#validated-software-version) [5](#validated-software-version)

[5.](#validation-procedures) [Validation
procedures](#validation-procedures) [5](#validation-procedures)

[5.1.](#installation-qualification-iq) [Installation Qualification
(IQ)](#installation-qualification-iq)
[5](#installation-qualification-iq)

[5.1.1.](#review-of-installation-documentation) [Review of installation
documentation](#review-of-installation-documentation)
[5](#review-of-installation-documentation)

[5.1.2.](#hardware-and-software-testing) [Hardware and software
verification](#hardware-and-software-testing)
[6](#hardware-and-software-testing)

[5.1.3.](#installation-registration) [Installation
registration](#installation-registration)
[6](#installation-registration)

[5.1.4.](#file-integrity-validation) [File integrity
validation](#file-integrity-validation) [7](#file-integrity-validation)

[5.2.](#operation-qualification-oq) [Operation Qualification
(OQ)](#operation-qualification-oq) [7](#operation-qualification-oq)

[5.2.1.](#basic-functionality-tests) [Basic Functionality
Testing](#basic-functionality-tests) [7](#basic-functionality-tests)

[5.2.2.](#integration-tests) [Integration Testing](#integration-tests)
[9](#integration-tests)

[5.2.3.](#performance-tests) [Performance Tests](#performance-tests)
[10](#performance-tests)

[5.2.4.](#security-check) [Security verification](#security-check)
[13](#security-check)

[5.3.](#performance-qualification-pq) [Performance Qualification
(PQ)](#performance-qualification-pq) [13](#performance-qualification-pq)

[5.3.1.](#user-acceptance-testing) [User Acceptance
Testing](#user-acceptance-testing) [13](#user-acceptance-testing)

[5.3.2.](#critical-scenario-testing) [Critical Scenario
Testing](#critical-scenario-testing) [15](#critical-scenario-testing)

[5.3.3.](#evaluating-user-documentation) [Evaluating user
documentation](#evaluating-user-documentation)
[16](#evaluating-user-documentation)

[6.](#results-and-conclusions) [Results and
conclusions](#results-and-conclusions) [17](#results-and-conclusions)

[7.](#version-history) [Version history](#version-history)
[17](#version-history)

[8.](#conformity-of-the-person-responsible-for-validation) [Conformity
of the person responsible for
validation](#conformity-of-the-person-responsible-for-validation)
[18](#conformity-of-the-person-responsible-for-validation)

# Introduction

This report presents the results of the validation of the VRCardio
VHET360 software, hereinafter VRCardio , developed by Spika Tech,
hereinafter SPIKA, specifically designed for the visualization and
analysis of cardiac signals. The validation verifies that VRCardio meets
the necessary functionality, reliability, and safety standards.

# Scope

Validation covers all aspects of the VRCardio environment, focusing on
three key areas: functionality, reliability, and security. It includes
verification of all environment functions, detection of critical errors,
and security assessment against known vulnerabilities.

# Definitions

Validation : The process of evaluating whether a system or
component meets requirements and functions as intended in its operating
environment.

Installation Qualification (IQ): Verification that the software
and all its components have been installed correctly in the target
environment.

Operational Qualification (OQ) : Confirmation that the software
operates correctly and that all major functionalities and modules
function as expected.

Performance Qualification (PQ) : Ensuring that the software meets
specific business requirements and operates according to user-defined
performance and functionality criteria.

# Validation plan

# Goals

The main objectives of the VRCardio software validation are:

-   Ensure that the software meets established functionality and
    performance requirements.

-   Verify the reliability and stability of the software under different
    operating conditions.

-   Evaluate software security against known and potential
    vulnerabilities.

# Validation methods

Methods used for validation include:

-   Installation and configuration testing.

-   Basic and advanced functionality testing.

-   Integration and communication tests with other systems.

-   Performance tests under different loads.

-   Security and attack resistance testing.

# Acceptance criteria

The software will be considered accepted if it meets the following
criteria:

-   Correct installation and configuration without errors.

-   Correct operation of all main functionalities.

-   Successful integration with external systems and hardware.

-   Adequate performance under different load conditions.

-   Compliance with established safety standards.

# Validated software version 

With the completion of this software validation report, the following
version of VRCardio is being carried out: 1.0.0.

# Validation procedures

# Installation Qualification (IQ)

# Review of installation documentation

All the information available for downloading the software and getting
started with creating a project has been compiled:

-   Download link: There is no download link yet, until the app is
    publicly released.

-   Installation: Unzip the .zip file and open the
    VRCardio-VHET360-Visualization.exe file.

-   Minimum requirements:

    -   Operating system: Windows 10 64-bit

    -   Processor: 8-Core Intel Core i5 or equivalent

    -   RAM: 8 GB or more

    -   For non-VR use: NVIDIA GeForce GTX 1050 ti or equivalent

    -   For use with VR: NVIDIA GeForce RTX 2070 or equivalent

    -   Disk space: Minimum 2 GB of free space

After this, the software was downloaded and installed successfully.

# Hardware and software testing

For the VRCardio version (1.0.0) the minimum requirements indicated for
its correct operation are:

-   Windows 10 or higher

-   x64 architecture

-   DX10, DX11 or DX12

The computers on which this software has been installed and tested have
the following characteristics:

-   Windows 10 or Windows 11

-   x64 architecture

-   DX12

# Installation registration









Process
Staff
Incidents




Access to internal download
Downloading and installing the software
Login with a private development account
Access to the developed software
David Pozo
None


Access to internal download
Downloading and installing the software
Login with a private development account
Access to the developed software
Daniel Cámara
None


Access to internal download
Downloading and installing the software
Login with a private development account
Access to the developed software
Javier Vico
None




# 

# File integrity validation

After each software download and installation, the local path folder was
accessed to verify that all files existed and had a modification date
consistent with the installation date, confirming that no files had been
modified in any way after installation.

# Operation Qualification (OQ)

# Basic functionality tests









Test performed
Result
Confirmation




Open the application.
The application opens without errors.
The application has started loading and then opening.


Login.
The user logs in without any problem.
The user successfully accesses his account.


Log out.
The user logs out of his account.
The user successfully logs out and returns to the login screen.


Access an offline room.
The user creates an offline room and successfully logs in.
The user can interact with the room panels without any problem.


Upload a case
The user accesses the list of cases, loads one of them and it
appears on the screen
The user can view and interact with the case without any
problem.


View and manage cardiac signals.
The user accesses the signals and can view them without any
problem.
The signals have been correctly represented in the graph.


Managing time
The user has been able to manage the session time using the
controllers.
The time has responded correctly to user actions.


Use VR glasses
The user has successfully entered a room using VR glasses
The user views the scene correctly using VR glasses


Use holographic display
The user has successfully entered a room using a holographic
display
The user visualizes the scene correctly using a holographic
display


Access an online room
The user accesses an online room using the code
The user can view the online scene next to the other users'
pointers.


Modify panel position
The user has been able to move and rotate the room panels without
any problem.
The panels have been modified in position and rotation.


Hide and show panels
The user has hidden several panels without any problem.
Panels have appeared and disappeared at the user's whim.




# Integration tests









Test performed
Result
Confirmation




Database integration
Data is stored and retrieved correctly.
Results of queries and updates:

Test query performed in 10ms, accurate data retrieval.
Registry update completed in 20ms, successful update
confirmation.



Communication with remote servers
Communication is stable and error-free.
Communications records:

HTTP request sent
Response received in 200 ms, no connection errors.



Data synchronization between devices
Data is synchronized properly.
Confirmation of data synchronized correctly between device A and
B.


User authentication
Users are authenticated successfully.
Authentication completed in 50ms, no errors.


Interaction with an API
The API responds correctly.
Response received in 300 ms with correct patient data


Use of cloud services
Cloud services run smoothly.
File uploaded and accessible in 5 seconds, without errors.


Interaction with external hardware
The hardware responds appropriately.
Data readings received in 100 ms, with no communication errors.


Real-time data synchronization
Synchronization is fast and error-free.
Confirmation of successful real-time synchronization.


User session management
Sessions are managed correctly.
Login and logout records:

User login at 12:00 PM.
Session closed at 12:30 PM.
Session managed without problems.



Integration with storage services
Data is stored and retrieved seamlessly.
Data stored in the database.
Data recovery completed in 2 seconds, no errors.


Application monitoring
Monitoring is performed without interruptions.
Confirmation of monitoring data received continuously without
interruptions.




# Performance tests









Test performed
Result
Confirmation




Maximum load of simultaneous users
The application supports maximum load without degradation.
Response time and resource utilization records:

Number of simultaneous users: 50
Average response time: 200 ms
CPU Utilization: 70%
usage : 65%



Stress test
The system recovers properly after stress.
Stress test results:

Application subjected to heavy file load
Full recovery to normal state in seconds.



Latency test
Latency remains within acceptable limits.
Latency test results:

Average latency: 150 ms
Maximum latency: 300 ms
Tests performed under different network conditions.



Concurrency test
The system handles multiple concurrent requests.
Concurrency test results:

1,000 concurrent applications.
All applications processed successfully without errors.



Memory Usage Test
The application handles memory usage properly .
Memory usage during load test: 65%
No memory leaks detected.


CPU Usage Tests
The application handles CPU usage properly.
CPU usage during load test: 75%


Bandwidth testing
The application works well with different bandwidths.
Bandwidth used: 10 Mbps, 50 Mbps, 100 Mbps.
Stable performance


Response testing on different networks
The application responds appropriately on different networks.
Test results on various networks:

Tested networks: 3G, 4G, 5G, Wi-Fi.
Average response time on 3G: 500 ms
Average response time on 4G: 300 ms
Average response time on 5G and Wi-Fi: 100 ms



Load time tests
Loading times are acceptable.
Initial load time: 6 seconds


Script runtime testing
Scripts run within the expected time.
Script execution time logs:

Average execution time: 50 ms
execution time : 200 ms



Background resource usage tests
The app handles background resources well.
Resource usage results:

Background CPU usage: 30%
Background memory usage: 35%





# Security check









Test performed
Result
Confirmation




Proof of unauthorized access
The system blocks unauthorized access.
Logs of access attempts and blockages:

All attempts were successfully blocked



SQL Injection Testing
The system is immune to SQL injections.
No SQL injection was successful.


Cross-Site Scripting (XSS) Testing
No XSS vulnerabilities found.
No XSS vulnerabilities were found.


Access control tests
Access controls are working properly.
Users with different roles tested.
All accesses were properly controlled according to the
permits.


Data integrity testing
Data integrity is guaranteed.
All data remained intact during the test.




# Performance Qualification (PQ)

# User acceptance testing









Test performed
Result
Confirmation




Installing and running the software
Users download, install and run the application without any
problems.
Feedback on the ease of configuration and functionality of the
parameters:

User A: "The process was very simple."
User B: "I was able to install the app without any
problems."
User C: "Downloading and installing the app is easy."



Using display panels
Users use data visualization dashboards to analyze patterns.
Comments on the effectiveness and ease of use of the display
panels:

User A: "The panels are useful and easy to use."
User B: "It's very convenient to use the panels to change the
display."
User C: "I enjoyed the experience of using the panels ."



Users evaluate the navigation and usability of the software
Users evaluate the navigation and usability of VRCardio
software.
Feedback on the user interface and ease of use:

User A: "It has been intuitive and comfortable."
User B: "The application has good usability."
User C: "Easy to use and easy to handle."





# Critical scenario testing









Test performed
Result
Confirmation




Data recovery after a failure
A system failure is simulated and data recovery is verified.
Recovery time and accuracy of recovered data:

Failure simulation performed.
Data recovery completed.
Recovery time: 1 minute.
All data was recovered accurately and without loss.



Real-time analysis
Real-time data analysis is evaluated during critical operations
Performance and accuracy of real-time analysis:

Recorded performance: Average response time of 50 ms.
Analysis accuracy: 99.5%



High demand scenarios
High-demand scenarios are simulated and software performance is
evaluated.
Software performance under high demand:

Test performed under high processing load
The software handled the load without significant performance
drops.
Average response time: 200 ms.



Managing large volumes of data
The software's ability to manage and analyze large volumes of data
is evaluated.
Performance and accuracy in analyzing large volumes of data:

Test performed with 10 GB of data.
Recorded performance: Processing completed in 30
minutes.
Analysis accuracy: 98.7%





# Evaluating user documentation









Test performed
Result
Confirmation




User manual review
Verification that the user manual covers all software features.
All major features are covered.


Setup Guide
The setup guide is ensured to be clear and complete.
The guide covers all the steps necessary for initial setup.


Good Practice Guide
The good practices guide is verified to be complete and
understandable.
The guide is comprehensive and covers all recommended best
practices.


Video tutorials
Video tutorials are said to be clear and educational.
The tutorials are clear and well structured.




# Results and conclusions

After conducting extensive installation (IQ), operational (OQ), and
functional (PQ) testing, it was concluded that VRCardio meets the
standards required for medical use. The results obtained at each stage
of validation indicate the following:

-   Successful Installation: VRCardio installation proceeded without
    incident, meeting the established hardware and software
    requirements. All files were installed correctly and their integrity
    was verified.

-   Successful Operation: Basic functionality, integration, performance,
    and security tests show that VRCardio operates correctly under
    various conditions. No significant errors were found, and all core
    features responded as expected.

-   Proper Operation: User acceptance testing and critical scenarios
    validate that the environment is suitable for developing cardiac
    signal visualization and analysis applications. Users found the
    software intuitive and effective for their purposes.

Based on the data collected, VRCardio is approved for use, ensuring that
it meets the necessary functionality, reliability, and safety criteria.

# Version history









**VERSION**
**REASON FOR CHANGE**
**DATE**




01
Initial edition
July 2024




# Conformity of the person responsible for validation

State:

☐According

☐Not compliant

Name:

Date:

Signature: