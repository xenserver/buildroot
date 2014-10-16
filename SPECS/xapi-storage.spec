Summary:       Xapi storage interface
Name:          xapi-storage
Version:       0.1
Release:       1%{?dist}
URL:           https://github.com/djs55/xapi-storage
Source0:       https://github.com/djs55/xapi-storage/archive/v%{version}/%{name}-%{version}.tar.gz
License:       LGPL+linking exception

BuildRequires: python-devel
BuildRequires: python-setuptools
BuildRequires: ocaml
BuildRequires: ocaml-findlib
BuildRequires: ocaml-cow-devel
BuildRequires: ocaml-xmlm-devel
BuildRequires: ocaml-cmdliner-devel
BuildRequires: ocaml-rpc-devel

%description
Xapi storage inteface libraries

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:       ocaml-findlib
Requires:       ocaml-cow-devel
Requires:       ocaml-xmlm-devel
Requires:       ocaml-cmdliner-devel
Requires:       ocaml-rpc-devel

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n %{name}-%{version}

%build
make
cd ocaml
ocaml setup.ml -configure --prefix %{_prefix} \
      --libdir %{_libdir} \
      --libexecdir %{_libexecdir} \
      --exec-prefix %{_exec_prefix} \
      --bindir %{_bindir} \
      --sbindir %{_sbindir} \
      --mandir %{_mandir} \
      --datadir %{_datadir} \
      --localstatedir %{_localstatedir} \
      --sharedstatedir %{_sharedstatedir} \
      --destdir $RPM_BUILD_ROOT
ocaml setup.ml -build

%install
cd ocaml
rm -rf $RPM_BUILD_ROOT
export DESTDIR=$RPM_BUILD_ROOT
export OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR
ocaml setup.ml -install
cd ../python
%{__python} setup.py install -O2 --root %{buildroot}
rm -rf %{buildroot}/%{python_sitelib}/*-py*.egg-info

%files
%defattr(-,root,root,-)
%{_libdir}/ocaml/xapi-storage
%exclude %{_libdir}/ocaml/xapi-storage/*.a
%exclude %{_libdir}/ocaml/xapi-storage/*.cmxa
%exclude %{_libdir}/ocaml/xapi-storage/*.ml
%{python_sitelib}/xapi.py*
%{python_sitelib}/d.py*
%{python_sitelib}/v.py*
%{python_sitelib}/p.py*

%files devel
%defattr(-,root,root,-)
%{_libdir}/ocaml/xapi-storage/*.a
%{_libdir}/ocaml/xapi-storage/*.cmxa
%{_libdir}/ocaml/xapi-storage/*.ml

%changelog
* Thu Oct 16 2014 David Scott <dave.scott@citrix.com> - 0.1-1
- Initial package
