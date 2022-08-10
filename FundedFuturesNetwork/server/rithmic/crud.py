import paramiko
from pprint import pprint

def add_user(user):
	pprint(user)
	fields = {
		"command": "add_user", # 1
		"user_type": "Trader", # 2
		"ib_id": "FundedFuturesNetwork", # 3
		"user_id": user['username'], # 4
		"first_name": user['firstName'], # 5
		"last_name": user['lastName'], # 6
		"password": user['password'], # 7
		"email": user['email'], # 8
		"user_max_count": "2", # 9
		"login_exp": "", # 10
		"life_span": "", # 11
		"trading_status": "Enabled", # 12
		"nlx_user_id": "", # 13
		"cme_user_id": "CME", # 14
		"ice user id": "", # 15 1
		"dme user id": "", # 16
		"read only": "", # 17
		"ullink user id": "", # 18
		"pulse order limit": "", # 19
		"cboe user id": "", # 20
		"cbsx user id": "", # 21
		"cfe user id": "", # 22
		"ic user id": "", # 23
		"risk read only": "", # 24
		"rithmic user type": "", # 25
		"ice-otc user id": "", # 26
		"nybot user id": "", # 27
		"wce user id": "", # 28
		"authorized ice user": "", # 29
		"authorized ice otc": "", # 30
		"authorized nybot": "", # 31
		"authorized wce user": "", # 32
		"address": user['address'].split(',')[0], # 33
		"address2": "", # 34
		"city": user['city'], # 35
		"country": user['country'], # 36
		"state": user['state'], # 37
		"postal": user['postal'], # 38
		"Home Phone": "", # 39
		"Work Phone": "", # 40
		"Mobile Phone": "", # 41
		"Fax": "", # 42
		"Billing Code": "", # 43
		"TDEX User Id": "", # 44
		"Associated User": "", # 45
		"EUREX User": "", # 46
		"Prior Market Data": "", # 47
		"Prior Market Data": "", # 48
		"Pre-Trade": "", # 49
		"Password": "", # 50
		"Demo User Valid": "", # 51
		"LIFFE User Id": "", # 52
		"LIFFE Authorized": "", # 53
		"ICE": "", # 54
		"MEFF Client Id Short": "", # 55
		"MEFF Investment": "", # 56
		"MEFF Execution": "", # 57
		"MEFF Trading": "", # 58
		"MATIF Trading": "", # 59
		"MATIF NonExecuting Broker": "", # 60
		"MATIF Investment": "", # 61
		"MATIF Execution": "", # 62
		"MATIF Client Id Short": "", # 63
		"AEX Trading Capacity": "", # 64
		"AEX Non-Executing": "", # 65
		"AEX Investment": "", # 66
		"AEX Execution": "", # 67
		"AEX Client Id Short": "", # 68
		"EUREX Client Id": "", # 69
		"EUREX Investment": "", #  70
		"EUREX Execution": "", # 71
		"Disable Add Accounts Only": "", # 72
		"Disable Add User Only": "", # 73
		"Disable Assign Only": "", # 74
		"Disable Edit Markets Only": "", # 75
		"Disable Edit Cash Only": "", # 76
		"Disable Edit Risk Only": "", # 77
		"Liquidating Only Cap ": "", # 78
		"SMFE Subscriber Token": "", # 79
		"SMFE User ID": "", # 80
		"?????": "",
		"MaxSessionCountORders": "10", # 81
		"MaxSessionCountMD": "1", # 82
		"Gain": "", #  83
		"Go Live": "" # 84
	}

	filename = f"{user['username']}AddUser.csv"
	with open(filename, "w") as f:
		f.write(','.join(fields.values()))

	host = "ritpz11300.11.rithmic.com"                    #hard-coded
	port = 22
	transport = paramiko.Transport((host, port))

	username = "uIDEJfOZY5fWl"                #hard-coded
	password = "xBIKmORYee7l"                #hard-coded
	transport.connect(None, username = username, password = password)

	sftp = paramiko.SFTPClient.from_transport(transport)
	sftp.put(f"{filename}", f"/home/uIDEJfOZY5fWl/RithmicPaperTrading/coperations/{filename}")


#
# user = {
# 	'user_id': "blanksheet-78995",
# 	'first_name': "tstingaccount123",
# 	'last_name': "last",
# 	'password': "testtest123",
# 	'email': "whatsmyemail@gmail.com",
# 	'address': "111 littelton road",
# 	'city': "parsippany",
# 	'country': "USA",
# 	'state': "NJ",
# 	'postal': "07077",
# }
#
# udata = add_user(user)
# with open("testuser.csv", "w") as f:
# 	f.write(udata)
#
# host = "ritpz11300.11.rithmic.com"                    #hard-coded
# port = 22
# transport = paramiko.Transport((host, port))
#
# username = "uIDEJfOZY5fWl"                #hard-coded
# password = "xBIKmORYee7l"                #hard-coded
# transport.connect(None, username = username, password = password)
#
# sftp = paramiko.SFTPClient.from_transport(transport)
# sftp.put("testuser.csv", "/home/uIDEJfOZY5fWl/RithmicPaperTrading/coperations/testuser.csv")
