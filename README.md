# iosxe-getshtechuponreload

*Gathers sh tech when reload is executed, before rebooting*


## Motivation

Often times, I've seen customers reload devices for various reasons, and critical troubleshooting info is lost, making root cause analysis difficult. This is designed to write the output of a "sh tech" to flash before reloading - in conjunction with EEM, however, you could adapt it to collect whatever you'd like.

## Technologies & Frameworks Used

This script relies on the IOS-XE guestshell, on-box python, and EEM

## Usage

Configure EEM to execute this script when someone issues a reload command. Example: 

event manager applet shtech authorization bypass

 event cli pattern "reload" sync no skip no default 60 maxrun 60
 
 action 0.01 syslog msg "Capturing sh tech before reload"

 action 0.02 cli command "enable"

 action 0.03 cli command "guestshell run python /bootflash/scripts/iosxe_getshtechuponreload.py"

## Documentation

This is it :)

## Authors & Maintainers

Smart people responsible for the creation and maintenance of this project:

- Chris Riling <criling@cisco.com>

## Credits

The following resources were influential in the creation of this project:

- This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and a derivative of the[audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage) project template.

- I also adapted some of the python from the examples in our network programmability lab guide, written by my fellow SEs - https://github.com/CiscoSE/LTRPRG-1100

## License

This project is licensed to you under the terms of the [Cisco SampleCode License](./LICENSE).
