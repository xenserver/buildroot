%define debug_package %{nil}

Name:           ocaml-oclock
Version:        0.3
Release:        2
Summary:        POSIX monotonic clock for OCaml
License:        ISC
Group:          Development/Other
URL:            https://github.com/polazarus/oclock
Source0:        oclock-0.3.tar.gz
Patch0:         oclock-1-cc-headers
Patch1:         oclock-2-destdir
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml ocaml-findlib
Requires:       ocaml ocaml-findlib

%description
A POSIX monotonic clock for OCaml

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
#Requires:       %{name} = %{version}-%{release}

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
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_libdir}/ocaml
mkdir -p %{buildroot}/%{_libdir}/ocaml/stublibs
export OCAMLFIND_LDCONF=ignore
make install DESTDIR=%{buildroot}/%{_libdir}/ocaml

%clean
rm -rf %{buildroot}

%files devel
%defattr(-,root,root)
%doc LICENSE README.markdown
%{_libdir}/ocaml/oclock/*
%{_libdir}/ocaml/stublibs/dlloclock.so
%{_libdir}/ocaml/stublibs/dlloclock.so.owner

%changelog
* Wed May 29 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

