%global srcname arpy

Name:          python-%{srcname}
Version:       2.3.0
Release:       1
Summary:       Library for accessing "ar" files
License:       BSD-2-Clause
URL:           https://github.com/viraptor/arpy
Source0:       https://github.com/viraptor/arpy/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:     noarch

%description
arpy is a library for accessing the archive files and reading the contents.

It supports extended long filenames in both GNU and BSD format. Right now it
does not support the symbol tables, but can ignore them gracefully.

%package -n    python3-%{srcname}
Summary:       %{summary}
BuildRequires: python3-devel python3-setuptools
BuildRequires: python3-pip python3-wheel python3-pytest

%description -n python3-%{srcname}
arpy is a library for accessing the archive files and reading the contents.

It supports extended long filenames in both GNU and BSD format. Right now it
does not support the symbol tables, but can ignore them gracefully.

This package allows using arpy in Python 3 applications.

%prep
%autosetup -n %{srcname}-%{version} -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%pytest

%files -n python3-%{srcname}
%doc README.md
%{python3_sitelib}/*

%changelog
* Tue Jun 17 2025 Songsong Zhang <U2FsdGVkX1@gmail.com> - 2.3.0-1
- Initial package
- Based on Fedora
