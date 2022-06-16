# Template: Sample Java Project

## Usage

Print "Hello World!" in terminal

- `Java` source files: `src/main/java/com/ve472/h0/`
- Dependency: None
- Plugin: None
- Input: None
- Output: None

## Compile and Run

- Remark: please install `Java`, `Maven`, `Makefile` first
- Compile: `$ mvn compile`
- Run: `$ java -jar target/ex4-1.0-SNAPSHOT.jar`
- Compile and run with `makefile`: `$ make`
- Clean target files: `$ make clean`

## Remark: How to use this template project

1. Copy and paste the folder into your working directory
2. Change folder `src/main/java/com/ve472/h0` name if wanted, e.g. `src/main/java/com/ve472/my_program_name`
3. Update `pom.xml`:
    - Update `groupID`: e.g. `<groupId>com.ve472.my_program_name</groupId>`
    - Update `artifactId`: e.g. `<artifactId>my_project_name</artifactId>`
    - Update `mainClass`: e.g. `<mainClass>com.ve472.my_program_name.Main</mainClass>`
    - Add your dependency and plugin:
      - Search in [MVN Repository](https://mvnrepository.com)
      - e.g.
        ```xml
        <dependency>
            <groupId>org.apache.hadoop</groupId>
            <artifactId>hadoop-common</artifactId>
            <version>3.3.3</version>
        </dependency>
        ```

4. Update `makefile`: e.g. `java -jar target/my_program_name-1.0-SNAPSHOT.jar`
