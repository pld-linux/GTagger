Summary:	ID3Tag editor
Name:		GTagger
Version:	0.1.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://freebits.yawsp.de/35/releases/%{name}-%{version}.tar.gz
URL:		http://gtagger.sf.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gcc >= 3.2
BuildRequires:	gtkmm-devel >= 2.2.0
BuildRequires:	libtool
BuildRequires:	intltool >= 0.25
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GTagger is an ID3Tag editor designed for easy and efficient usage.

%prep
%setup -q -n %{name}-0.1

%build
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	gtaggerdocdir=%{_docdir}/%{name}	

%find_lang %{name}

# header files seems to be useless
rm -rf $RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gtagger
%{_docdir}/*
