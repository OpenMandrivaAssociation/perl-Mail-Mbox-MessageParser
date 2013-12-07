%define	modname	Mail-Mbox-MessageParser
%define	modver	1.5002

Summary:	A fast and simple mbox folder reader 
Name:		perl-%{modname}
Epoch:		1
Version:	%perl_convert_version %{modver}
Release:	6
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Mail/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRequires:	perl(FileHandle::Unget)
BuildRequires:	perl(Text::Diff)
BuildRequires:	perl(Benchmark::Timer)

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
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor < /dev/null
%make

%check
make test

%install
%makeinstall_std

%files
%doc CHANGES LICENSE README
%{perl_vendorlib}/Mail
%{_mandir}/man3/*

