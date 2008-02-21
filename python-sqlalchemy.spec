Summary:	SQL toolkit and object relational mapper for Python
Name:		python-sqlalchemy
Version:	0.3.11
Release:	%mkrel 1
License:	MIT
Group:		Development/Python
URL:		http://www.sqlalchemy.org/
Source0:	http://dl.sf.net/sqlalchemy/SQLAlchemy-%{version}.tar.gz
BuildRequires:	python-devel
BuildRequires:	python-setuptools
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
SQLAlchemy is a SQL toolkit and object relational mapper for Python. It 
encourages "relational mapping" as opposed to "table mapping" and includes 
enterprise-level features such as eager loading, unit-of-work object commits, 
topological dependency sorting, and full usage of bind parameters. It 
supports MySQL, Postgres, Oracle, and SQLite.

%prep

%setup -q -n SQLAlchemy-%{version}

%build
python setup.py build

%install
rm -rf %{buildroot}

python setup.py install --skip-build --root=%{buildroot} --install-purelib=%{python_sitelib}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc LICENSE README doc/* examples
%{python_sitelib}/sqlalchemy/
%{python_sitelib}/SQLAlchemy-%{version}-py*.egg-info/

