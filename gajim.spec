# TODO
# - --disable-coca flag for configure seems to be broken, so
#   I've added BC: gnustep-gui-devel. Of course better sollution
#   is to fix configure.*
Summary:	A Jabber client written in PyGTK
Summary(pl.UTF-8):	Klient Jabbera napisany w PyGTK
Name:		gajim
Version:	0.12.1
Release:	1
Epoch:		1
License:	GPL v2
Group:		Applications/Communications
Source0:	http://gajim.org/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	195a7973d3fbfb538e2ee74156aa6e9e
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
BuildConflicts:	gnustep-gui-devel
Requires:	python-dns
Requires:	python-docutils >= 0.4-2
Requires:	python-pygtk-glade >= 2.8.0
Requires:	python-sqlite
Suggests:	gnome-keyring
Suggests:	gnupg2
Suggests:	gpgme >= 1.0.0
Suggests:	notification-daemon
Suggests:	python-Crypto
Suggests:	python-avahi
Suggests:	python-dbus >= 0.82.1
Suggests:	python-gnome-desktop-keyring
Suggests:	python-gnome-gconf
Suggests:	python-gnome-ui
Suggests:	python-pyOpenSSL
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
%setup -q

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
%doc AUTHORS ChangeLog README THANKS THANKS.artists
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/*.so
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_mandir}/man1/*
%{_pixmapsdir}/*.png
