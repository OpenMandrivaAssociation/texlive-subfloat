Name:		texlive-subfloat
Version:	29349
Release:	2
Summary:	Sub-numbering for figures and tables
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/subfloat
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/subfloat.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/subfloat.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/subfloat.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package enables sub-numbering of floats (figures and
tables) similar to the subequations-environment of the amsmath
package. The subfloat package is not to be confused with the
subfig package which generates sub-figures within one normal
figure, and manages their placement; subfloat only affects
captions and numbering.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/subfloat/subfloat.sty
%doc %{_texmfdistdir}/doc/latex/subfloat/ChangeLog
%doc %{_texmfdistdir}/doc/latex/subfloat/README
%doc %{_texmfdistdir}/doc/latex/subfloat/install.sh
%doc %{_texmfdistdir}/doc/latex/subfloat/subfloat.pdf
#- source
%doc %{_texmfdistdir}/source/latex/subfloat/Makefile
%doc %{_texmfdistdir}/source/latex/subfloat/subfloat.dtx
%doc %{_texmfdistdir}/source/latex/subfloat/subfloat.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
