Summary:	A Jabber client written in PyGTK
Summary(pl):	Klient Jabbera napisany w PyGTK
Name:		gajim
Version:	0.9
Release:	2
License:	GPL v2
Group:		Applications/Communications
Source0:	http://gajim.org/downloads/%{name}-%{version}.tar.bz2
# Source0-md5:	351c59ca1a162d134f546385b35bf804
Patch0:		%{name}-typos.patch
URL:		http://www.gajim.org/
BuildRequires:	gettext-devel
BuildRequires:	gtkspell-devel
BuildRequires:	intltool
BuildRequires:	python-pygtk-devel >= 2.8.0
BuildRequires:	rpmbuild(macros) >= 1.177
%pyrequires_eq	python-modules
%pyrequires_eq	python
Requires:	python-dns
Requires:	python-pygtk-glade >= 2.8.0
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

%build
%{__make} clean
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

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%banner %{name} -e << EOF
For full functionality, you need to install:
- python-dbus (for gajim-remote and notification-daemon support)
- python-gnome-gconf (for xmpp url-handler in GNOME)
- python-sqlite (for logs)
EOF

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
