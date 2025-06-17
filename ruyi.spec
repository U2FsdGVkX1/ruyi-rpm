Name:           ruyi
Version:        0.35.0
Release:        %autorelease
Summary:        RuyiSDK Package Manager

License:        Apache-2.0
URL:            https://github.com/ruyisdk/%{name}
Source0:        https://github.com/ruyisdk/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  libgit2-devel
BuildRequires:  python3-devel
BuildRequires:  pytest

%description
The package manager for RuyiSDK.

%prep
%autosetup -n %{name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{name}

%check
%pytest

%files -f %{pyproject_files}
%doc README.md
%license LICENSE-Apache.txt
%{_bindir}/ruyi

%changelog
%autochangelog
