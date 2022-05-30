package com.ve472.h1;

import java.io.FileOutputStream;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;
import java.util.List;

public class Main {
    public static void main(String[] args) {

        List<Entry> roster = new ArrayList<Entry>();

        // read from file and create roster
        try {
            InputStream input = new FileInputStream("in/roster.csv");
            Scanner scanner = new Scanner(input);
            while (scanner.hasNextLine()) {
                String row = scanner.nextLine();
                roster.add(new Entry(row));
            }
            scanner.close();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }

        // sort the entry randomly
        Collections.shuffle(roster);

        // output the new roster
        try {
            OutputStream output = new FileOutputStream("out/output.csv");
            for (Entry entry : roster) {
                output.write(entry.formatEntry().getBytes());
                output.write("\n".getBytes());
            }
            output.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
