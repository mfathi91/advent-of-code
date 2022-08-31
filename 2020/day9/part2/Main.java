package org.example;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.Collections;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;

public class Main {

    public static void main(String[] args) throws IOException {

        final List<String> lines = readLines("input");
        final List<Long> numbers = lines.stream()
                .map(Long::parseLong)
                .collect(Collectors.toList());
        final int target = 41682220;

        Set<Long> longestStreak = new HashSet<>();
        int sum = 0;
        int leftIdx = 0;
        for (int rightIdx = 0; rightIdx < numbers.size(); rightIdx++) {
            sum += numbers.get(rightIdx);
            while (sum > target) {
                sum -= numbers.get(leftIdx);
                leftIdx++;
            }
            if (sum == target) {
                if (rightIdx - leftIdx + 1 > longestStreak.size()) {
                    longestStreak.clear();
                    for (int i = leftIdx; i <= rightIdx; i++) {
                        longestStreak.add(numbers.get(i));
                    }
                }
                leftIdx++;
                sum = 0;
            }
        }

        System.out.println(Collections.max(longestStreak) + Collections.min(longestStreak));  // 5388976
    }

    /**
     * Reads and returns all the lines of the given file name in the parent directory.
     */
    private static List<String> readLines(final String fileName) throws IOException {

        final Path path = Paths.get(System.getProperty("user.dir")).getParent().resolve(fileName);
        return Files.readAllLines(path);
    }

}
