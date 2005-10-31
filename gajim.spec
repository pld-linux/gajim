%define		_snap	2005-10-31
Summary:	A Jabber client written in PyGTK
Summary(pl):	Klient Jabbera napisany w PyGTK
Name:		gajim
Version:	0.9
Release:	0.%(echo %{_snap}|tr -d -).1
License:	GPL v2+
Group:		Applications/Communications
Source0:	http://gajim.org/downloads/snap/%{name}-%{_snap}.tar.bz2
# Source0-md5:	a65eeb6778ea083acb327eb30dced4ba
URL:		http://www.gajim.org/
BuildRequires:	gtkspell-devel
BuildRequires:	gettext-devel
BuildRequires:	intltool
BuildRequires:	python-pygtk-devel >= 2.8.0
%pyrequires_eq	python-modules
%pyrequires_eq	python
Requires:	python-dbus
Requires:	python-dns
Requires:	python-gnome-gconf >= 2.12.0
Requires:	python-gnome-extras-egg >= 2.12.0
Requires:	python-gnome-extras-gtkspell >= 2.12.0
Requires:	python-pygtk-glade >= 2.8.0
Requires:	python-pygtk-gtk >= 2.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gajim is a Jabber client written in PyGTK. The goal of Gajim's
developers is to provide a full featured and easy to use XMPP client
for the GTK+ users. Gajim does not require GNOME to run, eventhough it
exists with it nicely.

%description -l pl
Gajim to klient Jabbera napisany w PyGTK. Celem twórców Gajima jest
dostarczenie w pe³ni funkcjonalnego i ³atwego w u¿yciu klienta XMPP
dla u¿ytkowników GTK+. Gajim nie wymaga do dzia³ania GNOME, choæ
dzia³a z nim ³adnie.

%prep
%setup -q

%build
%{__make} \
	PREFIX=%{_prefix} \
	LIBDIR=/%{_lib}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	PREFIX=%{_prefix} \
	LIBDIR=/%{_lib} \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_datadir}/%{name}/{setup_win32.pyo}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README Changelog
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/*.so
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_mandir}/man1/*
%{_pixmapsdir}/*.png
