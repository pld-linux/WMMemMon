# $Revision: 1.12 $ $Date: 2003-05-28 12:58:47 $
Summary:	Memory/Swap monitoring dock applet for Window Maker
Summary(pl):	Monitor zaj�to�ci pami�ci i swapa dla Window Makera
Name:		WMMemMon
Version:	0.3.1
Release:	1
License:	GPL
Group:		X11/Window Managers/Tools
# new version: http://www.sh.rim.or.jp/~ssato/src/wmmemmon-0.7.0.tar.bz2
Source0:	http://www.sh.rim.or.jp/~ssato/src/%{name}-%{version}.tar.gz
# Source0-md5:	82bb1b07e7675a502d62c4b12d7fc6f2
Source1:	%{name}.desktop
URL:		http://www.sh.rim.or.jp/~ssato/dockapp/index.shtml#wmmemmon
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libdockapp-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


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
%setup -q

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/DockApplets

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog AUTHORS TODO
%attr(755,root,root) %{_bindir}/wmmemmon

%{_applnkdir}/DockApplets/WMMemMon.desktop
