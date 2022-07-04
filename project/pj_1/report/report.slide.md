---
title: Big Data Analysis on [Million Song Dataset (MSD)](http://millionsongdataset.com)
subtitle: "ECE4710: Methods and Tools for Big Data"
author:
- Yiding Chang
- Yifan Shen
- Kexuan Huang
- Qinhang Wu
toc: true
toc-title: Overview\newline\newline\newline\newline
date: \today
lang: en
header-includes:
- |
    ```{=latex}
    \setbeamersize{text margin left=8mm,text margin right=8mm}

    \titlegraphic{
        \includegraphics[width=3.05cm]{img/drill.png}
        \hspace{0.2mm}
        \raisebox{0.05\height}{
          \includegraphics[width=4.4cm]{img/hadoop.png}
        }
        \includegraphics[width=3.1cm]{img/spark.png}
    }

    \setbeamertemplate{headline}{
        \moveright -0.03in
        \hbox{
            \begin{beamercolorbox}[wd=.5\paperwidth,ht=2.25ex,dp=1ex,right]{section in head/foot}
                \usebeamerfont{section in head/foot}
                \insertsubsectionhead
                \hspace*{2ex}
            \end{beamercolorbox}
            \begin{beamercolorbox}[wd=.5\paperwidth,ht=2.25ex,dp=1ex,left]{subsection in head/foot}
                \usebeamerfont{subsection in head/foot}
                \hspace*{2ex}
                \insertsectionhead
            \end{beamercolorbox}
        }
        \vskip0pt
    }

    \setbeamertemplate{footline}{
        \moveright -0.03in
        \hbox{
            \begin{beamercolorbox}[wd=.2\paperwidth,ht=2.25ex,dp=1ex,center]{author in head/foot}
                \usebeamerfont{author in head/foot}
                Group 4
            \end{beamercolorbox}
            \begin{beamercolorbox}[wd=.6\paperwidth,ht=2.25ex,dp=1ex,center]{title in head/foot}
                \usebeamerfont{title in head/foot}
                \insertshorttitle
            \end{beamercolorbox}
            \begin{beamercolorbox}[wd=.2\paperwidth,ht=2.25ex,dp=1ex,center]{date in head/foot}
                \insertframenumber{} / \inserttotalframenumber
                \hspace*{1ex}
            \end{beamercolorbox}
        }
        \vskip0pt
    }

    \setbeamertemplate{section in toc}{
        \leftskip=.18\paperwidth
        %\inserttocsectionnumber
        \bullet\kern1.25ex\inserttocsection\par
    }

    \setbeamertemplate{frametitle}{
        \vspace{0.5cm}
        \hspace{-2mm}\textbf{\color{bg}{\insertframetitle}}
    }

    \setbeamertemplate{enumerate items}[default]
    \setbeamertemplate{itemize items}[circle]

    ```
---

# Milestone 0: HDF5 Data Pre-process

## Goals

1. Compact small `hdf5` files into larger one

2. Read `hdf5` file and extract the information

3. Convert `hdf5` to `Avro` with `Apache Avro`


## 0. Environment

- `Python`: 3.9.2

- Install `PyGreSQL` env
  ```bash
  $ sudo apt-get install libpq-dev
  ```

- Install `python` packages
  ```bash
  $ python3 -m pip install -r requirements.txt
  ```

- Remark: some syntax are modified to accommodate `Python 3`, for example,
  ```python
  print hdf5_path
  ```

## 1. Compact small `hdf5` files into larger one

Creates an aggregate file from all song `hdf5` files in a given directory

- Usage:
  ```bash
  $ python3 create_aggregate_file.py ←
    → <H5 DIR> <OUTPUT.h5>
  ```

- Input: a directory contains `hdf5` song files

- Output: an aggregate `hdf5` song file

- Remark: Remove the existing file having the same name as the output file before running the `Python` script
  ```bash
  $ rm -f <OUTPUT.h5>
  ```

## 2. Read `hdf5` files and extract the information

Quickly display all we know about a single/aggregate/summary `hdf5` song file

- Usage:
  ```bash
  $ python3 display_song.py [FLAGS] ←
    → <HDF5 file> <OPT: song idx> <OPT: getter>
  ```

- Input: a `hdf5` song file

- Output: specified field content

- Remark: `getter` arguments must correspond to getters in `hdf5_getters.py`. Please refer to this file:
  ```bash
  m0/schema/valid_field.log
  ```

## 3. Convert `hdf5` to `Avro` with `Apache Avro`

Convert a single/aggregate song file from `hdf5` to `Avro`

- Usage:
  ```bash
  $ hdf5_to_avro.py [-h] -s <SCHEMA> -i <HDF5> -o <AVRO>
  ```

- Input: an `Avro` schema file, a `hdf5` song file to be converted

- Output: an `Avro` song file

- Remark: field names in schema file must correspond to getters in `hdf5_getters.py`. A sanity check will be performed before conversion. Please refer to this file:
  ```bash
  m0/schema/valid_field.log
  ```

## 4. Run `hdf5` file pre-process pipeline

- Usage:
  ```bash
  $ chmod +x m0.sh
  $ ./m0.sh
  ```

## Reference

1. MSongsDB
   [`https://github.com/tbertinmahieux/MSongsDB`](https://github.com/tbertinmahieux/MSongsDB)

2. MSongsDB Field List
   [`http://millionsongdataset.com/pages/field-list/`](http://millionsongdataset.com/pages/field-list/)

3. Apache Avro Documentation
   [`https://avro.apache.org/docs/current/index.html`](https://avro.apache.org/docs/current/index.html)

# Milestone 1: Drill Database Query

# Milestone 2: Advanced Data Analysis
