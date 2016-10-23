Name     : jdk-jodd
Version  : 3.5.2
Release  : 1
URL      : http://repo1.maven.org/maven2/org/jodd/jodd-bean/3.5.2/jodd-bean-3.5.2.jar
Source0  : http://repo1.maven.org/maven2/org/jodd/jodd-bean/3.5.2/jodd-bean-3.5.2.jar
Source1  : http://repo1.maven.org/maven2/org/jodd/jodd-bean/3.5.2/jodd-bean-3.5.2.pom
Source2  : http://repo1.maven.org/maven2/org/jodd/jodd-core/3.5.2/jodd-core-3.5.2.jar
Source3  : http://repo1.maven.org/maven2/org/jodd/jodd-core/3.5.2/jodd-core-3.5.2.pom
Source4  : http://repo1.maven.org/maven2/org/jodd/jodd-db/3.5.2/jodd-db-3.5.2.jar
Source5  : http://repo1.maven.org/maven2/org/jodd/jodd-db/3.5.2/jodd-db-3.5.2.pom
Source6  : http://repo1.maven.org/maven2/org/jodd/jodd-http/3.5.2/jodd-http-3.5.2.jar
Source7  : http://repo1.maven.org/maven2/org/jodd/jodd-http/3.5.2/jodd-http-3.5.2.pom
Source8  : http://repo1.maven.org/maven2/org/jodd/jodd-joy/3.5.2/jodd-joy-3.5.2.jar
Source9  : http://repo1.maven.org/maven2/org/jodd/jodd-joy/3.5.2/jodd-joy-3.5.2.pom
Source10  : http://repo1.maven.org/maven2/org/jodd/jodd-jtx/3.5.2/jodd-jtx-3.5.2.jar
Source11  : http://repo1.maven.org/maven2/org/jodd/jodd-jtx/3.5.2/jodd-jtx-3.5.2.pom
Source12  : http://repo1.maven.org/maven2/org/jodd/jodd-lagarto-web/3.5.2/jodd-lagarto-web-3.5.2.jar
Source13  : http://repo1.maven.org/maven2/org/jodd/jodd-lagarto-web/3.5.2/jodd-lagarto-web-3.5.2.pom
Source14  : http://repo1.maven.org/maven2/org/jodd/jodd-lagarto/3.5.2/jodd-lagarto-3.5.2.jar
Source15  : http://repo1.maven.org/maven2/org/jodd/jodd-lagarto/3.5.2/jodd-lagarto-3.5.2.pom
Source16  : http://repo1.maven.org/maven2/org/jodd/jodd-log/3.5.2/jodd-log-3.5.2.jar
Source17  : http://repo1.maven.org/maven2/org/jodd/jodd-log/3.5.2/jodd-log-3.5.2.pom
Source18  : http://repo1.maven.org/maven2/org/jodd/jodd-madvoc/3.5.2/jodd-madvoc-3.5.2.jar
Source19  : http://repo1.maven.org/maven2/org/jodd/jodd-madvoc/3.5.2/jodd-madvoc-3.5.2.pom
Source20  : http://repo1.maven.org/maven2/org/jodd/jodd-mail/3.5.2/jodd-mail-3.5.2.jar
Source21  : http://repo1.maven.org/maven2/org/jodd/jodd-mail/3.5.2/jodd-mail-3.5.2.pom
Source22  : http://repo1.maven.org/maven2/org/jodd/jodd-petite/3.5.2/jodd-petite-3.5.2.jar
Source23  : http://repo1.maven.org/maven2/org/jodd/jodd-petite/3.5.2/jodd-petite-3.5.2.pom
Source24  : http://repo1.maven.org/maven2/org/jodd/jodd-props/3.5.2/jodd-props-3.5.2.jar
Source25  : http://repo1.maven.org/maven2/org/jodd/jodd-props/3.5.2/jodd-props-3.5.2.pom
Source26  : http://repo1.maven.org/maven2/org/jodd/jodd-proxetta/3.5.2/jodd-proxetta-3.5.2.jar
Source27  : http://repo1.maven.org/maven2/org/jodd/jodd-proxetta/3.5.2/jodd-proxetta-3.5.2.pom
Source28  : http://repo1.maven.org/maven2/org/jodd/jodd-servlet/3.5.2/jodd-servlet-3.5.2.jar
Source29  : http://repo1.maven.org/maven2/org/jodd/jodd-servlet/3.5.2/jodd-servlet-3.5.2.pom
Source30  : http://repo1.maven.org/maven2/org/jodd/jodd-swingspy/3.5.2/jodd-swingspy-3.5.2.jar
Source31  : http://repo1.maven.org/maven2/org/jodd/jodd-swingspy/3.5.2/jodd-swingspy-3.5.2.pom
Source32  : http://repo1.maven.org/maven2/org/jodd/jodd-upload/3.5.2/jodd-upload-3.5.2.jar
Source33  : http://repo1.maven.org/maven2/org/jodd/jodd-upload/3.5.2/jodd-upload-3.5.2.pom
Source34  : http://repo1.maven.org/maven2/org/jodd/jodd-vtor/3.5.2/jodd-vtor-3.5.2.jar
Source35  : http://repo1.maven.org/maven2/org/jodd/jodd-vtor/3.5.2/jodd-vtor-3.5.2.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause
BuildRequires : javapackages-tools
BuildRequires : lxml
BuildRequires : openjdk-dev
BuildRequires : python3
BuildRequires : six

