main: clean
	mvn package
	java -jar target/lab_1_code-1.0-SNAPSHOT.jar --hall config --query input/test.in

clean:
	rm -rf target/
	rm -f dependency-reduced-pom.xml

zip:
	cd src/main/java && zip -r com.zip com && cd -
	mv src/main/java/com.zip .
