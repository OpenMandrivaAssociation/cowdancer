
Summary:	Copy-on-write directory tree utility
Name:		cowdancer
Version: 	0.89
Release: 	1
License: GPL
Group: Development/Other 
Source: http://httpredir.debian.org/debian/pool/main/c/cowdancer/cowdancer_%{version}.tar.xz
Patch0: makedev_glibc_fix.patch

%description
Tries to make copy-on-write semantics upon hard-link copied
directory trees generated with 'cp -la'.
'cow-shell' command invokes a shell session. Within that session,
under the directory cow-shell was invoked, cowdancer will create 
a new file when existing i-nodes are opened for  write.
Useful for quick scratch workspace and experimentation.
'cowbuilder' command is a wrapper for pbuilder which allows using 
pbuilder-like interface over cowdancer environment.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p0

%build
%{make}

%install
rm -rf %{buildroot}
%{makeinstall_std} LIBDIR=%_libdir

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc COPYING NEWS ChangeLog
%{_bindir}/*
%{_sbindir}/*
%{_libdir}/%{name}/*
%{_mandir}/man*/*
%{_sysconfdir}/bash_completion.d/*


%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0.48-4mdv2011.0
+ Revision: 617433
- the mass rebuild of 2010.0 packages

* Thu Sep 10 2009 Thierry Vignaud <tv@mandriva.org> 0.48-3mdv2010.0
+ Revision: 437128
- rebuild

* Fri Feb 27 2009 Anne Nicolas <ennael@mandriva.org> 0.48-2mdv2009.1
+ Revision: 345720
- bump
- fix libdir
- more cleaning
- clean spec file
- import cowdancer


