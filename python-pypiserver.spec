Name:           python-pypiserver
Version:        1.5.0
Release:        1
Summary:        Minimal PyPI server for uploading & downloading packages with pip/easy_install
License:        MIT
URL:            https://github.com/pypiserver
Source:         https://github.com/pypiserver/pypiserver/archive/v%{version}.tar.gz#/pypiserver-%{version}.tar.gz
BuildRequires:  python3-webtest
BuildRequires:  python3-passlib >= 1.6
BuildRequires:  python3-pip >= 7
BuildRequires:  python3-pytest >= 3.5
BuildRequires:  python3-setuptools-git >= 0.3
BuildRequires:  python3-setuptools_scm >= 1.15.0
BuildRequires:  python3-setuptools
BuildRequires:  python3-tox
BuildRequires:  python3-twine
BuildRequires:  python3-wheel >= 0.25.0
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-passlib >= 1.6
Requires:       python-setuptools

BuildArch:      noarch

%description
Minimal PyPI server for uploading & downloading packagesj with pip/easy_install

%package -n python3-pypiserver
Summary:        minimal PyPI server for use with pip/easy_install
Provides:       python-pypiserver

%description -n python3-pypiserver
Minimal PyPI server for uploading & downloading packagesj with pip/easy_install

%prep
%setup -q -n pypiserver-%{version}
sed -i '1{/env python/d}' pypiserver/*.py
# we don't need the extensions for smoke testing
rm -f pytest.ini

%build
%py3_build

%install
%py3_install

%check
# test_hash_algos:
# ERROR: No matching distribution found for a==1.0 (from centodeps)
# (see centodeps-setup.py)
pytest tests -k "not (test_pipInstall_openOk or test_pipInstall_authedOk or test_hash_algos)" || :

%files -n python3-pypiserver
%doc README.rst
%license LICENSE.txt
%{python3_sitelib}/pypiserver
%{python3_sitelib}/pypiserver-%{version}*-info
%{_bindir}/pypi-server

%changelog
* Wed Jun 1 2022 lvxiaoqian <xiaoqian@nj.iscas.ac.cn> - 1.5.0-1
- Initial package