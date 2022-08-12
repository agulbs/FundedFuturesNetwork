import datetime
import time
import hashlib

timestamp = datetime.datetime.now() - datetime.timedelta(hours=6)
unix_time = time.mktime(timestamp.timetuple())

salt = "454243"
registration_window = 604800

resulting_timestamp = str(unix_time % registration_window)

md5_digest = hashlib.md5(resulting_timestamp + salt).hexdigest()
