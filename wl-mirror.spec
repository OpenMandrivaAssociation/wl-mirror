Name:           wl-mirror
Version:        0.18.2
Release:        1
Summary:        Simple Wayland output mirror client
 
License:        GPL-3.0-or-later
URL:            https://github.com/Ferdi265/wl-mirror
Source0:       https://github.com/Ferdi265/wl-mirror/releases/download/v%{version}/%{name}-%{version}.tar.gz
 
BuildRequires:  cmake
BuildRequires:  gnupg
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(scdoc)
BuildRequires:  pkgconfig(wayland-protocols)
 
# wlr-protocols may have different licenses, but it does not affect
# the generated code or the binary file license
Provides:       bundled(wlr-protocols) = 0^20220905g4264185
 
%description
Simple output mirror client for Wlroots-based compositors.
 
wl-mirror attempts to provide a solution to sway's lack of output
mirroring by mirroring an output onto a client surface.
 
%prep
%autosetup -p1
# remove bundled wayland-protocols, just in case
rm -rf proto/wayland-protocols

%build
%cmake \
    -DFORCE_SYSTEM_WL_PROTOCOLS:BOOL=ON \
    -DINSTALL_DOCUMENTATION:BOOL=ON
%make_build
 
%install
%make_install -C build

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
