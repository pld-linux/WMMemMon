# $Revision: 1.5 $ $Date: 2002-03-24 23:28:13 $
Summary:	Memory/Swap monitoring dock applet for Window Maker
Summary(pl):	Monitor zajêto¶ci pamiêci i swapa dla Window Makera
Name:		WMMemMon
Version:	0.3.1
Release:	1
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://www.sh.rim.or.jp/~ssato/src/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
URL:		http://www.sh.rim.or.jp/~ssato/wmmemmon-e.html
BuildRequires:	libdockapp-devel
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _prefix         /usr/X11R6

%description
WMMemMon is a memory and swap monitoring dock applet for Window Maker.
Outside circle is Mem usage in percent. Inside is swap. It works fine
with AfterStep and BlackBox.

%description -l pl
WMemMon do dokowalny graficzny monitor zajêto¶ci pamiêci i swapa dla
Window Makera. Zewnêtrzne kó³ko to zajêto¶æ pamiêci, a wewnêtrzne to
swap. Mo¿na go u¿ywaæ z innymi zarz±dcami okien, takimi jak Afterstep
czy Blackbox.

%prep
%setup  -q

%build
aclocal
autoconf
automake -a -c -f
%configure 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%{__install} %{SOURCE1}	$RPM_BUILD_ROOT%{_applnkdir}/DockApplets

gzip -9nf README ChangeLog AUTHORS TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/wmmemmon

%{_applnkdir}/DockApplets/WMMemMon.desktop
