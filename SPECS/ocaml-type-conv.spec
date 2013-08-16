Name:           ocaml-type-conv
Version:        109.20.00
Release:        1
Summary:        OCaml base library for type conversion

Group:          Development/Other
License:        LGPLv2+ with exceptions and BSD
URL:            http://www.ocaml.info/home/ocaml_sources.html#type-conv
Source0:        https://ocaml.janestreet.com/ocaml-core/%{version}/individual/type_conv-%{version}.tar.gz
#Patch0:         type-conv-META.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

BuildRequires:  ocaml >= 4.00.0
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-camlp4
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-camlp4-devel

%description
The type-conv mini library factors out functionality needed by
different preprocessors that generate code from type specifications,
because this functionality cannot be duplicated without losing the
ability to use these preprocessors simultaneously.

%prep
%setup -q -n type_conv-%{version}
#%patch0 -p1
#dos2unix LICENSE.Tywith

%build
make

%install
rm -rf %{buildroot}
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR
make install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc CHANGES.txt COPYRIGHT.txt INRIA-DISCLAIMER.txt INSTALL.txt LICENSE-Tywith.txt LICENSE.txt README.md THIRD-PARTY.txt
%{_libdir}/ocaml/type_conv

%changelog
* Wed Nov 25 2010 Mike McClurg <mike.mcclurg@citrix.com>
- Updated to version 2.0.1 for compatability with OCaml 3.12.0

* Fri May 14 2010 David Scott <dave.scott@eu.citrix.com>
- Customised for XCP

* Wed Jan 07 2009 Florent Monnier <blue_prawn@mandriva.org> 1.6.5-1mdv2009.1
+ Revision: 326698
- corrected group
- import ocaml-type-conv


* Sat Dec 20 2008 Florent Monnier <fmonnier@linux-nantes.org> 1.6.5-1mdv
- Initial RPM release made from the fedora rpm .spec file (revision 1.9) by Richard W.M. Jones
# found there: http://cvs.fedoraproject.org/viewvc/devel/ocaml-type-conv/ocaml-type-conv.spec
