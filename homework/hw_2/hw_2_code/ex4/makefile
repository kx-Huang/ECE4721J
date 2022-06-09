.PHONY: clean

main: clean
	chmod +x script/generate.py
	./script/generate.py

	@echo [Success] Generate data done

	java -jar target/avro-tools-1.11.0.jar compile schema json/schema.json src/main/java

	mvn package

	@echo [Success] Build process done

	java -jar target/ex4-1.0-SNAPSHOT.jar

	@echo [Success] Run process done

	chmod +x script/diff.sh
	./script/diff.sh

	@echo [Success] Diff process done

clean:
	rm -rf data/
	rm -rf target/classes target/gen* target/maven* target/hw* target/original* target/test* target/*-SNAPSHOT.jar
	rm -f dependency-reduced-pom.xml
