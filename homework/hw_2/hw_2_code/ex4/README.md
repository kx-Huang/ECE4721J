# Homework 2: Ex.4

## 0. Install `Avro` related packages

My current latest version: `1.11.0`

### 1) Download Avro using `Maven`

1. Add dependency:

  ```xml
  <dependencies>
    <dependency>
    <!-- https://mvnrepository.com/artifact/org.apache.avro/avro-maven-plugin -->
    <groupId>org.apache.avro</groupId>
    <artifactId>avro</artifactId>
    <version>1.11.0</version>
    </dependency>
    <dependency>
      <groupId>org.xerial.snappy</groupId>
      <artifactId>snappy-java</artifactId>
      <version>1.1.2.1</version>
    </dependency>
    <dependency>
      <groupId>commons-codec</groupId>
      <artifactId>commons-codec</artifactId>
      <version>1.15</version>
    </dependency>
    <dependency>
      <groupId>org.slf4j</groupId>
      <artifactId>slf4j-log4j12</artifactId>
      <version>1.7.36</version>
    </dependency>
  </dependencies>
  ```

2. Add Avro Maven plugin (for `Java` code generation):

  ```xml
  <plugin>
    <groupId>org.apache.avro</groupId>
    <artifactId>avro-maven-plugin</artifactId>
    <version>1.11.0</version>
    <executions>
      <execution>
        <phase>generate-sources</phase>
        <goals>
          <goal>schema</goal>
        </goals>
      </execution>
    </executions>
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

- Compile: `$ java -jar target/avro-tools-1.11.0.jar compile schema json/schema.json src/main/java`
- Effect: auto-generated `AvroFile.java` by `Avro` in `src/main/java/avro/`

## 3. Compile and Run `Java` Source Code

- Compile: `$ mvn compile`
- Run: `$ java -jar target/ex4-1.0-SNAPSHOT.jar`
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

## 5. Run Clean/Build/Run/Diff Pipeline with `makefile`

- Run: `$ make`
