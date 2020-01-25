Summary:	The faubackup backup in filesystem tool
Summary(pl.UTF-8):	Narzędzie faubackup do wykonywania kopii w systemie plików
Name:		faubackup
Version:	0.5.9
Release:	1
License:	GPL
Group:		Applications
Source0:	http://dl.sourceforge.net/faubackup/%{name}-%{version}.tar.gz
# Source0-md5:	44d3723e3c2d7bc4a63f8ac91699c8c2
URL:		http://sourceforge.net/projects/faubackup/
BuildRequires:	popt-devel
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FauBackup uses a filesystem on a hard drive for incremental and full
backups. All backups can easily be accessed by standard filesystem
tools (ls, find, grep, cp, ...). Later backups to the same filesystem
will automatically be incremental, as unchanged files are only
hard-linked with the existing version of the file.

%description -l pl.UTF-8
Faubackup używa systemu plików na dysku twardym do wykonywania kopii
pełnych i przyrostowych. Wszystkie kopie są łatwo dostępne z
wykorzystaniem standardowych narzędzi (ls, find, grep, cp, ...).
Późniejsze kopie na tym samym systemie plików automatycznie będą
kopiami przyrostowymi ponieważ do niezmienionych plików są tylko
tworzone twarde dowiązania.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/faubackup.conf
%attr(755,root,root) %{_sbindir}/faubackup*
%{_mandir}/man5/*
%{_mandir}/man8/*
