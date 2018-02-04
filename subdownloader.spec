%global commit 2cb0ffbb
Summary:	Fast and Easy Subtitle Downloader
Summary(pl.UTF-8):	Narzędzie do automatycznego ściągania/wysyłania podpisów do plików wideo
Name:		subdownloader
Version:	2.0.19
Release:	0.1
License:	GPL v3
Group:		X11/Applications/Multimedia
#Source0:	https://launchpad.net/subdownloader/trunk/%{version}/+download/%{name}_%{version}.orig.tar.gz
Source0:	https://github.com/subdownloader/subdownloader/archive/%{commit}/%{name}-%{version}-%{commit}.tar.gz
# Source0-md5:	866b4ab1a2ed1c4670e29c7abdbae6b3
Source1:	%{name}.desktop
Source2:	%{name}.png
# Source2-md5:	de3d0cfa08b1572878cde6e3800205fa
Source3:	%{name}.sh
# site down, and was not in distfiles
#Source:	http://starowa.one.pl/~uzi/pld/%{name}-locale-pl.tar.gz
Patch0:		always-en.patch
URL:		http://www.subdownloader.net/
BuildRequires:	python-PyQt5
BuildRequires:	python-PyQt5-devel-tools
BuildRequires:	python-PyQt5-uic
BuildRequires:	rpm-pythonprov
Requires:	desktop-file-utils
Requires:	python >= 1:2.5
Requires:	python-PyQt5
Requires:	python-mmpython
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
- autodetect language of the subtitles
- upload entire series seasons' subtitles in less than 1 minute
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
%setup -qc
mv subdownloader-%{commit}*/* .
%patch0 -p1

#tar xzf %{SOURCE3}

%{__rm} gui/images/icon32.ico

# cleanup backups after patching
find '(' -name '*~' -o -name '*.orig' ')' -print0 | xargs -0 -r -l512 rm -f

%build
%{__make} -C gui clean
%{__make} -C gui all

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir},%{_pixmapsdir},%{_mandir}/man1,%{_localedir},%{_appdir}}

cp -a cli FileManagement gui languages modules run.py $RPM_BUILD_ROOT%{_appdir}
cp -a locale/* $RPM_BUILD_ROOT%{_localedir}
install -p %{SOURCE3} $RPM_BUILD_ROOT%{_bindir}/%{name}
cp -p subdownloader.1 $RPM_BUILD_ROOT%{_mandir}/man1
cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
cp -p %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%{__rm} $RPM_BUILD_ROOT%{_appdir}/gui/Makefile
#%{__rm} $RPM_BUILD_ROOT%{_appdir}/gui/Qt2Po.py
# images bundled into images_rc.py
%{__rm} -r $RPM_BUILD_ROOT%{_appdir}/gui/images
%{__rm} -r $RPM_BUILD_ROOT%{_appdir}/gui/images.qrc
# _ui.py via pyuic4
%{__rm} -r $RPM_BUILD_ROOT%{_appdir}/gui/*.ui

# duplicate with es
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/es_ES
# duplicate with pt
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/pt_PT
%{__rm} $RPM_BUILD_ROOT%{_localedir}/subdownloader.pot
%{__rm} $RPM_BUILD_ROOT%{_localedir}/*/LC_MESSAGES/subdownloader.po

%find_lang %{name}

%py_comp $RPM_BUILD_ROOT%{_appdir}
%py_ocomp $RPM_BUILD_ROOT%{_appdir}
%py_postclean %{_appdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database

%postun
%update_desktop_database

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog README.md
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/*.1*
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png

%dir %{_appdir}
%{_appdir}/*.py[co]
%{_appdir}/FileManagement
%{_appdir}/cli
%{_appdir}/modules
%{_appdir}/languages

%dir %{_appdir}/gui
%{_appdir}/gui/*[^_][^u][^i].py[co]
%{_appdir}/gui/about.py[co]

# generated resources.
# be sure to list them, otherwise we end up broken package again
%{_appdir}/gui/about_ui.py[co]
%{_appdir}/gui/chooseLanguage_ui.py[co]
#%{_appdir}/gui/expiration_ui.py[co]
%{_appdir}/gui/images_rc.py[co]
%{_appdir}/gui/imdb_ui.py[co]
%{_appdir}/gui/login_ui.py[co]
%{_appdir}/gui/main_ui.py[co]
%{_appdir}/gui/preferences_ui.py[co]
