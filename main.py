from plyer import notification
import time

def reminder():
    while True:
        notification.notify(
            title = 'Water Drinking reminder!',
            message = 'Drink enogh amount of water to stay hydrated.  Health authorities commonly recommend eight 8-ounce glasses, which equals about 2 liters, or half a gallon.',
            app_icon = 'home/vikas/Desktop/DesktopNotification/water.png',
            timeout = 10
        )
        time.sleep(20)

if __name__ == "__main__":
    reminder()