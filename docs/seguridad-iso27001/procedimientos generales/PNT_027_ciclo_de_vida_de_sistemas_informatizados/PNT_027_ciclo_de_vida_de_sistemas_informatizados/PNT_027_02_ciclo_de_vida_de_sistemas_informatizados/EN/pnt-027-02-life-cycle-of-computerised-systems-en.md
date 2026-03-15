Computerized Systems Development Life Cycle (SDLC)

| Function:   | Prepared by:      | Reviewed by:              | Approved by:      |
|-------------|-------------------|---------------------------|-------------------|
| Department: | Quality Assurance | Systems and cybersecurity | Quality Assurance |
| Name:       | Ivan Perez        | David Pozo                | Fernando Pozo     |
| Signature:  |                   |                           |                   |
| Date:       |                   |                           |                   |

| Valid until: | 02/06/2028 |
|--------------|------------|

| **DOCUMENT HISTORY** |                               |                    |                               |
|----------------------|-------------------------------|--------------------|-------------------------------|
| **VERSION**          | **CAUSES OF MODIFICATION**    | **EFFECTIVE DATE** | **REPLACES (CODE, REVISION)** |
| 01                   | Initial edition               | 22/02/2024         | N/A                           |
| 02                   | Change in Spika's departments | 02/06/2025         | PNT-027.01                    |

# Content

