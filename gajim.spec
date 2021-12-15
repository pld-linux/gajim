Summary:	A Jabber client written in PyGTK
Summary(pl.UTF-8):	Klient Jabbera napisany w PyGTK
Name:		gajim
Version:	1.0.3
Release:	3
Epoch:		1
License:	GPL v3+
Group:		Applications/Communications
Source0:	http://gajim.org/downloads/1.0/%{name}-%{version}.tar.bz2
# Source0-md5:	08091dafd70c092711dca73991e8aee4
Patch0:		ca-certificates.patch
URL:		http://www.gajim.org/
BuildRequires:	gettext-tools
BuildRequires:	python3 >= 3.5
BuildRequires:	python3-setuptools >= 1:3.5
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	ca-certificates
Requires:	hicolor-icon-theme
Requires:	python3-nbxmpp
Requires:	python3-pyOpenSSL >= 0.12
Requires:	python3-pygobject3
Suggests:	dbus(org.freedesktop.Notifications)
Suggests:	gnome-keyring
Suggests:	gnupg2
Suggests:	python3-Crypto
Suggests:	python3-avahi
Suggests:	python3-dbus >= 0.82.1
Suggests:	python3-pyasn1
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildArch:	noarch
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
%patch0 -p1

%build
%py3_build %{?with_tests:test}

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/nb_NO

[ -d $RPM_BUILD_ROOT%{_localedir}/sr@latin ] || \
       mv -f $RPM_BUILD_ROOT%{_localedir}/sr@{Latn,latin}
%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gajim*
%{_desktopdir}/org.gajim.Gajim.desktop
%{_mandir}/man1/*.1*
%{_iconsdir}/hicolor/*/apps/org.gajim.Gajim.png
%{_iconsdir}/hicolor/scalable/apps/org.gajim.Gajim.svg
%{_iconsdir}/hicolor/symbolic/apps/org.gajim.Gajim-symbolic.svg
%{_datadir}/metainfo/org.gajim.Gajim.appdata.xml
%{py3_sitescriptdir}/gajim
%{py3_sitescriptdir}/gajim-%{version}-py*.egg-info
