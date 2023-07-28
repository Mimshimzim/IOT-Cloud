import network

def wifi_connect(wifi_ssid,wifi_password):
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        wlan.connect(wifi_ssid, wifi_password)

