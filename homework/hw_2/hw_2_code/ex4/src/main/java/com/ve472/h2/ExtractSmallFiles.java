import avro.AvroFile;
import org.apache.avro.file.DataFileReader;
import org.apache.avro.io.DatumReader;
import org.apache.avro.specific.SpecificDatumReader;
import org.apache.commons.codec.digest.DigestUtils;

import java.io.File;
import java.io.FileWriter;
import java.nio.ByteBuffer;
import java.nio.CharBuffer;
import java.nio.charset.Charset;
import java.nio.charset.CharsetDecoder;
import java.nio.charset.StandardCharsets;

public class ExtractSmallFiles {

    // declare ByteBuffer
    private String decodeByte(ByteBuffer byteBuffer) {
        String ret = "";
        try {
            Charset charSet = StandardCharsets.UTF_8;
            CharsetDecoder charsetDecoder = charSet.newDecoder();
            CharBuffer charBuffer = charsetDecoder.decode(byteBuffer);
            ret = charBuffer.toString();
        } catch (Exception e) {
            e.printStackTrace();
            System.exit(-1);
        }
        return ret;
    }

    public void extract(String avroPath, String destPath) {
        try {

            // Create destination folder if not exist
            File dir = new File(destPath);
            if (!dir.exists()) {
                dir.mkdir();
            }

            // Create avro file reader
            DatumReader<AvroFile> datumReader = new SpecificDatumReader<>(AvroFile.class);
            DataFileReader<AvroFile> dataFileReader = new DataFileReader<AvroFile>(new File(avroPath), datumReader);

            // Extract each file
            AvroFile data = null;
            while (dataFileReader.hasNext()) {
                // get data
                data = dataFileReader.next();
                String content = decodeByte(data.getFilecontent());

                // get file name
                String filename = data.getFilename().toString();

                // calculate and compare SHA-1 checksum
                String sha = DigestUtils.sha1Hex(content);
                if (!data.getChecksum().toString().equals(sha)) {
                    System.err.println("Checksum not match: " + filename);
                    System.exit(-1);
                }

                // write extract file to destination folder
                File file = new File(destPath + "/" + filename);
                FileWriter writer = new FileWriter(file);
                writer.write(content);
                writer.close();
            }
            dataFileReader.close();
        } catch (Exception e) {
            e.printStackTrace();
            System.exit(-1);
        }
    }
}
