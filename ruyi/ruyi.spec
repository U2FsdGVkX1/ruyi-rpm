Name:           ruyi
Version:        0.35.0
Release:        1
Summary:        RuyiSDK Package Manager
License:        Apache-2.0
URL:            https://github.com/ruyisdk/%{name}
Source0:        https://github.com/ruyisdk/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(packaging)
BuildRequires:  python3dist(pip) >= 19
BuildRequires:  python3dist(poetry-core)
BuildRequires:  python3dist(arpy)
BuildRequires:  python3dist(fastjsonschema) >= 2.15.1
BuildRequires:  (python3dist(jinja2) < 4~~ with python3dist(jinja2) >= 3)
BuildRequires:  python3dist(packaging) >= 21
BuildRequires:  python3dist(pygit2) >= 1.6
BuildRequires:  python3dist(pyyaml) >= 5.4
BuildRequires:  (python3dist(requests) < 3~~ with python3dist(requests) >= 2)
BuildRequires:  python3dist(rich) >= 11.2
BuildRequires:  python3dist(semver) >= 2.10
BuildRequires:  python3dist(tomlkit) >= 0.9

%description
The package manager for RuyiSDK.

%prep
%autosetup -n %{name}-%{version}

%build
%pyproject_build

%install
%pyproject_install

%check
%pytest

%files
%doc README.md
%license LICENSE-Apache.txt
%{_bindir}/ruyi
%{python3_sitelib}/*

%changelog
* Tue Jun 17 2025 Songsong Zhang <U2FsdGVkX1@gmail.com> - 0.35.0-1
- Initial package
