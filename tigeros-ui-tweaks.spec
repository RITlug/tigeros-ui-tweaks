Name:           tigeros-ui-tweaks
Version:        1.0
Release:        1.0
Summary:        TigerOS User Interface Tweaks

License:        GPLv3+
URL:            https://github.com/RITlug/TigerOS
Source0:        %{name}-{version}.tar.gz

Prefix:         /usr
Requires:       bash
BuildArch:      noarch

%description
Various UI tweaks and modifications for TigerOS

%prep
%setup -q

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_prefix}/local/share
install -m 0644 dark-theme %{buildroot}%{_prefix}/local/share
install -m 0644 paper-icon-theme %{buildroot}%{_prefix}/local/share

%clean
rm -rf %{buildroot}

%post
exec .%{_prefix}/local/bin/dark-theme
exec .%{_prefix}/local/bin/dark-theme

%files
%{_prefix}/local/bin/dark-theme
%{_prefix}/local/bin/paper-icon-theme

%changelog
*  Feb 9, 2018 Tim Zabel <tjz8659@rit.edu> - 1.0-2
- Added files
- Updated spec file
*  Nov 3 2017 Aidan Kahrs <axk4545@rit.edu> - 1.0-1
- Initial package for TigerOS
