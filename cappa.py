from web3 import Web3
import json
import pandas as pd


def cappa(recipient):
	
	# create variables
	utput = pd.DataFrame(index=["ETH", "USDC", "CAP"])
	output.index.name = "Pool"

	web3 = Web3(Web3.HTTPProvider('https://arb1.arbitrum.io/rpc'))
	web3.eth.default_account = recipient

	USDC_Pool_Address = '0x958cc92297e6F087f41A86125BA8E121F0FbEcF2'
	ETH_Pool_Address = '0xE0cCd451BB57851c1B2172c07d8b4A7c6952a54e'
	CAP_Pool_Address = '0xC8CDd2Ea6A5149ced1F2d225D16a775ee081C67D'
	CAP_Pool_ETH_Rewards_Address = '0x1E91F67a5aa0137aD86eEbAD64E2C2a1B6ae30E5'
	CAP_Pool_USDC_Rewards_Address = '0xCEFFAc2522b837012B576770b6F5DD75a3F75C38'
	ETH_Pool_Rewards_Address = '0x29163356bBAF0a3bfeE9BA5a52a5C6463114Cb5f'	
	USDC_Pool_Rewards_Address = '0x10f2f3B550d98b6E51461a83AD3FE27123391029'

	CAP_Pool_ABI = json.loads('[{"inputs":[{"internalType":"address","name":"_currency","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"user","type":"address"},{"indexed":true,"internalType":"address","name":"currency","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"clpAmount","type":"uint256"}],"name":"Deposit","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"user","type":"address"},{"indexed":true,"internalType":"address","name":"currency","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"clpAmount","type":"uint256"}],"name":"Withdraw","type":"event"},{"stateMutability":"payable","type":"fallback"},{"inputs":[],"name":"UNIT","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"destination","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"creditUserProfit","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"currency","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"deposit","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"getBalance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"getCurrencyBalance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getUtilization","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"maxCap","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"minDepositTime","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"openInterest","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"rewards","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"router","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"setOwner","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_minDepositTime","type":"uint256"},{"internalType":"uint256","name":"_utilizationMultiplier","type":"uint256"},{"internalType":"uint256","name":"_maxCap","type":"uint256"},{"internalType":"uint256","name":"_withdrawFee","type":"uint256"}],"name":"setParams","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_router","type":"address"}],"name":"setRouter","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"trading","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"bool","name":"isDecrease","type":"bool"}],"name":"updateOpenInterest","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"utilizationMultiplier","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"currencyAmount","type":"uint256"}],"name":"withdraw","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"withdrawFee","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"stateMutability":"payable","type":"receive"}]')
	CAP_Rewards_ABI = json.loads('[{"inputs":[{"internalType":"address","name":"_pool","type":"address"},{"internalType":"address","name":"_currency","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"user","type":"address"},{"indexed":false,"internalType":"address","name":"poolContract","type":"address"},{"indexed":false,"internalType":"address","name":"currency","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"CollectedReward","type":"event"},{"stateMutability":"payable","type":"fallback"},{"inputs":[],"name":"UNIT","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"collectReward","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"cumulativeRewardPerTokenStored","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"currency","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getClaimableReward","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"notifyRewardReceived","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"pendingReward","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"pool","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"router","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"setOwner","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_router","type":"address"}],"name":"setRouter","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"trading","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"treasury","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"updateRewards","outputs":[],"stateMutability":"nonpayable","type":"function"},{"stateMutability":"payable","type":"receive"}]')


	# initialize contracts
	CAP_USDC_Contract = web3.eth.contract(address=USDC_Pool_Address, abi=CAP_Pool_ABI)
	CAP_ETH_Contract = web3.eth.contract(address=ETH_Pool_Address, abi=CAP_Pool_ABI)
	CAP_CAP_Contract = web3.eth.contract(address=CAP_Pool_Address, abi=CAP_Pool_ABI)

	CAP_Pool_ETH_Rewards_Contract = web3.eth.contract(address=CAP_Pool_ETH_Rewards_Address, abi=CAP_Rewards_ABI)
	CAP_Pool_USDC_Rewards_Contract = web3.eth.contract(address=CAP_Pool_USDC_Rewards_Address, abi=CAP_Rewards_ABI)
	USDC_Pool_Rewards_Contract = web3.eth.contract(address=USDC_Pool_Rewards_Address, abi=CAP_Rewards_ABI)
	ETH_Pool_Rewards_Contract = web3.eth.contract(address=ETH_Pool_Rewards_Address, abi=CAP_Rewards_ABI)

	# gather pool balances
	USDC_Pool_Balance = CAP_USDC_Contract.functions.getCurrencyBalance(recipient).call() / 10**18
	ETH_Pool_Balance = CAP_ETH_Contract.functions.getCurrencyBalance(recipient).call() / 10**18
	CAP_Pool_Balance = CAP_CAP_Contract.functions.getBalance(recipient).call() / 10**18
	
	# gather unclaimed rewards balances
	CAP_ETH_Rewards = CAP_Pool_ETH_Rewards_Contract.functions.getClaimableReward().call({"from": recipient}) / 10**18
	CAP_USDC_Rewards = CAP_Pool_USDC_Rewards_Contract.functions.getClaimableReward().call({"from": recipient}) / 10**18
	ETH_Rewards = ETH_Pool_Rewards_Contract.functions.getClaimableReward().call({"from": recipient}) / 10**18
	USDC_Rewards = USDC_Pool_Rewards_Contract.functions.getClaimableReward().call({"from": recipient}) / 10**18

	# output to the dataframe
	output.at["ETH", "Balance"] = ETH_Pool_Balance
	output.at["USDC", "Balance"] = USDC_Pool_Balance
	output.at["CAP", "Balance"] = CAP_Pool_Balance

	output.at["ETH", "Rewards (ETH)"] = ETH_Rewards
	output.at["USDC", "Rewards (USDC)"] = USDC_Rewards
	output.at["CAP", "Rewards (ETH)"] = CAP_ETH_Rewards
	output.at["CAP", "Rewards (USDC)"] = CAP_USDC_Rewards
	output.fillna(0, inplace=True)

	return output