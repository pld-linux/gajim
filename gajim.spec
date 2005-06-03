#
#%define		snap 20050603
#
Summary:	A Jabber client written in PyGTK
Summary(pl):	Klient Jabbera napisany w PyGTK
Name:		gajim
Version:	0.7
#Release:	0.%{snap}.1
Release:	0.1
License:	GPL
Group:		Applications/Communications
Source0:	http://gajim.org/downloads/gajim-0.7.tar.bz2
# Source0-md5:	70d6b882c496ea7fbacc4222da49b125
#Source0:	gajim-snap-%{snap}.tar.bz2
URL:		http://www.gajim.org/
BuildRequires:	gtkspell-devel
%pyrequires_eq	python-modules
%pyrequires_eq	python
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
#-n %{name}

%build
%{__make} \
	PREFIX=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	PREFIX=%{_prefix} \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_datadir}/%{name}/{COPYING,setup_win32.pyo}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README Changelog doc/*
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/*.so
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_mandir}/man1/*
