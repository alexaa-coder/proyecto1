---
id: pnt_026_04_design_and_development_en
title: "Pnt 026 04 Design And Development En"
sidebar_label: "Pnt 026 04 Design And Development En"
---

DESIGN AND DEVELOPMENT Aim
This procedure describes the process followed by Spika Tech, hereinafter SPIKA, to indicate how quality requirements related to product design and development are managed, ensuring compliance with specific design requirements (internal and regulatory) and ensuring that the transfer to the actual production process is appropriate for the product's intended use. Documentation of all stages of the process will ensure adequate data traceability, defined responsibilities, and the availability of the necessary resources.
Scope This procedure applies to the design and development stages of products developed and distributed by SPIKA.
This procedure applies to both the design of new products and the modification of existing ones.
Responsibilities and Departments Affected The Technical Manager will be responsible for supervising the design system and ensuring that the product is produced in accordance with the implemented quality system.
The operations department will be responsible for leading the design and development process in proper coordination with the other departments or applicable personnel, all in accordance with the established quality system.
The affected departments are those indicated in the following table:
Definitions and Acronyms Design and development : Process that ensures the correct transfer from the initial defined requirements of a product to its final characteristics or specifications.
Design input: requirement that a product must meet to begin the design process Design output: The result of a product's design process that establishes the characteristics it meets (specifications).
Incident (Jira): It should be noted that Jira uses the term incident to name a task that involves a design (if applicable) and development (if applicable), which must be distinguished from a real incident, according to the definitions of PNT004 Non-conformity Management.
Procedure The design process has different phases that lead to the final product, as shown in the following diagram:
Product design and development follow-up meetings Throughout the product design and development process, follow-up meetings are held to review the work done by all SPIKA teams and establish guidelines for continuing product development.
Research phase This phase is considered an early investigation phase and does not require formal documentary records according to the organization's quality system. Records may be generated in laboratory notebooks or similar, but the elements required by the quality system are not required.
Design control phase The operations department will prepare a design control report/plan, which will be duly documented, ensuring appropriate control of the design and development process and meeting established quality objectives.
The entire product design control plan developed at SPIKA is stored in an online board in the Jira tool:
( https://spikatech.atlassian.net/jira/software/c/projects/VRC/boards/32?assignee=63c51264d7f68827e6b55719&assignee=63be96382a526608c54ff184&assignee=62a997d93eb34d00685f176d&assignee=632082c8ed8abffd7ffc9b4d &assignee=712020%3Acdc726be-ff96-453e-82e6-1efc1a3b1447&assignee=6310bdf3316bbc56c424972d&assignee=633a 86d1f568615bdc7fbd5c&assignee=712020%3A095a3094-46f9-4e78-831d-e57b9ce328b2&assignee=712020%3Ace5b65be-8 481-4065-bec3-61d9789428cd&assignee=63a03e026f068efec8f48577&assignee=70121%3A191eeba2-ab1f-4a53-be51-3 b9fb48bfe89&assignee=642ae918f1f740eb291ef12a&assignee=6364da49fc0cc7a600b11a73&assignee=712020%3A974baa 9e-d7d0-418e-a169-b4ac97d78cb0&assignee=70121%3Aec60de9c-c393-461d-b55d-71eb70530b50&assignee=63da2b4928cddcc70770ca2b&assignee=631713743e578bb3b5ffb524&assignee=712020%3Ac713154d-2fda-46cc-9d57-d5b0429f4b42 ), which helps the organization and management of development, in addition to the measurement of all development processes carried out within SPIKA thanks to the registration of all tasks that have been performed and the reports automatically generated from these tasks.
The first step to be taken by the development department is the creation of an incident (a task that involves a design (if applicable) and a development (if applicable)) within the product developed in SPIKA.
This incident meets the resolution of an identified user need or an improvement identified by the development department.
These incidents are documented as follows:
Name of the incident.
Incident description: Detailed description of the problem to be solved or the feature to be designed and developed.
Acceptance criteria: These outline the essential requirements and boundaries for the development of a feature. They include a specific, quantifiable checklist covering both functional and non-functional aspects, guiding development and testing. These criteria are essential for aligning team expectations and ensuring that a feature effectively meets its intended objectives.
Assignee: person in charge of the development described in the incident.
Informer: person responsible for monitoring, verifying and validating the development described in the incident.
Priority: order of priority that will be given to said incident within the development process.
User Requirements:
The analysis of the needs of potential product users will be evaluated as a preliminary step before initiating the development and design process. User requirements will be recorded in the Jira board, matching an issue with a potential user requirement.
Design Input Phase The design input phase is performed to translate user requirements (and others such as technical, functional, regulatory) into a series of requirements that must be validated prior to implementation and progress to the next phase (validation and verification phase (design output)).
Design input requirements will be recorded as specified in the previous point by creating issues in the Jira online tool.
Scope of design input The scope of the design is determined by a detailed description of each issue in the Jira tool, which provides a detailed explanation of the process to be carried out, including its expected impact on the final product. This comprehensive description ensures a clear and complete understanding of the tasks to be performed and their implications for the desired outcome.
Assessment of adequacy Reviewing the suitability of input requirements for design involves the designated issue reporter in the Jira tool thoroughly analyzing the acceptance criteria established in the corresponding issue description. This process ensures that the design requirements adequately align with the project's needs and expectations, thereby validating their alignment with the specific objectives outlined in the issue. Through this rigorous review, the consistency and quality of the work performed are ensured, and the possibility of deviations or discrepancies that may arise during product development is minimized.
Coding Entry requirements will be coded as AAA-xxx , where:
“ AAA ”: refers to the acronym of the product being developed.
“ xxx ”: is a consecutive number that begins with 01.
Design validation and verification (Design output)
The validation and verification phase will ensure that the product meets user requirements and its intended use. This phase will ensure that the development works correctly. To this end, the development team will mark the incident as "test" so that the assigned person can verify its correct implementation and functionality before transferring the development to the general software.
Design transfer phase During this phase, the transfer to the production process takes place. At this point, it is assumed that the incident has been resolved correctly, the development has been carried out successfully, and the incident QA has been responsible for verifying and validating the correct functioning of the new development.
With this in mind, the new development branch is transferred to the production branch using the transfer and merge tools provided by SPIKA's repository and project management site (Github).
Design changes Design changes can occur at any stage of development, and can be internal or external in origin;
Changes of internal origin: due to non-compliance with specifications, complaint investigations, improvement processes, etc.
Changes from external sources: due to customer communications, operation, post-marketing monitoring, scientific publications, changes in regulatory requirements, malfunctions, suggestions for improvement, etc.
All changes associated with the design and development control process, once this entire design and development process is completed and a final version of the product is achieved, will be managed according to the PNT-005 Change Control Management procedure .
Within the product, changes are classified as “ Major ”, “ Minor ” or “ Patch ”, based on their impact and the following requirements:
Major Change :
This refers to significant modifications that affect the core functionality, architecture, design, or overall scope of the system/project. This type of change requires a comprehensive approach to ensure quality and compliance:
Requirements:
Functionality Check: All product functionalities must be re-verified to ensure they operate correctly and meet the specified requirements.
Risk analysis: It is essential to assess the risks associated with the change and update existing analyses to mitigate potential impacts.
Regulatory compliance assessment: Confirm that the product continues to comply with applicable regulations, as these changes could affect compliance.
Impact on product version: Increases the first version number of the product. (Example: from 1.0.0 to 2.0.0).
Minor Change :
These include minor modifications that affect existing functionality without significantly altering the overall behavior of the system. These changes have a more limited impact and require focused evaluation:
Requirements:
Functionality Check: Validate that the adjusted or modified functionalities operate correctly and that there are no collateral impacts.
Risk analysis: Review whether the change introduces new risks or affects existing ones, and update the corresponding documentation.
Impact on product version: Increases the second version number of the product. (Example: from 1.0.0 to 1.1.0).
Patch Change :
It includes modifications focused exclusively on correcting specific errors or problems without altering the functionality of the system or its general behavior:
Requirements:
Functionality check: Validate that the corrected error is resolved and that the affected areas are functioning properly. A thorough analysis outside the scope of the change is not required.
Impact on product version: Increases the third version number of the product. (Example: from 1.0.0 to 1.0.1).
Risk Analysis Risk analyses that may be generated when necessary due to the characteristics of the product or the production process will take into account the intended use of the product and will primarily follow the FMEA (Failure Mode and Effects Analysis) method, according to the principles of procedure PNT-002 Risk Management. The risk analysis will consider all stages of the design and development process (plan, design input, design output, verification, validation, and design transfer).
Backups Backup frequency
Backups of the source code and data stored in the database must be stored securely, following a rigorous procedure. It is recommended that these backups be made daily at 4:00 p.m., ensuring that both the code and data are protected against potential loss or failure. Furthermore, it is essential to store backups in secure, redundant locations to ensure information recovery in the event of an emergency.
Backup method The method for performing these backups must be automated to avoid human error and ensure they are performed daily without fail. Backups are stored in the database hosted on the Google Firebase service, ensuring both data security and availability.
Verification and restoration In the event of a failure or loss of source code, the most recent backup copy will be accessed. Before restoring this copy, a thorough analysis is required to ensure its proper functioning. This analysis ensures that the restored copy is error-free and fully operational, thus minimizing the risk of additional problems.
Product labeling and packaging The information collected during the design process will determine the labeling and wording of the product's usage instructions according to the design history file.
Historical design file The Design History File (DHF) will contain records associated with internal and external design requirements, design verification, validation, and transfer, minutes of review team meetings, and all applicable technical documentation.
This design history can be found in the Jira software in the view of all issues associated with a project.
Distribution of the Procedure Staff members in the departments listed in Section 3 (Responsibilities and Affected Departments) must be provided with a copy of this procedure. In addition, controlled copy No. 1 will be submitted to the Archives for paper archiving.
Controlled copies to be issued:
Annexes Related documentation
Training This version requires that the affected departments indicated in section 3 receive the training indicated below:

| Function: | Prepared by: | Reviewed by: | Approved by: |
| Department: | Quality Assurance | Systems and cybersecurity | Quality Assurance |
| Name: | Ivan Perez | David Pozo | Fernando Pozo |
| Signature: |  |  |  |
| Date: |  |  |  |

| Valid until: | 02/06/2028 |

| DOCUMENT HISTORY | DOCUMENT HISTORY | DOCUMENT HISTORY | DOCUMENT HISTORY |
| VERSION | CAUSES OF MODIFICATION | EFFECTIVE DATE | REPLACES (CODE, REVISION) |
| 01 | Initial edition | 22/02/2024 | N/A |
| 02 | Rewriting the procedure to adapt to the reality of SPIKA TECH's design process, according to AC-045/24 | 10/05/2024 | PNT-026.01 |
| 03 | Definition of backups | July 15, 2024 | PNT-026.02 |
| 04 | Specification of the types of changes in the design, change in Spika departments | 02/06/2025 | PNT-027.03 |

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

| NO. / REV. | QUALIFICATION |
| 1/01 | User requirements |

| Code | QUALIFICATION |
| N/A | EN ISO 13485 (4.2.3 Medical device archiving) |
| N/A | Regulation (EU) 2017/745 on medical devices |
| PNT-002 | Risk Management |
| PNT -005 | Change Control Management |

| Mark with an X | Type of training |
|  | Theoretical (reading and understanding of the procedure) |
|  | Theoretical – Practical (If you select this option, contact the Responsible Technician) |