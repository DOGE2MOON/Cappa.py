# Cappa.py
Pulls cap.finance v3 user pool balances and unclaimed rewards via web3 calls and returns them to a dataframe. Can easily be extended to export to CSV, or add timestamps for the purpose of tracking historical real yield. 

# Example Usage
cappa('YOUR_ADDRESS_HERE')

cappa("YOUR_ADDRESS_HERE").to_csv('filename.csv', encoding='utf-8')
