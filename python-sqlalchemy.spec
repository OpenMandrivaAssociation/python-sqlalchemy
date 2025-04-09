#%%define debug_package %%nil
%define module sqlalchemy
%ifarch %arm %mips
%define debug_package %nil
%endif
%bcond_without test

Name:		python-sqlalchemy
Version:	2.0.40
Release:	1
Summary:	SQL toolkit and object relational mapper for Python
URL:		https://www.sqlalchemy.org/
License:	MIT
Group:		Development/Python
Source0:	https://files.pythonhosted.org/packages/source/s/sqlalchemy/%{module}-%{version}.tar.gz
BuildSystem: python

BuildRequires:	python
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(cython)
%if %{with test}
BuildRequires:	python%{pyver}dist(pytest)
BuildRequires:	python%{pyver}dist(pytest-asyncio)
BuildRequires:	python%{pyver}dist(greenlet)
BuildRequires:	python%{pyver}dist(importlib-metadata)
BuildRequires:	python%{pyver}dist(typing-extensions)
%endif
Suggests:	%{name}-doc = %{version}-%{release}

%description
%{module_name} is a SQL toolkit and object relational mapper for Python. It
encourages "relational mapping" as opposed to "table mapping" and includes
enterprise-level features such as eager loading, unit-of-work object commits,
topological dependency sorting, and full usage of bind parameters. It
supports MySQL, Postgres, Oracle, and SQLite.

%package -n %{name}-doc
Summary:	Documentation for python-sqlalchemy
Provides:	python%{pyver}dist(%{module}-doc) = %{version}-%{release}
BuildArch:	noarch

%description -n %{name}-doc
This package contains the HTML documentation, tutorials and API
reference for %{name}.

%prep
%autosetup -n %{module}-%{version} -p1

# Remove unnecessary scripts for building docs
rm -rf doc/build
sed -i 's/\r$//' examples/dynamic_dict/dynamic_dict.py

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
%py3_build

%install
%py3_install

%if %{with test}
%check
# we dont need to stress-test our own builders here,
# run tests only to ensure the regular tests pass.
%__python -m pytest -v -q --nomemory --notimingintensive --nomypy \
-k "not test_parseconnect and not CreateEngineTest and not test_bad_args and not test_includes_none and not test_pep695_value"
%endif

%files
%{python3_sitearch}/sqlalchemy
%{python3_sitearch}/%{module}-%{version}.dist-info/
%doc CHANGES.rst README.rst README.dialects.rst README.unittests.rst
%license LICENSE

%files -n %{name}-doc
%doc doc/
%doc examples/
