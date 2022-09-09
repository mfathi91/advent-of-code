package org.example;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.List;

public class Main {

    private static final char EMPTY_SEAT = 'L';
    private static final char OCCUPIED_SEAT = '#';
    private static boolean seatsChange = true;

    /**
     * Reads and returns all the lines of the given file name in the parent directory.
     */
    private static List<String> readLines(final String fileName) throws IOException {

        final Path path = Paths.get(System.getProperty("user.dir")).getParent().resolve(fileName);
        return Files.readAllLines(path);
    }

    private static char[][] toCharArray(final List<String> lines) {

        final char[][] array = new char[lines.size()][lines.size()];
        for (int row = 0; row < lines.size(); row++) {
            for (int column = 0; column < lines.get(row).length(); column++) {
                array[row][column] = lines.get(row).charAt(column);
            }
        }
        return array;
    }

    private static int numAdjacentOccupiedSeats(final char[][] seats, final int row, final int column) {

        int num = 0;

        /* Upper row */
        if (row - 1 >= 0) {
            if (column - 1 >= 0) num = seats[row - 1][column - 1] == OCCUPIED_SEAT ? num + 1 : num;
            if (column + 1 < seats.length) num = seats[row - 1][column + 1] == OCCUPIED_SEAT ? num + 1 : num;
            num = seats[row - 1][column] == OCCUPIED_SEAT ? num + 1 : num;
        }

        /* The same row */
        if (column - 1 >= 0) num = seats[row][column - 1] == OCCUPIED_SEAT ? num + 1 : num;
        if (column + 1 < seats.length) num = seats[row][column + 1] == OCCUPIED_SEAT ? num + 1 : num;

        /* Below row */
        if (row + 1 < seats.length) {
            if (row + 1 < seats.length && column - 1 >= 0) num = seats[row + 1][column - 1] == OCCUPIED_SEAT ? num + 1 : num;
            if (row + 1 < seats.length && column + 1 < seats.length)
                num = seats[row + 1][column + 1] == OCCUPIED_SEAT ? num + 1 : num;
            num = seats[row + 1][column] == OCCUPIED_SEAT ? num + 1 : num;
        }

        return num;
    }

    private static char[][] nextSeats(final char[][] seats) {

        seatsChange = false;
        final char[][] nextSeats = new char[seats.length][seats.length];
        for (int row = 0; row < seats.length; row++) {
            for (int column = 0; column < seats[0].length; column++) {
                if (seats[row][column] == EMPTY_SEAT && numAdjacentOccupiedSeats(seats, row, column) == 0) {
                    nextSeats[row][column] = OCCUPIED_SEAT;
                    seatsChange = true;
                } else if (seats[row][column] == OCCUPIED_SEAT && numAdjacentOccupiedSeats(seats, row, column) >= 4) {
                    nextSeats[row][column] = EMPTY_SEAT;
                    seatsChange = true;
                } else {
                    nextSeats[row][column] = seats[row][column];
                }
            }
        }
        return nextSeats;
    }

    private static int numOccupied(final char[][] seats) {

        int numOccupied = 0;
        for (int row = 0; row < seats.length; row++) {
            for (int column = 0; column < seats[0].length; column++) {
                if (seats[row][column] == OCCUPIED_SEAT) {
                    numOccupied++;
                }
            }
        }
        return numOccupied;
    }

    public static void main(String[] args) throws IOException {

        final List<String> lines = readLines("input");
        char[][] seats = toCharArray(lines);
        while (seatsChange) {
            seats = nextSeats(seats);
        }
        System.out.println(numOccupied(seats));    // 2483
    }

    private static void printSeats(final char[][] seats) {

        for (int row = 0; row < seats.length; row++) {
            for (int column = 0; column < seats[0].length; column++) {
                System.out.print(seats[row][column]);
            }
            System.out.println();
        }
        System.out.println("---------------------------");
    }
}
