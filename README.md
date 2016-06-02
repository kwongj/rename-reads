# rename-reads
Creates symlinks to rename reads for either parsing to Nullarbor or for uploading to SRA/ENA

##Author

Jason Kwong (@kwongjc)

##Dependencies
* Python 2.7.x
* [Readfinder](https://github.com/kwongj/readfinder)

##Usage

```
$ rename-reads.py -h
usage: 
  rename-reads.py [OPTIONS] KEYFILE

Rename reads eg. for uploading to SRA

positional arguments:
  KEYFILE        tab-separated file with old names in column 1, new names in column 2

optional arguments:
  -h, --help     show this help message and exit
  --dir READDIR  directory to search for reads (not required for MDU reads)
  --version      show program's version number and exit
```

##Basic usage

1. To rename read files, the script requires a tab-separated text file with two columns for each isolate to be renamed (eg. rename.txt): 
    
    ```
    isolate1-old    isolate1-new
    isolate2-old    isolate2-new
    isolate3-old    isolate3-new
    ```  

2. Create a directory for the new read symlinks to be created, and enter that directory:
  ```
  $ mkdir reads_renamed
  $ cd reads_renamed
  ```

3. The script uses [*readfinder*](https://github.com/kwongj/readfinder) to recursively search the specified directory for reads and prints out the command line input required to generate the symlinks.
  ```
  $ rename-reads.py --dir path/to/reads rename.txt
  ln -s path/to/reads/isolate1-old/isolate1-old_R1.fastq.gz isolate1-new_R1.fastq.gz
  ln -s path/to/reads/isolate1-old/isolate1-old_R2.fastq.gz isolate1-new_R2.fastq.gz
  ln -s path/to/reads/isolate1-old/isolate2-old_R1.fastq.gz isolate2-new_R1.fastq.gz
  ln -s path/to/reads/isolate1-old/isolate2-old_R2.fastq.gz isolate2-new_R2.fastq.gz
  ln -s path/to/reads/isolate1-old/isolate3-old_R1.fastq.gz isolate3-new_R1.fastq.gz
  ln -s path/to/reads/isolate1-old/isolate3-old_R2.fastq.gz isolate3-new_R2.fastq.gz
  ```
  
3. To execute the command line, pipe the script to shell:
  ```
  $ rename-reads.py --dir path/to/reads rename.txt | sh
  ```

4. There should now be a bunch of symlinks to the original reads with the required new names in the folder `reads_renamed`.
5. (Optional) If you want to put the read symlinks for each isolate into a separate subfolder for each isolate, run the accompanying script `run-put_into_folders.sh`:  

  ```
  $ run-put_into_folders.sh -h
  Name:
    run-put_into_folders
  Author:
    Jason Kwong <j.kwong1@student.unimelb.edu.au>
  Description:
    Puts read files into folders
  Usage:
    run-put_into_folders.sh <readsA_R1.fastq.gz> <readsA_R2.fastq.gz ... <readsN_R2.fastq.gz>
  Parameters:
    <reads.fastq.gz>	Reads to place into folders. Should be renamed with underscore after unique desired name
  Options:
    -h             Show this help
  ```
  Check desired output:
  ```
  $ run-put_into_folders.sh *.fastq.gz
  ```
  Pipe to shell to execute:
  ```
  $ run-put_into_folders.sh *.fastq.gz | sh
  ```

##Bugs

Please submit via the [GitHub issues page](https://github.com/kwongj/rename-reads/issues).  

##Software Licence

[GPLv3](https://github.com/kwongj/rename-reads/blob/master/LICENSE)
