# Homework 2: Ex.4

## 0. Install `Avro` related packages

My current latest version: `1.11.0`

### 1) Download Avro using `Maven`

1. Add dependency:

  ```xml
  <dependency>
    <groupId>org.apache.avro</groupId>
    <artifactId>avro</artifactId>
    <version>1.11.0</version>
  </dependency>
  ```

2. Add Avro Maven plugin (for performing code generation):

  ```xml
  <plugin>
    <groupId>org.apache.avro</groupId>
    <artifactId>avro-maven-plugin</artifactId>
    <version>1.10.2</version>
    <executions>
      <execution>
        <phase>generate-sources</phase>
        <goals>
          <goal>schema</goal>
        </goals>
        <configuration>
          <sourceDirectory>src/main/avro/</sourceDirectory>
          <outputDirectory>src/main/java/</outputDirectory>
        </configuration>
      </execution>
    </executions>
  </plugin>
  <plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-compiler-plugin</artifactId>
    <configuration>
      <source>1.8</source>
      <target>1.8</target>
    </configuration>
  </plugin>
  ```

3. Run `Maven` command to install packages:

  ```bash
  $ mvn package
  ```

### 2) Download Avro-tools `jar`

1. Download lastest version of avro-tools `jar`:
- Download current latest version: e.g. `avro-tools-1.11.0.jar`
- URL: https://dlcdn.apache.org/avro/stable/java/

2. Put it into `ex4/target/` for future schema compilation

## 1. Generate Small `csv` files with `generate.py`

- Run: `$ python3 generate.py`
- Input: None
- Specification:
  - DATA_NUMBER: raw data number (default: `1000`)
  - ENTRY_NUMBER: lines number in each `csv` file (default: `100`)
  - CSV_NUMBER: `csv` files number (default: `10`)
- Output: generate folder `data/small_generated/` with 10 csv files named `grades_#.csv`

## 2. Compile `json` Schema

- Compile: `$ java -jar target/avro-tools-1.11.0.jar compile schema json/schema.json src/main/java/com/ve472/h2`
- Effect: auto-generated `AvroFile.java` by `Avro` in `src/main/java/com/ve472/h2/avro/`

## 3. Compile and Run `Java` Source Code

- Compile: `$ mvn compile`
- Run: `$ mvn -q exec:java -Dexec.mainClass="Main"`
- Notes: All files are readed from or generated to folder `data/`
- Effect:
  1. Compact small files:
    - Input: 10 csv files `grades_#.csv` from `small_generated/`
    - Ouput: a single compacted file `large.avro`
  2. Extract small files:
    - Input: a single compacted file `large.avro`
    - Output: 10 csv files `grades_#.csv` to `small_extracted/`

## 4. `Diff` Extracted Files with Original Files

- Run: `$ ./script/diff.sh`
- Input:
  - 10 csv files `grades_#.csv` in `small_generated/`
  - 10 csv files `grades_#.csv` in `small_extracted/`
- Effect: No output if the extracted files and original files are the same.
