# Pi Clock

## Screen Drivers

https://github.com/adafruit/Raspberry-Pi-Installer-Scripts

```bash
sudo python3 adafruit-pitft.py --display=35r --rotation=270 --install-type=console
```

## Autostart

Edit `/etc/rc.local` and add `/home/pi/pi-clock/main.py > /dev/tty1` before the `exit 0`.

## Change Font Size

Run `sudo dpkg-reconfigure console-setup` and select:
1. UTF-8
2. Guess optimal character set
3. Terminus
4. 6x12 (framebuffer only)

## Set Locale

Run `sudo raspi-config` and set en_AU.UTF-8 as the default locale.

## Connnecting to TTY1

Run `sudo linuxvnc 1` and connect using a VNC client.
