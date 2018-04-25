Name:           tigeros-ui-tweaks
Version:        1
Release:        5%{?dist}
Summary:        TigerOS User Interface Tweaks

License:        GPLv3+
URL:            https://github.com/RITlug/tigeros-ui-tweaks
Source0:        %{name}-%{version}-%{release}.tar.gz

BuildArch:      noarch
Requires:       bash
Requires:       paper-icon-theme
Requires:       arc-theme

%description
Various UI tweaks and modifications for TigerOS. 
Such changes include paper-icons and changing to 
a default dark GTK theme.

%prep
%setup -q

%pre
dnf -y config-manager --add-repo \
    https://download.opensuse.org/repositories/home:snwh:paper/Fedora_25/home:paper.repo

%install
%{__mkdir_p} %{buildroot}%{_prefix}/local/bin
%{__mkdir_p} %{buildroot}%{_datadir}/glib-2.0/schemas
install -p -m 755 dark-theme %{buildroot}%{_prefix}/local/bin/dark-theme
install -p -m 755 paper-icon-theme %{buildroot}%{_prefix}/local/bin/paper-icon-theme
install -p -m 644 tigeros.ui-tweaks.gschema.override %{buildroot}%{_datadir}/glib-2.0/schemas/tigeros.ui-tweaks.gschema.override

%post
exec .%{_prefix}/local/bin/dark-theme
exec .%{_prefix}/local/bin/dark-theme
glib-compile-schemas /usr/share/glib-2.0/schemas/ 2>/dev/null
dconf update

%postun
# remove dark-theme
path="/home/$USER/.config/gtk-3.0"
cmd=$( grep "gtk-application-prefer-dark-theme" \
    $path/settings.ini | tail -c 2 )

if [ $cmd -eq 1 ]
then
    sed -i 's/1/0' $path/settings.ini
fi

# remove paper-icon-theme
dnf remove -y paper-icon-theme

# remove arc-darker
dnf remove -y arc-theme
rm /usr/share/glib-2.0/schemas/tigeros.ui-tweaks.gschema.override
glib-compile-schemas /usr/share/glib-2.0/schemas/ 2>/dev/null
dconf update

%files
%{_prefix}/local/bin/dark-theme
%{_prefix}/local/bin/paper-icon-theme
%defattr(-,root,root,-)
%doc LICENSE
%{_datadir}/glib-2.0/schemas/tigeros.ui-tweaks.gschema.override

%changelog
* Wed Apr 25 2018 Tim Zabel <tjz8659@rit.edu> - 1.0-5
- Add Arc-Dark gschema installation

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
