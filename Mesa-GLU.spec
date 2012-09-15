%define		gitver	f98fdc4d8a77497d1921e3dc26cab0e28abb92fc

Summary:	SGI implementation of libGLU OpenGL library
Name:		Mesa-GLU
Version:	9.0.0
%if "%{gitver}" != "%{nil}"
Release:	0.%{gitver}.1
Source:		http://cgit.freedesktop.org/mesa/glu/snapshot/glu-%{gitver}.tar.bz2
%else
Release:	1
Source0:	ftp://ftp.freedesktop.org/pub/mesa/%{version}/MesaLib-%{version}.tar.gz
# Source0-md5:	301e5674b574682b4bc6121136fe2b16
%endif
License:	SGI Free Software License B v1.1
Group:		X11/Libraries
URL:		http://www.mesa3d.org/
BuildRequires:	OpenGL-devel >= 1.2
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
Requires:	OpenGL >= 1.2
Provides:	OpenGL-GLU = 1.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SGI implementation of libGLU OpenGL library. It implements OpenGL GLU
1.3 specifications.

%package devel
Summary:	Header files for SGI libGLU library
License:	SGI Free Software License B v1.1
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	OpenGL-devel >= 1.2
Requires:	libstdc++-devel
Provides:	OpenGL-GLU-devel = 1.3

%description devel
Header files for SGI libGLU library.

%prep
%if "%{gitver}" != "%{nil}"
%setup -qn glu-%{gitver}
%else
%setup -q
%endif

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules	\
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_includedir}/GL/{[a-fh-np-wyz],gg,glf,glut}*.h

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libGLU.so.1
%attr(755,root,root) %{_libdir}/libGLU.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libGLU.so
%{_includedir}/GL/glu.h
%{_includedir}/GL/glu_mangle.h
%{_pkgconfigdir}/glu.pc

