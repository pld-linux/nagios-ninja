# TODO
# - system kohana (uses v2.3.1)
Summary:	NInja, Nagios GUI, GUI, User Interface
Summary(pl.UTF-8):	-
Name:		nagios-ninja
Version:	1.1.0
Release:	0.3
License:	GPL v2
Group:		Applications/WWW
Source0:	http://www.op5.org/op5media/op5.org/downloads/ninja-%{version}.tar.gz
# Source0-md5:	f9df45b7761a3081e0a1893f2ff77cf5
Source1:	apache.conf
Source2:	lighttpd.conf
URL:		http://www.op5.org/community/plugin-inventory/op5-projects/ninja
Requires:	/usr/bin/php
Requires:	nagios >= 3.0
Requires:	nagios-merlin >= 0.9.0
Requires:	php-common >= 4:5.1.6
Requires:	php-iconv
Requires:	php-pcre
Requires:	php-session
Requires:	php-simplexml
Requires:	php-spl
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_webapps	/etc/webapps
%define		_webapp		ninja
%define		_sysconfdir	%{_webapps}/%{_webapp}
%define		appdir		%{_datadir}/%{_webapp}

%description
The Ninja project is an effort to develop an alternative Nagios gui
with the aim of being the most useful Open Source web front end for
Nagios. You will be able to use them as a combination or replacement
to the existing Nagios CGI's. Ninja is in steady development so we
would love to get your input, ideas or most preferibly patches ;)

%prep
%setup -q -n ninja-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{appdir}/htdocs}
cp -a index.php application modules system $RPM_BUILD_ROOT%{appdir}
# as per http://docs.kohanaphp.com/installation/deployment
ln -s ../index.php $RPM_BUILD_ROOT%{appdir}/htdocs

cp -a %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/apache.conf
cp -a %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/lighttpd.conf
cp -a $RPM_BUILD_ROOT%{_sysconfdir}/{apache,httpd}.conf

%clean
rm -rf $RPM_BUILD_ROOT

%triggerin -- apache1 < 1.3.37-3, apache1-base
%webapp_register apache %{_webapp}

%triggerun -- apache1 < 1.3.37-3, apache1-base
%webapp_unregister apache %{_webapp}

%triggerin -- apache < 2.2.0, apache-base
%webapp_register httpd %{_webapp}

%triggerun -- apache < 2.2.0, apache-base
%webapp_unregister httpd %{_webapp}

%triggerin -- lighttpd
%webapp_register lighttpd %{_webapp}

%triggerun -- lighttpd
%webapp_unregister lighttpd %{_webapp}

%files
%defattr(644,root,root,755)
%doc docs/COPYRIGHT docs/README
%dir %attr(750,root,http) %{_sysconfdir}
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/apache.conf
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/httpd.conf
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/lighttpd.conf
%{appdir}
