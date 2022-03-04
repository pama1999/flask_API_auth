import requests
import socket
import subprocess
hwid = str(subprocess.check_output(
    'wmic csproduct get uuid')).split('\\r\\n')[1].strip('\\r').strip()
print(hwid)

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

print(get_ip())

payload = {'api': "34336566-3961-3539-3335-623934343136"}

r = requests.get('http://127.0.0.1:5000/api/v1/result', params=payload)
print(r.text)
input('Press ENTER to exit')
