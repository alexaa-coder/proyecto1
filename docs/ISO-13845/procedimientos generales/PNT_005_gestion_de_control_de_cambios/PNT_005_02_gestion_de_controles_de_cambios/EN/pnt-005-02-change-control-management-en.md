---
id: pnt_005_02_change_control_management_en
title: "Pnt 005 02 Change Control Management En"
sidebar_label: "Pnt 005 02 Change Control Management En"
---

CHANGE CONTROL MANAGEMENT Aim
The objective of this procedure is to define Spika Tech's (hereinafter SPIKA) strategy and requirements for change management, in order to prevent uncontrolled and unevaluated changes that could negatively affect the safety and quality of the products manufactured by SPIKA.
Good change control management ensures that all departments involved in processes take the necessary precautions to ensure these changes are properly evaluated, documented, approved, and implemented.
Scope This procedure applies to all planned or unplanned changes that may affect the product developed, used or maintained by the organization, including:
Source code, algorithms and functional logic.
Architecture, modules and system components.
Software documentation (requirements, specifications, validations, etc.).
Support systems (IT infrastructure, databases, APIs...).
Development or testing tools that impact product quality.
Elements of the quality management system that affect the software lifecycle (e.g., procedures, templates, key configurations).
Responsibilities and Departments Affected All SPIKA staff must manage changes in their area and are responsible for adhering to the guidelines of this procedure.
The Responsible Technician will ensure compliance with this procedure.
The affected departments are those indicated in the following table:
Definitions and Acronyms Change: Any planned addition, modification, replacement, or elimination, whether temporary or permanent, to an established standard. This includes processes, specifications, source code, software components, services, or documentation related to the software quality management system.
Temporary change: A change that, after a defined period of time, reverts to the previous state. It is used when the change is justified for a specific situation. Its duration, follow-up, and reversion mechanisms must be recorded.
Change Control : A formal process by which qualified personnel review, evaluate, approve, and document changes that may impact the security, performance, regulatory compliance, or traceability of a software product or quality system. Its objective is to ensure that the system remains compliant and valid after the change is implemented.
CC: Change Control Procedure
Introduction Proper management of the change control process is considered a fundamental pillar of the Quality Management System. This procedure ensures that any planned modification to the product, technological infrastructure, associated processes, or relevant documentation is evaluated, approved, and documented in a structured manner, guaranteeing regulatory compliance, safety, and the effectiveness of the system.
This procedure establishes the phases required for change management, from its inception to its full implementation. It is divided into three main stages , each with defined activities and responsibilities:
Phase I Proposal and description of the change Phase II Evaluation and Approval
Phase III Implementation and closure Classification of changes
Major Change : This refers to significant modifications that affect the core functionality, architecture, design, or overall scope of the system/project. This type of change requires a comprehensive approach to ensure quality and compliance.
Minor Change : Includes minor modifications that affect existing functionality, but without significantly altering the overall behavior of the system. These changes have a more limited impact and require focused evaluation .
Patch Change : It includes modifications focused exclusively on correcting specific errors or problems without altering the functionality of the system or its general behavior.
Coding exchange controls Each change control will be identified with a unique number automatically assigned by the Jira software, as follows:
CC – XX Where:
CC stands for Change Control XX 2-digit consecutive number
Phase I: proposal and description of the change Once the need for a change has been identified, the change requester must initiate the request directly in Jira. The requester is responsible for detailing the reason for the change, as well as the implications of its implementation.
In Jira, the requester will complete the necessary fields to describe the change, its justification, and a description of the expected impact. Once this information is completed, the change will be logged and ready for initial assessment.
Phase II: evaluation and approval Depending on the type of change, the following evaluation must be carried out:
Major Change:
Functionality Check: All product functionalities must be re-verified to ensure they operate correctly and meet the specified requirements.
Risk analysis: It is essential to assess the risks associated with the change and update existing analyses to mitigate potential impacts.
Regulatory Compliance Assessment: Confirm that the product continues to comply with applicable regulations, as these changes could affect compliance.
Minor Change :
Functionality Check: Validate that the adjusted or modified functionalities operate correctly and that there are no collateral impacts.
Risk analysis: Review whether the change introduces new risks or affects existing ones, and update the corresponding documentation.
Patch Change :
Functionality check: Validate that the corrected error is resolved and that the affected areas are functioning properly. A thorough analysis outside the scope of the change is not required.
Phase III: Classification and approval of the change In this phase, once the change has been approved, it is implemented with the goal of releasing a new version of the affected product. All tasks required to execute the change must be properly planned, assigned, and monitored in Jira.
During this stage, the technical team will be responsible for coordinating the execution of the plan, including activities such as development, testing, internal validation, generation of updated documentation, and communication to users or clients, if applicable.
Once the change has been implemented, the corresponding version number should be recorded in Jira, along with a brief description of the changes included. Successful implementation should also be documented, identifying any deviations or issues that arose during the process.
The version will be considered finalized and closed in Jira when:
All tasks are completed and verified.
The result of the change has been properly documented.
The product version has been updated and is available to users or production.
Modifications to the initial proposal If for any reason the initial proposal for the change changes, that change will be cancelled and a new one will have to be opened.
List of change controls All change controls will be recorded and managed through the Jira dashboard, where the complete change history can be viewed at any time. In the project's Issues section , a list of all generated change controls will automatically appear, along with their unique identifiers, statuses, responsible parties, key dates, change types, and any relevant associated information. This digital record replaces manual listings and ensures traceability, review, and oversight.
Distribution of the Procedure Staff members in the departments listed in Section 3 (Responsibilities and Affected Departments) must be provided with a copy of this procedure. In addition, controlled copy No. 1 will be submitted to the Archives for paper archiving.
Controlled copies to be issued:
Related documentation Training
This version requires that the affected departments indicated in section 3 receive the training indicated below:

| Function: | Prepared by: | Reviewed by: | Approved by: |
| Department: | Quality Assurance | Systems and cybersecurity | Quality Assurance |
| Name: | Ivan Perez | David Pozo | Fernando Pozo |
| Signature: |  |  |  |
| Date: |  |  |  |

| Valid until: | 02/06/2025 |

| DOCUMENT HISTORY | DOCUMENT HISTORY | DOCUMENT HISTORY | DOCUMENT HISTORY |
| VERSION | CAUSES OF MODIFICATION | EFFECTIVE DATE | REPLACES (Code, Revision) |
| 01 | Initial edition | 02/14/2024 | N/A |
| 02 | Change in Spika's departments. Adaptation to a digital format. | 02/06/2025 | PNT-005.01 |

| Department | Apply | Apply |
| Department | Yeah | No |
| Address |  |  |
| Environment |  |  |
| Quality Assurance |  |  |
| Systems and Cybersecurity |  |  |
| Research and Development |  |  |
| Marketing and Sales |  |  |
| Management |  |  |

| Controlled Copy No. | Departments |
| 1 | Archive |

| Code | QUALIFICATION |
| MQ-01 | Quality Manual |

| Mark with an X | Type of training |
|  | Theoretical (reading and understanding of the procedure) |
|  | Theoretical – Practical (If you select this option, contact the Responsible Technician) |