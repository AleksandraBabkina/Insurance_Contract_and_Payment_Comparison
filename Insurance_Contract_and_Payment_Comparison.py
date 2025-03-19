import pandas as pd

file_contracts_23 = r"СК договоры 0109.csv"
file_contracts_24 = r"СК договоры 0109.csv"
file_payments_23 = r"СК платежи 0109.csv"
file_payments_24 = r"СК платежи 0109.csv"

headers_contracts_23 = pd.read_csv(file_contracts_23, nrows = 0, index_col=0, on_bad_lines = 'skip', encoding_errors='ignore', sep=';', encoding ='cp1251', quoting=3).columns
headers_contracts_24 = pd.read_csv(file_contracts_24, nrows = 0, index_col=0, on_bad_lines = 'skip', encoding_errors='ignore', sep=';', encoding ='cp1251', quoting=3).columns

compare_contracts = list(set(headers_contracts_23) & set(headers_contracts_24))
compare_contracts
# Loading takes 10-15 minutes!!!

# Reading file 1
payments_df_23 = pd.read_csv(file_payments_23, on_bad_lines = 'skip', encoding_errors='ignore', sep=';', encoding ='cp1251', quoting=3, usecols = compare_payments)
print("Reading file 1 payments completed")

# Reading file 2
payments_df_24 =  pd.read_csv(file_payments_24, on_bad_lines = 'skip', encoding_errors='ignore', sep=';', encoding ='cp1251', quoting=3, usecols = compare_payments)
print("Reading file 2 payments completed\nProceeding to read contract files")

# Reading file 3
contracts_df_23 =  pd.read_csv(file_contracts_23, on_bad_lines = 'skip', encoding_errors='ignore', sep=';', encoding ='cp1251', quoting=3, usecols = compare_contracts)
print("Reading file 1 contracts completed")

# Reading file 4
contracts_df_24 =  pd.read_csv(file_contracts_24, on_bad_lines = 'skip', encoding_errors='ignore', sep=';', encoding ='cp1251', quoting=3, usecols = compare_contracts)
print("Reading file 2 contracts completed\nProceeding to find missing contracts")

delited_data_payments_23 = payments_df_23[~payments_df_23['contract_number'].isin(payments_df_24['contract_number'])]
delited_data_payments_24 = payments_df_24[~payments_df_24['contract_number'].isin(payments_df_23['contract_number'])]

# Finding rows that match exactly
full_match_payments = payments_df_24.merge(payments_df_23, how = 'inner')

# Keep only unmatched rows
missing_payment_df = payments_df_24[~payments_df_24.index.isin(full_match_payments.index)]
missing_payment_df


partial_match_payment = pd.merge(missing_payment_df, payments_df_23, how = 'left', indicator = True)
chenge_data_payment = partial_match_payment[partial_match_payment['_merge'] == 'both']
chenge_data_payment

desappeard_data_payment = partial_match_payment[partial_match_payment['_merge'] == 'left_only']
desappeard_data_payment = desappeard_data_payment.drop(columns=['_merge'])  # Удаление столбца '_merge'
desappeard_data_payment

# Creating a new Excel file and saving data
output_file = r"C:\Users\aleksandra.babkina\Desktop\Comparison_files_payments.xlsx"  # Путь без одиночных кавычек
with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
    delited_data_payments_23.to_excel(writer, sheet_name='Existed_in_old_but_missing_in_new', index=False)
    delited_data_payments_24.to_excel(writer, sheet_name='Existed_in_new_but_missing_in_old', index=False)
    desappeard_data_payment.to_excel(writer, sheet_name='Changed_in_new', index=False)

print("Done")

# delited_data_contracts_23 = contracts_df_23[~contracts_df_23['contract_number'].isin(contracts_df_24['contract_number'])]
delited_data_contracts_24 = contracts_df_24[~contracts_df_24['contract_number'].isin(contracts_df_23['contract_number'])]

# Finding rows that match exactly
full_match_contracts = contracts_df_24.merge(contracts_df_23, how = 'inner')

# Keep only unmatched rows
missing_contracts_df = contracts_df_24[~contracts_df_24.index.isin(full_match_contracts.index)]
missing_contracts_df.head()

partial_match_contracts = pd.merge(missing_contracts_df, contracts_df_23, how = 'left', indicator = True)
chenge_data_contracts = partial_match_contracts[partial_match_contracts['_merge'] == 'both']
chenge_data_contracts.head()

desappeard_data_contracts = partial_match_contracts[partial_match_contracts['_merge'] == 'left_only']
desappeard_data_contracts = desappeard_data_contracts.drop(columns=['_merge'])  # Удаление столбца '_merge'
desappeard_data_contracts.head()

# Creating a new Excel file and saving data
output_file_contracts = r"C:\Users\aleksandra.babkina\Desktop\Comparison_files_contracts.xlsx"  # Путь без одиночных кавычек
with pd.ExcelWriter(output_file_contracts, engine='openpyxl') as writer:
    delited_data_contracts_24.to_excel(writer, sheet_name='Existed_in_new_but_missing_in_old', index=False)
    desappeard_data_contracts.to_excel(writer, sheet_name='Changed_in_new', index=False)

print("Done")
