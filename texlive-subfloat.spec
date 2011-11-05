# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/subfloat
# catalog-date 2008-06-17 13:09:54 +0200
# catalog-license lppl
# catalog-version 2.14
Name:		texlive-subfloat
Version:	2.14
Release:	1
Summary:	Sub-numbering for figures and tables
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/subfloat
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/subfloat.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/subfloat.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/subfloat.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
This package enables sub-numbering of floats (figures and
tables) similar to the subequations-environment of the amsmath
package. The subfloat package is not to be confused with the
subfig package which generates sub-figures within one normal
figure, and manages their placement; subfloat only affects
captions and numbering.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}