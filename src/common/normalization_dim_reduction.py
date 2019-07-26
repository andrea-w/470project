"""
This script contains various functions that may be used to 
normalize certain data features, or to reduce the dimensionality
of the data by combining 2 or more features into 1.
"""

# takes dataframe as input @param data
# adds new column to dataframe representing total spending per student
# (calculates total_expenditure/enroll)
def spending_per_student(data):
    new_df = data.assign(Spend_per_Student = lambda x: x.TOTAL_EXPENDITURE/x.ENROLL)
    return new_df

# takes dataframe as input @param data
# adds new column to dataframe representing ratio of instruction spending over total expenditure
# (calculates instruction_expenditure/total_expenditure)
def instruction_spending_ratio(data):
    new_df = data.assign(Instruction_Spending_Ratio = lambda x: x.INSTRUCTION_EXPENDITURE/x.TOTAL_EXPENDITURE)
    return new_df

# takes dataframe as input @param data
# adds new column to dataframe representing ratio of support services expenditure over total expenditure
# (calculates support_services_expenditure/total_expenditure)
def support_services_spending_ratio(data):
    new_df = data.assign(Support_Services_Spending_Ratio = lambda x: x.SUPPORT_SERVICES_EXPENDITURE/x.TOTAL_EXPENDITURE)
    return new_df

# takes dataframe as input @param data
# adds new column to dataframe representing ratio of capital expenditure over total expenditure
# (calculates capital_expenditure/total_expenditure)
def capital_expenditure_ratio(data):
    new_df = data.assign(Capital_Expenditure_Ratio = lambda x: x.CAPITAL_OUTLAY_EXPENDITURE/x.TOTAL_EXPENDITURE if 'CAPITAL_OUTLAY_EXPENDITURE' in x.columns else 0)
    return new_df

# takes dataframe as input @param data
# adds new column to dataframe representing ratio of other expenditure over total expenditure
# (calculates other_expenditure/total_expenditure)
def other_expenditure_ratio(data):
    new_df = data.assign(Other_Expenditure_Ratio = lambda x: x.OTHER_EXPENDITURE/x.TOTAL_EXPENDITURE if 'OTHER_EXPENDITURE' in x.columns else 0)
    return new_df

# takes dataframe as input @param data
# adds new column to dataframe representing federal spending per student
# (calculates federal_revenue/enroll)
def federal_spending_per_student(data):
    new_df = data.assign(Federal_Spending_per_Student = lambda x: x.FEDERAL_REVENUE/x.ENROLL)
    return new_df

# takes dataframe as input @param data
# adds new column to dataframe representing state spending per student
# (calculates state_revenue/enroll)
def state_spending_per_student(data):
    new_df = data.assign(State_Spending_per_Student = lambda x: x.STATE_REVENUE/x.ENROLL)
    return new_df

# takes dataframe as input @param data
# adds new column to dataframe representing local spending per student
# (calculates local_revenue/enroll)
def local_spending_per_student(data):
    new_df = data.assign(Local_Spending_per_Student = lambda x: x.LOCAL_REVENUE/x.ENROLL)
    return new_df

# takes dataframe as input @param data
# adds new column to dataframe representing ratio of budget spent
# (calculates total_expenditure/total_revenue)
def ratio_budget_spend(data):
    new_df = data.assign(Ratio_Budget_Spent = lambda x: x.TOTAL_EXPENDITURE/x.TOTAL_REVENUE)
    return new_df