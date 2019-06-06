# generated by cabal-rpm-1.0.0 --standalone
# https://fedoraproject.org/wiki/Packaging:Haskell

%global ghc_without_dynamic 1
%global ghc_without_shared 1
%global without_prof 1
%global without_haddock 1
%global debug_package %{nil}

Name:           pkgtreediff
Version:        0.2.1
Release:        1%{?dist}
Summary:        Package tree diff tool

License:        GPLv3+
Url:            https://hackage.haskell.org/package/%{name}
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{name}-%{version}/%{name}-%{version}.tar.gz
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
%if %{defined fedora}
BuildRequires:  ghc-async-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-filepath-devel
#BuildRequires:  ghc-http-directory-devel
#BuildRequires:  ghc-simple-cmd-args-devel
BuildRequires:  ghc-simple-cmd-devel
BuildRequires:  ghc-text-devel
# End cabal-rpm deps
# simple-cmd-args
BuildRequires:  ghc-optparse-applicative-devel
# http-directory -> html-conduit
BuildRequires:  ghc-attoparsec-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-conduit-devel
BuildRequires:  ghc-conduit-extra-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-resourcet-devel
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-xml-conduit-devel
BuildRequires:  ghc-xml-types-devel
%else
BuildRequires:  ghc-libraries
BuildRequires:  zlib-devel
%endif
BuildRequires:  cabal-install > 1.18

%description
Tool for comparing RPM package files in OS dist trees.


%prep
# Begin cabal-rpm setup:
%setup -q
# End cabal-rpm setup


%build
# Begin cabal-rpm build:
%global cabal cabal
%cabal update
%cabal sandbox init
%cabal install --only-dependencies
%ghc_bin_build
# End cabal-rpm build


%install
# Begin cabal-rpm install
%ghc_bin_install
# End cabal-rpm install


%files
# Begin cabal-rpm files:
%license LICENSE
%doc CHANGELOG.md README.md TODO
%{_bindir}/%{name}
# End cabal-rpm files


%changelog
* Thu Jun  6 2019 fedora-toolbox <petersen@redhat.com> - 0.2.1-1
- improve recursion and add --ignore-arch

* Thu Jun  6 2019 fedora-toolbox <petersen@redhat.com> - 0.2-1
- add summary and --ignore-arch

* Tue Jun  4 2019 Jens Petersen <petersen@redhat.com> - 0.1-1
- update to 0.1
- added --ignore-version option

* Fri May 31 2019 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 0.0-1
- spec file generated by cabal-rpm-1.0.0
