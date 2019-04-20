#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Log-Log4perl
Version  : 1.49
Release  : 9
URL      : https://cpan.metacpan.org/authors/id/M/MS/MSCHILLI/Log-Log4perl-1.49.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/MS/MSCHILLI/Log-Log4perl-1.49.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libl/liblog-log4perl-perl/liblog-log4perl-perl_1.49-1.debian.tar.xz
Summary  : 'Log4j implementation for Perl'
Group    : Development/Tools
License  : Artistic-1.0 GPL-1.0
Requires: perl-Log-Log4perl-bin = %{version}-%{release}
Requires: perl-Log-Log4perl-license = %{version}-%{release}
Requires: perl-Log-Log4perl-man = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
######################################################################
Log::Log4perl 1.49
######################################################################

%package bin
Summary: bin components for the perl-Log-Log4perl package.
Group: Binaries
Requires: perl-Log-Log4perl-license = %{version}-%{release}
Requires: perl-Log-Log4perl-man = %{version}-%{release}

%description bin
bin components for the perl-Log-Log4perl package.


%package dev
Summary: dev components for the perl-Log-Log4perl package.
Group: Development
Requires: perl-Log-Log4perl-bin = %{version}-%{release}
Provides: perl-Log-Log4perl-devel = %{version}-%{release}

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


%prep
%setup -q -n Log-Log4perl-1.49
cd ..
%setup -q -T -D -n Log-Log4perl-1.49 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Log-Log4perl-1.49/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Log-Log4perl
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-Log-Log4perl/LICENSE
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-Log-Log4perl/deblicense_copyright
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
/usr/lib/perl5/vendor_perl/5.28.2/Log/Log4perl.pm
/usr/lib/perl5/vendor_perl/5.28.2/Log/Log4perl/Appender.pm
/usr/lib/perl5/vendor_perl/5.28.2/Log/Log4perl/Appender/Buffer.pm
/usr/lib/perl5/vendor_perl/5.28.2/Log/Log4perl/Appender/DBI.pm
/usr/lib/perl5/vendor_perl/5.28.2/Log/Log4perl/Appender/File.pm
/usr/lib/perl5/vendor_perl/5.28.2/Log/Log4perl/Appender/Limit.pm
/usr/lib/perl5/vendor_perl/5.28.2/Log/Log4perl/Appender/RRDs.pm
/usr/lib/perl5/vendor_perl/5.28.2/Log/Log4perl/Appender/Screen.pm
/usr/lib/perl5/vendor_perl/5.28.2/Log/Log4perl/Appender/ScreenColoredLevels.pm
/usr/lib/perl5/vendor_perl/5.28.2/Log/Log4perl/Appender/Socket.pm
/usr/lib/perl5/vendor_perl/5.28.2/Log/Log4perl/Appender/String.pm
/usr/lib/perl5/vendor_perl/5.28.2/Log/Log4perl/Appender/Synchronized.pm
/usr/lib/perl5/vendor_perl/5.28.2/Log/Log4perl/Appender/TestArrayBuffer.pm
/usr/lib/perl5/vendor_perl/5.28.2/Log/Log4perl/Appender/TestBuffer.pm
/usr/lib/perl5/vendor_perl/5.28.2/Log/Log4perl/Appender/TestFileCreeper.pm
/usr/lib/perl5/vendor_perl/5.28.2/Log/Log4perl/Catalyst.pm
/usr/lib/perl5/vendor_perl/5.28.2/Log/Log4perl/Config.pm
/usr/lib/perl5/vendor_perl/5.28.2/Log/Log4perl/Config/BaseConfigurator.pm
/usr/lib/perl5/vendor_perl/5.28.2/Log/Log4perl/Config/DOMConfigurator.pm
/usr/lib/perl5/vendor_perl/5.28.2/Log/Log4perl/Config/PropertyConfigurator.pm
/usr/lib/perl5/vendor_perl/5.28.2/Log/Log4perl/Config/Watch.pm
/usr/lib/perl5/vendor_perl/5.28.2/Log/Log4perl/DateFormat.pm
/usr/lib/perl5/vendor_perl/5.28.2/Log/Log4perl/FAQ.pm
/usr/lib/perl5/vendor_perl/5.28.2/Log/Log4perl/Filter.pm
/usr/lib/perl5/vendor_perl/5.28.2/Log/Log4perl/Filter/Boolean.pm
/usr/lib/perl5/vendor_perl/5.28.2/Log/Log4perl/Filter/LevelMatch.pm
/usr/lib/perl5/vendor_perl/5.28.2/Log/Log4perl/Filter/LevelRange.pm
/usr/lib/perl5/vendor_perl/5.28.2/Log/Log4perl/Filter/MDC.pm
/usr/lib/perl5/vendor_perl/5.28.2/Log/Log4perl/Filter/StringMatch.pm
/usr/lib/perl5/vendor_perl/5.28.2/Log/Log4perl/InternalDebug.pm
/usr/lib/perl5/vendor_perl/5.28.2/Log/Log4perl/JavaMap.pm
/usr/lib/perl5/vendor_perl/5.28.2/Log/Log4perl/JavaMap/ConsoleAppender.pm
/usr/lib/perl5/vendor_perl/5.28.2/Log/Log4perl/JavaMap/FileAppender.pm
/usr/lib/perl5/vendor_perl/5.28.2/Log/Log4perl/JavaMap/JDBCAppender.pm
/usr/lib/perl5/vendor_perl/5.28.2/Log/Log4perl/JavaMap/NTEventLogAppender.pm
/usr/lib/perl5/vendor_perl/5.28.2/Log/Log4perl/JavaMap/RollingFileAppender.pm
/usr/lib/perl5/vendor_perl/5.28.2/Log/Log4perl/JavaMap/SyslogAppender.pm
/usr/lib/perl5/vendor_perl/5.28.2/Log/Log4perl/JavaMap/TestBuffer.pm
/usr/lib/perl5/vendor_perl/5.28.2/Log/Log4perl/Layout.pm
/usr/lib/perl5/vendor_perl/5.28.2/Log/Log4perl/Layout/NoopLayout.pm
/usr/lib/perl5/vendor_perl/5.28.2/Log/Log4perl/Layout/PatternLayout.pm
/usr/lib/perl5/vendor_perl/5.28.2/Log/Log4perl/Layout/PatternLayout/Multiline.pm
/usr/lib/perl5/vendor_perl/5.28.2/Log/Log4perl/Layout/SimpleLayout.pm
/usr/lib/perl5/vendor_perl/5.28.2/Log/Log4perl/Level.pm
/usr/lib/perl5/vendor_perl/5.28.2/Log/Log4perl/Logger.pm
/usr/lib/perl5/vendor_perl/5.28.2/Log/Log4perl/MDC.pm
/usr/lib/perl5/vendor_perl/5.28.2/Log/Log4perl/NDC.pm
/usr/lib/perl5/vendor_perl/5.28.2/Log/Log4perl/Resurrector.pm
/usr/lib/perl5/vendor_perl/5.28.2/Log/Log4perl/Util.pm
/usr/lib/perl5/vendor_perl/5.28.2/Log/Log4perl/Util/Semaphore.pm
/usr/lib/perl5/vendor_perl/5.28.2/Log/Log4perl/Util/TimeTracker.pm

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
/usr/share/package-licenses/perl-Log-Log4perl/LICENSE
/usr/share/package-licenses/perl-Log-Log4perl/deblicense_copyright

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/l4p-tmpl.1
