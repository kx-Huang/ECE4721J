# ECE4721J Lab 1: `Java` Programming

Goals:
- Write and use packages in `Java`
- File input and output in `Java`
- Object-oriented programming in `Java`

## 0. `Java` Environment Setup

### `MacOS`

#### Download from `Oracle` website

Download `Oracle JDK` from `https://www.oracle.com/technetwork/java/javase/downloads/index.html` and run the installer.

#### Download with [`Homebrew` package manager](https://brew.sh)

```bash
$ brew install openjdk
```

### `Linux`

#### `Debian` and derived distribution (e.g. `Ubuntu`, `Linux Mint`)

```bash
$ apt-get update
$ apt-get install software-properties-common sh $ add-apt-repository <repository>
$ apt-get update
$ apt-get install oracle-java<X>-installer
```
- Replace `<repository>` with a third-party repository
- Replace `<X>` with the version number
- Third-party repositories can be found at `https://launchpad.net/`, e.g. `Java 8`: `ppa:webupd8team/java`, or `Java 12`: `ppa:linuxuprising/java`.

#### `Arch Linux` and derived distribution (e.g. `Manjaro`)

1. Install AUR helper tool `yay`

    ```bash
    $ sudo pacman -S git
    $ git clone https://aur.archlinux.org/yay.git
    $ cd yay
    $ makepkg -si
    ```

2. Display all available Oracle JDK and JRE versions and select whichever you want

   ```bash
   $ sudo pacman -Syyu
   $ yay jdk
   ```

## 1. `Java` Project Initialization

Please refer to [`template/java`](https://github.com/kx-Huang/ECE4721J/tree/master/template/java), which is a template for all `Java` programs in this course

- Project structure:

    ```log
    template/java
    ├── README.md
    ├── makefile
    ├── pom.xml
    └── src
        └── main
            └── java
                └── com
                    └── ve472
                        └── h0
                            └── Main.java

    6 directories, 4 files
    ```

- Content of `Main.java`:

    ```java
    package com.ve472.h0;

    public class Main {
        public static void main(String[] args) {
            // write your code here
            System.out.println("Hello World!");
        }
    }

    ```
