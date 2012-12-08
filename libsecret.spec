%define	api	1
%define	major	0
%define	libname	%mklibname secret %{api} %{major}
%define	girname	%mklibname secret-gir %{api} 
%define	devname	%mklibname secret -d

Summary:	Library for accessing the Secret Service API
Name:		libsecret
Version:	0.8
Release:	1
License:	LGPLv2+
Group:		System/Libraries
Url:		http://www.gnome.org/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libsecret/%{name}-%{version}.tar.xz
BuildRequires:	intltool
BuildRequires:	libgcrypt-devel
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)

%description
libsecret is a library for storing and retrieving passwords and other
secrets. It communicates with the "Secret Service" using DBus.

%package tools
Summary:	Library for accessing the Secret Service API -- Tools
Group:		System/Libraries

%description tools
libsecret is a library for storing and retrieving passwords and other
secrets. It communicates with the "Secret Service" using DBus.

%package -n %{libname}
Summary:	Library for accessing the Secret Service API
Group:		System/Libraries

%description -n %{libname}
This package contains the shared library for %{name}.

%package -n %{girname}
Summary:	GObject Introspection interface description for %{name}
Group:		System/Libraries

%description -n %{girname}
GObject Introspection interface description for %{name}.

%package -n %{devname}
Summary:	Library for accessing the Secret Service API -- Development Files
Group:		Development/C
Requires:	%{libname} = %{version}
Requires:	%{girname} = %{version}

%description -n %{devname}
This package contains the development files for %{name}.

%prep
%setup -q

%build
%configure2_5x \
	--disable-static

%make

%install
%makeinstall_std

%find_lang %{name}

%files tools -f %{name}.lang
%doc AUTHORS COPYING NEWS README
%{_bindir}/secret-tool

%files -n %{libname}
%{_libdir}/libsecret-%{api}.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/Secret-%{api}.typelib
%{_libdir}/girepository-1.0/SecretUnstable-0.typelib

%files -n %{devname}
%{_libdir}/libsecret-%{api}.so
%{_libdir}/pkgconfig/libsecret-%{api}.pc
%{_libdir}/pkgconfig/libsecret-unstable.pc
%{_includedir}/libsecret-%{api}/
%{_datadir}/gir-1.0/Secret-%{api}.gir
%{_datadir}/gir-1.0/SecretUnstable-0.gir
%doc %{_datadir}/gtk-doc/html/libsecret-%{api}/



%changelog
* Mon Aug 06 2012 Matthew Dawkins <mattydaw@mandriva.org> 0.8-1
+ Revision: 811873
- update to new version 0.8

* Mon Jul 16 2012 Matthew Dawkins <mattydaw@mandriva.org> 0.7-1
+ Revision: 809890
- update to new version 0.7

* Sat Jul 14 2012 Matthew Dawkins <mattydaw@mandriva.org> 0.6-1
+ Revision: 809291
- another new version 0.6
- new api 1
- updated files lists
- update to new version 0.5

* Mon Jun 25 2012 Matthew Dawkins <mattydaw@mandriva.org> 0.3-1
+ Revision: 806812
- imported package libsecret

