# Design Proposal

##  Table of Contents
1.	ER Diagram (Finalized)
2.	Mission Statement for Client
3.  Mission Objectives for Client
4.  Relational Schema
5.	Functional Dependencies	
6.  3 NF Normalization
7.  Sample Data
8.  Business Rules
9.  Referential Integrity

## 1. ER Diagram

![ERD](https://github.com/ankity09/learn/blob/master/Alumni_Database/images/Project0503-02_ERD.png)

## 2. Mission Statement for Client

The client’s mission is to provide an informational database for the alumni of the University of Maryland. The database will have alumni contact information, prior education history, current job detail, work experience and company. 

## 3. Mission Objectives for Client

1.	Provide a contact database for the alumni of the University of Maryland.
2.	Provide insight into University of Maryland alumni’s educational background.
3.	Provide insight into which companies their alumni are working at, and in what capacity.


## 4. Relational Schema

1.	Alumnus (**alumId**, alumFName, alumLName, alumGender, alumDob, contactId)
2.	Education (**schoolId**, schoolName, schoolType, schoolGradYear, schoolGPA, alumId)
3.	Company (**companyId**, companyName, companyLocation)
4.	JobDetails (**jobId**, jobDomain, jobTitle, companyId)
5.	ContactDetails (**contactId**, homePhone, workPhone, homeEmail, workEmail, workAddr)
6.	WorkIn (**alumId**, **companyId**, alumWorkEx)
7.	WorkAs (**alumId, jobId**)


## 5. Functional Dependencies

1.	alumId:arrow_right:alumFName, alumLName, alumGender, alumDOB
2.	companyId:arrow_right:companyName, companyLocation[…]
3.	jobId:arrow_right:jobDomain, jobTitle
4.	schoolId:arrow_right:schoolName,schoolType,schoolGradYear,schoolGPA
5.	contactId:arrow_right:homePhone,workPhone,homeEmail,workEmail,workAddr
6.	alumId, companyId:arrow_right:alumWorkEx


## 6. 3 NF Normalization

1.	Alumnus (**alumId**, alumFName, alumLName, alumGender, alumDob, contactId)
2.	Education (**schoolId**, schoolName, schoolType, schoolGradYear, schoolGPA, alumId)
3.	Company (**companyId**, companyName, companyLocation)
4.	JobDetails (**jobId**, jobDomain, jobTitle, companyId)
5.	ContactDetails (**contactId**, homePhone, workPhone, homeEmail, workEmail, workAddr)
6.	WorkIn (**alumId, companyId**, alumWorkEx)
7.	WorkAs (**alumId, jobId**)


## 7. Sample Data

Alumnus ('01', 'Victor', 'Smith', 'M', '04/21/1990','3001','2001')

Education ('4001', '01','JM High School', 'High School','2006','3.4')

Education ('4002','01', 'R H Smith', 'Graduate','2012','3.2')

JobDetails ('5001','2001','Healthcare', 'Analyst')

Company ('2001','Wecare','Dallas')

WorkIn ('01','2001','6')

ContactDetails ('3001', '01', '2408472901', '9876472565', 'vict@hotmail.com', 'victor.smith@wecare.com', '2240, 88th Street, Dallas')

WorkAs ('01','5001')


## 8. Business Rules

R1: When contact details are deleted from the database, the corresponding alumnus contact details are set to null.

R2: When contact details are changed in the database, the corresponding alumnus contact details are changed.

R3: When an alumnus has studied from a particular school and had grades and GPA, then that alumni cannot be deleted.

R4: When Alumni details are changed in the database, the corresponding education information should be updated accordingly.

R5: When company is deleted from the database, the corresponding job information for that company should also be deleted.

R6: When company status is changed in the database, the corresponding job information should be updated accordingly.

R7:  An alumnus cannot be deleted from the database, if the alumnus works in a company.

R8: If an alumnus information is changed in the database, the corresponding alumnus working in company information should be changed accordingly.

R9: A company cannot be deleted from the database, if an alumnus works in the company.

R10: If a company information is changed in the database, the corresponding alumnus working in hat company information should be changed accordingly.

R11: An alumnus cannot be deleted from the database, if the alumnus works a job.

R12: If an alumnus information is changed in the database, the corresponding alumnus working a job information should be changed accordingly.

R13: A job cannot be deleted from the database, if the alumnus works that job.

R14: If a job information is changed in the database, the corresponding alumnus working that job information should be changed accordingly.

## 9. Referential Integrity

| Relation | Foreign Key | Base Relation | Primary Key | Constraint: ON DELETE | Business Rule | Constraint: ON UPDATE | Business Rule |
|---|---|---|---|---|---|---|---|
| Alumnus | contactId | ContactDetails | contactId | SET NULL | R1 | CASCADE | R2 |
| Education | alumId | Alumnus | alumId | NO ACTION | R3 | CASCADE | R4 |
| JobDetails  | companyId | Company | companyId | CASCADE | R5 | CASCADE | R6 |
| WorkIn | alumId | Alumnus | alumId | NO ACTION | R7 | CASCADE | R8 |
| WorkIn | companyId | Company | companyId | NO ACTION | R9 | CASCADE | R10 |
| WorkAs | alumId | Alumnus | alumId | NO ACTION | R11 | CASCADE | R12 |
| WorkAs | jobId | JobDetails | jobId | NO ACTION | R13 | CASCADE | R14 |

