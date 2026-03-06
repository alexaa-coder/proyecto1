---
id: pnt_027_02_life_cycle_of_computerised_systems_en
title: "Pnt 027 02 Life Cycle Of Computerised Systems En"
sidebar_label: "Pnt 027 02 Life Cycle Of Computerised Systems En"
---

|Col1|Computerized Systems Development<br />Life Cycle (SDLC)|Code: PNT-027.02|
|---|---|---|
||OFFICIAL USE INTERNAL|Effective date: 02/06/2025|

# **Computerized Systems Development Life Cycle (SDLC)**

|Function:|Prepared by:|Reviewed by:|Approved by:|
|---|---|---|---|
|Department:|Quality Assurance|Systems<br />and<br />cybersecurity|Quality Assurance|
|Name:|Ivan Perez|David Pozo|Fernando Pozo|
|Signature:||||
|Date:||||

|Col1|Computerized Systems<br />Development Life Cycle (SDLC)|Code: PNT-027.02|
|---|---|---|
||Computerized Systems<br />Development Life Cycle (SDLC)|Effective date: 02/06/2025|

|DOCUMENT HISTORY|Col2|Col3|Col4|
|---|---|---|---|
|VERSION|CAUSES OF MODIFICATION|EFFECTIVE<br />DATE|REPLACES<br />(CODE,<br />REVISION)|
|01|Initial edition|22/02/2024|N/A|
|02|Change in Spika's departments|02/06/2025|PNT-027.01|

Page 2 of 16

|Col1|Computerized Systems<br />Development Life Cycle (SDLC)|Code: PNT-027.02|
|---|---|---|
||Computerized Systems<br />Development Life Cycle (SDLC)|Effective date: 02/06/2025|

## Content
1. Objective 2. Scope
3. Responsibilities and Departments affected 4. Definitions and Acronyms
5. Procedure 5.1. Generalities
5.2. Software Classification 5.3. Planning
5.3.1. Software requirements analysis.
5.4. Design 5.5. Construction and coding
5.6. Tests 5.7. Operation and Maintenance
5.7.1. Maintenance plan 6. Distribution of Procedure
7. Annexes 8. Related documentation
9. Formation Software Classification
Page 3 of 16

|Col1|Computerized Systems<br />Development Life Cycle (SDLC)|Code: PNT-027.02|
|---|---|---|
||Computerized Systems<br />Development Life Cycle (SDLC)|Effective date: 02/06/2025|

## **1. Aim**
The objective of this procedure is to describe the process of the Computerized Systems Development Life Cycle, hereinafter SDLC, _in English_, Software Development Life Cycle,
including the software validation life cycle, in Spika Tech, hereinafter SPIKA.
## **2. Scope**
This SDLC process is applied to software developed at Spika to comply with regulations applicable to medical devices, as well as customer requirements, ensuring that the user
meets the stated requirements. This ensures compliance with Spika's quality system.
## **3. Responsibilities and Departments Affected**
The research and development department is responsible for managing and documenting the life cycle of the systems developed by Spika.
The Technical Manager is responsible for overseeing the management of generated documents, as well as safeguarding them and maintaining copies. He or she will also be
responsible for monitoring compliance with this procedure.
The affected departments are:
Page 4 of 16

|Department|Apply|Col3|
|---|---|---|
|Department|Yeah|No|
|Address|☒|☐|
|Environment|`☒`|`☐`|
|Quality Assurance|☒|☐|
|Systems and Cybersecurity|☒|☐|
|Research and Development|☒|☐|
|Marketing and Sales|☒|☐|

|Col1|Computerized Systems<br />Development Life Cycle (SDLC)|Code: PNT-027.02|
|---|---|---|
||Computerized Systems<br />Development Life Cycle (SDLC)|Effective date: 02/06/2025|

## **4. Definitions and Acronyms** • Software element : any identifiable part of a computer program, for example, source
code, object code, control code, control data, or a set of these elements.
## • Release : A particular version of a configuration item that is made available for a
specific purpose.
## • SDLC: Software Development Lyfe Cycle. 5. Procedure **5.1. Generalities**
This procedure will provide controls over the system lifecycle and software documentation, and aims to control the following points:
## • Configuration • Exchange controls • Version control • Record Retention • Information management • Incident management • Periodic review • Approval/Release
The following diagram summarizes the phases of the life cycle:
Page 5 of 16

