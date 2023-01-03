%define	modname	Mail-Mbox-MessageParser

Summary:	A fast and simple mbox folder reader 
Name:		perl-%{modname}
Version:	1.5111
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Mail/%{modname}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRequires:	perl(Text::Diff)
BuildRequires:  perl(File::Path) 
BuildRequires:  perl(ExtUtils::MakeMaker) 
BuildRequires:  perl(File::Slurper)
BuildRequires:  perl(FileHandle::Unget)

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
%autosetup -p1 -n %{modname}-%{version}
perl Makefile.PL INSTALLDIRS=vendor < /dev/null

%build
%make_build

%install
%make_install

%files
%doc CHANGES LICENSE README
%{perl_vendorlib}/Mail
%{_mandir}/man3/*
