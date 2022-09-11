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
        final Ferry ferry = new Ferry();
        for (final String line: lines) {
            final Action action = Action.valueOf(String.valueOf(line.charAt(0)));
            final int val = Integer.parseInt(line.substring(1));
            ferry.move(action, val);
        }
        System.out.println(Math.abs(ferry.verticalLocation) + Math.abs(ferry.horizontalLocation));    // 845
    }

    static class Ferry {

        private int degree = 0;
        int horizontalLocation = 0;
        int verticalLocation = 0;


        void move(final Action action, final int val) {

            if (action == Action.R) {
                degree -= val;
                if (degree < 0) degree = degree == -90 ? 270 : (degree == -180 ? 180 : 90);
            } else if (action == Action.L) {
                degree += val;
                if (degree >= 360) degree = degree - 360;
            } else if (action == Action.F) {
                if (degree == 0) horizontalLocation += val;
                else if (degree == 90) verticalLocation += val;
                else if (degree == 180) horizontalLocation -= val;
                else if (degree == 270) verticalLocation -= val;
            }else if (action == Action.N) {
                verticalLocation += val;
            } else if (action == Action.S) {
                verticalLocation -= val;
            } else if (action == Action.E) {
                horizontalLocation += val;
            } else if (action == Action.W) {
                horizontalLocation -= val;
            }

            if (degree < 0 || degree > 360) {
                throw new IllegalStateException(String.format("Degree is invalid: %d. Action %s, val %d", degree, action, val));
            }
        }
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

