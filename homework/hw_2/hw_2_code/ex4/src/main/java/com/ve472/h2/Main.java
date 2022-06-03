public class Main {
    public static void main(String[] args) {
        String schema = "json/schema.json";
        String compactSrcDir = "data/small_generated";
        String largeDataDir = "data/large.avro";
        String extractDestDir = "data/small_extracted";

        CompactSmallFiles compactSmallFiles = new CompactSmallFiles();
        compactSmallFiles.compact(schema, compactSrcDir, largeDataDir);
        ExtractSmallFiles extractSmallFiles = new ExtractSmallFiles();
        extractSmallFiles.extract(largeDataDir, extractDestDir);
    }
}