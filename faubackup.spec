Summary:	The faubackup backup in filesystem tool
Summary(pl):	Narzêdzie faubackup do wykonywania kopii w systemie plików
Name:		faubackup
Version:	0.5.8
Release:	1
License:	GPL
Group:		Applications
Source0:	http://dl.sourceforge.net/faubackup/%{name}-%{version}.tar.gz
# Source0-md5:	6b57b076cd5669ae3b8fae29835c3e34
BuildRequires:	popt-devel
URL:		http://sourceforge.net/projects/faubackup/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FauBackup uses a filesystem on a hard drive for incremental and full
backups. All backups can easily be accessed by standard filesystem
tools (ls, find, grep, cp, ...). Later backups to the same filesystem
will automatically be incremental, as unchanged files are only
hard-linked with the existing version of the file.

%description -l pl
Faubackup u¿ywa systemu plików na dysku twardym do wykonywania kopii
pe³nych i przyrostowych. Wszystkie kopie s± ³atwo dostêpne z
wykorzystaniem standardowych narzêdzi (ls, find, grep, cp, ...).
Pó¼niejsze kopie na tym samym systemie plików automatycznie bêd±
kopiami przyrostowymi poniewa¿ do niezmienionych plików s± tylko
tworzone twarde dowi±zania.

%prep
%setup -q -n %{name}

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
