Name:           moblin-ux-settings
Version:        0.19
Release:        %mkrel 3
Summary:        Package to set schemas for the Moblin Shell
Group:          Graphical desktop/Other
License:        LGPLv2.1
URL:            https://www.moblin.org
Source0:        README
Source1:        %gconf-tree.xml
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:      noarch

BuildRequires:	GConf2

Requires: gnome-vfs2
Requires: nautilus
Requires: fonts-ttf-droid
Requires: mutter-moblin
Requires: mojito
Requires: moblin-gtk-engine
Requires: moblin-icon-theme
Requires: moblin-sound-theme
Requires: moblin-panel-applications
Requires: moblin-panel-media
Requires: moblin-panel-myzone
Requires: moblin-panel-pasteboard
Requires: moblin-panel-people
Requires: moblin-panel-status
Requires: moblin-web-browser-panel

%description
Package to install Moblin schema file.

%prep
%setup -q -c -T
cp -a %{_sysconfdir}/gconf/2/path gconf.path

%build
sed -i -e 's@\(include /etc/gconf/2/local-defaults.path\)@\1\n\n# Moblin settings.\nxml:readonly:/etc/gconf/gconf.xml.moblin@' gconf.path

%install
cp %{SOURCE0} .
install -d $RPM_BUILD_ROOT%{_sysconfdir}/gconf/gconf.xml.moblin
install -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/gconf/gconf.xml.moblin

mkdir -p %{buildroot}%{_sysconfdir}/gconf/2
cp gconf.path %{buildroot}%{_sysconfdir}/gconf/2/moblin.path

%files
%defattr(-,root,root,-)
%doc README
%{_sysconfdir}/gconf/gconf.xml.moblin/%gconf-tree.xml
%{_sysconfdir}/gconf/2/moblin.path


%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.19-3mdv2011.0
+ Revision: 620386
- the mass rebuild of 2010.0 packages

* Wed Oct 07 2009 Olivier Blin <oblin@mandriva.com> 0.19-2mdv2010.0
+ Revision: 455666
- build a /etc/gconf/2/moblin.path including moblin defaults
  to be used with GCONF_DEFAULT_SOURCE_PATH in moblin-session
  (idea from /sbrabec:/branches:/Moblin:/UI/openSUSE_Factory)
- revert hijacking of /etc/gconf/2/path, we will do this cleanly in the moblin session
- use /etc/gconf/gconf.xml.moblin by default in GConf

* Wed Oct 07 2009 Olivier Blin <oblin@mandriva.com> 0.19-1mdv2010.0
+ Revision: 455340
- fix group
- initial import (from Caio Begotti, based on Moblin package)
- Created package structure for moblin-ux-settings.

