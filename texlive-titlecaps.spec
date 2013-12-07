# revision 30911
# category Package
# catalog-ctan /macros/latex/contrib/titlecaps
# catalog-date 2013-06-19 11:29:28 +0200
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-titlecaps
Version:	1.0
Release:	5
Summary:	Setting rich-text input into Titling Caps
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/titlecaps
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/titlecaps.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/titlecaps.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package is intended for setting rich text into titling
capitals (in which the first character of words are
capitalized). It automatically accounts for diacritical marks
(like umlauts), national symbols (like "ae"), punctuation, and
font changing commands that alter the appearance or size of the
text. It allows a list of predesignated words to be protected
as lower-cased, and also allows for titling exceptions of
various sorts.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/titlecaps/titlecaps.sty
%doc %{_texmfdistdir}/doc/latex/titlecaps/README
%doc %{_texmfdistdir}/doc/latex/titlecaps/titlecaps.pdf
%doc %{_texmfdistdir}/doc/latex/titlecaps/titlecaps.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
