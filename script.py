from pyzabbix import ZabbixAPI
import smtplib

ip = 'SomeIP/zabbix'
user = 'someUser'
password= 'somePassword'
from_address = example@zabbix.com
to_addresses = ["example@email.com","example2@mail.com"]

zAPI = ZabbixAPI(ip, user, password)

hosts = zAPI.host.get(monitored_hosts=1, ouput='extend')

message = "To:"
message += ",".join(str(x) for x in to_addresses)
message += "\nSubject: Health Report \n"
message += "Hostname \tError \n";
for host in hosts:
       message += host["host"] + "\t" + host["error"] + "\n"

mail = smtplib.SMTP()
mail.connect()
mail.sendmail(from_address, to_addresses, message)
mail.close()
