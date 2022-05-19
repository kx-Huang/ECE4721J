package com.ve472.l1;

import org.apache.commons.cli.*;

public class Main {
    private static CommandLine cmd;
    private static final Options options = new Options();
    private static HelpFormatter formatter = new HelpFormatter();

    public static void main(String[] args) {
        handleCommandLineInput(args);

        // print the help message
        if (cmd.hasOption("help")) {
            formatter.printHelp("cinema", options, false);
            return;
        }

        // get command line input
        String cinemaConfigDir = cmd.getOptionValue("hall");
        String inputQueryFile = cmd.getOptionValue("query");
        new Cinema(cinemaConfigDir, inputQueryFile);
    }

    private static void handleCommandLineInput(String[] args) {
        // command line options
        options.addOption(Option.builder("h")
                            .longOpt("help")
                            .desc("print this message")
                            .build()
                         );
        options.addOption(Option.builder()
                            .longOpt("hall")
                            .required()
                            .hasArg()
                            .argName("arg")
                            .desc("path of the hall config directory")
                            .build()
                         );
        options.addOption(Option.builder()
                            .longOpt("query")
                            .required()
                            .hasArg()
                            .argName("arg")
                            .desc("query of customer orders")
                            .build()
                         );

        // parse command line input
        CommandLineParser parser = new DefaultParser();
        try {
            cmd = parser.parse(options, args);
        } catch (ParseException e) {
            formatter.printHelp("cinema", options, false);
            System.exit(0);
        }
    }
}
