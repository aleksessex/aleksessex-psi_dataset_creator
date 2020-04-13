# PSI Dataset Creator

A basic command-line tool for generating synthetic datasets for use in private set intersection (PSI) applications and testing. Records are randomized web-safe ASCII strings--online record per line.

## Installation
Run `setup.sh` to install via `pip`

## Example usage

```
psi_dataset_creator --sender-size 10000 --receiver-size 100 --num-common 10 --record-length 64
```

Creates a dataset where where the Sender's set contains 10,000 records, the Receiver's set contains 100 records, the two sets contain 10 records in common, and each record contains 64 bytes.


## Command-line arugments

```
$ psi_dataset_creator -h

```
Outputs:

```
usage: psi_dataset_creator [-h] [--sender-size SENDER_SIZE] [--receiver-size RECEIVER_SIZE] [--num-common NUM_COMMON] [--record-length RECORD_LENGTH]
                           [--output-path OUTPUT_PATH]

A tool to generate synthetic datasets for PSI matching

optional arguments:
  -h, --help            show this help message and exit
  --sender-size SENDER_SIZE
                        Number of records in Sender's dataset
  --receiver-size RECEIVER_SIZE
                        Number of records in Receiver's dataset
  --num-common NUM_COMMON
                        Number of elements to share in common
  --record-length RECORD_LENGTH
                        Length of synthetic data element in characters
  --output-path OUTPUT_PATH
                        Optional output path
```
