Name:		polybar
Version:	3.4.0
Release:	1
Summary:	A fast and easy-to-use status bar
License:	MIT
URL:		https://github.com/polybar/polybar
Source0:	https://github.com/polybar/polybar/archive/%{version}.tar.gz
Source1:	https://github.com/polybar/xpp/archive/d2ff2aaba6489f606bbcc090c0a78a8a3f9fcd1f.zip

BuildRequires:  cmake
BuildRequires:  cmake(jsoncpp)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  wireless-tools
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(libnl-3.0)
BuildRequires:  pkgconfig(xcb-xrm)
BuildRequires:  pkgconfig(xcb-cursor)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  fonts-ttf-unifont
BuildRequires:  python2-devel
BuildRequires:  x11-font-misc
Requires:	fonts-ttf-unifont
Requires:	x11-font-misc

%description
A fast and easy-to-use status bar

%prep
%autosetup -a 1
# Submodule path 'lib/i3ipcpp': checked out '21ce9060ac7c502225fdbd2f200b1cbdd8eca08d'
# Submodule path 'lib/xpp': checked out 'd2ff2aaba6489f606bbcc090c0a78a8a3f9fcd1f'

rm -rf lib/xpp
mv xpp-d2ff2aaba6489f606bbcc090c0a78a8a3f9fcd1f/ lib/xpp

%build
%cmake
%make_build

%install
%make_install -C build

%files
%dir %{_datadir}/bash-completion/
%dir %{_datadir}/bash-completion/completions
%dir %{_datadir}/doc/%{name}
%dir %{_datadir}/zsh/
%dir %{_datadir}/zsh/site-functions
%{_bindir}/%{name}
%{_bindir}/%{name}-msg
%{_datadir}/doc/%{name}/config
%{_mandir}/man1/%{name}.1*
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/zsh/site-functions/_%{name}
%{_datadir}/zsh/site-functions/_%{name}_msg
%{_datadir}/doc/polybar/
