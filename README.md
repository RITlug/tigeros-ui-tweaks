# TigerOS UI Tweaks
This repository hosts all of the User Interface tweaks that go on top of the default Gnome Desktop Environment.
The first addition, `dark-theme`, is in charge of changing the default GTK theme from light to dark. Secondly, 
the `paper-icon-theme` package is in charge of enabling the [Paper Icon Theme](https://snwh.org/paper). This
removes the necessity of using a tool such as the Gnome Tweak Tool and allows for a more streamlined process.

### Prerequisites
This software is built assuming you are running TigerOS or a Fedora derivative

### Installing
Assuming the tigeros repository has been added to your `/etc/yum.repos.d/` directory, run:
```
sudo dnf install tigeros-ui-tweaks
```

### TODO
* Change source to point to mirror.ritlug.com
* Create uninstall portion when running `dnf remove tigeros-ui-tweaks`
* Upon install, check if dark mode is already installed. If so, don't change the value.
* Add bash commands (e.g. `tigeros-ui paper`)

## Authors
* Tim Zabel <tjz8659@rit.edu>
