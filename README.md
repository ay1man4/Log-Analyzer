# Log Analyzer

Log Analyzer is a python script to analyze logs of a news blog. It give answers of three questions using three methods:

1. What are the most popular three articles of all time?
1. Who are the most popular article authors of all time?
1. On which days did more than 1% of requests lead to errors?

## Install

Before using this script, you have to prepare news DB and required softwares to run the Log Analyzer. This illustration showing how to use VM environment using vagrant. Follow below steps to prepare the environment and DB:

- Install [vagrant](https://www.vagrantup.com/downloads.html) and [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
- Download and unzip the VM configuration [FSND-Virtual-Machine.zip](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip)
- Change terminal directory to vagrant directory inside unzipped directory
- Start the virtual Machine using `vagrant up`
- Once done run `vagrant ssh` to log into linux environment
- Download and unzip [news DB sql file](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) to vagrant folder which is shared between your OS and VM
- From VM run `psql -d news -f newsdata.sql` to load DB data

## Usage

In VM terminal run the Log Analyzer to see the output using python or python3:
`python3 analyzer.py`

## License

The content of this repository is licensed under a [Creative Commons Attribution License](http://creativecommons.org/licenses/by/3.0/us/)