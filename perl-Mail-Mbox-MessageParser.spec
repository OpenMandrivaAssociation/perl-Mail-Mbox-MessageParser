%define	upstream_name	 Mail-Mbox-MessageParser
%define	upstream_version 1.5002

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4
Epoch:		1

Summary:	A fast and simple mbox folder reader 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Mail/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(FileHandle::Unget)
BuildRequires:	perl(Text::Diff)
BuildRequires:	perl(Benchmark::Timer)

BuildArch:	noarch

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


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1:1.500.200-3mdv2012.0
+ Revision: 765412
- rebuilt for perl-5.14.2
- rebuilt for perl-5.14.x

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - update to new version 1.5002

* Sat May 21 2011 Oden Eriksson <oeriksson@mandriva.com> 1:1.500.200-2
+ Revision: 676861
- rebuild

* Tue Sep 15 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1:1.500.200-1mdv2011.0
+ Revision: 442942
- bumping epoch
- update to 1.5002

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.5000-5mdv2010.0
+ Revision: 430485
- rebuild

* Wed Oct 01 2008 Oden Eriksson <oeriksson@mandriva.com> 1.5000-4mdv2009.0
+ Revision: 290413
- sync with fedora

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Wed May 02 2007 Olivier Thauvin <nanardon@mandriva.org> 1.5000-1mdv2008.0
+ Revision: 20264
- 1.5000


* Mon Aug 28 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.4005-1mdv2007.0
- New version 1.4005

* Thu Jun 01 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.4003-1mdv2007.0
- New release 1.4003
- this is a noarch package

* Wed May 03 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.4002-2mdk
- Fix According to perl Policy
	- BuildRequires
	- Source URL

* Mon Mar 06 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.4002-1mdk
- New release 1.4002

* Wed Dec 14 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.4001-2mdk
- spec cleanup
- don't ship empty directories
- %%mkrel
- better summary and description

* Thu Aug 18 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.4001-1mdk
- New release 1.4001

* Sun Jul 10 2005 Oden Eriksson <oeriksson@mandriva.com> 1.4000-1mdk
- initial Mandriva package