|Col1|Computerized Systems<br />Development Life Cycle (SDLC)|Code: PNT-027.02|
|---|---|---|
||Computerized Systems<br />Development Life Cycle (SDLC)|Effective date: 02/06/2025|

The generated documentation must be approved by a team that includes a representative with knowledge of regulatory standards and a quality representative, who must review and
approve key stages of the project.
The documentation that will be used to implement the SDLC process may be the following, always depending on the criticality of the product:
## • Validation Plan (VP): This will incorporate the results of the risk assessment and the
validation phases, including their strategy, milestones, roles and responsibilities, and security classification. The plan must define the software development lifecycle or
model to be followed.
## • User Requirements (URS): Describes the requirements that the user needs to solve a
problem or achieve objectives.
## • Design Documentation (DQ) : The document content describes elements such as
logical, control, and data structures, error messages, system configurations, security features, etc.
## • Installation Qualification (IQ): Documents the installation, configuration, and
qualification instructions for hardware and software, including middleware, to demonstrate that all of these items can perform the functions required by the
application software.
Page 6 of 16

|Col1|Computerized Systems<br />Development Life Cycle (SDLC)|Code: PNT-027.02|
|---|---|---|
||Computerized Systems<br />Development Life Cycle (SDLC)|Effective date: 02/06/2025|

