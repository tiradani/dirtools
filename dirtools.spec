%if 0%{?rhel} && 0%{?rhel} <= 5
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%endif


Name:           py_dirtools
Group:          System Environment/Libraries
Version:        0
Release:        1%{?dist}
Summary:        Provides many helper modules for common uses cases when programming with Python (2.6+)

License:        MIT
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  python2-devel

Provides:       py_dirtools = %{version}-%{release}

Source:         dirtools-%{version}.tar.gz


%description
Provides an rpm package for the globster project hosted at https://github.com/tsileo/globster

%prep
%setup -q -n dirtools-%{version}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{python_sitelib}
install -d $RPM_BUILD_ROOT%{python_sitelib}/dirtools
cp -r __init__.py $RPM_BUILD_ROOT%{python_sitelib}/dirtools
cp -r CHANGES.rst $RPM_BUILD_ROOT%{python_sitelib}/dirtools
cp -r dirtools.py $RPM_BUILD_ROOT%{python_sitelib}/dirtools
cp -r LICENSE $RPM_BUILD_ROOT%{python_sitelib}/dirtools
cp -r README.rst $RPM_BUILD_ROOT%{python_sitelib}/dirtools
cp -r test_dirtools.py $RPM_BUILD_ROOT%{python_sitelib}/dirtools

%files
%{python_sitelib}/dirtools/

%changelog
* Fri Aug 23 2013 Anthony Tiradani <anthony.tiradani@gmail.com> - 0.1
- initial packaging