%description
No detailed description available

%prep

%build

%install
mkdir -p %{buildroot}/usr/share/maven-poms
mkdir -p %{buildroot}/usr/share/maven-metadata
mkdir -p %{buildroot}/usr/share/java

mv %{SOURCE0} %{buildroot}/usr/share/java/jodd-bean.jar
mv %{SOURCE1} %{buildroot}/usr/share/maven-poms/jodd-bean.pom

mv %{SOURCE2} %{buildroot}/usr/share/java/jodd-core.jar
mv %{SOURCE3} %{buildroot}/usr/share/maven-poms/jodd-core.pom

mv %{SOURCE4} %{buildroot}/usr/share/java/jodd-db.jar
mv %{SOURCE5} %{buildroot}/usr/share/maven-poms/jodd-db.pom

mv %{SOURCE6} %{buildroot}/usr/share/java/jodd-http.jar
mv %{SOURCE7} %{buildroot}/usr/share/maven-poms/jodd-http.pom

mv %{SOURCE8} %{buildroot}/usr/share/java/jodd-joy.jar
mv %{SOURCE9} %{buildroot}/usr/share/maven-poms/jodd-joy.pom

mv %{SOURCE10} %{buildroot}/usr/share/java/jodd-jtx.jar
mv %{SOURCE11} %{buildroot}/usr/share/maven-poms/jodd-jtx.pom

mv %{SOURCE12} %{buildroot}/usr/share/java/jodd-lagarto-web.jar
mv %{SOURCE13} %{buildroot}/usr/share/maven-poms/jodd-lagarto-web.pom

mv %{SOURCE14} %{buildroot}/usr/share/java/jodd-lagarto.jar
mv %{SOURCE15} %{buildroot}/usr/share/maven-poms/jodd-lagarto.pom

mv %{SOURCE16} %{buildroot}/usr/share/java/jodd-log.jar
mv %{SOURCE17} %{buildroot}/usr/share/maven-poms/jodd-log.pom

mv %{SOURCE18} %{buildroot}/usr/share/java/jodd-madvoc.jar
mv %{SOURCE19} %{buildroot}/usr/share/maven-poms/jodd-madvoc.pom

mv %{SOURCE20} %{buildroot}/usr/share/java/jodd-mail.jar
mv %{SOURCE21} %{buildroot}/usr/share/maven-poms/jodd-mail.pom

mv %{SOURCE22} %{buildroot}/usr/share/java/jodd-petite.jar
mv %{SOURCE23} %{buildroot}/usr/share/maven-poms/jodd-petite.pom

mv %{SOURCE24} %{buildroot}/usr/share/java/jodd-props.jar
mv %{SOURCE25} %{buildroot}/usr/share/maven-poms/jodd-props.pom

mv %{SOURCE26} %{buildroot}/usr/share/java/jodd-proxetta.jar
mv %{SOURCE27} %{buildroot}/usr/share/maven-poms/jodd-proxetta.pom

