# TigerOS UI Tweaks
This repository hosts all of the User Interface tweaks that go on top of the default Gnome Desktop Environment.

### Prerequisites
This software is built assuming you are running TigerOS or a Fedora 27 derivative

### Installing
Assuming the tigeros repository has been added to your `/etc/yum.repos.d/` directory, run:
```
sudo dnf install tigeros-ui-tweaks
```
Otherwise you can clone this repository and run each file separately:
```
git clone git@github.com:RITlug/tigeros-ui-tweaks.git
cd tigeros-ui-tweaks/tigeros-ui-tweaks-1.0 
sudo ./paper-icon-theme && ./dark-theme
```

### TODO
* Add dash-to-dock tweaks
* Add bash commands (e.g. `tigeros-ui paper`)
* Change source to point to mirror.ritlug.com
* Create uninstall portion when running `dnf remove tigeros-ui-tweaks`
* Upon install, check if dark mode is already installed. If so, don't change the value.

## Authors
* Tim Zabel <tjz8659@rit.edu>
