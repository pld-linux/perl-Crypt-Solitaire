#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	Solitaire
Summary:	Crypt::Solitaire Perl module - Solitaire cryptosystem
Summary(pl):	Modu� Perla Crypt::Solitaire - system kryptograficzny Solitaire
Name:		perl-Crypt-Solitaire
Version:	2.0
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a1e7410aa42d2904628219b52217d1bd
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Solitaire is a top-notch pencil-and-paper encryption system developed
by Bruce Schneier, basing on story from Neal Stephenson's novel
Cryptonomicon.

%description -l pl
Solitaire to system szyfrowania, do kt�rego wystarczy o��wek i kartka
papieru. Zosta� opracowany przez Bruce'a Schneiera na podstawie
zdarzenia z powie�ci Neala Stephensona "Cryptonomicom".

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
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
%{perl_vendorlib}/Crypt/Solitaire.pm
%dir %{perl_vendorlib}/auto/Crypt/Solitaire
%{perl_vendorlib}/auto/Crypt/Solitaire/autosplit.ix
%{_mandir}/man3/*
