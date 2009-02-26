%define name    cowdancer
%define version 0.48
%define release %mkrel 1

Summary:	Copy-on-write directory tree utility.
Name:		%name
Version: 	%version
Release: 	%release
License: GPL
Group: System Environment/Shells
Source: %{name}_%{version}.tar.gz
Patch0: Makefile.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Tries to make copy-on-write semantics upon hard-link copied
directory trees generated with 'cp -la'
'cow-shell' command invokes a shell session. Within that session,
under the directory cow-shell was invoked, 
cowdancer will create a new file when existing i-nodes are opened for 
write.
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
%{makeinstall_std}

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
