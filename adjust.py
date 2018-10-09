#!/usr/bin/python
import sys
import gi
import math

gi.require_version('Notify', '0.7')
from gi.repository import Notify

# Change these
BRIGHTNESS_BASE = "/sys/class/backlight/intel_backlight/"
BRIGHTNESS_MAX = "max_brightness"
BRIGHTNESS_ACTUAL = "actual_brightness"
BRIGHTNESS_SET = "brightness"
MAX_BRIGHTNESS_DIVIDED_BY = 10
NOTIFICATIONS = True

def get_max_brightness():
    f = open(BRIGHTNESS_BASE + BRIGHTNESS_MAX, "rt")
    value = f.readline().strip()
    return int(value)

def get_actual_brightness():
    f = open(BRIGHTNESS_BASE + BRIGHTNESS_ACTUAL, "rt")
    value = f.readline().strip()
    return int(value)

def adjust_brightness(new_brightness):
    f = open(BRIGHTNESS_BASE + BRIGHTNESS_SET, "w")
    f.write(str(new_brightness))

def show_notification(header, content):
    if NOTIFICATIONS:
        Notify.init(header)
        notification = Notify.Notification.new(header, content, "dialog-information")
        notification.show()

def main():
    args = sys.argv
    step = math.floor(get_max_brightness() / MAX_BRIGHTNESS_DIVIDED_BY)
    
    if len(args) < 2:
        show_notification("Screen brightness error", "Incorrect arguments!")
    else:
        if args[1] == 'inc':
            #increase screen brightness
            if(get_max_brightness() >= (get_actual_brightness() + step)):
                adjust_brightness(get_actual_brightness() + step)
            else:
                show_notification("Screen brightness", "Full brightness already!")
                adjust_brightness(get_max_brightness())
        else:
            #decrease screen brightness
            if((get_actual_brightness() - step) >= 0):
                adjust_brightness(get_actual_brightness() - step)
            else:
                show_notification("Screen brightness", "Minimum brightness already!")
                #adjust_brightness(0)        
        show_notification("Screen brightness", "Brightness: " + str(get_actual_brightness()))

if __name__ == '__main__':
    main()