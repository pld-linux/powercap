Summary:	Powercap sysfs C Bindings and Utilities
Summary(pl.UTF-8):	Wiązania C i narzędzia do interfejsu sysfs powercap
Name:		powercap
Version:	0.3.1
Release:	1
License:	BSD
Group:		Applications/System
#Source0Download: https://github.com/powercap/powercap/releases
Source0:	https://github.com/powercap/powercap/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	5ad0b2f60f1adaeba97cb8d0fa5b598b
URL:		https://github.com/powercap/powercap
BuildRequires:	cmake >= 2.8.12
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This project provides the powercap library - a generic C interface to
the Linux power capping framework (sysfs interface). It includes an
implementation for working with Intel Running Average Power Limit
(RAPL).

%description -l pl.UTF-8
Ten projekt dostarcza bibliotekę powercap - ogólny interfejs C do
szkieletu Linuksa ograniczającego zużycie energii (przez interfejs
sysfs). Zawiera implementację działającą z Intel RAPL (Running Average
Power Limit).

%package devel
Summary:	Header files for powercap library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki powercap
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for powercap library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki powercap.

%prep
%setup -q

%build
install -d build
cd build
%cmake ..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS LICENSE README.md RELEASES.md
%attr(755,root,root) %{_bindir}/powercap-info
%attr(755,root,root) %{_bindir}/powercap-set
%attr(755,root,root) %{_bindir}/rapl-info
%attr(755,root,root) %{_bindir}/rapl-set
%attr(755,root,root) %{_libdir}/libpowercap.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpowercap.so.0
%{_mandir}/man1/powercap-info.1*
%{_mandir}/man1/powercap-set.1*
%{_mandir}/man1/rapl-info.1*
%{_mandir}/man1/rapl-set.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpowercap.so
%{_includedir}/powercap
%{_pkgconfigdir}/powercap.pc
