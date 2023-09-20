%define url_ver %(echo %{version}|cut -d. -f1,2)

%define	api 1
%define	major 0
%define	libname %mklibname secret %{api} %{major}
%define	girname %mklibname secret-gir %{api}
%define	devname %mklibname secret -d

%global optflags %{optflags} -Wno-incompatible-function-pointer-types

%bcond_without gir

Summary:	Library for accessing the Secret Service API
Name:		libsecret
Version:	0.21.1
Release:	1
License:	LGPLv2+
Group:		System/Libraries
Url:		https://www.gnome.org/
Source0:	https://ftp.gnome.org/pub/GNOME/sources/libsecret/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	gtk-doc
BuildRequires:	meson
BuildRequires:	xsltproc
BuildRequires:	gjs
BuildRequires:	pkgconfig(gi-docgen)
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(glib-2.0)
%if %{with gir}
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	vala-tools
BuildRequires:	pkgconfig(vapigen)
%endif
BuildRequires:	pkgconfig(libgcrypt)
BuildRequires:	pkgconfig(gpg-error)

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
# For compatibility with 3rd party Skype packages from
# https://repo.skype.com/rpm/
Provides:	libsecret = %{EVRD}

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
%autosetup -p1
%meson \
%if %{with gir}
	-Dintrospection=true
%else
	-Dintrospection=false \
	-Dgtk_doc=false
%endif

%build
%meson_build

%install
%meson_install

%find_lang %{name}

%files tools -f %{name}.lang
%doc COPYING NEWS README.md
%if %{with gir}
%doc %{_docdir}/libsecret-1/
%endif
%{_bindir}/secret-tool
%doc %{_mandir}/man1/secret-tool.1*

%files -n %{libname}
%{_libdir}/libsecret-%{api}.so.%{major}*

%if %{with gir}
%files -n %{girname}
%{_libdir}/girepository-1.0/Secret-%{api}.typelib
%endif

%files -n %{devname}
%{_libdir}/libsecret-%{api}.so
%{_libdir}/pkgconfig/libsecret-%{api}.pc
%{_libdir}/pkgconfig/libsecret-unstable.pc
%{_includedir}/libsecret-%{api}/
%if %{with gir}
%{_datadir}/gir-1.0/Secret-%{api}.gir
%{_datadir}/vala/vapi/*
%endif
