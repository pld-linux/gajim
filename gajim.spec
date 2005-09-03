# TODO
# - use /usr/share/locale
#
Summary:	A Jabber client written in PyGTK
Summary(pl):	Klient Jabbera napisany w PyGTK
Name:		gajim
Version:	0.8.1
Release:	0.1
License:	GPL
Group:		Applications/Communications
Source0:	http://gajim.org/downloads/%{name}-%{version}.tar.bz2
# Source0-md5:	d4cbbd64078b9c93fdd1492c27dbcdab
Patch0:		%{name}-makefile.patch
Patch1:		%{name}-remote.patch
URL:		http://www.gajim.org/
BuildRequires:	gtkspell-devel
BuildRequires:	gettext-devel
BuildRequires:	python-pygtk-devel
%pyrequires_eq	python-modules
%pyrequires_eq	python
Requires:	python-dbus
Requires:	python-dns
Requires:	python-gnome-extras-egg >= 2.10.0
Requires:	python-gnome-extras-gtkspell >= 2.10.0
Requires:	python-pygtk-glade >= 2.6.0
Requires:	python-pygtk-gtk >= 2.6.0
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
%patch0 -p1
%patch1 -p1

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README Changelog
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/*.so
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_mandir}/man1/*
%{_pixmapsdir}/*.png
