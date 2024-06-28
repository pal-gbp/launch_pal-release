%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/humble/.*$
%global __requires_exclude_from ^/opt/ros/humble/.*$

Name:           ros-humble-launch-pal
Version:        0.1.13
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS launch_pal package

License:        Apache License 2.0
URL:            https://github.com/pal-robotics/launch_pal
Source0:        %{name}-%{version}.tar.gz

Requires:       python%{python3_pkgversion}-yaml
Requires:       ros-humble-ament-index-python
Requires:       ros-humble-launch
Requires:       ros-humble-launch-ros
Requires:       ros-humble-ros-workspace
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-yaml
BuildRequires:  ros-humble-ament-index-python
BuildRequires:  ros-humble-launch
BuildRequires:  ros-humble-launch-ros
BuildRequires:  ros-humble-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  ros-humble-ament-copyright
BuildRequires:  ros-humble-ament-flake8
BuildRequires:  ros-humble-ament-pep257
%endif

%description
Utilities for launch files

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
%py3_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
%py3_install -- --prefix "/opt/ros/humble"

%if 0%{?with_tests}
%check
# Look for a directory with a name indicating that it contains tests
TEST_TARGET=$(ls -d * | grep -m1 "\(test\|tests\)" ||:)
if [ -n "$TEST_TARGET" ] && %__python3 -m pytest --version; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
%__python3 -m pytest $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/humble

%changelog
* Fri Jun 28 2024 Jordan Palacios <jordan.palacios@pal-robotics.com> - 0.1.13-1
- Autogenerated by Bloom

* Tue Jun 18 2024 Jordan Palacios <jordan.palacios@pal-robotics.com> - 0.1.12-1
- Autogenerated by Bloom

* Wed May 08 2024 Jordan Palacios <jordan.palacios@pal-robotics.com> - 0.1.6-1
- Autogenerated by Bloom

* Tue Apr 23 2024 Jordan Palacios <jordan.palacios@pal-robotics.com> - 0.1.4-1
- Autogenerated by Bloom

* Thu Feb 29 2024 Jordan Palacios <jordan.palacios@pal-robotics.com> - 0.0.18-1
- Autogenerated by Bloom

* Fri Jan 19 2024 Jordan Palacios <jordan.palacios@pal-robotics.com> - 0.0.16-1
- Autogenerated by Bloom

* Wed Jan 17 2024 Jordan Palacios <jordan.palacios@pal-robotics.com> - 0.0.15-1
- Autogenerated by Bloom

* Mon Dec 18 2023 Jordan Palacios <jordan.palacios@pal-robotics.com> - 0.0.14-1
- Autogenerated by Bloom

* Mon Jul 10 2023 Jordan Palacios <jordan.palacios@pal-robotics.com> - 0.0.8-2
- Autogenerated by Bloom

* Thu Jun 29 2023 Jordan Palacios <jordan.palacios@pal-robotics.com> - 0.0.8-1
- Autogenerated by Bloom

* Tue Apr 04 2023 Jordan Palacios <jordan.palacios@pal-robotics.com> - 0.0.7-1
- Autogenerated by Bloom

