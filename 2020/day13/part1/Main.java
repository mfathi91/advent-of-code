package org.example;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

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
        final int timeStamp = Integer.parseInt(lines.get(0));
        final List<Integer> busses = Arrays.stream(lines.get(1).split(","))
                .filter(s -> !s.equals("x"))
                .map(Integer::parseInt).collect(Collectors.toList());

        for (int i=timeStamp; i<Integer.MAX_VALUE; i++) {
            for (int b : busses) {
                if (i%b == 0) {
                    System.out.println((i - timeStamp) * b);    // 6568
                    return;
                }
            }
        }
    }
}

