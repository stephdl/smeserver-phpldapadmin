# $Id: smeserver-phpldapadmin.spec,v 1.8 2013/11/06 22:56:23 unnilennium Exp $
# Authority: nocvs
# Name: Michel Van hees

Summary: PhpLdapAdmin for SME server
%define name smeserver-phpldapadmin
Name: %{name}
%define version 1.5.0
%define release 1
Version: %{version}
Release: %{release}%{?dist}
License: Freely distributable
Group: Apache
Source: %{name}-%{version}.tar.gz
#{name}-%{version}.patch.yyyymmddnn
BuildRoot: /var/tmp/e-smith-buildroot
BuildRequires: e-smith-devtools
BuildArchitectures: noarch
Requires: smeserver-release >= 9
Requires: phpldapadmin >= 1.2.3
AutoReqProv: no

%changelog
* Sat Jun 21 2014 stephane de Labrusse <stephdl@de-labrusse.fr> 1.5.0-1.sme
- Initial release to sme9

* Wed Nov 6 2013 JP Pialasse <tests@pialasse.com> 1.2.3-6.sme
- fix bug [SME: 5762]
- default admin read only but kamikaze mod for root modify access.

* Mon Nov 4 2013 JP Pialasse <tests@pialasse.com> 1.2.3-4.sme
- wrong template path for config file [SME: 7975]
- patching also incorrect template.
- error binding to server swith to http auth to prevent

* Sun May 26 2013 JP Pialasse <tests@pialasse.com> 1.2.3-1.sme
- remove phpldapadmin from package
- added Requires phpldapadmin-1.2.3-1
- clean spec file
- added default db value (patch file)

* Thu Jun  26 2007 Michel Van hees <michel@vanhees.cc>
- Restart contrib from scratch
- Use of phpldapadmin 0.9.8.3

%description
SME server - phpmyadmin multiuser for smeserver

%prep
%setup

%build
perl createlinks

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
rm -f %{name}-%{version}-filelist
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT > %{name}-%{version}-filelist
echo "%doc COPYING"          >> %{name}-%{version}-filelist

%clean 
rm -rf $RPM_BUILD_ROOT

%pre

%preun

%post

%postun

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
