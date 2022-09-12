package org.example;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.List;

public class Main {

    /**
     * Reads and returns all the lines of the given file name in the parent directory.
     */
    private static List<String> readLines(final String fileName) throws IOException {

        final Path path = Paths.get(System.getProperty("user.dir")).getParent().resolve(fileName);
        return Files.readAllLines(path);
    }

    public static void main(String[] args) throws IOException {

        List<String> lines = readLines("input");
        final Ship ship = new Ship();
        for (final String line : lines) {
            final Action action = Action.valueOf(String.valueOf(line.charAt(0)));
            final int val = Integer.parseInt(line.substring(1));
            ship.move(action, val);
        }
        System.out.println(Math.abs(ship.y) + Math.abs(ship.x));    // 27016
    }

    static class Ship {

        final Waypoint waypoint = new Waypoint();
        int x = 0;
        int y = 0;


        void move(final Action action, final int val) {

            if (action == Action.R) {
                if (val == 90) {
                    int tmp = waypoint.x;
                    waypoint.x = waypoint.y;
                    waypoint.y = -tmp;
                } else if (val == 180) {
                    waypoint.x = -waypoint.x;
                    waypoint.y = -waypoint.y;
                } else if (val == 270) {
                    int tmp = waypoint.x;
                    waypoint.x = -waypoint.y;
                    waypoint.y = tmp;
                } else {
                    throw new UnsupportedOperationException();
                }
            } else if (action == Action.L) {
                if (val == 90) {
                    int tmp = waypoint.x;
                    waypoint.x = -waypoint.y;
                    waypoint.y = tmp;
                } else if (val == 180) {
                    waypoint.x = -waypoint.x;
                    waypoint.y = -waypoint.y;
                } else if (val == 270) {
                    int tmp = waypoint.x;
                    waypoint.x = waypoint.y;
                    waypoint.y = -tmp;
                } else {
                    throw new UnsupportedOperationException();
                }
            } else if (action == Action.F) {
                x += waypoint.x * val;
                y += waypoint.y * val;
            } else if (action == Action.N) {
                waypoint.y += val;
            } else if (action == Action.S) {
                waypoint.y -= val;
            } else if (action == Action.E) {
                waypoint.x += val;
            } else if (action == Action.W) {
                waypoint.x -= val;
            }

            if (waypoint.degree < 0 || waypoint.degree > 360) {
                throw new IllegalStateException(String.format("Degree is invalid: %d. Action %s, val %d", waypoint.degree, action, val));
            }
        }

        @Override
        public String toString() {
            return String.format("Ship: (%d, %d), waypoint: (%d, %d)", x, y, waypoint.x, waypoint.y);
        }
    }

    static class Waypoint {

        int degree = 0;
        int x = 10;
        int y = 1;
    }

    enum Action {

        N,
        S,
        E,
        W,
        L,
        R,
        F
    }
}

