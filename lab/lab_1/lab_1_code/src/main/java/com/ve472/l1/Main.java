package com.ve472.l1;

import org.apache.commons.cli.*;

public class Main {
    public static void main(String[] args) {

        // command line options
        Options options = new Options();
        options.addOption("h", "help", false, "print this message");
        options.addOption(null, "hall", true, "path of the hall config directory");
        options.addOption(null, "query", true, "query of customer orders");

        // command line parser
        CommandLineParser parser = new DefaultParser();
        CommandLine cmd;
        try {
            cmd = parser.parse(options, args);
            // print the help message
            if (cmd.hasOption("h")) {
                HelpFormatter formatter = new HelpFormatter();
                formatter.printHelp("cinema", options, false);
            }
            // get the value of the hall config directory
            String hallPath = cmd.getOptionValue("hall");
            if (hallPath != null) {
                // TODO: parses the configuration files
            }
        } catch (ParseException e) {
            e.printStackTrace();
        }

    }
}
