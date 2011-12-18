Summary:	Fast and Easy Subtitle Downloader
Summary(pl.UTF-8):	Narzędzie do automatycznego ściągania/wysyłania podpisów do plików wideo
Name:		subdownloader
Version:	2.0.14
Release:	1
License:	GPL v3
Group:		X11/Applications/Multimedia
Source0:	https://launchpad.net/subdownloader/trunk/%{version}/+download/%{name}-%{version}.tar.gz
# Source0-md5:	b60443cfcefd89b0893628b18eccae9c
Source1:	%{name}.desktop
Source2:	%{name}.png
Source3:	%{name}.sh
# site down, and was not in distfiles
#Source:	http://starowa.one.pl/~uzi/pld/%{name}-locale-pl.tar.gz
Patch0:		always-en.patch
URL:		http://www.subdownloader.net/
BuildRequires:	rpm-pythonprov
Requires:	python >= 1:2.5
Requires:	python-PyQt4
Requires:	python-mmpython
Requires:	shared-mime-info
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/%{name}

%description
SubDownloader is a program for automatic download/upload subtitles for
videofiles (DivX, MPEG, AVI, VOB, etc) and DVDs using fast hashing.

Features:
- no spyware, no adware, source code is available
- it uses fast hashing algorithm (27 GB movies/7 seconds)
- recursively folders search
- Autodetect language of the subtitles
- Upload entire series seasons' subtitles in less than 1 minute
- and many more

%description -l pl.UTF-8
Subdownloader to napisane w Pythonie wolnodostępne narzędzie do
automatycznego ściągania/wysyłania podpisów do filmów (DivX, MPEG, AVI
itp.).

Cechy:
- brak spyware, adware; dostępny kod źródłowy
- wykorzystuje szybki algorytm haszujący (27 GB filmów/7 sekund)
- rekurencyjne wyszukiwanie napisów z folderów divx
- wysyłanie całych serii podpisów seriali w czasie poniżej minuty
- automatyczne wykrywanie języka podpisów
- i wiele więcej

%prep
%setup -q
%patch0 -p1

#tar xzf %{SOURCE3}

%{__rm} gui/images/icon32.ico
%{__rm} gui/images_rc.py

%build
%{__make} -C gui images_rc.py

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir},%{_pixmapsdir},%{_mandir}/man1,%{_datadir}/locale,%{_appdir}}

cp -a cli FileManagement gui languages modules run.py $RPM_BUILD_ROOT%{_appdir}
cp -a locale/* $RPM_BUILD_ROOT%{_datadir}/locale
install -p %{SOURCE3} $RPM_BUILD_ROOT%{_bindir}/%{name}
cp -p subdownloader.1 $RPM_BUILD_ROOT%{_mandir}/man1
cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
cp -p %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%{__rm} $RPM_BUILD_ROOT%{_appdir}/gui/Makefile
%{__rm} $RPM_BUILD_ROOT%{_appdir}/gui/Qt2Po.py
# images bundled into images_rc.py
%{__rm} -r $RPM_BUILD_ROOT%{_appdir}/gui/images
%{__rm} -r $RPM_BUILD_ROOT%{_appdir}/gui/images.qrc
# _ui.py via pyuic4
%{__rm} -r $RPM_BUILD_ROOT%{_appdir}/gui/*.ui

# duplicate with es
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/es_ES
# duplicate with pt
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/pt_PT
%{__rm} $RPM_BUILD_ROOT%{_datadir}/locale/subdownloader.pot
%{__rm} $RPM_BUILD_ROOT%{_datadir}/locale/*/LC_MESSAGES/subdownloader.po

%find_lang %{name}

%py_comp $RPM_BUILD_ROOT%{_appdir}
%py_ocomp $RPM_BUILD_ROOT%{_appdir}
%py_postclean %{_appdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_mime_database

%postun
%update_mime_database

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/*.1*
%dir %{_appdir}
%{_appdir}/*.py[co]
%{_appdir}/FileManagement
%{_appdir}/cli
%{_appdir}/gui
%{_appdir}/modules
%{_appdir}/languages
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
