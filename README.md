# Insurance_Contract_and_Payment_Comparison

## Description

This program compares two datasets of insurance contracts and payments for different periods (2023 and 2024). It identifies:
- Contracts and payments that exist in one file but are missing in the other.
- Contracts and payments that have changed.
  
The comparison helps in detecting discrepancies, deletions, or changes in the records between the two datasets.

## Functional Description

The program performs the following steps:
1. **Reads CSV files** for contracts and payments for two periods (2023 and 2024).
2. **Compares column headers** to ensure consistency between datasets.
3. **Loads data** using common columns to optimize memory and comparison efficiency.
4. **Identifies:**
   - Rows present in 2023 data but missing in 2024 data.
   - Rows present in 2024 data but missing in 2023 data.
   - Rows present in both datasets but with differences (changed data).
5. **Saves the results** into separate Excel files for contracts and payments.

## How It Works

1. The script reads four CSV files:
   - Contracts for 2023
   - Contracts for 2024
   - Payments for 2023
   - Payments for 2024
2. It compares columns between the two periods and only keeps common columns.
3. It finds:
   - Records existing in one dataset but not in the other.
   - Records existing in both datasets but with differences.
4. Results are saved in Excel format, organized by:
   - Missing records
   - Changed records

## Input Structure

The program uses the following CSV files:
- `СК договоры 0109.csv` (for both 2023 and 2024 contracts)
- `СК платежи 0109.csv` (for both 2023 and 2024 payments)

Columns are expected to have consistent headers.

## Output

The program generates two Excel files:
1. **Comparison_files_payments.xlsx** — Contains:
   - Payments existing in old but missing in new dataset.
   - Payments existing in new but missing in old dataset.
   - Payments changed between datasets.
2. **Comparison_files_contracts.xlsx** — Contains:
   - Contracts existing in new but missing in old dataset.
   - Contracts changed between datasets.

## Technical Requirements

- Python 3.x
- Required libraries: `pandas`, `openpyxl`

## Usage

1. Place your CSV files in the same directory as the script or adjust file paths accordingly.
2. Run the script.
3. The script will output:
   - Excel file with payment discrepancies: `Comparison_files_payments.xlsx`
   - Excel file with contract discrepancies: `Comparison_files_contracts.xlsx`

## Example Output

- **Existed_in_old_but_missing_in_new:** Records present in the 2023 dataset but missing in the 2024 dataset.
- **Existed_in_new_but_missing_in_old:** Records present in the 2024 dataset but missing in the 2023 dataset.
- **Changed_in_new:** Records present in both datasets but with differences.

## Conclusion

This tool simplifies the comparison process of contract and payment datasets across different periods. It helps identify deleted, added, or modified records, ensuring data integrity and facilitating audits or reconciliations.
