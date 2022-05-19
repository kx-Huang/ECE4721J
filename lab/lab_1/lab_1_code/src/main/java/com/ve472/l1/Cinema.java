package com.ve472.l1;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.InputStream;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Scanner;

public class Cinema {
    private HashMap<String, Hall> halls = new HashMap<>();
    private HashMap<String, List<Hall>> movies = new HashMap<>();

    public Cinema(String configDirPath, String queryFilePath) {
        initCinemaFromDir(configDirPath);
        readQuery(queryFilePath);
    }

    private void initCinemaFromDir(String configDirPath) {
        File dir = new File(configDirPath);

        // check if path is not a directory
        if (!dir.isDirectory()) {
            System.out.println("Error: " + configDirPath + " is not a directory");
            System.exit(-1);
        }

        // Read the config files
        File[] configFiles = dir.listFiles();
        for (File configFile : configFiles) {
            // initialize a hall
            Hall hall = new Hall(configFile.getPath());
            // add hall to the halls of cinema
            halls.put(hall.getHallName(), hall);
            // add hall to the current movie if exists, or create a new movie as key
            List<Hall> hallListForCurrentMovie = movies.getOrDefault(hall.getMovieName(), new ArrayList<>());
            hallListForCurrentMovie.add(hall);
            hallListForCurrentMovie.sort(Comparator.comparing(o -> o.getHallName()));
            movies.put(hall.getMovieName(), hallListForCurrentMovie);
        }
    }

    private void readQuery(String queryFilePath) {
        try {
            InputStream query = new FileInputStream(queryFilePath);
            Scanner scanner = new Scanner(query);
            while (scanner.hasNextLine()) {
                // parse query
                String[] ticketDetails = scanner.nextLine().split(", ");
                String customerName = ticketDetails[0];
                String movieName = ticketDetails[1];
                Integer ticketQuantity = Integer.parseInt(ticketDetails[2]);

                // book the ticket
                Boolean bookSucceess = false;
                if (movies.containsKey(movieName)) {
                    List<Hall> hallListForCurrentMovie = movies.get(movieName);
                    // find the hall which can book the ticket
                    for (Hall hall : hallListForCurrentMovie) {
                        if (hall.bookTicket(customerName, ticketQuantity)) {
                            bookSucceess = true;
                            break;
                        }
                    }
                    // no seat available
                    if (bookSucceess == false)
                    System.out.println(customerName + "," + movieName);
                    continue;
                }
                // no movie matched
                System.out.println(customerName + "," + movieName);
            }
        } catch (FileNotFoundException e) {
            System.out.println("Error: " + e.getMessage());
            System.exit(-1);
        }
    }
}
