from pyzabbix import ZabbixAPI
import smtplib

IP = 'SomeIP/zabbix'

zAPI = ZabbixAPI(IP, user='user', password='somepass')
from_address = zabbix@zabbix.zabbix
to_addresses = ["email1","email2"]

hosts = zAPI.host.get(monitored_hosts=1, ouput='extend')

message = "To:"
message = message + ",".join(str(x) for x in to_addresses)
message = message + "\n"
message = message + "Subject: Health Report" + "\n"
message = message + "Hostname \tError \n";
for host in hosts:
       message = message + host["host"] + "\t" + host["error"] + "\n"

mail = smtplib.SMTP()
mail.connect()
mail.sendmail(from_address, to_addresses, message)
mail.close()
