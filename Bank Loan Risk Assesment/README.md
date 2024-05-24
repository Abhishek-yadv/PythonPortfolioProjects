# Exploratory Data Analysis: Managing Risk in Lending

## Introduction

In this case study, we'll dive into the practical application of Exploratory Data Analysis (EDA) within the banking and financial services sector. The main focus will be on understanding how data analysis helps in managing risk when lending money to customers or simply reducing potential financial losses.

## Business Understanding

As per my experience with one of India's premier financial institutions, ICICI, I've observed that one of the key challenges for NBFCs or the BFSI sector is assessing the risk of lending to customers with insufficient or no credit history while taking care of their business. Some customers would take advantage of this situation and become defaulters, leading to financial losses for the bank.

It is crucial to analyze the patterns present in the data to ensure that loan applicants capable of repaying are not rejected while minimizing the risk of approving loans to potential defaulters.

When a customer applies for a loan, the company must decide whether to approve or reject the application based on the applicant's profile. Two risks are associated with this decision:

1. If the applicant is likely to repay the loan, but the loan is not approved, it results in a loss of business for the company.
2. If the applicant is unlikely to repay the loan (i.e., they are likely to default), approving the loan may lead to a financial loss for the company.

The available data contains information about loan applications, including two types of scenarios:

- Clients with payment difficulties: They had late payments for more than a specified number of days on at least one of the initial loan installments.
- All other cases: Payments were made on time.

The company can take one of four decisions regarding a loan application:

- Approved: The loan application is approved.
- Cancelled: The client cancelled the application during the approval process, either due to a change of mind or unfavorable pricing due to higher risk.
- Refused: The company rejected the loan application (e.g., the client did not meet the requirements).
- Unused offer: The loan was cancelled by the client at different stages of the process.

## Business Objectives

This case study aims to identify patterns which indicate if a client has difficulty paying their installments, which may be used for taking actions such as denying the loan, reducing the amount of loan, lending (to risky applicants) at a higher interest rate, etc. This will ensure that the consumers capable of repaying the loan are not rejected. Identification of such applicants using EDA is the aim of this case study.

In other words, the company wants to understand the driving factors (or driver variables) behind loan default, i.e., the variables which are strong indicators of default. The company can utilize this knowledge for its portfolio and risk assessment.

## Data Description

The data utilized in this analysis has been sourced from Kaggle.

- The file `application_data.csv` contains comprehensive client information at the time of application, particularly focusing on discerning if a client encounters payment difficulties.
- Additionally, the dataset `previous_application.csv` provides insights into the client's historical loan data, detailing whether past applications were approved, cancelled, refused, or resulted in an unused offer.
