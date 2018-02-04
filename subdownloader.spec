%global commit df8427e
%define		module		subdownloader
%define		egg_name	SubDownloader
Summary:	Fast and Easy Subtitle Downloader
Summary(pl.UTF-8):	Narzędzie do automatycznego ściągania/wysyłania podpisów do plików wideo
Name:		subdownloader
Version:	2.0.19
Release:	0.6
License:	GPL v3
Group:		X11/Applications/Multimedia
#Source0:	https://launchpad.net/subdownloader/trunk/%{version}/+download/%{name}_%{version}.orig.tar.gz
Source0:	https://github.com/subdownloader/subdownloader/archive/%{commit}/%{name}-%{version}-%{commit}.tar.gz
# Source0-md5:	50efbf629daefd04bd261a4d8f0d2346
Source1:	%{name}.desktop
Source2:	%{name}.png
# Source2-md5:	de3d0cfa08b1572878cde6e3800205fa
Source3:	%{name}.sh
# site down, and was not in distfiles
#Source:	http://starowa.one.pl/~uzi/pld/%{name}-locale-pl.tar.gz
Patch0:		always-en.patch
Patch1:		egginfo.patch
URL:		http://www.subdownloader.net/
BuildRequires:	python3 >= 1:3.4
BuildRequires:	python3-PyQt5
#BuildRequires:	python3-PyQt5-devel-tools
BuildRequires:	python3-PyQt5-uic
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	desktop-file-utils
#Requires:	python-mmpython
Requires:	python3-PyQt5 >= 5.0.0
Requires:	python3-pymediainfo
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/%{name}
%define		_localedir %{py3_sitescriptdir}/subdownloader/client/locale

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
#%patch0 -p1
%patch1 -p1

#tar xzf %{SOURCE3}

%{__rm} scripts/gui/rc/images/icon32.ico

# cleanup backups after patching
find '(' -name '*~' -o -name '*.orig' ')' -print0 | xargs -0 -r -l512 rm -f

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT
%py3_install

%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/tests
cp -p subdownloader.1 $RPM_BUILD_ROOT%{_mandir}/man1
cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
cp -p %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%{__rm} $RPM_BUILD_ROOT%{py3_sitescriptdir}/subdownloader/client/locale/subdownloader.pot
%{__rm} $RPM_BUILD_ROOT%{py3_sitescriptdir}/subdownloader/client/locale/*/subdownloader.po

%find_lang %{name}

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
%if 0
%{_mandir}/man1/*.1*
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
%endif

%dir %{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}/*.py
%{py3_sitescriptdir}/%{module}/__pycache__
%dir %{py3_sitescriptdir}/%{module}/client
%{py3_sitescriptdir}/%{module}/client/*.py
%{py3_sitescriptdir}/%{module}/client/__pycache__
%{py3_sitescriptdir}/%{module}/client/cli
%{py3_sitescriptdir}/%{module}/client/gui
%{py3_sitescriptdir}/%{module}/client/locale
%{py3_sitescriptdir}/%{module}/client/modules
%{py3_sitescriptdir}/%{module}/languages
%{py3_sitescriptdir}/%{module}/provider
%{py3_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
