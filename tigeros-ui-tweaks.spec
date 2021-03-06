Name:           tigeros-ui-tweaks
Version:        1.0
Release:        10%{?dist}
Summary:        TigerOS User Interface Tweaks

License:        GPLv3+
URL:            https://github.com/RITlug/tigeros-ui-tweaks
Source0:        %{name}-%{version}-%{release}.tar.gz

BuildArch:      noarch
Requires:       bash
Requires:       paper-icon-theme
Requires:       arc-theme
Requires:       overpass-fonts
Requires:       overpass-mono-fonts

%description
Various UI tweaks and modifications for TigerOS. 
Such changes include paper-icons and changing to 
a default dark GTK theme.

%prep
%setup -q

%install
%{__mkdir_p} %{buildroot}%{_prefix}/local/bin
%{__mkdir_p} %{buildroot}%{_datadir}/glib-2.0/schemas
#install -p -m 755 dark-theme %{buildroot}%{_prefix}/local/bin/dark-theme
install -p -m 644 10_tigeros.ui-tweaks.gschema.override %{buildroot}%{_datadir}/glib-2.0/schemas/10_tigeros.ui-tweaks.gschema.override

%post
#%{_prefix}/local/bin/dark-theme
glib-compile-schemas /usr/share/glib-2.0/schemas/ 2>/dev/null
dconf update

%postun
path="/home/$USER/.config/gtk-3.0"
cmd=$( grep "gtk-application-prefer-dark-theme" \
    $path/settings.ini | tail -c 2 )

# remove dark theme if file exists
if [ -f $path/settings.ini && $cmd -eq 1 ] ; then
    sed -i 's/1/0' $path/settings.ini
fi

rm /usr/share/glib-2.0/schemas/tigeros.ui-tweaks.gschema.override
glib-compile-schemas /usr/share/glib-2.0/schemas/ 2>/dev/null
dconf update

%files
#%{_prefix}/local/bin/dark-theme
%defattr(-,root,root,-)
%license LICENSE
%{_datadir}/glib-2.0/schemas/10_tigeros.ui-tweaks.gschema.override

%changelog
* Wed Oct 17 2018 Tim Zabel <tjz8659@rit.edu> - 1.0-10
- Fedora 29 Build

* Sat Aug 18 2018 Tim Zabel <tjz8659@rit.edu> - 1.0-9
- Remove dark theme installation

* Mon Aug 13 2018 Tim Zabel <tjz8659@rit.edu> - 1.0-8
- Create /etc/skel/.config/gtk-3.0 directory

* Thu Aug 09 2018 Tim Zabel <tjz8659@rit.edu> - 1.0-7
- Fix #8
- Add /etc/skel settings.ini file

* Fri Jun 15 2018 Tim Zabel <tjz8659@rit.edu> - 1.0-6
- fix dark-theme post exec

* Wed Apr 25 2018 Tim Zabel <tjz8659@rit.edu> - 1.0-5
- Add Arc-Dark gschema installation
- Removed snwh:paper repo
- Updated package removal
- paper-icon-theme bash script no longer necessary

* Tue Mar 27 2018 Tim Zabel <tjz8659@rit.edu> - 1.0-4
- Updated to follow newer Fedora docs
- Updated proper permissioning system
- General cleanup

* Fri Mar 2 2018 Tim Zabel <tjz8659@rit.edu> - 1.0-3
- Added proper file locations
- Created post section for execution of scripts

* Fri Feb 9 2018 Tim Zabel <tjz8659@rit.edu> - 1.0-2
- Added files
- Updated spec file

* Fri Nov 3 2017 Aidan Kahrs <axk4545@rit.edu> - 1.0-1
- Initial package for TigerOS
