#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v21
# autospec commit: 94c6be0
#
Name     : perl-Log-Log4perl
Version  : 1.57
Release  : 40
URL      : https://cpan.metacpan.org/authors/id/E/ET/ETJ/Log-Log4perl-1.57.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/E/ET/ETJ/Log-Log4perl-1.57.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libl/liblog-log4perl-perl/liblog-log4perl-perl_1.49-1.debian.tar.xz
Summary  : 'Log4j implementation for Perl'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Log-Log4perl-bin = %{version}-%{release}
Requires: perl-Log-Log4perl-license = %{version}-%{release}
Requires: perl-Log-Log4perl-man = %{version}-%{release}
Requires: perl-Log-Log4perl-perl = %{version}-%{release}
Requires: perl(Log::Dispatch::FileRotate)
Requires: perl(XML::DOM)
BuildRequires : buildreq-cpan
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
######################################################################
Log::Log4perl 1.49
######################################################################

%package bin
Summary: bin components for the perl-Log-Log4perl package.
Group: Binaries
Requires: perl-Log-Log4perl-license = %{version}-%{release}

%description bin
bin components for the perl-Log-Log4perl package.


%package dev
Summary: dev components for the perl-Log-Log4perl package.
Group: Development
Requires: perl-Log-Log4perl-bin = %{version}-%{release}
Provides: perl-Log-Log4perl-devel = %{version}-%{release}
Requires: perl-Log-Log4perl = %{version}-%{release}

%description dev
dev components for the perl-Log-Log4perl package.


%package license
Summary: license components for the perl-Log-Log4perl package.
Group: Default

%description license
license components for the perl-Log-Log4perl package.


%package man
Summary: man components for the perl-Log-Log4perl package.
Group: Default

%description man
man components for the perl-Log-Log4perl package.


%package perl
Summary: perl components for the perl-Log-Log4perl package.
Group: Default
Requires: perl-Log-Log4perl = %{version}-%{release}

%description perl
perl components for the perl-Log-Log4perl package.


%prep
%setup -q -n Log-Log4perl-1.57
cd %{_builddir}
tar xf %{_sourcedir}/liblog-log4perl-perl_1.49-1.debian.tar.xz
cd %{_builddir}/Log-Log4perl-1.57
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Log-Log4perl-1.57/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Log-Log4perl
cp %{_builddir}/Log-Log4perl-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-Log-Log4perl/3c593274c224f71d76a246007a4fae4f2cde1ed2 || :
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Log-Log4perl/e928184e28ed624377834253ec32699f20042a39 || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/l4p-tmpl

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Log::Log4perl.3
/usr/share/man/man3/Log::Log4perl::Appender.3
/usr/share/man/man3/Log::Log4perl::Appender::Buffer.3
/usr/share/man/man3/Log::Log4perl::Appender::DBI.3
/usr/share/man/man3/Log::Log4perl::Appender::File.3
/usr/share/man/man3/Log::Log4perl::Appender::Limit.3
/usr/share/man/man3/Log::Log4perl::Appender::RRDs.3
/usr/share/man/man3/Log::Log4perl::Appender::Screen.3
/usr/share/man/man3/Log::Log4perl::Appender::ScreenColoredLevels.3
/usr/share/man/man3/Log::Log4perl::Appender::Socket.3
/usr/share/man/man3/Log::Log4perl::Appender::String.3
/usr/share/man/man3/Log::Log4perl::Appender::Synchronized.3
/usr/share/man/man3/Log::Log4perl::Appender::TestArrayBuffer.3
/usr/share/man/man3/Log::Log4perl::Appender::TestBuffer.3
/usr/share/man/man3/Log::Log4perl::Appender::TestFileCreeper.3
/usr/share/man/man3/Log::Log4perl::Catalyst.3
/usr/share/man/man3/Log::Log4perl::Config.3
/usr/share/man/man3/Log::Log4perl::Config::BaseConfigurator.3
/usr/share/man/man3/Log::Log4perl::Config::DOMConfigurator.3
/usr/share/man/man3/Log::Log4perl::Config::PropertyConfigurator.3
/usr/share/man/man3/Log::Log4perl::Config::Watch.3
/usr/share/man/man3/Log::Log4perl::DateFormat.3
/usr/share/man/man3/Log::Log4perl::FAQ.3
/usr/share/man/man3/Log::Log4perl::Filter.3
/usr/share/man/man3/Log::Log4perl::Filter::Boolean.3
/usr/share/man/man3/Log::Log4perl::Filter::LevelMatch.3
/usr/share/man/man3/Log::Log4perl::Filter::LevelRange.3
/usr/share/man/man3/Log::Log4perl::Filter::MDC.3
/usr/share/man/man3/Log::Log4perl::Filter::StringMatch.3
/usr/share/man/man3/Log::Log4perl::InternalDebug.3
/usr/share/man/man3/Log::Log4perl::JavaMap.3
/usr/share/man/man3/Log::Log4perl::JavaMap::ConsoleAppender.3
/usr/share/man/man3/Log::Log4perl::JavaMap::FileAppender.3
/usr/share/man/man3/Log::Log4perl::JavaMap::JDBCAppender.3
/usr/share/man/man3/Log::Log4perl::JavaMap::NTEventLogAppender.3
/usr/share/man/man3/Log::Log4perl::JavaMap::RollingFileAppender.3
/usr/share/man/man3/Log::Log4perl::JavaMap::SyslogAppender.3
/usr/share/man/man3/Log::Log4perl::JavaMap::TestBuffer.3
/usr/share/man/man3/Log::Log4perl::Layout.3
/usr/share/man/man3/Log::Log4perl::Layout::NoopLayout.3
/usr/share/man/man3/Log::Log4perl::Layout::PatternLayout.3
/usr/share/man/man3/Log::Log4perl::Layout::PatternLayout::Multiline.3
/usr/share/man/man3/Log::Log4perl::Layout::SimpleLayout.3
/usr/share/man/man3/Log::Log4perl::Level.3
/usr/share/man/man3/Log::Log4perl::Logger.3
/usr/share/man/man3/Log::Log4perl::MDC.3
/usr/share/man/man3/Log::Log4perl::NDC.3
/usr/share/man/man3/Log::Log4perl::Resurrector.3
/usr/share/man/man3/Log::Log4perl::Util.3
/usr/share/man/man3/Log::Log4perl::Util::Semaphore.3
/usr/share/man/man3/Log::Log4perl::Util::TimeTracker.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Log-Log4perl/3c593274c224f71d76a246007a4fae4f2cde1ed2
/usr/share/package-licenses/perl-Log-Log4perl/e928184e28ed624377834253ec32699f20042a39

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/l4p-tmpl.1

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
