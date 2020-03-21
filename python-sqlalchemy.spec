%define debug_package %{nil}
%define module_name SQLAlchemy
%ifarch %arm %mips
%define debug_package %nil
%endif

Summary:	SQL toolkit and object relational mapper for Python

Name:		python-sqlalchemy
Version:	1.3.15
Release:	1
License:	MIT
Group:		Development/Python
Url:		http://www.sqlalchemy.org/
Source0:	https://files.pythonhosted.org/packages/8c/30/4134e726dd5ed13728ff814fa91fc01c447ad8700504653fe99d91fdd34b/SQLAlchemy-1.3.15.tar.gz
BuildRequires:	python-nose
BuildRequires:	python-setuptools
BuildRequires:	pkgconfig(python)

%description
%{module_name} is a SQL toolkit and object relational mapper for Python. It
encourages "relational mapping" as opposed to "table mapping" and includes
enterprise-level features such as eager loading, unit-of-work object commits,
topological dependency sorting, and full usage of bind parameters. It
supports MySQL, Postgres, Oracle, and SQLite.

%prep

%setup -qn %{module_name}-%{version}

%build
%__python setup.py build

%install
PYTHONDONTWRITEBYTECODE= %__python setup.py install --skip-build --root=%{buildroot} --install-purelib=%{py_platlibdir}

#%check
#%__python setup.py test

%files
%doc CHANGES LICENSE README* doc/* examples
%{py_platsitedir}/sqlalchemy/*
%{py_platsitedir}/%{module_name}-%{version}-py*.egg-info/
#{python_sitelib}/sqlalchemy_nose/
