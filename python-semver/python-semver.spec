%global srcname semver

Name:           python-%{srcname}
Version:        3.0.2
Release:        1
Summary:        Python helper for Semantic Versioning
License:        BSD-3-Clause
URL:            https://github.com/python-semver/python-semver
Source0:        https://github.com/python-semver/python-semver/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%global _description %{expand:
A Python module for semantic versioning. Simplifies comparing versions.}

%description %{_description}

%package -n     python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel python3-setuptools python3-setuptools_scm
BuildRequires:  python3-pip python3-wheel python3-pytest python3-pytest-cov

%description -n python3-%{srcname}
%{_description}

%prep
%autosetup -n %{srcname}-%{version} -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%pytest

%files -n python3-%{srcname}
%license LICENSE.txt
%doc README.rst CHANGELOG.rst
%{_bindir}/pysemver
%{python3_sitelib}/*

%changelog
* Tue Jun 17 2025 Songsong Zhang <U2FsdGVkX1@gmail.com> - 3.0.2-1
- Initial package
- Based on Fedora
