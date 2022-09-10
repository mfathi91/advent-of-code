package org.example;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.List;
import java.util.function.Function;
import java.util.function.IntFunction;

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

    private static boolean isBetween(final int num, final int lowerLimitInclusive, final int upperLimitExclusive) {

        return num >= lowerLimitInclusive && num < upperLimitExclusive;
    }

    private static boolean hasOccupiedSeatInDirection(final char[][] seats, final int row, final int column,
            final IntFunction<Integer> rowFunction, final IntFunction<Integer> columnFunction) {

        int tmpRow = row;
        int tmpColumn = column;
        while (true) {
            tmpRow = rowFunction.apply(tmpRow);
            tmpColumn = columnFunction.apply(tmpColumn);
            if (!isBetween(tmpRow, 0, seats.length) || !isBetween(tmpColumn, 0, seats[0].length) || seats[tmpRow][tmpColumn] == EMPTY_SEAT)
                return false;
            if (seats[tmpRow][tmpColumn] == OCCUPIED_SEAT) return true;
        }
    }

    private static int numOccupiedSeats(final char[][] seats, final int row, final int column) {

        int num = 0;
        num = hasOccupiedSeatInDirection(seats, row, column, r -> r - 1, c -> c - 1) ? num + 1 : num;
        num = hasOccupiedSeatInDirection(seats, row, column, r -> r - 1, c -> c) ? num + 1 : num;
        num = hasOccupiedSeatInDirection(seats, row, column, r -> r - 1, c -> c + 1) ? num + 1 : num;
        num = hasOccupiedSeatInDirection(seats, row, column, r -> r, c -> c + 1) ? num + 1 : num;
        num = hasOccupiedSeatInDirection(seats, row, column, r -> r + 1, c -> c + 1) ? num + 1 : num;
        num = hasOccupiedSeatInDirection(seats, row, column, r -> r + 1, c -> c) ? num + 1 : num;
        num = hasOccupiedSeatInDirection(seats, row, column, r -> r + 1, c -> c - 1) ? num + 1 : num;
        num = hasOccupiedSeatInDirection(seats, row, column, r -> r, c -> c - 1) ? num + 1 : num;
        return num;
    }

    private static char[][] nextSeats(final char[][] seats) {

        seatsChange = false;
        final char[][] nextSeats = new char[seats.length][seats.length];
        for (int row = 0; row < seats.length; row++) {
            for (int column = 0; column < seats[0].length; column++) {
                if (seats[row][column] == EMPTY_SEAT && numOccupiedSeats(seats, row, column) == 0) {
                    nextSeats[row][column] = OCCUPIED_SEAT;
                    seatsChange = true;
                } else if (seats[row][column] == OCCUPIED_SEAT && numOccupiedSeats(seats, row, column) >= 5) {
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
        printSeats(seats);
        System.out.println(numOccupied(seats));    // 2285
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
