%define		_class		Config
%define		upstream_name	%{_class}

Name:		php-pear-%{upstream_name}
Version:	1.10.12
Release:	5
Summary:	Class for reading and writing Config-"files"
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/Config/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
The Config package provides methods for editing configuration
datasources. It does so in an object oriented manner, defining each
and every items found in the config datasource as a Config_Container
of various types (comments, sections, directives, blanks, ...). Items
can then be edited, added, removed, inserted. This package is not
intended for reading configuration data only, but for editing them. If
you only want to read your configuration data, use functions like
parse_ini_file() and the like instead, they are much faster.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/docs/*
%{_datadir}/pear/%{_class}.php
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.10.12-2mdv2011.0
+ Revision: 667486
- mass rebuild

* Wed Dec 29 2010 Oden Eriksson <oeriksson@mandriva.com> 1.10.12-1mdv2011.0
+ Revision: 625888
- 1.10.12

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 1.10.11-7mdv2011.0
+ Revision: 607091
- rebuild

* Sun Dec 13 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.10.11-6mdv2010.1
+ Revision: 478290
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.10.11-5mdv2010.0
+ Revision: 426604
- rebuild

* Wed Dec 31 2008 Oden Eriksson <oeriksson@mandriva.com> 1.10.11-4mdv2009.1
+ Revision: 321800
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.10.11-3mdv2009.0
+ Revision: 224688
- rebuild

* Tue Mar 04 2008 Oden Eriksson <oeriksson@mandriva.com> 1.10.11-2mdv2008.1
+ Revision: 178501
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Jul 23 2007 Oden Eriksson <oeriksson@mandriva.com> 1.10.11-1mdv2008.0
+ Revision: 54557
- 1.10.11

* Fri Apr 20 2007 Oden Eriksson <oeriksson@mandriva.com> 1.10.10-1mdv2008.0
+ Revision: 15534
- 1.10.10


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 1.10.6-1mdv2007.0
+ Revision: 81078
- Import php-pear-Config

* Sat Apr 08 2006 Oden Eriksson <oeriksson@mandriva.com> 1.10.6-1mdk
- 1.10.6

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 1.10.5-1mdk
- 1.10.5
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 1.10.4-6mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 1.10.4-5mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 1.10.4-4mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 1.10.4-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 1.10.4-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 1.10.4-1mdk
- initial Mandriva package (PLD import)

