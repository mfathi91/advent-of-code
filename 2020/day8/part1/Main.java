package com.github.mfathi91;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class Main {

    private static int accumulator = 0;
    private static Set<Integer> executedInstructions = new HashSet<>();

    public static void main(String[] args) throws IOException {

        final List<String> lines = readLines("input");
        execute(lines, 0);
        System.out.println(accumulator);    // 1179
    }

    /**
     * Reads and returns all the lines of the given file name in the parent directory.
     */
    private static List<String> readLines(final String fileName) throws IOException {

        final Path path = Paths.get(System.getProperty("user.dir")).getParent().resolve(fileName);
        return Files.readAllLines(path);
    }

    /**
     * Executes the instruction in the given lines, and modifies the status of accumulator 
     * and executedInstructions.
     *
     * @lines the lines which contain all the instructions
     * @instruction the index of the instruction to be executed
     */
    private static void execute(final List<String> lines, final int instruction) {

        if (executedInstructions.contains(instruction)) {
            return;
        }
        executedInstructions.add(instruction);

        final String[] lineSplit = lines.get(instruction).split(" ");
        final String command = lineSplit[0];
        final int val = Integer.valueOf(lineSplit[1]);
        if (command.equals("nop")) {
            execute(lines, instruction+1);
        } else if (command.equals("acc")) {
            accumulator += val;
            execute(lines, instruction+1);
        } else if (command.equals("jmp")) {
            execute(lines, instruction+val);
        }
    }
}
