import requests

url = "https://api.sendchamp.com/api/v1/sms/send"

payload = "{
    "to": [
        "2348188469520"
    ],
    "message": "Lorem ipsum d, no lele",
    "sender_name": "Dash",
    "route": "non_dnd"
}"

headers = {
  'Accept': 'application/json',
  'Authorization': 'Bearer ACCESS_KEY',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
