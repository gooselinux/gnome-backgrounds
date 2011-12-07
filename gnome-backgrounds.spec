Summary: Desktop backgrounds packaged with the GNOME desktop
Name: gnome-backgrounds
Version: 2.28.0
Release: 2%{?dist}
License: GPLv2
Group: Applications/Multimedia
URL: http://www.gnome.org
Source0: http://download.gnome.org/sources/gnome-backgrounds/2.28/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch
BuildRequires: intltool
BuildRequires: gettext

Patch0: gnome-backgrounds-paths.patch

# update translations
# https://bugzilla.redhat.com/show_bug.cgi?id=589197
Patch1: gnome-backgrounds-translations.patch

%description
The gnome-backgrounds package contains images and tiles
to use for your desktop background which are packaged
with the GNOME desktop.

%prep
%setup -q
%patch0 -p1 -b .paths
%patch1 -p1 -b .translations

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_datadir}/backgrounds/images

mv $RPM_BUILD_ROOT%{_datadir}/pixmaps/backgrounds/gnome/abstract $RPM_BUILD_ROOT%{_datadir}/backgrounds
mv $RPM_BUILD_ROOT%{_datadir}/pixmaps/backgrounds/gnome/nature $RPM_BUILD_ROOT%{_datadir}/backgrounds

# all translations are merged back into xml by intltool
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc COPYING NEWS README AUTHORS
%{_datadir}/gnome-background-properties
%dir %{_datadir}/backgrounds
%{_datadir}/backgrounds/*

%changelog
* Mon May 10 2010 Matthias Clasen <mclasen@redhat.com> - 2.28.0-2
- Updated translations
Resolves: #589197

* Mon Sep 21 2009 Matthias Clasen <mclasen@redhat.com> - 2.28.0-1
- Update to 2.28.0

* Mon Sep  7 2009 Matthias Clasen <mclasen@redhat.com> - 2.27.91-1
- Update to 2.27.91

* Sun Aug  2 2009 Matthias Clasen <mclasen@redhat.com> - 2.24.1-3
- Co-own /usr/share/backgrounds instead of requiring desktop-backgrounds-basic

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.24.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Mar 17 2009 Matthias Clasen <mclasen@redhat.com> - 2.24.1-1
- Update to 2.24.1

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.24.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Oct 28 2008 Lennart Poettering <lpoetter@redhat.com> - 2.24.0-3
- Include AUTHORS file in package

* Fri Oct 10 2008 Matthias Clasen <mclasen@redhat.com> - 2.24.0-2
- Don't ship unneeded translations

* Tue Sep 23 2008 Matthias Clasen <mclasen@redhat.com> - 2.24.0-1
- Update to 2.24.0

* Mon Sep  8 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.92-1
- Update to 2.23.92

* Tue Sep  2 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.91-1
- Update to 2.23.91

* Fri Aug 22 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.90-1
- Update to 2.23.90

* Tue Jul 22 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.0-1
- Update to 2.23.0

* Mon Mar 10 2008 Matthias Clasen <mclasen@redhat.com> - 2.22.0-1
- Update to 2.22.0

* Mon Sep 17 2007 Matthias Clasen <mclasen@redhat.com> - 2.20.0-1
- Update to 2.20.0

* Wed Aug 15 2007 Matthias Clasen <mclasen@redhat.com> - 2.18.3-2
- Small fixes from package review

* Tue Aug  7 2007 Matthias Clasen <mclasen@redhat.com> - 2.18.3-1
- Update to 2.18.3
- Update the license field

* Sun Jun 17 2007 Matthias Clasen <mclasen@redhat.com> - 2.16.2-1
- Update to 2.16.2
- Require desktop-backgrounds-basic for directory ownership

* Sat Oct 21 2006 Matthias Clasen <mclasen@redhat.com> - 2.16.1-1
- Update to 2.16.1

* Mon Aug 21 2006 Matthias Clasen <mclasen@redhat.com> - 2.15.92-1.fc6
- Update to 2.15.92

* Fri Jun  9 2006 Matthias Clasen <mclasen@redhat.com> - 2.14.2.1-3
- Add missing BuildRequires

* Thu Jun  1 2006 Matthias Clasen <mclasen@redhat.com> - 2.14.2.1-2
- Update to 2.14.2.1

* Mon Mar 13 2005 Ray Strode <rstrode@redhat.com> - 2.14.0-1
- Update to 2.14.0

* Mon Jan 31 2005 Matthias Clasen <mclasen@redhat.com> - 2.9.90-1
- Initial build.

