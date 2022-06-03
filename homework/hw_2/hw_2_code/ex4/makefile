.PHONY: clean

main:
	chmod +x script/generate.py
	./script/generate.py

	java -jar target/avro-tools-1.11.0.jar compile schema json/schema.json src/main/java/com/ve472/h2

	mvn package

	mvn -q exec:java -Dexec.mainClass="Main"

	chmod +x script/diff.sh
	./script/diff.sh

	@echo [Success] Build/run/diff process done

clean:
	rm -rf data/
	rm -rf target/classes target/gen* target/maven* target/hw* target/original* target/test*
	rm -f dependency-reduced-pom.xml