mv %{SOURCE28} %{buildroot}/usr/share/java/jodd-servlet.jar
mv %{SOURCE29} %{buildroot}/usr/share/maven-poms/jodd-servlet.pom

mv %{SOURCE30} %{buildroot}/usr/share/java/jodd-swingspy.jar
mv %{SOURCE31} %{buildroot}/usr/share/maven-poms/jodd-swingspy.pom

mv %{SOURCE32} %{buildroot}/usr/share/java/jodd-upload.jar
mv %{SOURCE33} %{buildroot}/usr/share/maven-poms/jodd-upload.pom

mv %{SOURCE34} %{buildroot}/usr/share/java/jodd-vtor.jar
mv %{SOURCE35} %{buildroot}/usr/share/maven-poms/jodd-vtor.pom

# Creates metadata
for j in bean core db http joy jtx lagarto-web lagarto log madvoc mail petite \
	props proxetta servlet swingspy upload vtor
do

	python3 /usr/share/java-utils/maven_depmap.py \
	-n "" \
	--pom-base %{buildroot}/usr/share/maven-poms \
	--jar-base %{buildroot}/usr/share/java \
	%{buildroot}/usr/share/maven-metadata/jodd-$j.xml \
	%{buildroot}/usr/share/maven-poms/jodd-$j.pom \
	%{buildroot}/usr/share/java/jodd-$j.jar 
done

%files
%defattr(-,root,root,-)
/usr/share/java/jodd-bean.jar
/usr/share/java/jodd-core.jar
/usr/share/java/jodd-db.jar
/usr/share/java/jodd-http.jar
/usr/share/java/jodd-joy.jar
/usr/share/java/jodd-jtx.jar
/usr/share/java/jodd-lagarto-web.jar
/usr/share/java/jodd-lagarto.jar
/usr/share/java/jodd-log.jar
/usr/share/java/jodd-madvoc.jar
/usr/share/java/jodd-mail.jar
/usr/share/java/jodd-petite.jar
/usr/share/java/jodd-props.jar
/usr/share/java/jodd-proxetta.jar
/usr/share/java/jodd-servlet.jar
/usr/share/java/jodd-swingspy.jar
/usr/share/java/jodd-upload.jar
/usr/share/java/jodd-vtor.jar
/usr/share/maven-metadata/jodd-bean.xml
/usr/share/maven-metadata/jodd-core.xml
/usr/share/maven-metadata/jodd-db.xml
/usr/share/maven-metadata/jodd-http.xml
/usr/share/maven-metadata/jodd-joy.xml
/usr/share/maven-metadata/jodd-jtx.xml
/usr/share/maven-metadata/jodd-lagarto-web.xml
/usr/share/maven-metadata/jodd-lagarto.xml
/usr/share/maven-metadata/jodd-log.xml
/usr/share/maven-metadata/jodd-madvoc.xml
/usr/share/maven-metadata/jodd-mail.xml
/usr/share/maven-metadata/jodd-petite.xml
/usr/share/maven-metadata/jodd-props.xml
/usr/share/maven-metadata/jodd-proxetta.xml
/usr/share/maven-metadata/jodd-servlet.xml
/usr/share/maven-metadata/jodd-swingspy.xml
/usr/share/maven-metadata/jodd-upload.xml
/usr/share/maven-metadata/jodd-vtor.xml
/usr/share/maven-poms/jodd-bean.pom
/usr/share/maven-poms/jodd-core.pom
/usr/share/maven-poms/jodd-db.pom
/usr/share/maven-poms/jodd-http.pom
/usr/share/maven-poms/jodd-joy.pom
/usr/share/maven-poms/jodd-jtx.pom
/usr/share/maven-poms/jodd-lagarto-web.pom
/usr/share/maven-poms/jodd-lagarto.pom
/usr/share/maven-poms/jodd-log.pom
/usr/share/maven-poms/jodd-madvoc.pom
/usr/share/maven-poms/jodd-mail.pom
/usr/share/maven-poms/jodd-petite.pom
/usr/share/maven-poms/jodd-props.pom
/usr/share/maven-poms/jodd-proxetta.pom
/usr/share/maven-poms/jodd-servlet.pom
/usr/share/maven-poms/jodd-swingspy.pom
/usr/share/maven-poms/jodd-upload.pom
/usr/share/maven-poms/jodd-vtor.pom
