Summary:	Fan control for MacBook
Name:		macfanctld
# note fedora and opensuse repos have same code but version as 3.8.4, wtf
Version:	0.6
Release:	0.1
License:	GPL v3
Group:		X11/Applications
Source0:	https://github.com/MikaelStrom/macfanctld/archive/master.tar.gz?/%{name}-%{version}.tgz
# Source0-md5:	903ee608f5e3a08f5908c581eab456fd
Source1:	%{name}.service
URL:		https://github.com/MikaelStrom/macfanctld
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	rpmbuild(macros) >= 1.647
Requires:	systemd-units >= 38
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
macfanctld is a daemon that reads temperature sensors and adjust the
fan(s) speed on MacBook's. mac‐ fanctld is configurable and logs temp
and fan data to a file. macfanctld uses three sources to deter‐ mine
the fan speeed: 1) average temperature from all sensors, 2) sensor
TC0P [CPU 0 Proximity Temp and 3] and sensor TG0P [GPU 0 Proximity
Temp]. Each source's impact on fan speed can be individually adjusted
to fine tune working temperature on different MacBooks.

Important: macfanctld depends on applesmc-dkms.

%prep
%setup -qc
mv %{name}-*/* .
cp -p %{SOURCE1} .

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_sbindir},%{systemdunitdir}}
install -p macfanctld $RPM_BUILD_ROOT%{_sbindir}
cp -p macfanctl.conf $RPM_BUILD_ROOT%{_sysconfdir}
cp -p macfanctld.service $RPM_BUILD_ROOT%{systemdunitdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/macfanctl.conf
%attr(755,root,root) %{_sbindir}/macfanctld
%{systemdunitdir}/macfanctld.service
