Summary:	Collection of CMake functions specific to the LDAS Tools Suite
Summary(pl.UTF-8):	Zbiór funkcji CMake dla zestawu narzędzi LDAS Tools
Name:		ldas-tools-cmake
Version:	1.3.0
Release:	1
License:	GPL v2+
Group:		Development/Libraries
Source0:	http://software.igwn.org/lscsoft/source/%{name}-%{version}.tar.gz
# Source0-md5:	a4cbdff87cbb1cb2cd554188f818e0d1
URL:		https://wiki.ligo.org/Computing/LDASTools
BuildRequires:	cmake >= 3.0.2
BuildRequires:	igwn-cmake-macros >= 1.3.2
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	sed >= 4.0
Requires:	cmake >= 3.0.2
Requires:	igwn-cmake-macros >= 1.3.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This collection of cmake macros was developed as part of the LDAS
Tools Suite to have consitency across all of the packages.

%description -l pl.UTF-8
Ten zbiór makr cmake'a powstał jako część zestawu narzędzi LDAP Tools,
aby zachować spójność między pakietami.

%prep
%setup -q

# to make package noarch
%{__sed} -i -e '/^libdir=/d' config/ldastoolscmake.pc.in

%build
install -d build
cd build
%cmake .. \
	-DCMAKE_INSTALL_DATADIR=share

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog.md
%dir %{_datadir}/ldas-tools
%{_datadir}/ldas-tools/cmake
%{_npkgconfigdir}/ldastoolscmake.pc
