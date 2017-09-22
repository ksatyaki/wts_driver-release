Name:           ros-lunar-wts-driver
Version:        1.0.4
Release:        2%{?dist}
Summary:        ROS wts_driver package

Group:          Development/Libraries
License:        GPLv3
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-lunar-message-runtime
Requires:       ros-lunar-roscpp
Requires:       ros-lunar-std-msgs
BuildRequires:  ros-lunar-catkin
BuildRequires:  ros-lunar-message-generation
BuildRequires:  ros-lunar-roscpp
BuildRequires:  ros-lunar-std-msgs

%description
The wts_driver package

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/lunar" \
        -DCMAKE_PREFIX_PATH="/opt/ros/lunar" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/lunar

%changelog
* Fri Sep 22 2017 Chittaranjan Srinivas Swaminathan <chitt@live.in> - 1.0.4-2
- Autogenerated by Bloom

* Fri Sep 22 2017 Chittaranjan Srinivas Swaminathan <chitt@live.in> - 1.0.4-1
- Autogenerated by Bloom

* Fri Sep 22 2017 Chittaranjan Srinivas Swaminathan <chitt@live.in> - 1.0.4-0
- Autogenerated by Bloom

