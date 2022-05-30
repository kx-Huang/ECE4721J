package com.ve472.h1;

public class Entry {
    public String name, firstName, email;

    public Entry(String row) {
        String[] info = row.split(",");
        firstName = info[0];
        name = info[1];
        email = info[2];
    }

    public String formatEntry() {
        return name + "," + firstName + "," + email;
    }
}
