import math
import sys
import pyspark
from mrjob.protocol import RawValueProtocol
from mrjob.job import MRJob


class MRSparkBFS(MRJob):
    # automatically setup output temporary directory by system, # usually in /tmp/spa.<username>.*timestamp.*
    MAX_DIST = 9999
    INPUT_PROTOCOL = RawValueProtocol
    OUTPUT_PROTOCOL = RawValueProtocol

    def mapRead(self, line):
        line = line.strip()
        words = line.split('|')
        id = words[0]
        neigh = words[2].split(',')
        dist = int(words[1])

        return (id, (neigh, dist))

    def spark(self, inputPath, outputPath):
        sp = pyspark.SparkContext(appName='bfs spark')
        # specify input path
        lines = sp.textFile(inputPath)
        lines.collect()
        lines = lines.map(self.mapRead)

        for iteration in range(5):
            mapped = lines.flatMap(self.sparkMapper)
            lines = mapped.reduceByKey(self.sparkReducer)

        lines.saveAsTextFile(outputPath)
        # output is streamed towards stdout
        sp.stop()

    def sparkMapper(self, node):
        results = []
        id = node[0]
        data = node[1]
        neigh = data[0]
        dist = data[1]

        results.append((id, (neigh, dist)))
        return results

    def sparkReducer(self, left, right):
        dist = self.MAX_DIST
        if (len(left[0]) > 0):
            edges.extend(left[0])
        if (len(right[0]) > 0):
            edges.extend(right[0])

        dist1 = left[1]
        dist2 = right[1]
        edges = []
        if (dist1 < dist):
            dist = dist1
        if (dist2 < dist):
            dist = dist2

        return (edges, dist)


if __name__ == '__main__':
    MRSparkBFS.run()
