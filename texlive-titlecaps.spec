%global tl_name titlecaps
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.3
Release:	%{tl_revision}.1
Summary:	Setting rich-text input into Titling Caps
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/titlecaps
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/titlecaps.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/titlecaps.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package is intended for setting rich text into titling capitals (in
which the first character of words are capitalized). It automatically
accounts for diacritical marks (like umlauts), national symbols (like
"ae"), punctuation, and font changing commands that alter the appearance
or size of the text. It allows a list of predesignated words to be
protected as lower-cased, and also allows for titling exceptions of
various sorts.

