# Lab 1: Java Programming

## 0. Environment Installation
### a. Java Installation

On Linux, we can install Java 8 on your computer using the following lines

```bash
# Install jdk8
sudo apt-get install openjdk-8-jdk-headless -qq > /dev/null

# Set environment variable JAVA_HOME
echo "export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64" >> ~/.bashrc
source ~/.bashrc
sudo update-alternatives --set java /usr/lib/jvm/java-8-openjdk-amd64/jre/bin/java
```

Or you can follow the steps on the lab manual. You can then check whether installation has been completed with `java -version`.

### b. Maven Installation

`maven` is the tool for building and managing Java-based project.

```bash
wget https://mirrors.ocf.berkeley.edu/apache/maven/maven-3/3.8.1/binaries/apache-maven-3.8.1-bin.tar.gz
tar xzvf apache-maven-3.8.1-bin.tar.gz

# Set PATH environment variable
cd ./apache-maven-3.8.1/bin
echo "export PATH=$(pwd):$PATH" >> ~/.bashrc
source ~/.bashrc
```

Confirm installation with `mvn -v`

## 1. Add Dependency
In this program, we use package `org.apache.commons.cli` to parse command line arguments.

When we want to add a dependency, for example `Apache Commons CLI`, then we can search on [mvnrepository](mvnrepository.com) for the package, find the maven configuration, then copy and paste the configuration into the `<dependencies>` block in `pom.xml`.

   For example, on this [website](https://mvnrepository.com/artifact/commons-cli/commons-cli/1.4) we can find the configuration to `Apache Common CLI 1.4`. Copying it into the `pom.xml` file gives us

   ```xml
    <dependencies>
        <!-- https://mvnrepository.com/artifact/commons-cli/commons-cli -->
        <dependency>
            <groupId>commons-cli</groupId>
            <artifactId>commons-cli</artifactId>
            <version>1.4</version>
        </dependency>
    </dependencies>
   ```

## 2. Compile and run with makefile
```sh
.../lab_1_code/ $ make
```

### a. Compile with `maven`
```sh
.../lab_1_code/ $ mvn package
```

### b. Run with different arguments
```sh
.../lab_1_code/ $ java -jar target/lab_1_code-1.0-SNAPSHOT.jar --hall config --query input/test.in
```

Change command line input in the end to run program, e.g. `--help`

```sh
.../lab_1_code/ $ java -jar target/lab_1_code-1.0-SNAPSHOT.jar --help
```
