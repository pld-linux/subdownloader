Summary:	Tool for automatic download/upload subtitles for videofiles
Summary(pl.UTF-8):	Narzędzie do automatycznego ściągania/wysyłania podpisów do plików wideo
Name:		subdownloader
Version:	1.2.9
Release:	0.1
License:	free (see license.txt)
Group:		X11/Applications/Games
Source0:	http://www.vinalinux.com/projects/subdownloader/repository/sources.%{version}.zip
# Source0-md5:	31bd12d5edc11f05f51ea43c58cfb9e4
Source1:        %{name}.desktop
Source2:        %{name}.png
Source3:	http://starowa.one.pl/~uzi/pld/subdownloader-locale-pl.tar.gz
Patch0:		%{name}-conf.patch
URL:		http://trac.opensubtitles.org/projects/subdowloader/
BuildRequires:	rpm-pythonprov
BuildRequires:	unzip
Requires:	python >= 1:2.5
Requires:	python-mmpython
Requires:	python-imdb >= 2.6
Requires:	python-wxPython >= 2.8
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Subdownloader is a Free OpenSource tool written in Python for
automatic download/upload subtitles for videofiles (DivX, MPEG, AVI,
etc.).

Features:
- no spyware, no adware, source code is available
- it uses fast hashing algorithm (27 GB movies/7 seconds)
- Search subtitles recursively from your divx folders
- Upload entire series seasons' subtitles in less than 1 minute
- Autodetect language of the subtitles
- and many more

%description -l pl.UTF-8
Subdownloader to napisane w Pythonie wolnodostępne narzędzie do
automatycznego ściągania/wysyłania podpisów do filmów (DivX, MPEG,
AVI itp.).

Cechy:
- brak spyware, adware; dostępny kod źródłowy
- wykorzystuje szybki algorytm haszujący (27 GB filmów/7 sekund)
- rekurencyjne wyszukiwanie napisów z folderów divx
- wysyłanie całych serii podpisów seriali w czasie poniżej minuty
- automatyczne wykrywanie języka podpisów
- i wiele więcej

%prep
%setup -q -c
%patch0 -p1

tar xzf %{SOURCE3}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/%{name},%{_bindir},%{_desktopdir},%{_pixmapsdir}}

cp -fr conf		$RPM_BUILD_ROOT%{_datadir}/%{name}
cp -fr data		$RPM_BUILD_ROOT%{_datadir}/%{name}
cp -fr extra		$RPM_BUILD_ROOT%{_datadir}/%{name}
cp -fr flags		$RPM_BUILD_ROOT%{_datadir}/%{name}
cp -fr images		$RPM_BUILD_ROOT%{_datadir}/%{name}
cp -fr lm		$RPM_BUILD_ROOT%{_datadir}/%{name}
cp -fr locale		$RPM_BUILD_ROOT%{_datadir}/%{name}
cp -fr flags		$RPM_BUILD_ROOT%{_datadir}/%{name}
cp -fr preferences	$RPM_BUILD_ROOT%{_datadir}/%{name}
cp -fr wxglade		$RPM_BUILD_ROOT%{_datadir}/%{name}
cp -f *.py		$RPM_BUILD_ROOT%{_datadir}/%{name}

cp -f subdownloader.sh  $RPM_BUILD_ROOT%{_bindir}
cp -f %{SOURCE1}  $RPM_BUILD_ROOT%{_desktopdir}
cp -f %{SOURCE2}  $RPM_BUILD_ROOT%{_pixmapsdir}

%py_comp $RPM_BUILD_ROOT%{_datadir}/%{name}
%py_ocomp $RPM_BUILD_ROOT%{_datadir}/%{name}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc TODO.txt license.txt tips.txt credits.txt
%attr(755,root,root) %{_bindir}/subdownloader.sh
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