## • Test environment: This environment, separate from the production environment,
ensures data independence and stability, in anticipation of errors.
## • Validation test documentation: These are organized as follows, with special care being
taken between phases and respecting the order of execution. With validation tests carried out under a protocol duly approved before their execution by the evaluation
team, the activities will be documented to demonstrate the processes, methods, and data used in the structural and functional evaluation of the system.
The order of execution will be:
Installation Qualification (IQ  Operation Qualification  OQ)
Performance Qualification (PQ 
## • System Installation and Implementation: Provides technical details and instructions on
how to put the system into operation.
## • Instructions for use : Describes information with instructions for use and operation. **5.2. Software classification**
In the classification phase, the software's safety must be identified based on the risk of harm to the patient. The software will be identified as Safety Class A, B, or C, as follows:

|CLASSIFICATION|EFFECTS OF DAMAGE|
|---|---|
|TO|You cannot contribute to a dangerous situation.|
|TO|It may contribute to a hazardous situation that does not result in an<br />unacceptable risk after considering the external risk control<br />measures applied.|
|B|It may contribute to a hazardous situation resulting in an<br />unacceptable risk after considering the external risk control<br />measures applied and the resulting potential harm is a NON-<br />SERIOUS injury.|

Page 7 of 16

|Col1|Computerized Systems<br />Development Life Cycle (SDLC)|Code: PNT-027.02|
|---|---|---|
||Computerized Systems<br />Development Life Cycle (SDLC)|Effective date: 02/06/2025|

Below is a decision diagram for software classification and during the requirements gathering and development of software, the classification of the software must be documented
following the scheme and argumentation included in Annex 1. If such classification does not exist, the software will be taken by default as class C. Once sufficient documentation exists,
the corresponding class may be assigned.
Page 8 of 16

|Col1|Computerized Systems<br />Development Life Cycle (SDLC)|Code: PNT-027.02|
|---|---|---|
||Computerized Systems<br />Development Life Cycle (SDLC)|Effective date: 02/06/2025|

Page 9 of 16

|Col1|Computerized Systems<br />Development Life Cycle (SDLC)|Code: PNT-027.02|
|---|---|---|
||Computerized Systems<br />Development Life Cycle (SDLC)|Effective date: 02/06/2025|

## **5.3. Planning**
In the planning phase, the use of the system and the documentation required for the SDLC are identified. At this point, a risk management study can be used to determine the scope and
extent of testing and associated documentation. The scope and depth of testing and phases may be condensed or omitted, with due justification.
In this phase, the URS are developed. The following points must also be addressed:
## • The processes to be used in the development of the system, existing or new
processes.
## • The deliverables, including the documentation to be generated, activities and tasks • Traceability between system requirements, software requirements, software system
testing, and risk control measures
## • Software configuration and change management • Software troubleshooting to handle problems detected in products and activities at
each stage of the lifecycle.
**5.3.1.** **Analysis of software requirements.**
For each software system, the manufacturer must define and document the system requirements, which must include the following points:

|REQUIREMENTS|DESCRIPTION/EXAMPLE|
|---|---|
|Functional and capacity requirements|Functions<br />(purpose),<br />physical<br />characteristics (code language, platform,<br />operating system), computing environment<br />(hardware, memory size), need for support<br />for enhancements.|
|Entrances and exits|Data characteristics, ranges, limits and<br />default values.|
|Interfaces between the system and other<br />systems|If applicable|
|Alarms|Software-driven operator warnings and<br />messages|

Page 10 of 16

|Col1|Computerized Systems<br />Development Life Cycle (SDLC)|Code: PNT-027.02|
|---|---|---|
||Computerized Systems<br />Development Life Cycle (SDLC)|Effective date: 02/06/2025|

|REQUIREMENTS|DESCRIPTION/EXAMPLE|
|---|---|
|Safety requirements|Authentication,<br />authorization,<br />auditing,<br />communication integrity|
|Fitness-for-use engineering requirements<br />that are sensitive to human error and<br />training|Support for manual operations, human-<br />machine interactions, staff coercion, and<br />highlighting areas of people's attention|
|Data definition and database requirements|Form, fit and function|
|Software<br />installation<br />and<br />acceptance<br />requirements|N/A|
|Requirements relating to operating and<br />maintenance methods|N/A|
|User documentation to be developed|Manual|
|User maintenance requirements|N/A|
|Regulatory requirements|N/A|

## **5.4. Design**
The design phase includes software design specifications that describe how the software should function. That is, software requirements must be translated into a documented
architecture that describes the software structure and identifies its elements. The implementation process and how risks can be mitigated by mapping user requirements to
the developed design functionalities are discussed.
Design specifications related to:
## • System architecture: hardware, software, communications, security, etc.
requirements.
## • Database: Logical and physical representation of data definitions, critical components,
security, and database size.
## • Interfaces: including user interfaces, navigation, and report design.
Page 11 of 16

|Col1|Computerized Systems<br />Development Life Cycle (SDLC)|Code: PNT-027.02|
|---|---|---|
||Computerized Systems<br />Development Life Cycle (SDLC)|Effective date: 02/06/2025|

## **5.5. Construction and coding**
In this phase, the system design is implemented in source code and configuration settings for use by the end customer. It is desirable to develop the testing protocols to be performed
in this phase to verify proper operation.
## **5.6. Evidence**
The testing phase verifies that the system operates according to the approved specifications in a test environment. The manufacturer must establish and perform a set of tests with a
pass/fail criterion to ensure all software requirements are met.
Testing includes software exercises under known conditions and documented results. All detected issues must be logged, reviewed, and addressed before the product is put into
service. At this point, the design, installation, operation, and performance qualification protocols will be used.
The tests are documented in detail, highlighting the maximum possible data value, such as screenshots, and always identifying who performed them, when they were performed, and a
list of any anomalies found.
If changes are to be made after testing, in order to correct errors/anomalies, tests should be repeated, modified or additional tests performed, as appropriate, in the same way verifying
that undesirable side effects have not been included by a change and where applicable reviewing the corresponding risk management activities.
## **5.7. Operation and Maintenance**
During the operation and maintenance phase, the software is in the production environment and all changes to be made must be managed under a regulated change control system; see
PNT-005 Change Control Management.
"software release" will occur, where the manufacturer must ensure that the software verification has been completed and that the results have been evaluated before release. The
version of the software being released must be clearly indicated.
The manufacturer must establish procedures to ensure that the released product or software can be delivered at the point of use without distortion or unauthorized changes. These
procedures must address the production and handling of media containing software, including, where applicable, the following points:
## • Replication
Page 12 of 16

|Col1|Computerized Systems<br />Development Life Cycle (SDLC)|Code: PNT-027.02|
|---|---|---|
||Computerized Systems<br />Development Life Cycle (SDLC)|Effective date: 02/06/2025|

## • Labeled • Storage • Supply
**5.7.1.** **Maintenance plan**
A software maintenance plan must be established to perform maintenance process activities and tasks. This plan must address the following:
## • Procedures for: Reception, documentation, evaluation, resolution and follow-up. • Criteria for determining whether returns (see complaints) are considered a problem,
see PNT-007 Complaints Management
## • Using the risk management process • Using the problem resolution process, see PNT-004 Nonconformity Management • Using the Configuration Management Process • Procedures for improvements, troubleshooting, fixes, and obsolescence.
Of information returns that occur after release.
In this phase, a backup or disaster recovery plan, as well as an incident and periodic monitoring system, are essential.
## **6. Distribution of the Procedure**
Staff members in the departments listed in Section 3 (Responsibilities and Affected Departments) must be provided with a copy of this procedure. In addition, controlled copy No.
1 will be submitted to the Archives for paper archiving.
Controlled copies to be issued:

|Controlled Copy No.|Departments|
|---|---|
|1|Archive|

## **7. Annexes**
Page 13 of 16

|Col1|Computerized Systems<br />Development Life Cycle (SDLC)|Code: PNT-027.02|
|---|---|---|
||Computerized Systems<br />Development Life Cycle (SDLC)|Effective date: 02/06/2025|

## **8. Related documentation**

|Code|QUALIFICATION|
|---|---|
|N/A|ISO 13485|
|N/A|Regulation 2017/745|
|N/A|UNE-EN 62304|
|SGC-004|Non-conformity management|
|SGC-007|Claims management|

## **9. Training**
This version requires that the affected departments indicated in section 3 receive the training indicated below:

|Mark with<br />an X|Type of training|
|---|---|
|☒|Theoretical(reading and understanding of the procedure)|
|☐|Theoretical – Practical(If you select this option,contact the Responsible<br />Technician)|

Page 14 of 16

|Col1|Computerized Systems<br />Development Life Cycle (SDLC)|Code: PNT-027.02|
|---|---|---|
||Computerized Systems<br />Development Life Cycle (SDLC)|Effective date: 02/06/2025|

## **Software classification**
Annex 1_VERSION_02

|SOFTWARE CLASSIFICATION|Col2|Col3|Col4|
|---|---|---|---|
|SECURITY EVALUATION|SECURITY EVALUATION|SECURITY EVALUATION|SECURITY EVALUATION|
|Description||||
|Intended use||||
|Ask|Answer|Answer|Justification|
|Ask|Yeah|No|No|
|1. Can the software<br />produce<br />a <br />dangerous situation<br />due to a system<br />failure?|☐|☐||
|2. Is software failure<br />an<br />unacceptable<br />risk? (see note 1)|☐|☐||
|3. Does the software<br />failure cause non-<br />serious injury? (see<br />note 2)|☐|☐||
|4.Does the software<br />failure<br />cause<br />SERIOUS injury?|☐|☐||

_NOTE 1: 2. If you answer yes, continue to point 3._ _NOTE 2: 3. If you answer yes, you have finished the questionnaire, if you answer no, continue to_
_question 4._ Page 15 of 16

|Col1|Computerized Systems<br />Development Life Cycle (SDLC)|Code: PNT-027.02|
|---|---|---|
||Computerized Systems<br />Development Life Cycle (SDLC)|Effective date: 02/06/2025|

ANNEX 1/02

|BOTTOM LINE|Col2|TO|☐|B|☐|Col7|C|☐|
|---|---|---|---|---|---|---|---|---|
|Justification:|Justification:||||||||
|Reviewed by:|Signature:|Signature:|Signature:|Signature:|Signature:|Date:|Date:|Date:|
|Approved by:|Signature:|Signature:|Signature:|Signature:|Signature:|Date:|Date:|Date:|

Page 16 of 16