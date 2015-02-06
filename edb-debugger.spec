%define _name   debugger 
%define _exe    edb

Name:           edb-debugger
Summary:        A free OllyDbg like debugger
Version:        0.9.17
Release:        3
Source0:        http://www.codef00.com/projects/%{_name}-%{version}.tgz
URL:            http://www.codef00.com/projects

Group:          Development/Other
License:        GPLv2 

BuildRequires: qt4-devel >= 4.5
BuildRequires: boost-devel >= 1.35
BuildRequires: imagemagick
BuildRequires: desktop-file-utils


%description
One of the main goals of this debugger is modularity. 
The interface is written in Qt4 and is therefore source portable 
to many platforms. The debugger core is a plugin and the platform 
specific code is isolated to just a few files, porting to a new OS 
would require porting these few files and implementing a plugin 
which implements the DebuggerCoreInterface interface. Also, 
because the plugins are based on the QPlugin API, and do their work 
through the DebuggerCoreInterface object, they are almost always 
portable with just a simple recompile.
The disassembly engine is my edisassm project. I feel that this 
disassembler is mature and works well. It is worth noting that the 
current version of edb has temporarily dropped AT&T syntax support. 
Once this is implemented in edisassm, it will return.

%prep 
%setup -q -n %{_name}

%build
%{qmake_qt4} PREFIX=%{_prefix} DEFAULT_PLUGIN_PATH="%{_libdir}/%{_exe}/"
%make

%install
make install INSTALL_ROOT=%{buildroot}
mkdir -p %{buildroot}{%{_miconsdir},%{_iconsdir},%{_liconsdir},%{_bindir},%{_libdir}}/
install -c -m 0755 src/images/edb48-logo.png "$RPM_BUILD_ROOT%{_liconsdir}/%{_exe}.png"
%{__mv} %{buildroot}/bin/* %{buildroot}%{_bindir}/
%{__mv} %{buildroot}/%{_lib}/* %{buildroot}%{_libdir}/
%{__rm} -fr %{buildroot}/bin
%{__rm} -fr %{buildroot}/%{_lib}

convert src/images/edb48-logo.png -resize 32x32 $RPM_BUILD_ROOT%{_iconsdir}/%{_exe}.png
convert src/images/edb48-logo.png -resize 16x16 $RPM_BUILD_ROOT%{_miconsdir}/%{_exe}.png

desktop-file-install --vendor="" \
		     --dir $RPM_BUILD_ROOT%{_datadir}/applications \
		     %{_exe}.desktop



%files
%defattr(-,root,root,-)
%{_bindir}/%{_exe}
%{_libdir}/%{_exe}/*.so
%{_datadir}/applications/%{_exe}.desktop
%{_liconsdir}/%{_exe}.png
%{_miconsdir}/%{_exe}.png
%{_iconsdir}/%{_exe}.png



%changelog
* Thu Jul 14 2011 Angelo Naselli <anaselli@mandriva.org> 0.9.17-1mdv2011
+ Revision: 690008
- import edb-debugger

