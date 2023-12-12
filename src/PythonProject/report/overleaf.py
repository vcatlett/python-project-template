import requests

report = requests.get("")
print(report, report.content)