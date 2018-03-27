Name:           tigeros-ui-tweaks
Version:        1
Release:        4%{?dist}
Summary:        TigerOS User Interface Tweaks

License:        GPLv3+
URL:            https://github.com/RITlug/TigerOS
Source0:        https://builder.ritlug.com/packages/x86_64/%{name}-{version}.tar.gz

Requires:       bash
BuildArch:      noarch

%description
Various UI tweaks and modifications for TigerOS. Such changes include paper-icons 
and changing to a default dark GTK theme.

%prep
%setup -q

%install
%{__mkdir_p} %{buildroot}%{_prefix}/local/bin
install -p -m 755 dark-theme %{buildroot}%{_prefix}/local/bin/dark-theme
install -p -m 755 paper-icon-theme %{buildroot}%{_prefix}/local/bin/paper-icon-theme

%post
exec .%{_prefix}/local/bin/dark-theme
exec .%{_prefix}/local/bin/dark-theme

%files
%doc README.md
%{_prefix}/local/bin/dark-theme
%{_prefix}/local/bin/paper-icon-theme

%changelog
* Mar 27, 2018 Tim Zabel <tjz8659@rit.edu> - 1.0-4
- Removed %clean directive to follow newer Fedora docs
- Updated proper permissioning system
- General cleanup

* Mar 2, 2018 Tim Zabel <tjz8659@rit.edu> - 1.0-3
- Added proper file locations
- Created post section for execution of scripts

*  Feb 9, 2018 Tim Zabel <tjz8659@rit.edu> - 1.0-2
- Added files
- Updated spec file

*  Nov 3 2017 Aidan Kahrs <axk4545@rit.edu> - 1.0-1
- Initial package for TigerOS
