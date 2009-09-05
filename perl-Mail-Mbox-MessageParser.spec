%define	upstream_name	 Mail-Mbox-MessageParser
%define	upstream_version 1.5002

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	A fast and simple mbox folder reader 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Mail/%{upstream_name}-%{upstream_version}.tar.gz

%if %{mdkversion} < 1010
Buildrequires:	perl-devel
%endif
BuildRequires:	perl(FileHandle::Unget)
BuildRequires:	perl(Text::Diff)
BuildRequires:	perl(Benchmark::Timer)

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
This module implements a fast but simple mbox folder reader. One of three
implementations (Cache, Grep, Perl) will be used depending on the wishes of the
user and the system configuration. The first implementation is a cached-based
one which stores email information about mailboxes on the file system.
Subsequent accesses will be faster because no analysis of the mailbox will be
needed. The second implementation is one based on GNU grep, and is
significantly faster than the Perl version for mailboxes which contain very
large (10MB) emails. The final implementation is a fast Perl-based one which
should always be applicable.

The Cache implementation is about 6 times faster than the standard Perl
implementation. The Grep implementation is about 4 times faster than the
standard Perl implementation. If you have GNU grep, it's best to enable both
the Cache and Grep implementations. If the cache information is available,
you'll get very fast speeds. Otherwise, you'll take about a 1/3 performance hit
when the Grep version is used instead.

The overriding requirement for this module is speed. If you wish more
sophisticated parsing, use Mail::MboxParser (which is based on this module) or
Mail::Box.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor < /dev/null
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES LICENSE README
%{perl_vendorlib}/Mail
%{_mandir}/man3/*
