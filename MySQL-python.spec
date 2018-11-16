#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : MySQL-python
Version  : 1.2.5
Release  : 32
URL      : https://pypi.python.org/packages/source/M/MySQL-python/MySQL-python-1.2.5.zip
Source0  : https://pypi.python.org/packages/source/M/MySQL-python/MySQL-python-1.2.5.zip
Summary  : Python interface to MySQL
Group    : Development/Tools
License  : GPL-2.0
Requires: MySQL-python-python = %{version}-%{release}
BuildRequires : MySQL-python
BuildRequires : buildreq-distutils
BuildRequires : buildreq-distutils3
BuildRequires : mariadb-dev
BuildRequires : openssl-dev
BuildRequires : setuptools-legacypython
BuildRequires : zlib-dev

%description
=========================
        Python interface to MySQL
        =========================
        
        MySQLdb is an interface to the popular MySQL_ database server for

%package legacypython
Summary: legacypython components for the MySQL-python package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the MySQL-python package.


%package python
Summary: python components for the MySQL-python package.
Group: Default
Provides: mysql-python-python

%description python
python components for the MySQL-python package.


%prep
%setup -q -n MySQL-python-1.2.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1540414117
python2 setup.py build -b py2

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
py.test-2.7 || :
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)
