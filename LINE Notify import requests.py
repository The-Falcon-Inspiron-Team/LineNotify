import requests
url = 'https://notify-api.line.me/api/notify'
token =  "IUmNdJYFQuetWIZDUlbvOBS5vSjXZvJOAwlT8Zcmd03"
headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}

msg = 'ขโมยมาจาก พ.อ.อ.สมพร  ทองทรัพย์ รร.การบิน'
r = requests.post(url, headers=headers, data = {'message':msg})
print (r.text)