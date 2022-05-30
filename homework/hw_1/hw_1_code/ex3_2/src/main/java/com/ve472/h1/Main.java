package com.ve472.h1;

public class Main {
    public static void main(String[] args) {
        // get instance
        Tesla car = new Tesla();
        Tesla sportsCar = new Roadster();
        BMW SUV = new X7();

        // call methods
        car.demo();
        sportsCar.demo();
        SUV.demo();
    }
}

abstract class Car {
    abstract void demo();
}

class Tesla extends Car {
    @Override
    void demo() {
        System.out.println("Tesla");
    }
}

class Roadster extends Tesla {
    @Override
    void demo() {
        System.out.println("Roadster");
    }
}

class BMW extends Car {
    @Override
    void demo() {
        System.out.println("BMW");
    }
}

class X7 extends BMW {
    @Override
    void demo() {
        System.out.println("X7");
    }
}
