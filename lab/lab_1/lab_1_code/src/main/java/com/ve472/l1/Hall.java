package com.ve472.l1;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.InputStream;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Hall {
    private String hallName;
    private String movieName;
    private List<List<Boolean>> seats = new ArrayList<>();
    private Integer rowCount = 0;
    private Integer colCount = 0;
    private float colCenterLine = 0;

    public Hall(String configFilePath) {
        initHallFromFile(configFilePath);
    }

    public String getHallName() {
        return hallName;
    }

    public String getMovieName() {
        return movieName;
    }

    public Integer getRowCount() {
        return rowCount;
    }

    public Integer getColCount() {
        return colCount;
    }

    private void initHallFromFile(String configFilePath) {
        try {
            InputStream hall = new FileInputStream(configFilePath);
            Scanner scanner = new Scanner(hall);

            // read the hall and movie name
            hallName = scanner.nextLine();
            movieName = scanner.nextLine();

            // read the hall seat
            while (scanner.hasNextLine()) {
                seats.add(new ArrayList<Boolean>());
                String rowString = scanner.nextLine();
                String[] rowArray = rowString.split(" ");
                for (String s : rowArray)
                    seats.get(rowCount).add(s.equals("1"));
                rowCount++;
            }

            // update hall parameters
            colCount = seats.isEmpty() ? 0 : seats.get(0).size();
            colCenterLine = (float) (colCount + 1) / 2;

            scanner.close();
        } catch (FileNotFoundException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }

    public Boolean bookTicket(String customerName, Integer ticketQuantity) {
        // not inialize seats or seats are not enough in a row
        if (seats.isEmpty() || ticketQuantity > colCount)
            return false;

        // possible choices of seat position (not optimized)
        List<int[]> seatsList = new ArrayList<>();
        for (int i = 0; i < rowCount; i++) {
            List<Boolean> rowStatus = seats.get(i);
            // check continuous seats in one row is avaiable
            for (int j = 0; j < colCount - ticketQuantity + 1; j++) {
                boolean seatsAvailable = true;
                // check each seat
                for (int k = 0; k < ticketQuantity; k++) {
                    if (rowStatus.get(j + k) == false) {
                        seatsAvailable = false;
                        break;
                    }
                }
                // save row and column into seatList if continuous seats are found
                if (seatsAvailable) {
                    int[] pos = new int[2];
                    pos[0] = i;
                    pos[1] = j;
                    seatsList.add(pos);
                }
            }
        }

        // find optimized seat position
        int bestChoice = -1;
        double minDistance = Double.MAX_VALUE;
        for (int i = 0; i < seatsList.size(); i++) {

            // calculate distance to central col of the last row
            int[] pos = seatsList.get(i);
            double rowDistance = rowCount - (pos[0] + 1);
            double colDistance = colCenterLine - (pos[1] + (float) (ticketQuantity + 1) / 2);
            double distance = Math.pow(rowDistance, 2) + Math.pow(colDistance, 2);

            // find smaller distance
            if (distance < minDistance) {
                bestChoice = i;
                minDistance = distance;
                continue;
            }
            // find same distance
            if (distance == minDistance) {
                // choose the row with the larger row number
                if (pos[0] > seatsList.get(bestChoice)[0]) {
                    bestChoice = i;
                    minDistance = distance;
                    continue;
                }
                // choose the centroid on the left if same distance in one row
                if (pos[0] == seatsList.get(bestChoice)[0] && pos[1] < seatsList.get(bestChoice)[1]) {
                    bestChoice = i;
                    minDistance = distance;
                    continue;
                }
            }
        }

        // no choice found
        if (bestChoice == -1)
            return false;

        // print best seats selected
        int[] bestPos = seatsList.get(bestChoice);
        String colPos = "";
        for (int i = 0; i < ticketQuantity; i++) {
            int col = bestPos[1] + i;
            // set seat to unavailable
            seats.get(bestPos[0]).set(col, false);
            colPos += "," + Integer.toString(col + 1);
        }
        System.out.println(
                customerName + "," + movieName + "," + hallName + "," + Integer.toString(bestPos[0] + 1) + colPos);
        return true;
    }
}
