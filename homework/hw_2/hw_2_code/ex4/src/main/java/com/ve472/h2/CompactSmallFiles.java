package com.ve472.h2;

import avro.AvroFile;

import org.apache.avro.Schema;
import org.apache.avro.file.CodecFactory;
import org.apache.avro.file.DataFileWriter;
import org.apache.avro.io.DatumWriter;
import org.apache.avro.specific.SpecificDatumWriter;
import org.apache.commons.codec.digest.DigestUtils;

import java.io.File;
import java.nio.ByteBuffer;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Objects;
import java.util.Scanner;

public class CompactSmallFiles {

    // array list of files to be compacted
    private final ArrayList<File> fileList = new ArrayList<>();

    // add files under dir to fileList
    private void getFileList(String dir) {
        File file = new File(dir);
        if (file.isDirectory())
            fileList.addAll(Arrays.asList(Objects.requireNonNull(file.listFiles())));
    }

    // compact to avro file
    public void compact(String schemaPath, String srcPath, String destPath) throws NullPointerException {

        // get file list
        getFileList(srcPath);

        try {

            // get schema from json
            Schema schema = new Schema.Parser().parse(new File(schemaPath));

            // create avro file writer
            DatumWriter<AvroFile> datumWriter = new SpecificDatumWriter<>(AvroFile.class);
            DataFileWriter<AvroFile> dataFileWriter = new DataFileWriter<>(datumWriter);

            // enable Snappy compression
            dataFileWriter.setCodec(CodecFactory.snappyCodec());
            dataFileWriter.create(schema, new File(destPath));

            // convert each csv file to byte stream
            for (File file : fileList) {

                // cascade each line using StingBuilder
                StringBuilder buffer = new StringBuilder();
                Scanner scanner = new Scanner(file);
                while (scanner.hasNextLine()) buffer.append(scanner.nextLine()).append("\n");
                scanner.close();

                // Convert StringBuilder to string
                String string = buffer.toString();
                // Convert string to byte array
                byte[] stringByte = string.getBytes();
                // Convert a byte array into a buffer.
                ByteBuffer byteBuffer = ByteBuffer.wrap(stringByte);

                // calculate SHA-1 checksum
                String sha = DigestUtils.sha1Hex(string);

                // create new Avro file with filename and checksum
                AvroFile avroFile = AvroFile.newBuilder()
                                            .setFilename(file.getName())
                                            .setFilecontent(byteBuffer)
                                            .setChecksum(sha)
                                            .build();

                // append Avro file using Avro data file writer
                dataFileWriter.append(avroFile);
            }
            // close avro file writer
            dataFileWriter.close();

        } catch (Exception e) {
            e.printStackTrace();
            System.exit(-1);
        }
    }
}
