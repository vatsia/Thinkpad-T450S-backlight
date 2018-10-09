# Thinkpad T450S Backlight adjusting
Simple Python-script for adjusting Lenovo Thinkpad T450S screen backlight.

## Requirements
- Python 3 (tested with Python 3.7.0)
- python-gobject (needed for notifications to openbox-based environment)

## Adjust.py usage
Remember to check "Check these" -section from `adjust.py`. You can find needed information for these looking to your `/sys/class/backlight/`-directory, if it exists. If it does'nt, you can't use this script.

Test the script first from command line.
`python adjust.py inc` will increase the backlight.
`python adjust.py dec` will decrease the backlight.
You may also want to change the count of steps where maximum screen brightness is divided, as default it is divided by 10.

## Using with openbox-based environment
Please locate your Openbox -configuration file. By default it is `/home/<username>/.config/openbox/rc.xml`. Locate there `<keyboard>`-section, and paste lines inside `ob-configuration.xml` inside it. Then start your openbox-session again (for example log out and log in), and keybindings should work. I copied `adjust.py` to `/home/<username>/.config/`-directory. If you chose different one, please change paths in the openbox configuration file.

## Udev-rules
In some cases normal users have no right to write in the backlight adjustement file in `/sys/class/backlight/`. This can be fixed by adding file `backlight.rules` to `/etc/udev/rules.d/`. It contais two rules, which will brightness-file's group to `video` and give write access to that group. Remember to check if your user account is in that group by running command `groups`.

## Kernel-parameters
There is also needed a couple of kernel parameters, which are in `kernelparams.txt` -file. In mine configuration they are pasted to `/boot/grub/grub.cfg`-file.