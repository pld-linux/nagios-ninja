Summary:	NInja, Nagios GUI, GUI, User Interface
Summary(pl.UTF-8):	-
Name:		nagios-ninja
Version:	1.1.0
Release:	0.1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://www.op5.org/op5media/op5.org/downloads/ninja-%{version}.tar.gz
# Source0-md5:	f9df45b7761a3081e0a1893f2ff77cf5
URL:		http://www.op5.org/community/plugin-inventory/op5-projects/ninja
Requires:	nagios-merlin >= 0.9.0
Requires:	php-common >= 4:5.1.6
Requires:	/usr/bin/php
Requires:	nagios >= 3.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		appdir	%{_datadir}/ninja

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
install -d $RPM_BUILD_ROOT%{appdir}
cp -a . $RPM_BUILD_ROOT%{appdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/COPYRIGHT docs/README
%{appdir}
