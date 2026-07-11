%global tl_name cqubeamer
%global tl_revision 54512

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	LaTeX Beamer Template for Chongqing University
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/xetex/latex/cqubeamer
License:	mit cc-by-4
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cqubeamer.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cqubeamer.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides a LaTeX beamer template designed for researchers
of Chongqing University. It can be used for academic reports,
conferences, or thesis defense, and can be helpful for delivering a
speech. It should be used with the XeTeX engine.