[1.](#aim) [Objective](#aim) [[4](#aim)](#aim)

[2.](#scope) [Scope](#scope) [[4](#scope)](#scope)

[3.](#responsibilities-and-departments-affected) [Responsibilities and
Departments affected](#responsibilities-and-departments-affected)
[[4](#responsibilities-and-departments-affected)](#responsibilities-and-departments-affected)

[4.](#definitions-and-acronyms) [Definitions and
Acronyms](#definitions-and-acronyms)
[[5](#definitions-and-acronyms)](#definitions-and-acronyms)

[5.](#procedure) [Procedure](#procedure) [[5](#procedure)](#procedure)

[5.1.](#generalities) [Generalities](#generalities)
[[5](#generalities)](#generalities)

[5.2.](#software-classification) [Software
Classification](#software-classification)
[[7](#software-classification)](#software-classification)

[5.3.](#planning) [Planning](#planning) [[10](#planning)](#planning)

[5.3.1.](#analysis-of-software-requirements.) [Software requirements
analysis.](#analysis-of-software-requirements.)
[[10](#analysis-of-software-requirements.)](#analysis-of-software-requirements.)

[5.4.](#design) [Design](#design) [[11](#design)](#design)

[5.5.](#construction-and-coding) [Construction and
coding](#construction-and-coding)
[[12](#construction-and-coding)](#construction-and-coding)

[5.6.](#evidence) [Tests](#evidence) [[12](#evidence)](#evidence)

[5.7.](#operation-and-maintenance) [Operation and
Maintenance](#operation-and-maintenance)
[[12](#operation-and-maintenance)](#operation-and-maintenance)

[5.7.1.](#maintenance-plan) [Maintenance plan](#maintenance-plan)
[[13](#maintenance-plan)](#maintenance-plan)

[6.](#distribution-of-the-procedure) [Distribution of
Procedure](#distribution-of-the-procedure)
[[13](#distribution-of-the-procedure)](#distribution-of-the-procedure)

[7.](#annexes) [Annexes](#annexes) [[14](#annexes)](#annexes)

[8.](#related-documentation) [Related
documentation](#related-documentation)
[[14](#related-documentation)](#related-documentation)

[9.](#training) [Formation](#training) [[14](#training)](#training)

[Software Classification](#software-classification-1)
[[15](#software-classification-1)](#software-classification-1)

# Aim

The objective of this procedure is to describe the process of the
Computerized Systems Development Life Cycle, hereinafter SDLC, *in
English* , Software Development Life Cycle, including the software
validation life cycle, in Spika Tech, hereinafter SPIKA.

# Scope

This SDLC process is applied to software developed at Spika to comply
with regulations applicable to medical devices, as well as customer
requirements, ensuring that the user meets the stated requirements. This
ensures compliance with Spika's quality system.

#  Responsibilities and Departments Affected

The research and development department is responsible for managing and
documenting the life cycle of the systems developed by Spika.

The Technical Manager is responsible for overseeing the management of
generated documents, as well as safeguarding them and maintaining
copies. He or she will also be responsible for monitoring compliance
with this procedure.

The affected departments are:

| Department                | Apply |     |
|---------------------------|-------|-----|
|                           | Yeah  | No  |
| Address                   | ☒     | ☐   |
| Environment               | ☒     | ☐   |
| Quality Assurance         | ☒     | ☐   |
| Systems and Cybersecurity | ☒     | ☐   |
| Research and Development  | ☒     | ☐   |
| Marketing and Sales       | ☒     | ☐   |
| Management                | ☒     | ☐   |

# Definitions and Acronyms

- Software element : any identifiable part of a computer program,
  for example, source code, object code, control code, control data, or
  a set of these elements.

- Release : A particular version of a configuration item that is
  made available for a specific purpose.

- SDLC: Software Development Lyfe Cycle.

# Procedure

# Generalities

This procedure will provide controls over the system lifecycle and
software documentation, and aims to control the following points:

- Configuration

- Exchange controls

- Version control

- Record Retention

- Information management

- Incident management

- Periodic review

- Approval/Release

The following diagram summarizes the phases of the life cycle:


style="width:6.69236in;height:3.70278in" />

The generated documentation must be approved by a team that includes a
representative with knowledge of regulatory standards and a quality
representative, who must review and approve key stages of the project.

The documentation that will be used to implement the SDLC process may be
the following, always depending on the criticality of the product:

- **Validation Plan (VP):** This will incorporate the results of the
  risk assessment and the validation phases, including their strategy,
  milestones, roles and responsibilities, and security classification.
  The plan must define the software development lifecycle or model to be
  followed.

- **User Requirements (URS):** Describes the requirements that the user
  needs to solve a problem or achieve objectives.

- **Design Documentation (DQ)** : The document content describes
  elements such as logical, control, and data structures, error
  messages, system configurations, security features, etc.

- **Installation Qualification (IQ):** Documents the installation,
  configuration, and qualification instructions for hardware and
  software, including middleware, to demonstrate that all of these items
  can perform the functions required by the application software.

- **Test environment:** This environment, separate from the production
  environment, ensures data independence and stability, in anticipation
  of errors.

- **Validation test documentation:** These are organized as follows,
  with special care being taken between phases and respecting the order
  of execution. With validation tests carried out under a protocol duly
  approved before their execution by the evaluation team, the activities
  will be documented to demonstrate the processes, methods, and data
  used in the structural and functional evaluation of the system.

The order of execution will be:

> **Installation Qualification (IQ )**
>
> **Operation Qualification ( OQ)**
>
> **Performance Qualification (PQ )**

- **System Installation and Implementation:** Provides technical details
  and instructions on how to put the system into operation.

- **Instructions for use** : Describes information with instructions for
  use and operation.

# Software classification

In the classification phase, the software's safety must be identified
based on the risk of harm to the patient. The software will be
identified as Safety Class A, B, or C, as follows:

| **CLASSIFICATION** | **EFFECTS OF DAMAGE**                                                                                                                                                                               |
|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TO                 | You cannot contribute to a dangerous situation.                                                                                                                                                     |
|                    | It may contribute to a hazardous situation that does not result in an unacceptable risk after considering the external risk control measures applied.                                               |
| B                  | It may contribute to a hazardous situation resulting in an unacceptable risk after considering the external risk control measures applied and the resulting potential harm is a NON-SERIOUS injury. |
| C                  | You may contribute to a dangerous situation that results in an unacceptable risk after considering external risk control measures and the resulting potential harm is SERIOUS injury.               |

Below is a decision diagram for software classification and during the
requirements gathering and development of software, the classification
of the software must be documented following the scheme and
argumentation included in **Annex 1.** If such classification does not
exist, the software will be taken by default as class C. Once sufficient
documentation exists, the corresponding class may be assigned.

# Planning 

In the planning phase, the use of the system and the documentation
required for the SDLC are identified. At this point, a risk management
study can be used to determine the scope and extent of testing and
associated documentation. The scope and depth of testing and phases may
be condensed or omitted, with due justification.

In this phase, the URS are developed. The following points must also be
addressed:

- The processes to be used in the development of the system, existing or
  new processes.

- The deliverables, including the documentation to be generated,
  activities and tasks

- Traceability between system requirements, software requirements,
  software system testing, and risk control measures

- Software configuration and change management

- Software troubleshooting to handle problems detected in products and
  activities at each stage of the lifecycle.

# Analysis of software requirements.

For each software system, the manufacturer must define and document the
system requirements, which must include the following points:

| REQUIREMENTS                                                                            | DESCRIPTION/EXAMPLE                                                                                                                                                          |
|-----------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Functional and capacity requirements                                                    | Functions (purpose), physical characteristics (code language, platform, operating system), computing environment (hardware, memory size), need for support for enhancements. |
| Entrances and exits                                                                     | Data characteristics, ranges, limits and default values.                                                                                                                     |
| Interfaces between the system and other systems                                         | If applicable                                                                                                                                                                |
| Alarms                                                                                  | Software-driven operator warnings and messages                                                                                                                               |
| Safety requirements                                                                     | Authentication, authorization, auditing, communication integrity                                                                                                             |
| Fitness-for-use engineering requirements that are sensitive to human error and training | Support for manual operations, human-machine interactions, staff coercion, and highlighting areas of people's attention                                                      |
| Data definition and database requirements                                               | Form, fit and function                                                                                                                                                       |
| Software installation and acceptance requirements                                       | N/A                                                                                                                                                                          |
| Requirements relating to operating and maintenance methods                              | N/A                                                                                                                                                                          |
| User documentation to be developed                                                      | Manual                                                                                                                                                                       |
| User maintenance requirements                                                           | N/A                                                                                                                                                                          |
| Regulatory requirements                                                                 | N/A                                                                                                                                                                          |

# Design

The design phase includes software design specifications that describe
how the software should function. That is, software requirements must be
translated into a documented architecture that describes the software
structure and identifies its elements. The implementation process and
how risks can be mitigated by mapping user requirements to the developed
design functionalities are discussed.

Design specifications related to:

- System architecture: hardware, software, communications, security,
  etc. requirements.

- Database: Logical and physical representation of data definitions,
  critical components, security, and database size.

- Interfaces: including user interfaces, navigation, and report design.

# Construction and coding

In this phase, the system design is implemented in source code and
configuration settings for use by the end customer. It is desirable to
develop the testing protocols to be performed in this phase to verify
proper operation.

# Evidence

The testing phase verifies that the system operates according to the
approved specifications in a test environment. The manufacturer must
establish and perform a set of tests with a pass/fail criterion to
ensure all software requirements are met.

Testing includes software exercises under known conditions and
documented results. All detected issues must be logged, reviewed, and
addressed before the product is put into service. At this point, the
design, installation, operation, and performance qualification protocols
will be used.

The tests are documented in detail, highlighting the maximum possible
data value, such as screenshots, and always identifying who performed
them, when they were performed, and a list of any anomalies found.

If changes are to be made after testing, in order to correct
errors/anomalies, tests should be repeated, modified or additional tests
performed, as appropriate, in the same way verifying that undesirable
side effects have not been included by a change and where applicable
reviewing the corresponding risk management activities.

# Operation and Maintenance

During the operation and maintenance phase, the software is in the
production environment and all changes to be made must be managed under
a regulated change control system; see **PNT-005 Change Control
Management.**

**"software release"** will occur , where the manufacturer must ensure
that the software verification has been completed and that the results
have been evaluated before release. The version of the software being
released must be clearly indicated.

The manufacturer must establish procedures to ensure that the released
product or software can be delivered at the point of use without
distortion or unauthorized changes. These procedures must address the
production and handling of media containing software, including, where
applicable, the following points:

- Replication

- Labeled

- Storage

- Supply

# Maintenance plan

A software maintenance plan must be established to perform maintenance
process activities and tasks. This plan must address the following:

- Procedures for: Reception, documentation, evaluation, resolution and
  follow-up.

- Criteria for determining whether returns (see complaints) are
  considered a problem, see **PNT-007 Complaints Management**

- Using the risk management process

- Using the problem resolution process, see **PNT-004 Nonconformity
  Management**

- Using the Configuration Management Process

- Procedures for improvements, troubleshooting, fixes, and obsolescence.

Of information returns that occur after release.

In this phase, a backup or disaster recovery plan, as well as an
incident and periodic monitoring system, are essential.

# Distribution of the Procedure

Staff members in the departments listed in Section 3 (Responsibilities
and Affected Departments) must be provided with a copy of this
procedure. In addition, controlled copy No. 1 will be submitted to the
Archives for paper archiving.

Controlled copies to be issued:

| **Controlled Copy No.** | **Departments** |
|-------------------------|-----------------|
| 1                       | Archive         |

# Annexes

| **NO. / REV.** | **QUALIFICATION**       |
|----------------|-------------------------|
| 1/01           | Software classification |

# Related documentation

| **Code** | **QUALIFICATION**         |
|----------|---------------------------|
| N/A      | ISO 13485                 |
| N/A      | Regulation 2017/745       |
| N/A      | UNE-EN 62304              |
| SGC-004  | Non-conformity management |
| SGC-007  | Claims management         |

# Training

This version requires that the affected departments indicated in section
3 receive the training indicated below:

| **Mark with an X** | **Type of training**                                                                               |
|--------------------|----------------------------------------------------------------------------------------------------|
| ☒                  | **Theoretical** (reading and understanding of the procedure)                                       |
| ☐                  | **Theoretical – Practical** (If you select this option, contact the Responsible Technician) |

# 

**Annex 1_VERSION_02**

# Software classification

| **SOFTWARE CLASSIFICATION**                                                 |            |     |        |                   |
|-----------------------------------------------------------------------------|------------|-----|--------|-------------------|
| **SECURITY EVALUATION**                                                     |            |     |        |                   |
| **Description**                                                             |            |     |        |                   |
| **Intended use**                                                            |            |     |        |                   |
| **Ask**                                                                     | **Answer** |     |        | **Justification** |
|                                                                             | **Yeah**   |     | **No** |                   |
| 1\. Can the software produce a dangerous situation due to a system failure? | ☐          |     | ☐      |                   |
| 2\. Is software failure an unacceptable risk? (see note 1)                  | ☐          |     | ☐      |                   |
| 3\. Does the software failure cause non-serious injury? (see note 2)        | ☐          |     | ☐      |                   |
| 4.Does the software failure cause SERIOUS injury?                           | ☐          |     | ☐      |                   |

*NOTE 1: 2. If you answer yes, continue to point 3.*

*NOTE 2: 3. If you answer yes, you have finished the questionnaire, if
you answer no, continue to question 4.*

*  
*

**ANNEX 1/02**

| **BOTTOM LINE**    |            | **TO** | ☐   | **B** | ☐   |       | **C** | ☐   |
|--------------------|------------|--------|-----|-------|-----|-------|-------|-----|
| **Justification:** |            |        |     |       |     |       |       |     |
| **Reviewed by:**   | Signature: |        |     |       |     | Date: |       |     |
| **Approved by:**   | Signature: |        |     |       |     | Date: |       |     |