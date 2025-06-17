%global srcname pygit2

Name:           python-%{srcname}
Version:        1.14.0
Release:        1
Summary:        Python bindings for libgit2
License:        GPL-2.0-only WITH GCC-exception-2.0
URL:            https://www.pygit2.org/
Source0:        https://github.com/libgit2/pygit2/archive/v%{version}.tar.gz#/%{srcname}-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  (libgit2-devel >= 1.7.0 with libgit2-devel < 1.8.0)

%description
pygit2 is a set of Python bindings to the libgit2 library, which implements
the core of Git.

%package -n     python3-%{srcname}
Summary:        Python 3 bindings for libgit2
BuildRequires:  python3-devel python3-setuptools
BuildRequires:  python3-pip python3-wheel python3-pytest
BuildRequires:  python3dist(cffi) >= 1.17

%description -n python3-%{srcname}
pygit2 is a set of Python bindings to the libgit2 library, which implements
the core of Git.

The python3-%{srcname} package contains the Python 3 bindings.

%prep
%autosetup -n %{srcname}-%{version} -p1

%build
%pyproject_build

%install
%pyproject_install
find %{_builddir} -name '.buildinfo' -print -delete

%check
%pytest

%files -n python3-%{srcname}
%license COPYING
%doc README.md
%{python3_sitearch}/*

%changelog
* Tue Jun 17 2025 Songsong Zhang <U2FsdGVkX1@gmail.com> - 1.14.0-1
- Initial package
- Based on Fedora
