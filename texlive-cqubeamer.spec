Name:		texlive-cqubeamer
Version:	54512
Release:	2
Summary:	LaTeX Beamer Template for Chongqing University
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/cqubeamer
License:	mit cc-by-4
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cqubeamer.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cqubeamer.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a LaTeX beamer template designed for
researchers of Chongqing University. It can be used for
academic reports, conferences, or thesis defense, and can be
helpful for delivering a speech. It should be used with the
XeTeX engine.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/xelatex/cqubeamer
%doc %{_texmfdistdir}/doc/xelatex/cqubeamer

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
