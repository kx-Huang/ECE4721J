.PHONY: clean

main: clean
	java -jar target/avro-tools-1.11.0.jar compile schema json/schema.json src/main/java
	mvn package
	hdfs dfs -rm -r -f /kexuan/h3e3/input
	hdfs dfs -rm -r -f /kexuan/h3e3/output
	hdfs dfs -put input/large.avro /kexuan/h3e3/input
	hadoop jar target/ex3-1.0-SNAPSHOT.jar /kexuan/h3e3/input /kexuan/h3e3/output
	hdfs dfs -get /kexuan/h3e3/output/part-r-00000.avro
	mkdir -p output/
	mv part-r-00000.avro output/

clean:
	rm -rf data/
	rm -rf target/classes target/gen* target/maven* target/hw* target/original* target/test* target/*-SNAPSHOT.jar
	rm -f dependency-reduced-pom.xml
