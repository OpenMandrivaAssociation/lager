%define devname %mklibname lager -d

Name: lager
Version: 0.1.0
Release: 1
Source0: https://github.com/arximboldi/lager/archive/refs/tags/v%{version}.tar.gz
Patch0: lager-0.1.0-sassc.patch
Summary: C++ library to assist value-oriented design by implementing the unidirectional data-flow architecture
URL: https://github.com/arximboldi/lager
License: BSL-1.0
Group: System/Libraries
BuildRequires: cmake
BuildRequires: ninja
BuildRequires: %mklibname -d zug
BuildRequires: cmake(Immer)
BuildRequires: sassc
BuildRequires: boost-devel
BuildArch: noarch

%description
lager is a C++ library to assist value-oriented design by implementing the
unidirectional data-flow architecture. It is heavily inspired by Elm and Redux,
and enables composable designs by promoting the use of simple value types and
testable application logic via pure functions. And you get time-travel for
free!

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{name} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%autosetup -p1
%cmake -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_datadir}/%{name}

%files -n %{devname}
%{_includedir}/*
%{_prefix}/lib/cmake/*
