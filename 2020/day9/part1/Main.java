package org.example;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {

        final List<String> lines = readLines("input");
        final List<Long> numbers = new LinkedList<>();
        final int preambleLen = 25;
        for (int i = 0; i < preambleLen; i++) {
            numbers.add(Long.parseLong(lines.get(i)));
        }

        for (int i = preambleLen; i < lines.size(); i++) {
            final long newNumber = Long.parseLong(lines.get(i));
            if (twoElemsSumToTheGivenNumber(numbers, newNumber)) {
                numbers.remove(0);
                numbers.add(newNumber);
            } else {
                System.out.println(newNumber);    // 41682220
                break;
            }
        }
    }

    private static boolean twoElemsSumToTheGivenNumber(final List<Long> numbers, final long newNumber) {

        for (int i=0; i<numbers.size(); i++) {
            if (numbers.contains(newNumber - numbers.get(i))) {
                return true;
            }
        }
        return false;
    }

    /**
     * Reads and returns all the lines of the given file name in the parent directory.
     */
    private static List<String> readLines(final String fileName) throws IOException {

        final Path path = Paths.get(System.getProperty("user.dir")).getParent().resolve(fileName);
        return Files.readAllLines(path);
    }

}
