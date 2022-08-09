import paramiko


def add_user(user):
	fields = {
		"command": "add_user",
		"user_type": "Trader",
		"ib_id": "FundedFuturesNetwork",
		"user_id": user['username'],
		"first_name": user['firstName'],
		"last_name": user['lastName'],
		"password": user['password'],
		"email": user['email'],
		"user_max_count": "2",
		"login_exp": "",
		"life_span": "",
		"trading_status": "Enabled",
		"nlx_user_id": "",
		"cme_user_id": "cme",
		"ice user id": "",
		"dme user id": "",
		"read only": "",
		"ullink user id": "",
		"pulse order limit": "",
		"cboe user id": "",
		"cbsx user id": "",
		"cfe user id": "",
		"ic user id": "",
		"risk read only": "",
		"rithmic user type": "",
		"ice-otc user id": "",
		"nybot user id": "",
		"wce user id": "",
		"authorized ice user": "",
		"authorized ice otc": "",
		"authorized nybot": "",
		"authorized wce user": "",
		"address": user['address'].split(',')[0],
		"address2": "",
		"city": user['city'],
		"country": user['country'],
		"state": user['state'],
		"postal": user['postal'],
		"Home Phone": "",
		"Work Phone": "",
		"Mobile Phone": "",
		"Fax": "",
		"Billing Code": "",
		"TDEX User Id": "",
		"Associated User": "",
		"EUREX User": "",
		"Prior Market Data": "",
		"Prior Market Data": "",
		"Pre-Trade": "",
		"Password": "",
		"Demo User Valid": "",
		"LIFFE User Id": "",
		"LIFFE Authorized": "",
		"ICE": "",
		"MEFF Client Id Short": "",
		"MEFF Investment": "",
		"MEFF Execution": "",
		"MEFF Trading": "",
		"MATIF Trading": "",
		"MATIF NonExecuting Broker": "",
		"MATIF Investment": "",
		"MATIF Execution": "",
		"MATIF Client Id Short": "",
		"AEX Trading Capacity": "",
		"AEX Non-Executing": "",
		"AEX Investment": "",
		"AEX Execution": "",
		"AEX Client Id Short": "",
		"EUREX Client Id": "",
		"EUREX Investment": "",
		"EUREX Execution": "",
		"Disable Add Accounts Only": "",
		"Disable Add User Only": "",
		"Disable Assign Only": "",
		"Disable Edit Markets Only": "",
		"Disable Edit Cash Only": "",
		"Disable Edit Risk Only": "",
		"Liquidating Only Cap ": "",
		"SMFE Subscriber Token": "",
		"SMFE User ID": "",
		"MaxSessionCountORders": "10",
		"idk": "",
		"MaxSessionCountMD": "1",
		"Gain": "",
		"Go Live": ""
	}

	filename = f"{user['username']}-add_user.csv"
	with open(filename, "w") as f:
		f.write(','.join(fields.values()))

	host = "ritpz11300.11.rithmic.com"                    #hard-coded
	port = 22
	transport = paramiko.Transport((host, port))

	username = "uIDEJfOZY5fWl"                #hard-coded
	password = "xBIKmORYee7l"                #hard-coded
	transport.connect(None, username = username, password = password)

	sftp = paramiko.SFTPClient.from_transport(transport)
	sftp.put(filename, "/home/uIDEJfOZY5fWl/RithmicPaperTrading/coperations/testuser.csv")


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
