Name:           moblin-ux-settings
Version:        0.19
Release:        %mkrel 1
Summary:        Package to set schemas for the Moblin Shell
Group:          Desktop/Interface
License:        LGPLv2.1
URL:            http://www.moblin.org
Source0:        README
Source1:        %gconf-tree.xml
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:      noarch

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

%install
cp %{SOURCE0} .
install -d $RPM_BUILD_ROOT%{_sysconfdir}/gconf/gconf.xml.moblin
install -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/gconf/gconf.xml.moblin

%files
%defattr(-,root,root,-)
%doc README
%{_sysconfdir}/gconf/gconf.xml.moblin/%gconf-tree.xml