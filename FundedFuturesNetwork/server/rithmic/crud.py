import paramiko
from pprint import pprint
from flask import current_app as app
# from products import tiers as rms
from .products import tiers as rms
import random
import string


def add_user(user):
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

	with app.db() as db:
		sql = """
		INSERT INTO Rithmic.AddUser (`type`, `ib_id`, `user_id`, `first_name`, `last_name`, `password`, `email`, `user_max_count`, `trading_status`, `cme_user_id`, `address`, `city`, `country`, `state`, `postal`, `max_session_count_orders`, `max_session_count_md`)
		VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s )
		"""

		params = {
			'user_type': fields['user_type'],
			'ib_id': fields['ib_id'],
			'user_id': fields['user_id'],
			'first_name': fields['first_name'],
			'last_name': fields['last_name'],
			'password': fields['password'],
			'email': fields['email'],
			'user_max_count': fields['user_max_count'],
			'trading_status': fields['trading_status'],
			'cme_user_id': fields['cme_user_id'],
			'address': fields['address'],
			'city': fields['city'],
			'country': fields['country'],
			'state': fields['state'],
			'postal': fields['postal'],
			'MaxSessionCountORders': fields['MaxSessionCountORders'],
			'MaxSessionCountMD': fields['MaxSessionCountMD'],
		}

		commit = db.commit(sql, params)

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

