Summary:	Configuration files for smart
Name:		smart-config
Version:	2.99
Release:	1
License:	GPL
Group:		Base
Source0:	%{name}-th.channel
Source1:	%{name}-th-test.channel
Requires:	smart
Provides:	smart-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains smart configuration files for PLD.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_sysconfdir}/smart/channels
install %{SOURCE0} $RPM_BUILD_ROOT%{_sysconfdir}/smart/channels/pld-th.channel
install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/smart/channels/pld-th-test.channel

for file in $RPM_BUILD_ROOT%{_sysconfdir}/smart/channels/*.channel; do
	sed -i -e's,@ARCH@,%{_target_cpu},g' $file
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_sysconfdir}/smart
%dir %{_sysconfdir}/smart/channels
%config(noreplace) %{_sysconfdir}/smart/channels/*.channel
