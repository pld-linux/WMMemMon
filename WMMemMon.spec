# $Revision: 1.1 $ $Date: 2001-09-23 07:58:56 $
Summary:	Memory/Swap monitoring dock applet for Window Maker
Summary(pl):	Monitor zaj�to�ci pami�ci i swapa dla Window Makera
Name:		WMMemMon
Version:	0.3.1
Release:	1
License:	GPL
Group:		X11/Window Managers/Tools
Group(de):	X11/Fenstermanager/Werkzeuge
Group(pl):	X11/Zarz�dcy Okien/Narz�dzia
Source0:	http://www.sh.rim.or.jp/~ssato/src/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
URL:		http://www.sh.rim.or.jp/~ssato/wmmemmon-e.html
BuildPrereq:	libdockapp-devel
BuildPrereq:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _prefix         /usr/X11R6

%description
WMMemMon is a memory and swap monitoring dock applet for Window Maker.
Outside circle is Mem usage in percent. Inside is swap. It works fine
with AfterStep and BlackBox.

%description -l pl
WMemMon do dokowalny graficzny monitor zaj�to�ci pami�ci i swapa dla
Window Makera. Zewn�trzne k�ko to zaj�to�� pami�ci, a wewn�trzne to
swap. Mo�na go u�ywa� z innymi zarz�dcami okien, takimi jak Afterstep
czy Blackbox.

%prep
%setup  -q

%build
aclocal
autoconf
automake -a -c
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