def add_account(user):
	unassign_account = {
		"command": "remove_account_from_user",
		"ib_id": "FundedFuturesNetwork",
		"user_id": user['username'],
		"account_id": ""
	}

	exch_entitlements = {
		"command": "set_user_exchange_entitlements",
		"user_id": user['username'],
		"exchange": "CME",
		"status": "Enabled",
		"market_depth": "Enabled",
	}

	ffn = "FFN-" + ''.join(random.choice(string.digits) for _ in range(8))

	add_account = {
		"command": "add_account", # 1
		"ib_id": "FundedFuturesNetwork", # 2
		"account_id": ffn, # 3
		"account_name": ffn, # 4
		"currency": "USD", # 5
		"type": "Customer Account (4)", # 6
		"customer_firm": "Customer", # 7
		"status": "Active", # 8
		"risk_algo": "Quantity Limits", # 9
		"rms": "Enabled", # 10
		"11 ": "", # 11
		"12 ": "", # 12
		"13 ": "", # 13
		"14 ": "", # 14
		"15 ": "", # 15
		"16 ": "", # 16
		"17 ": "", # 17
		"18 ": "", # 18
		"19 ": "", # 19
		"20 ": "", # 20
		"21 ": "", # 21
		"22 ": "", # 22
		"23 ": "", # 23
		"24 ": "", # 24
		"25 ": "", # 25
		"26 ": "", # 26
		"27 ": "", # 27
		"28 ": "", # 28
		"29 ": "", # 29
		"30 ": "", # 30
		"31 ": "", # 31
		"32 ": "", # 32
		"33 ": "", # 33
		"34 ": "", # 34
		"35 ": "", # 35
		"36 ": "", # 36
		"37 ": "", # 37
		"38 ": "", # 38
		"39 ": "", # 39
		"40 ": "", # 40
		"41 ": "", # 41
		"42 ": "", # 42
		"43 ": "", # 43
		"44 ": "", # 44
		"45 ": "", # 45
		"46 ": "", # 46
		"47 ": "", # 47
		"48 ": "", # 48
		"49 ": "", # 49
		"50 ": "", # 50
		"51 ": "", # 51
		"52 ": "", # 52
		"53 ": "", # 53
		"54 ": "", # 54
		"55 ": "", # 55
		"56 ": "", # 56
		"57 ": "", # 57
		"58 ": "", # 58
		"59 ": "", # 59
		"60 ": "", # 60
		"61 ": "", # 61
		"62 ": "", # 62
		"63 ": "", # 63
		"64 ": "", # 64
		"65 ": "", # 65
		"66 ": "", # 66
		"67 ": "", # 67
		"68 ": "", # 68
		"69 ": "", # 69
		"70 ": "", # 70
		"71 ": "", # 71
		"72 ": "", # 72
		"73 ": "", # 73
		"74": "", # 74
		"75": "", # 75
		"76": "", # 76
		"77 ": "", # 77
		"78 ": "", # 78
		"79 ": "", # 79
		"80 ": "", # 80
		"81 ": "", # 81
		"82 ": "", # 82
		"83 ": "", # 83
		"84 ": "", # 84
		"85 ": "", # 85
		"86 ": "", # 86
		"87 ": "", # 87
		"88 ": "", # 88
		"89 ": "", # 89
		"90 ": "", # 90
		"91 ": "", # 91
		"92 ": "", # 92
		"93 ": "", # 93
		"94 ": "", # 94
		"95 ": "", # 95
		"96 ": "", # 96
		"97 ": "", # 97
		"98 ": "", # 98
		"99 ": "", # 99
		"100 ": "", # 100
		"101 ": "", # 101
		"102 ": "", # 102
		"103 ": "", # 103
		"104 ": "", # 104
		"105 ": "", # 105
		"106 ": "", # 106
		"107 ": "", # 107
		"108 ": "", # 108
		"109 ": "", # 109
		"110 ": "", # 110
		"111 ": "", # 111
		"112 ": "", # 112
		"113 ": "", # 113
		"114 ": "", # 114
		"115 ": "", # 115
		"116 ": "", # 116
		"117 ": "", # 117
		"118 ": "", # 118
		"119 ": "", # 119
		"120 ": "", # 120
		"121 ": "", # 121
		"122 ": "", # 122
		"123 ": "", # 123
		"124 ": "", # 124
		"125 ": "", # 125
		"126 ": "", # 126
		"127 ": "", # 127
		"128 ": "", # 128
		"129 ": "", # 129
		"130 ": "", # 130
		"131 ": "", # 131
		"132 ": "", # 132
		"133 ": "", # 133
		"134 ": "", # 134
		"135 ": "", # 135
		"136 ": "", # 136
		"137 ": "", # 137
		"138 ": "", # 138
		"139 ": "", # 139
		"140 ": "", # 140
		"141 ": "", # 141
		"142 ": "", # 142
		"143 ": "", # 143
		"144 ": "", # 144
		"145 ": "", # 145
		"146 ": "", # 146
		"147 ": "", # 147
		"148 ": "", # 148
		"149 ": "", # 149
		"150 ": "", # 150
		"151 ": "", # 151
		"152 ": "", # 152
		"153 ": "", # 153
		"154 ": "", # 154
		"155 ": "", # 155
		"156 ": "", # 156
		"157 ": "", # 157
		"158 ": "", # 158
		"159 ": "", # 159
		"160 ": "", # 160
		"161 ": "", # 161
		"162 ": "", # 162
		"163 ": "", # 163
		"164 ": "", # 164
		"165 ": "", # 165
		"166 ": "", # 166
		"167 ": "", # 167
		"168 ": "", # 168
		"169 ": "", # 169
		"170 ": "", # 170
		"171 ": "", # 171
		"172 ": "", # 172
		"173 ": "", # 173
		"auto_liquidate": "Enabled", # 174
		"auto_liquidate_criteria": "Trailing Minimum Account Balance", # 175
		"auto_liquidate_threshold": "1500", # 176
		"177 ": "", # 177
		"178 ": "", # 178
		"179 ": "", # 179
		"180 ": "", # 180
		"181 ": "", # 181
		"182 ": "", # 182
		"183 ": "", # 183
		"184 ": "", # 184
		"185 ": "", # 185
		"186 ": "", # 186
		"187 ": "", # 187
		"188 ": "", # 188
		"189 ": "", # 189
		"190 ": "", # 190
		"191 ": "", # 191
		"192 ": "", # 192
		"193 ": "", # 193
		"194 ": "", # 194
		"195 ": "", # 195
		"196 ": "", # 196
		"197 ": "", # 197
		"198 ": "", # 198
		"include_commission_pnl": "Enabled", # 199
		"200 ": "", # 200
		"201 ": "", # 201
		"202 ": "", # 202
		"203 ": "", # 203
		"204 ": "", # 204
		"205 ": "", # 205
		"206 ": "", # 206
		"207 ": "", # 207
		"208 ": "", # 208
		"209 ": "", # 209
		"210 ": "", # 210
		"211 ": "", # 211
		"212 ": "", # 212
		"213 ": "", # 213
		"214 ": "", # 214
		"215 ": "", # 215
		"216 ": "", # 216
		"217 ": "", # 217
		"218 ": "", # 218
		"219 ": "", # 219
		"220 ": "", # 220
		"221 ": "", # 221
		"222 ": "", # 222
		"223 ": "", # 223
		"224 ": "", # 224
		"225 ": "", # 225
		"226 ": "", # 226
		"227 ": "", # 227
		"228 ": "", # 228
		"229 ": "", # 229
		"230 ": "", # 230
		"231 ": "", # 231
		"232 ": "", # 232
		"233 ": "", # 233
		"234 ": "", # 234
		"235 ": "", # 235
		"236 ": "", # 236
		"237 ": "", # 237
		"238 ": "", # 238
		"239 ": "", # 239
		"240 ": "", # 240
		"241 ": "", # 241
		"242 ": "", # 242
		"243 ": "", # 243
		"244 ": "", # 244
		"245 ": "", # 245
		"246 ": "", # 246
		"247 ": "", # 247
		"248 ": "", # 248
		"249 ": "", # 249
		"250 ": "", # 250
		"251 ": "", # 251
		"252 ": "", # 252
		"253 ": "", # 253
		"disable_on_auto_liq": "Enabled", # 254
		"255 ": "", # 255
		"256 ": "", # 256
		"257 ": "", # 257
		"258 ": "", # 258
		"259 ": "", # 259
		"260 ": "", # 260
		"261 ": "", # 261
		"262 ": "", # 262
		"263 ": "", # 263
		"264 ": "", # 264
		"265 ": "", # 265
		"266 ": "", # 266
		"267 ": "", # 267
		"268 ": "", # 268
		"269 ": "", # 269
		"270 ": "", # 270
		"271 ": "", # 271
		"272 ": "", # 272
		"273 ": "", # 273
		"274 ": "", # 274
		"275 ": "", # 275
		"276 ": "", # 276
		"277 ": "", # 277
		"278 ": "", # 278
		"279 ": "", # 279
		"280 ": "", # 280
		"281 ": "", # 281
		"282 ": "", # 282
		"283 ": "", # 283
		"284 ": "", # 284
		"285 ": "", # 285
		"286 ": "", # 286
		"287 ": "", # 287
		"288 ": "", # 288
		"289 ": "", # 289
		"290 ": "", # 290
		"291 ": "", # 291
		"292 ": "", # 292
		"293 ": "", # 293
		"294 ": "", # 294
		"295 ": "", # 295
		"296 ": "", # 296
		"297 ": "", # 297
		"298 ": "", # 298
		"299 ": "", # 299
		"300 ": "", # 300
		"301 ": "", # 301
		"302 ": "", # 302
		"smfee_omnibus_acct": "Disabled", # 303
		"smfee_cust_firm": "Enabled", # 304
	}

	assign_account = {
		"command": "assign_account_to_user",
		"ib_id": "FundedFuturesNetwork",
		"user_id": user['username'],
		"account_id": ffn,
		"access_type": "Read/Write"
	}

	equity_run = {
		"command": "equity_run",
		"operation": "set",
		"fcm_id": "Rithmic-FCM",
		"ib_id": "FundedFuturesNetwork",
		"account_id": ffn,
		"cash": f"{user['cash']}"
	}

	print(user)

	fout = ""
	filename = f"{user['username']}NewAccount.csv"
	if user['ffn']:
		filename = f"{user['username']}ResetAccount.csv"
		unassign_account['account_id'] = user['ffn']
		print(unassign_account.values())
		fout += ','.join(unassign_account.values()) + "\n"

	fout += ','.join(exch_entitlements.values()) + "\n"
	fout += ','.join(add_account.values()) + "\n"
	fout += ','.join(assign_account.values()) + "\n"
	fout += ','.join(equity_run.values()) + "\n"


	key = str(user['tier'])
	for (i, tier) in enumerate(rms[key]):
		if i == 0:
			fout += f"set_rms_account,FundedFuturesNetwork,{ffn}," + ','.join(tier)  + "\n"
		else:
			fout += f"set_rms_product,FundedFuturesNetwork,{ffn}," + ','.join(tier)  + "\n"



	with open(filename, "w") as f:
		f.write(fout)

	host = "ritpz11300.11.rithmic.com"                    #hard-coded
	port = 22
	transport = paramiko.Transport((host, port))

	username = "uIDEJfOZY5fWl"                #hard-coded
	password = "xBIKmORYee7l"                #hard-coded
	transport.connect(None, username = username, password = password)

	sftp = paramiko.SFTPClient.from_transport(transport)
	sftp.put(f"{filename}", f"/home/uIDEJfOZY5fWl/RithmicPaperTrading/coperations/{filename}")

	with app.db() as db:
		if user['reset']:
			sql_unasign = "INSERT INTO Rithmic.UnassignAccount (ib_id, user_id, account_id) VALUES (%s, %s, %s)"
			del unassign_account['command']
			db.commit(sql_unasign, unassign_account)

		sql_ffns = "INSERT INTO FundedFuturesNetwork.FFN (username, ffn) VALUES (%s, %s)"
		db.commit(sql_ffns, {'username': user['username'], 'ffn': ffn})

		sql_update = "UPDATE FundedFuturesNetwork.Users SET ffn=%s where username=%s"
		params = {'ffn': ffn, 'username': user['username']}
		db.commit(sql_update, params)

		sql_exch_entitlements = "INSERT INTO Rithmic.ExchEntitlements ( user_i, exchang, statu, market_depth ) VALUES (%s, %s, %s, %s)"
		del exch_entitlements['command']
		db.commit(sql_exch_entitlements, exch_entitlements)

		sql_add_account = """
		INSERT INTO Rithmic.AddAccount ( ib_id, account_id, account_name, currency, type, customer_firm, status, risk_algo, rms, auto_liquidate, auto_liquidate_criteria, auot_liquidate_threshold, include_comission_pnl, disable_on_auto_liq, smfee_omnibus_acct, smfee_cust_firm )
		VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s )
		"""
		params = {
			'ib_id': add_account['ib_id'],
			'account_id': add_account['account_id'],
			'account_name': add_account['account_name'],
			'currency': add_account['currency'],
			'type': add_account['type'],
			'customer_firm': add_account['customer_firm'],
			'status': add_account['status'],
			'risk_algo': add_account['risk_algo'],
			'rms': add_account['rms'],
			'auto_liquidate': add_account['auto_liquidate'],
			'auto_liquidate_criteria': add_account['auto_liquidate_criteria'],
			'auto_liquidate_threshold': add_account['auto_liquidate_threshold'],
			'include_commission_pnl': add_account['include_commission_pnl'],
			'disable_on_auto_liq': add_account['disable_on_auto_liq'],
			'smfee_omnibus_acct': add_account['smfee_omnibus_acct'],
			'smfee_cust_firm': add_account['smfee_cust_firm'],
		}
		db.commit(sql_add_account, params)

		sql_assign_account = "INSERT INTO Rithmic.AssignAccount (ib_id, user_id, account_id, access_type) VALUES (%s, %s, %s, %s)"
		del assign_account['command']
		db.commit(sql_assign_account, assign_account)

		sql_equity_run = "INSERT INTO Rithmic.EquityRun (operation, fcm_id, ib_id, account_id, cash) VALUES (%s, %s, %s, %s, %s)"
		del equity_run['command']
		db.commit(sql_equity_run, equity_run)


