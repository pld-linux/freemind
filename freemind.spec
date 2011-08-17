Summary:	A free mind-mapping software
Summary(pl.UTF-8):	Program do tworzenia map umysłu
Name:		freemind
Version:	0.9.0
%define		_rc Beta_19
Release:	0.%{_rc}.1
License:	GPL v2
Group:		X11/Applications
Source0:	http://heanet.dl.sourceforge.net/freemind/%{name}-src-%{version}_%{_rc}.tar.gz
# Source0-md5:	9ea298574370fcb4fe08bec60dd26499
Source1:	%{name}.desktop
Source2:	%{name}.xml
URL:		http://freemind.sourceforge.net/
BuildRequires:	ant-apache-regexp
BuildRequires:	ant-trax
BuildRequires:	jdk >= 1.4
BuildRequires:	sed >= 4.0
Requires:	jre-X11
Requires(post,postun):  desktop-file-utils
Requires(post,postun):  shared-mime-info
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FreeMind is an open source mind mapping software that enables you to
visualize ideas, projects, concepts, brainstorming, research or any
other task that can benefit from a structured overview.

%description -l pl.UTF-8
FreeMind jest otwartym programem do tworzenia map umysłu
umożliwiającym wizualne przedstawienie pomysłów, projektów, koncepcji,
burzy mózgów, pracy naukowej czy dowolnego innego problemu, który
mógłby skorzystać ze zorganizowanej formy prezentacji.

%prep
%setup -q -c
mv %{name}/* .
sed -i s,./doc/freemind.mm,%{_docdir}/freemind.mm, freemind.properties

%build
#JAVA_HOME=%{java_home}
%ant dist browser

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/mime/packages
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_pixmapsdir}
install -d $RPM_BUILD_ROOT%{_desktopdir}

cp -a bin/dist $RPM_BUILD_ROOT%{_datadir}/%{name}
rm $RPM_BUILD_ROOT%{_datadir}/%{name}/[Ff]ree[Mm]ind.*
rm $RPM_BUILD_ROOT%{_datadir}/%{name}/license
rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}/doc
cp -a bin/dist/%{name}.sh $RPM_BUILD_ROOT%{_bindir}/%{name}
cp -a freemind/images/FreeMindWindowIcon.png $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png
cp %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
cp %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/mime/packages

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
update-mime-database %{_datadir}/mime ||:
%update_desktop_database_post

%postun
umask 022
update-mime-database %{_datadir}/mime ||:
%update_desktop_database_postun

%files
%defattr(644,root,root,755)
%doc bin/dist/doc/freemind*
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_pixmapsdir}/%{name}.png
%{_desktopdir}/*.desktop
%{_datadir}/mime/packages/*
