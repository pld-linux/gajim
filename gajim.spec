%define		_snap	20061012
%define		_snap_with_dashes 2006-10-12
Summary:	A Jabber client written in PyGTK
Summary(pl):	Klient Jabbera napisany w PyGTK
Name:		gajim
Version:	0.11.0
Release:	0.%{_snap}.1
License:	GPL v2
Group:		Applications/Communications
Source0:	http://www.gajim.org/downloads/snap/%{name}-%{_snap_with_dashes}.tar.gz
# Source0-md5:	d16bac44a496ad1b70a92efba3903fa8
URL:		http://www.gajim.org/
BuildRequires:	gettext-devel
BuildRequires:	gtkspell-devel
BuildRequires:	intltool
BuildRequires:	python-pygtk-devel >= 2.8.0
BuildRequires:	rpmbuild(macros) >= 1.177
BuildRequires:	rpm-pythonprov
BuildRequires:	xorg-lib-libXScrnSaver-devel
%pyrequires_eq	python-modules
%pyrequires_eq	python
Requires:	python-docutils >= 0.4-2
Requires:	python-dns
Requires:	python-pygtk-glade >= 2.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gajim is a Jabber client written in PyGTK. The goal of Gajim's
developers is to provide a full featured and easy to use XMPP client
for the GTK+ users. Gajim does not require GNOME to run, eventhough it
exists with it nicely.

%description -l pl
Gajim to klient Jabbera napisany w PyGTK. Celem tw�rc�w Gajima jest
dostarczenie w pe�ni funkcjonalnego i �atwego w u�yciu klienta XMPP
dla u�ytkownik�w GTK+. Gajim nie wymaga do dzia�ania GNOME, cho�
dzia�a z nim �adnie.

%prep
%setup -q

%build
%{__intltoolize}
%{__aclocal} -I m4
%{__libtoolize}
%{__autoheader}
%{__autoconf}
%{__automake}
%{configure}
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

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%banner %{name} -e << EOF
For full functionality, you need to install:
- avahi-discover (for zeroconf chat over local networks)
- python-dbus (for gajim-remote and notification-daemon support)
- python-gnome-gconf (for xmpp url-handler in GNOME)
- python-sqlite (for logs)
EOF

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
