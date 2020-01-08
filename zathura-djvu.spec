Summary:	DjVu support for zathura
Summary(pl.UTF-8):	Obsługa DjVu dla zathury
Name:		zathura-djvu
Version:	0.2.9
Release:	1
License:	BSD-like
Group:		Applications/Publishing
Source0:	https://pwmt.org/projects/zathura-djvu/download/%{name}-%{version}.tar.xz
# Source0-md5:	414a6a3dd040a714f40d49ce5fcf3d7e
URL:		https://pwmt.org/projects/zathura-djvu/
BuildRequires:	cairo-devel
BuildRequires:	djvulibre-devel
# C11
BuildRequires:	gcc >= 6:4.7
BuildRequires:	girara-devel >= 0.1.8
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	meson >= 0.43
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.727
BuildRequires:	zathura-devel >= 0.3.8
Requires(post,postun):	desktop-file-utils
Requires:	girara >= 0.1.8
Requires:	zathura >= 0.3.8
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

%meson_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install -C build

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
