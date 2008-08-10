%define		snap	20080810
%define		snap_date	2008-08-10
Summary:	A Jabber client written in PyGTK
Summary(pl.UTF-8):	Klient Jabbera napisany w PyGTK
Name:		gajim
Version:	0.11.4.4
Release:	0.%{snap}.1
Epoch:		1
License:	GPL v2
Group:		Applications/Communications
Source0:	http://www.gajim.org/downloads/snap/%{name}-%{snap_date}.tar.gz
# Source0-md5:	0153260f2ccfa5b3d9edb811d23f2510
URL:		http://www.gajim.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtkspell-devel
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	python-pygtk-devel >= 2.8.0
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.177
BuildRequires:	xorg-lib-libSM-devel
BuildRequires:	xorg-lib-libXScrnSaver-devel
%pyrequires_eq	python-modules
%pyrequires_eq	python
Requires:	python-dns
Requires:	python-docutils >= 0.4-2
Requires:	python-pygtk-glade >= 2.8.0
Requires:	python-sqlite
Suggests:	gpgme >= 1.0.0
Suggests:	python-avahi
Suggests:	python-dbus >= 0.82.1
Suggests:	python-gnome-desktop-keyring
Suggests:	python-gnome-gconf
Suggests:	python-pyOpenSSL
Suggests:	python-sqlite
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gajim is a Jabber client written in PyGTK. The goal of Gajim's
developers is to provide a full featured and easy to use XMPP client
for the GTK+ users. Gajim does not require GNOME to run, eventhough it
exists with it nicely.

%description -l pl.UTF-8
Gajim to klient Jabbera napisany w PyGTK. Celem twórców Gajima jest
dostarczenie w pełni funkcjonalnego i łatwego w użyciu klienta XMPP
dla użytkowników GTK+. Gajim nie wymaga do działania GNOME, choć
działa z nim ładnie.

%prep
%setup -q -n %{name}-%{version}-svn

%build
%{__intltoolize}
%{__aclocal} -I m4
%{__libtoolize}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure

%{__make} \
	CC="%{__cc}" \
	PREFIX=%{_prefix} \
	LIBDIR=/%{_lib}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	PREFIX=%{_prefix} \
	LIBDIR=/%{_lib} \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_datadir}/%{name}/{setup_win32.pyo}
rm -r $RPM_BUILD_ROOT%{_datadir}/locale/no

rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/*.la

[ -d $RPM_BUILD_ROOT%{_datadir}/locale/sr@latin ] || \
       mv -f $RPM_BUILD_ROOT%{_datadir}/locale/sr@{Latn,latin}
%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README THANKS
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/*.so
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_mandir}/man1/*
%{_pixmapsdir}/*.png
