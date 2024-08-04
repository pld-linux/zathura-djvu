%define		_zathura_api_ver	%(pkg-config --variable=apiversion zathura)
%define		_zathura_abi_ver	%(pkg-config --variable=abiversion zathura)

Summary:	DjVu support for zathura
Summary(pl.UTF-8):	Obsługa DjVu dla zathury
Name:		zathura-djvu
Version:	0.2.10
Release:	1
License:	BSD-like
Group:		Applications/Publishing
Source0:	https://pwmt.org/projects/zathura-djvu/download/%{name}-%{version}.tar.xz
# Source0-md5:	2c57b30d050ee41d60d93c19c9c017c1
URL:		https://pwmt.org/projects/zathura-djvu/
BuildRequires:	cairo-devel
BuildRequires:	djvulibre-devel
# C17
BuildRequires:	gcc >= 6:8.1.0
BuildRequires:	girara-devel >= 0.1.8
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	meson >= 0.61
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	zathura-devel >= 0.3.8
Requires(post,postun):	desktop-file-utils
Requires:	girara >= 0.1.8
Requires:	zathura >= 0.3.8
Requires:	zathura(plugin-abi) = %_zathura_abi_ver
Requires:	zathura(plugin-api) = %_zathura_api_ver
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The zathura-djvu plugin adds DjVu support to zathura by using the
djvulibre library.

%description -l pl.UTF-8
Wtyczka zathura-djvu dodaje do zathury obsługę DjVu z wykorzystaniem
biblioteki djvulibre.

%prep
%setup -q

%build
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post

%postun
%update_desktop_database_postun

%files
%defattr(644,root,root,755)
%doc AUTHORS LICENSE
%attr(755,root,root) %{_libdir}/zathura/libdjvu.so
%{_desktopdir}/org.pwmt.zathura-djvu.desktop
%{_datadir}/metainfo/org.pwmt.zathura-djvu.metainfo.xml
