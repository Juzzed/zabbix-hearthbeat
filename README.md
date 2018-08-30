# zabbix-hearthbeat
Sends daily a summary of all hosts with the errors with help of an python3 script. 
### Requirements:
- Python3
- Pip
- py-zabbix
- For daily notifications you need to configure a cronjob.

### In pip:
pip3 install py-zabbix

### Example cron:
30 09 * * * python3 /path/to/script.py
