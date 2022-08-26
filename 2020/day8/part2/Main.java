package com.github.mfathi91;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class Main2 {

    private static int accumulator = 0;
    private static Set<Integer> executedInstructions = new HashSet<>();

    private static List<String> readLines(final String fileName) throws IOException {

        final Path path = Paths.get(System.getProperty("user.dir")).getParent().resolve(fileName);
        return Files.readAllLines(path);
    }

    private static List<Integer> getIndexesOfCommand(final List<String> lines, final String command) {

        final List<Integer> indexes = new ArrayList<>();
        for (int i = 0; i < lines.size(); i++) {
            if (lines.get(i).startsWith(command)) {
                indexes.add(i);
            }
        }
        return indexes;
    }

    private static void resetProgram() {

        accumulator = 0;
        executedInstructions.clear();
    }

    /**
     * Modifies the given lines from the given commandFrom to commandTo one by one, and then executes
     * the lines. If execution reaches to the end, it prints the accumulator value.
     *
     * @param lines the lines to be modified and executed
     * @param commandFrom the command that needs to be changed
     * @param commandTo the command that will be set as the new one
     * @return {@code true} if the execution reaches the end of modified instruction set
     */
    private static boolean executeWithModifiedInstructions(final List<String> lines, final String commandFrom, final String commandTo) {

        final List<Integer> nopIndexes = getIndexesOfCommand(lines, commandFrom);
        for (final int idx : nopIndexes) {
            final String oldLine = lines.get(idx);
            final String[] fields = oldLine.split(" ");
            final String newLine = String.format("%s %s", commandTo, fields[1]);
            lines.set(idx, newLine);
            resetProgram();
            if (execute(lines, 0)) {
                System.out.println(accumulator);
                return true;
            } else {
                lines.set(idx, oldLine);
            }
        }
        return false;
    }

    public static void main(String[] args) throws IOException {

        final List<String> lines = readLines("input");
        executeWithModifiedInstructions(lines, "nop", "jmp");
        executeWithModifiedInstructions(lines, "jmp", "nop");   // 1089
    }

    /**
     * Executes the given instruction and returns {@code true} if the given instruction
     * is the last instruction.
     *
     * @param lines the lines of the instruction set
     * @param instruction the index of the instruction to be executed
     * @return {@code true} if the given instruction is the last one (program finished)
     */
    private static boolean execute(final List<String> lines, final int instruction) {

        if (executedInstructions.contains(instruction)) {
            return false;
        }
        executedInstructions.add(instruction);

        final String[] lineSplit = lines.get(instruction).split(" ");
        final String command = lineSplit[0];
        final int val = Integer.valueOf(lineSplit[1]);
        if (command.equals("nop")) {
            return instruction == lines.size() - 1 || execute(lines, instruction + 1);
        } else if (command.equals("acc")) {
            accumulator += val;
            return instruction == lines.size() - 1 || execute(lines, instruction + 1);
        } else if (command.equals("jmp")) {
            return instruction == lines.size() - 1 || execute(lines, instruction + val);
        } else {
            throw new UnsupportedOperationException("Unknown command: " + command);
        }
    }
}

