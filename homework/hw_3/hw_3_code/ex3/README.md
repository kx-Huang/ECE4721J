# Homework 3: Ex.3

With Hadoop MapReduce, filter the studentID ends with a three using `Bloom Filter` in mapper and serialize the combined bloom filter into an Avro file in reducer

## 0. Install `Hadoop` and `Avro` related packages

My current latest version:
- `Apache Haddop`: `3.3.3`
- `Apache Avro`: `1.11.0`

### 1) Download Avro using `Maven`

1. Add dependency:

  ```xml
  <dependencies>
    <!-- https://mvnrepository.com/artifact/org.apache.hadoop/hadoop-common -->
    <dependency>
      <groupId>org.apache.hadoop</groupId>
      <artifactId>hadoop-common</artifactId>
      <version>3.3.3</version>
    </dependency>
    <!-- https://mvnrepository.com/artifact/org.apache.hadoop/hadoop-mapreduce-client-core -->
    <dependency>
      <groupId>org.apache.hadoop</groupId>
      <artifactId>hadoop-mapreduce-client-core</artifactId>
      <version>3.3.3</version>
    </dependency>
    <!-- https://mvnrepository.com/artifact/org.apache.avro/avro-maven-plugin -->
    <dependency>
      <groupId>org.apache.avro</groupId>
      <artifactId>avro</artifactId>
      <version>1.11.0</version>
    </dependency>
    <!-- https://mvnrepository.com/artifact/org.apache.avro/avro-mapred -->
    <dependency>
      <groupId>org.apache.avro</groupId>
      <artifactId>avro-mapred</artifactId>
      <version>1.11.0</version>
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

2. Put it into `ex3/target/` for future schema compilation

## 1. Put `large.avro` to local and HDFS folder

The `large.avro` can be found in `homework/hw_2/hw_2_code/ex4/data/large.avro`

- Put it into local folder `input/`: for `makefile`
- Put it into HDFS input folder for MapReduce task: e.g. `$ hdfs dfs -put input/large.avro /kexuan/h3e3/input`

## 2. Compile `json` Schema

- Compile: `$ java -jar target/avro-tools-1.11.0.jar compile schema json/schema.json src/main/java`
- Effect: auto-generated `AvroFile.java` by `Avro` in `src/main/java/avro/`

## 3. Compile `java` source code
- Compile: `$ mvn compile`

## 4. Submit Hadoop MapReduce task to cluster

- Remarks: clean HDFS output folder: e.g. `$ hdfs dfs -rm -r -f /kexuan/h3e3/output`
- Run: `$ hadoop jar target/ex3-1.0-SNAPSHOT.jar /kexuan/h3e3/input /kexuan/h3e3/output`
- Output: the generated `Avro` file `part-r-00000.avro` can be found in HDFS folder `/kexuan/h3e3/output/`

## 5. Run pipeline with `makefile`

- Run: `$ make`

## Reference

1. [Apache Avro™ 1.11.0 Hadoop MapReduce guide](https://avro.apache.org/docs/current/mr.html)

2. [Apache Hadoop® Bloom Filter](https://hadoop.apache.org/docs/r2.7.1/api/index.html?org/apache/hadoop/util/bloom/BloomFilter.html)