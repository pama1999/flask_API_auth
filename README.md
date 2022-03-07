# Flask Simple API Auth

This is a Python Flask oriented simple API Authentication through a local JSON File

## Required Libraries

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install flask.

```bash
pip install flask
```

## Usage
Simple import of the given Key into our Flask Application from our API url
```python
from flask import Flask,request
import json

# returns 'words'
@app.route('/api/v1/result', methods=['GET'])
def check_status():
    with open('data.json', 'r') as database:
        data = json.loads(database.read())
    print(data)

    key = request.args.get('api')
```

## API Key from URL
In this step the written Key from API URL will be checked with the gattered data from our simple JSON file which could b located in a database.
```python
for user in data['users']:
        #return according to the users status from JSON
        if key == user['key']:
            return "Access granted! your status is: " + user['status']
        else:
            return "Sorry your status is not Active"
```

Please make sure to update tests as appropriate.

# JSON Structure
```json
{
  "users": [
    {
      "key": "34336566-3961-3539-3335-623934343136",
      "status": "active",
      "locked_ip": "127.0.0.1"
    }
  ]
}
```

# Usage of API
Note: you could also retrieve the IP from your clients browser or .py application and POST it with your API url to prevent multiple users to have the same key on different IP's.

```python
#get unique id
hwid = str(subprocess.check_output(
    'wmic csproduct get uuid')).split('\\r\\n')[1].strip('\\r').strip()
print(hwid)
```
Get Users IP
```python
def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP
```

API Get request to recieve the information
```python
payload = {'api': "34336566-3961-3539-3335-623934343136"}

r = requests.get('http://127.0.0.1:5000/api/v1/result', params=payload)
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