# def reset_account(user):
# 	equity_run = {
# 		"command": "equity_run",
# 		"operation": "set",
# 		"fcm_id": "Rithmic-FCM",
# 		"ib_id": "FundedFuturesNetwork",
# 		"account_id": user['ffn'],
# 		"cash": f"{user['cash']}"
# 	}
#
# 	modify_account = {
# 		"command": "modify_account",
# 		"ib_id": "FundedFuturesNetwork",
# 		"account_id": user['ffn'],
# 		"account_name": user['ffn'],
# 		"currency": "USD",
# 		"type": "",
# 		"customer_firm": "",
# 		"status": "Active",
# 		"risk_alog": "Quantity Limits",
# 		"rms": "Enabled",
# 	}
#
# 	with app.db() as db:
# 		sql_update = "INSERT INTO FundedFuturesNetwork.Subscriptions (username, tier) values (%s, %s)"
# 		params = {'username': user['username'], 'tier': user['tier']}
# 		db.commit(sql_update, params)
#
# 		sql_equity_run = "INSERT INTO Rithmic.EquityRun (operation, fcm_id, ib_id, account_id, cash) VALUES (%s, %s, %s, %s, %s)"
# 		del equity_run['command']
# 		db.commit(sql_equity_run, equity_run)
#
# 		sql_modify_account = """
# 		INSERT INTO Rithmic.ModifyAccount (ib_id, account_id, account_name, currency, customer_firm, status, risk_algo, rms)
# 		VALUES (%s, %s, %s, %s, %s)
# 		"""
# 		del modify_account['command']
# 		db.commit(sql_modify_account, modify_account)




# user = {
# 	'username': 'autotest',
# 	'cash': 25000,
# 	'tier': '1'
# }
#
#
# add_account(user)
