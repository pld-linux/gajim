
%define	snap		20110531
%define	snap_date	2011-05-31

Summary:	A Jabber client written in PyGTK
Summary(pl.UTF-8):	Klient Jabbera napisany w PyGTK
Name:		gajim
Version:	0.15.0
Release:	0.%{snap}.1
Epoch:		1
License:	GPL v2
Group:		Applications/Communications
Source0:	http://www.gajim.org/downloads/snap/%{name}-%{snap_date}.tar.gz
# Source0-md5:	fbec05d05eb557de97e03c3421a42012
URL:		http://www.gajim.org/
BuildRequires:	gtkspell-devel
BuildRequires:	pkgconfig
BuildRequires:	python-pygtk-devel >= 2.8.0
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.177
BuildRequires:	xorg-lib-libSM-devel
BuildRequires:	xorg-lib-libXScrnSaver-devel
Requires:	python-modules-sqlite
%pyrequires_eq	python-modules
%pyrequires_eq	python
BuildConflicts:	gnustep-gui-devel
Requires:	python-dns
Requires:	python-docutils >= 0.4-2
Requires:	python-pygtk-glade >= 2.8.0
Suggests:	dbus(org.freedesktop.Notifications)
Suggests:	gnome-keyring
Suggests:	gnupg2
Suggests:	gpgme >= 1.0.0
Suggests:	python-Crypto
Suggests:	python-avahi
Suggests:	python-dbus >= 0.82.1
Suggests:	python-farsight2
Suggests:	python-gnome-desktop-keyring
Suggests:	python-gnome-gconf
Suggests:	python-gnome-ui
Suggests:	python-gstreamer
Suggests:	python-pyOpenSSL >= 0.9
Suggests:	python-sexy
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
%setup -q -n %{name}-0.14.0.1-76858b8db934

%build
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
%doc AUTHORS ChangeLog README THANKS THANKS.artists
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_mandir}/man1/*
%{_iconsdir}/hicolor/64x64/apps/gajim.png
%{_iconsdir}/hicolor/scalable/apps/gajim.svg
%{_docdir}/gajim
