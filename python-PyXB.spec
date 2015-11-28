%define 	module	PyXB
Summary:	Python XML Schema Bindings
Summary(pl.UTF-8):	Wiązania schematów XML do Pythona
Name:		python-%{module}
Version:	1.1.1
Release:	2
License:	Apache v2.0
Group:		Development/Languages/Python
Source0:	http://downloads.sourceforge.net/pyxb/PyXB-base-%{version}.tar.gz
# Source0-md5:	90e38bf24693478f664c8fdf78d92f05
Patch0:		shebang.patch
URL:		http://pyxb.sourceforge.net
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-PyXML
Requires:	python-libs
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PyXB ("pixbee") is a pure Python package that generates Python source
code for classes that correspond to data structures defined by
XMLSchema. In concept it is similar to JAXB for Java and CodeSynthesis
XSD for C++.

%description -l pl.UTF-8
PyXB ("pixbee") to czysto pythonowy pakiet generujący kod źródłowy w
Pythonie dla klas odpowiadających strukturom danych zdefiniowanym w
schemacie XML. Idea jest podobna do JAXB dla Javy oraz CodeSynthesis
XSD dla C++.

%package -n PyXB
Summary:	Python XML Schema Bindings tools
Summary(pl.UTF-8):	Narzędzia dla wiązań schematów XML do Pythona
Group:		Development/Languages/Python
Requires:	%{name} = %{version}-%{release}

%description -n PyXB
Tools that generate Python source code for classes that correspond to
data structures defined in XMLSchema.

%description -n PyXB -l pl.UTF-8
Narzędzia generujące kod źródłowy w Pythonie dla klas odpowiadających
strukturom danych zdefiniowanym w schemacie XML.

%package examples
Summary:	Python XML Schema Bindings examples
Summary(pl.UTF-8):	Przykłady dla wiązań schematów XML do Pythona
Group:		Documentation
Requires:	PyXB = %{version}-%{release}

%description examples
Some examples for PyXB package.

%description examples -l pl.UTF-8
Trochę przykładów dla pakietu PyXB.

%prep
%setup -q -n %{module}-%{version}
%patch0 -p1

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NOTICE README.txt doc/*
%dir %{py_sitescriptdir}/pyxb
%{py_sitescriptdir}/pyxb/*.py[co]
%dir %{py_sitescriptdir}/pyxb/binding
%{py_sitescriptdir}/pyxb/binding/*.py[co]
%dir %{py_sitescriptdir}/pyxb/bundles
%{py_sitescriptdir}/pyxb/bundles/*.py[co]
%dir %{py_sitescriptdir}/pyxb/namespace
%{py_sitescriptdir}/pyxb/namespace/*.py[co]
%dir %{py_sitescriptdir}/pyxb/utils
%{py_sitescriptdir}/pyxb/utils/*.py[co]
%dir %{py_sitescriptdir}/pyxb/xmlschema
%{py_sitescriptdir}/pyxb/xmlschema/*.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/%{module}-*.egg-info
%endif

%files -n PyXB
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pyxbdump
%attr(755,root,root) %{_bindir}/pyxbgen
%attr(755,root,root) %{_bindir}/pyxbwsdl

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
