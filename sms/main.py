import requests

url = "https://api.sendchamp.com/api/v1/sms/send"

payload= "{"to":'["2349039099438"]', "message":"Hello from Olumide Latest","sender_name":"sadiqful"}"
headers = {
  'Accept': 'application/json',
  'Authorization': 'Bearer ACCESS_KEY',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)