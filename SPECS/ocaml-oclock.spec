%define debug_package %{nil}

Name:           ocaml-oclock
Version:        0.3
Release:        2%{?dist}
Summary:        POSIX monotonic clock for OCaml
License:        ISC
Group:          Development/Libraries
URL:            https://github.com/polazarus/oclock
Source0:        http://github.com/polazarus/oclock/archive/v0.3/oclock-%{version}.tar.gz
Patch0:         oclock-1-cc-headers
Patch1:         oclock-2-destdir
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib-devel

%description
A POSIX monotonic clock for OCaml

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n oclock-%{version}
%patch0 -p1
%patch1 -p1

%build
if [ -x ./configure ]; then
  ./configure
fi
make

%install
mkdir -p %{buildroot}/%{_libdir}/ocaml
mkdir -p %{buildroot}/%{_libdir}/ocaml/stublibs
export OCAMLFIND_LDCONF=ignore
make install DESTDIR=%{buildroot}/%{_libdir}/ocaml


%files
# This space intentionally left blank

%files devel
%doc LICENSE README.markdown
%{_libdir}/ocaml/oclock/*
%{_libdir}/ocaml/stublibs/dlloclock.so
%{_libdir}/ocaml/stublibs/dlloclock.so.owner

%changelog
* Wed May 29 2013 David Scott <dave.scott@eu.citrix.com> - 0.3-2
- Initial package

