#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	DBIx
%define	pnam	Class-DynamicDefault
Summary:	DBIx::Class::DynamicDefault - Automatically set and update fields
Summary(pl.UTF-8):	DBIx::Class::DynamicDefault - Automatycznie ustawia i aktualizuje pola
Name:		perl-DBIx-Class-DynamicDefault
Version:	0.04
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-module/DBIx/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	0f4ae1e7bc8a638f679922b387fbb011
URL:		https://metacpan.org/dist/DBIx-Class-DynamicDefault
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(DBICx::TestDatabase)
BuildRequires:	perl-DBIx-Class >= 0.08127
BuildRequires:	perl-parent
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Automatically set and update fields with values calculated at runtime.

%description -l pl.UTF-8
Automatycznie ustawia i aktualizuje pola wartosiami wyliczonymi w
czasie wykonywania.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/DBIx/Class/*.pm
%{_mandir}/man3/*
