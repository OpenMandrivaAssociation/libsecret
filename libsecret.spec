%define url_ver %(echo %{version}|cut -d. -f1,2)

%define	api 1
%define	major 0
%define	libname %mklibname secret %{api} %{major}
%define	girname %mklibname secret-gir %{api}
%define	devname %mklibname secret -d

Summary:	Library for accessing the Secret Service API
Name:		libsecret
Version:	0.20.4
Release:	2
License:	LGPLv2+
Group:		System/Libraries
Url:		http://www.gnome.org/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libsecret/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	xsltproc
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(libgcrypt)
BuildRequires:	pkgconfig(gpg-error)
BuildRequires:	vala-tools
BuildRequires:	pkgconfig(vapigen)

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
%configure \
	--enable-introspection=yes \
	--enable-vala=yes \
	--disable-static

%make_build

%install
%make_install

%find_lang %{name}

%files tools -f %{name}.lang
%doc AUTHORS COPYING NEWS README
%{_bindir}/secret-tool
%{_mandir}/man1/secret-tool.1*

%files -n %{libname}
%{_libdir}/libsecret-%{api}.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/Secret-%{api}.typelib

%files -n %{devname}
%{_libdir}/libsecret-%{api}.so
%{_libdir}/pkgconfig/libsecret-%{api}.pc
%{_libdir}/pkgconfig/libsecret-unstable.pc
%{_includedir}/libsecret-%{api}/
%{_datadir}/gir-1.0/Secret-%{api}.gir
%{_datadir}/vala/vapi/*
%doc %{_datadir}/gtk-doc/html/libsecret-%{api}/
