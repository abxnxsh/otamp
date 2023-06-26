# main.py
import machine
import network
import time
import urequests

# Function to connect to Wi-Fi
def connect_to_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    if not wlan.isconnected():
        wlan.active(True)
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            pass
    print("Wi-Fi connected!")
    print("IP address:", wlan.ifconfig()[0])

# Function to update the siu.py file from GitHub
def update_siu_file():
    url = "https://raw.githubusercontent.com/your-username/your-repo/main/siu.py"
    response = urequests.get(url)
    code = response.text
    with open("siu.py", "w") as f:
        f.write(code)
    print("siu.py file updated!")

# Connect to Wi-Fi
ssid = "Redmi"
password = "Abinesh07"
connect_to_wifi(ssid, password)

# Update siu.py file
update_siu_file()

# Import and execute siu.py code
import siu

# Run siu.siu() function
siu.siu()
