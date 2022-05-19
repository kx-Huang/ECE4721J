## Functionality
Please refer to `l1.pdf`

## Dependency
- `maven`: the tool for building and managing Java-based project
- `org.apache.commons.cli`: the package used to parse command line arguments

## Compile and run with makefile
```sh
lab/lab_1/lab_1_code/ $ make
```

### Compile with `maven`
```sh
lab/lab_1/lab_1_code/ $ mvn package
```

### Run with different arguments
Change command line input in the end to run program, e.g. `--help`
```sh
lab/lab_1/lab_1_code/ $ java -cp target/lab_1_code-1.0-SNAPSHOT.jar:target/commons-cli-1.5.0.jar com.ve472.l1.Main --help
```
