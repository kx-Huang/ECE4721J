main: clean
	mvn package
	hdfs dfs -rm -r -f /kexuan/h3e1/input
	hdfs dfs -rm -r -f /kexuan/h3e1/output
	hdfs dfs -put input/grades_100.csv /kexuan/h3e1/input
	hadoop jar target/ex1-1.0-SNAPSHOT.jar /kexuan/h3e1/input /kexuan/h3e1/output
	hdfs dfs -get /kexuan/h3e1/output/part-r-00000
	mkdir -p output/
	mv part-r-00000 output/

clean:
	rm -rf target/
	rm -f dependency-reduced-pom.xml
