Summary:	A Jabber client written in PyGTK
Summary(pl.UTF-8):	Klient Jabbera napisany w PyGTK
Name:		gajim
Version:	0.16.7
Release:	2
Epoch:		1
License:	GPL v3+
Group:		Applications/Communications
Source0:	http://gajim.org/downloads/0.16/%{name}-%{version}.tar.bz2
# Source0-md5:	08d6fc3025977700e5bafde12cda36f4
URL:		http://www.gajim.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRequires:	gtkspell-devel
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	python-pygtk-devel >= 2.8.0
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.177
BuildRequires:	xorg-lib-libSM-devel
BuildRequires:	xorg-lib-libXScrnSaver-devel
Requires:	hicolor-icon-theme
Requires:	python-modules-sqlite
%pyrequires_eq	python-modules
%pyrequires_eq	python
BuildConflicts:	gnustep-gui-devel
Requires:	python-dns
Requires:	python-docutils >= 0.4-2
Requires:	python-nbxmpp
Requires:	python-pygtk-glade >= 2.8.0
Suggests:	dbus(org.freedesktop.Notifications)
Suggests:	gnome-keyring
Suggests:	gnupg2
Suggests:	gpgme >= 1.0.0
Suggests:	python-Crypto
Suggests:	python-avahi
Suggests:	python-dbus >= 0.82.1
Suggests:	python-gnome-desktop-keyring
Suggests:	python-gnome-gconf
Suggests:	python-gnome-ui
Suggests:	python-pyOpenSSL >= 0.9
Suggests:	python-pyasn1
Suggests:	python-modules-sqlite
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

cp -a plugins/plugin_installer/*.pem $RPM_BUILD_ROOT%{_datadir}/%{name}/plugins/plugin_installer/

%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/nb_NO

[ -d $RPM_BUILD_ROOT%{_datadir}/locale/sr@latin ] || \
       mv -f $RPM_BUILD_ROOT%{_datadir}/locale/sr@{Latn,latin}
%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README THANKS THANKS.artists
%attr(755,root,root) %{_bindir}/gajim*
%{_datadir}/%{name}
%{_desktopdir}/gajim.desktop
%{_desktopdir}/gajim-remote.desktop
%{_mandir}/man1/*.1*
%{_iconsdir}/hicolor/64x64/apps/gajim.png
%{_iconsdir}/hicolor/128x128/apps/gajim.png
%{_iconsdir}/hicolor/scalable/apps/gajim.svg
