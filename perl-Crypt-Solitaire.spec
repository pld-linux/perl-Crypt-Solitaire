#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	Solitaire
Summary:	Crypt::Solitaire Perl module - Solitaire cryptosystem
Summary(pl):	Modu³ Perla Crypt::Solitaire - system kryptograficzny Solitaire
Name:		perl-Crypt-Solitaire
Version:	2.0
Release:	1
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Solitaire is a top-notch pencil-and-paper encryption system developed
by Bruce Schneier, basing on story from Neal Stephenson's novel
Cryptonomicon.

%description -l pl
Solitaire to system szyfrowania, do którego wystarczy o³ówek i kartka
papieru. Zosta³ opracowany przez Bruce'a Schneiera na podstawie
zdarzenia z powie¶ci Neala Stephensona "Cryptonomicom".

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_sitelib}/Crypt/Solitaire.pm
%{perl_sitelib}/auto/Crypt/Solitaire/autosplit.ix
%{_mandir}/man3/*
