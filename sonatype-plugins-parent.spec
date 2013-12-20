%_javapackages_macros
%global tag a594629

Name:           sonatype-plugins-parent
Version:        8
Release:        6.0%{?dist}
Summary:        Sonatype Plugins Parent POM
BuildArch:      noarch

License:        ASL 2.0
URL:            https://github.com/sonatype/oss-parents
Source:         https://github.com/sonatype/oss-parents/tarball/plugins-parent-%{version}/%{name}-%{version}.tar.gz
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt

BuildRequires:  maven-local
BuildRequires:  forge-parent

%description
This package provides Sonatype plugins parent POM used by other Sonatype
packages.

%prep
%setup -q -n sonatype-oss-parents-%{tag}
cp -p %{SOURCE1} LICENSE

%build
cd ./plugins-parent
%mvn_build

%install
cd ./plugins-parent
%mvn_install

%files -f plugins-parent/.mfiles
%doc LICENSE
