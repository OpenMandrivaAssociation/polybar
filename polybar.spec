Name:		polybar
Version:	3.7.2
Release:	2
Summary:	A fast and easy-to-use status bar
License:	MIT
URL:		https://github.com/polybar/polybar
Source0:	https://github.com/polybar/polybar/archive/%{version}/%{name}-%{version}.tar.gz
# Bundled libs
Source1:        %{url}/i3ipcpp/archive/i3ipcpp-0daa58349ab3373161a4a73c1ccd2822328d2c73.tar.gz
Source2:        %{url}/xpp/archive/xpp-a8b9e682ba65ca4a6d805c8be97c5232bae3c0c1.tar.gz

BuildRequires:  cmake
BuildRequires:  cmake(jsoncpp)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libuv)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(libpulse)
#BuildRequires:  wireless-tools
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(libnl-3.0)
BuildRequires:  pkgconfig(xcb-xrm)
BuildRequires:  pkgconfig(xcb-cursor)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  pkgconfig(xcb-xrm)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  fonts-ttf-unifont
BuildRequires:  python3dist(sphinx)
BuildRequires:  x11-font-misc
# Optional BR:
BuildRequires:  %{_lib}xcb-xkb1
BuildRequires:  i3-wm
BuildRequires:  pkgconfig(jsoncpp)
BuildRequires:  pkgconfig(libmpdclient)

Requires:	fonts-ttf-unifont
Requires:	x11-font-misc

Provides:       bundled(i3ipcpp) = 0.7.1
Provides:       bundled(xpp) = 1.4.0

%description
A fast and easy-to-use status bar

%prep
%autosetup -p1

tar xf %{S:1}
tar xf %{S:2}
mv i3ipcpp-* lib/i3ipcpp
mv xpp-*     lib/xpp

%build
%cmake
%make_build

%install
%make_install -C build

%files
%doc %{_datadir}/doc/polybar/
%dir %{_datadir}/bash-completion/
%dir %{_datadir}/bash-completion/completions
%dir %{_datadir}/zsh/
%dir %{_datadir}/zsh/site-functions
%{_sysconfdir}/polybar/config.ini
%{_bindir}/%{name}
%{_bindir}/%{name}-msg
#{_datadir}/doc/%{name}/config
#% {_mandir}/man1/%{name}.1*
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/zsh/site-functions/_%{name}
%{_datadir}/zsh/site-functions/_%{name}_msg
%{_mandir}/man1/polybar-msg.1.*
%{_mandir}/man1/polybar.1.*
%{_mandir}/man5/polybar.5.*
