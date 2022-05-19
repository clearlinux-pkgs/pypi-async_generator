#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-async_generator
Version  : 1.10
Release  : 18
URL      : https://files.pythonhosted.org/packages/ce/b6/6fa6b3b598a03cba5e80f829e0dadbb49d7645f523d209b2fb7ea0bbb02a/async_generator-1.10.tar.gz
Source0  : https://files.pythonhosted.org/packages/ce/b6/6fa6b3b598a03cba5e80f829e0dadbb49d7645f523d209b2fb7ea0bbb02a/async_generator-1.10.tar.gz
Summary  : Async generators and context managers for Python 3.5+
Group    : Development/Tools
License  : Apache-2.0 MIT
Requires: pypi-async_generator-license = %{version}-%{release}
Requires: pypi-async_generator-python = %{version}-%{release}
Requires: pypi-async_generator-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
.. image:: https://img.shields.io/badge/chat-join%20now-blue.svg
:target: https://gitter.im/python-trio/general
:alt: Join chatroom

%package license
Summary: license components for the pypi-async_generator package.
Group: Default

%description license
license components for the pypi-async_generator package.


%package python
Summary: python components for the pypi-async_generator package.
Group: Default
Requires: pypi-async_generator-python3 = %{version}-%{release}

%description python
python components for the pypi-async_generator package.


%package python3
Summary: python3 components for the pypi-async_generator package.
Group: Default
Requires: python3-core
Provides: pypi(async_generator)

%description python3
python3 components for the pypi-async_generator package.


%prep
%setup -q -n async_generator-1.10
cd %{_builddir}/async_generator-1.10
pushd ..
cp -a async_generator-1.10 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1653003054
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-async_generator
cp %{_builddir}/async_generator-1.10/LICENSE.APACHE2 %{buildroot}/usr/share/package-licenses/pypi-async_generator/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/async_generator-1.10/LICENSE.MIT %{buildroot}/usr/share/package-licenses/pypi-async_generator/f8c5fdc67d412f3435473ee8ce595f06d921ca44
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot}/usr/share/clear/optimized-elf/ %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-async_generator/2b8b815229aa8a61e483fb4ba0588b8b6c491890
/usr/share/package-licenses/pypi-async_generator/f8c5fdc67d412f3435473ee8ce595f06d921ca44

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
