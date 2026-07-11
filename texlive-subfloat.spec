%global tl_name subfloat
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.14
Release:	%{tl_revision}.1
Summary:	Sub-numbering for figures and tables
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/subfloat
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/subfloat.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/subfloat.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/subfloat.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package enables sub-numbering of floats (figures and tables)
similar to the subequations-environment of the amsmath package. The
subfloat package is not to be confused with the subfig package which
generates sub-figures within one normal figure, and manages their
placement; subfloat only affects captions and numbering.

