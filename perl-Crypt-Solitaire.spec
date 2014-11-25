#
# Conditional build:
%bcond_without	tests	# Do not perform "make test"

%define		pdir	Crypt
%define		pnam	Solitaire
%include	/usr/lib/rpm/macros.perl
Summary:	Crypt::Solitaire Perl module - Solitaire cryptosystem
Summary(pl.UTF-8):	Moduł Perla Crypt::Solitaire - system kryptograficzny Solitaire
Name:		perl-Crypt-Solitaire
Version:	2.0
Release:	5
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a1e7410aa42d2904628219b52217d1bd
URL:		http://search.cpan.org/dist/Crypt-Solitaire/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Solitaire is a top-notch pencil-and-paper encryption system developed
by Bruce Schneier, basing on story from Neal Stephenson's novel
Cryptonomicon.

%description -l pl.UTF-8
Solitaire to system szyfrowania, do którego wystarczy ołówek i kartka
papieru. Został opracowany przez Bruce'a Schneiera na podstawie
zdarzenia z powieści Neala Stephensona "Cryptonomicom".

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}
%{?with_tests:%{__make} test}

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
