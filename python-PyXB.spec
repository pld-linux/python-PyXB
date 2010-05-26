%define 	module	PyXB
Summary:	Python XML Schema Bindings
Name:		python-%{module}
Version:	1.1.1
Release:	0.1
License:	Apache v. 2.0
Group:		Development/Languages/Python
Source0:	http://downloads.sourceforge.net/project/pyxb/pyxb/1.1.1%20%28Beta%29/PyXB-base-%{version}.tar.gz
# Source0-md5:	90e38bf24693478f664c8fdf78d92f05
URL:		http://pyxb.sourceforge.net
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PyXB (“pixbee”) is a pure Python package that generates Python source
code for classes that correspond to data structures defined by
XMLSchema. In concept it is similar to JAXB for Java and CodeSynthesis
XSD for C++.

%package -n PyXB
Summary:	Python XML Schema Bindings tools
Group:		Development/Languages/Python
Requires:	%{name} = %{version}-%{release}

%description -n PyXB
Tools that generate Python source code for classes that correspond to
data structures defined in XMLSchema.

%package examples
Summary:	Python XML Schema Bindings examples
Group:		Documentation
Requires:	PyXB = %{version}-%{release}

%description examples
Some examples for PyXB package.

%prep
%setup -q -n %{module}-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

install -d $RPM_BUILD_ROOT%{_examplesdir}
cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NOTICE README.txt doc/*
%{py_sitescriptdir}/pyxb/*.py[co]
%{py_sitescriptdir}/pyxb/binding/*.py[co]
%{py_sitescriptdir}/pyxb/bundles/*.py[co]
%{py_sitescriptdir}/pyxb/namespace/*.py[co]
%{py_sitescriptdir}/pyxb/utils/*.py[co]
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
%{_examplesdir}/%{name}
