"""
Evaluation script.

Run:
    python eval.py file_ground_truth file_predictions

Where:
    - file_ground_truth is a csv file with a ground truth
    - file_predictions is a csv file with the predictions

The files should contain a header and have the following format:
Id,Target
1,<=50K
2,<=50K
3,<=50K
4,<=50K
5,<=50K
6,>50K
7,<=50K
8,>50K
etc.
where Id is the line number and Target is the prediction (<=50K or >50K).

@author: Krisztian Balog
"""

from __future__ import division

import sys
import csv


def load_file(filename):
    """Load a csv file into a dictionary."""
    data = {}
    with open(filename, 'rb') as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=',')
        for row in csvreader:
            if row['Target'] not in ["<=50K", ">50K"]:
                    print "Error: Unrecognized or missing class label '" + row['Target'] + "' in file '" + filename + "'"
                    return -1

            data[row['Id']] = row['Target']
    return data


def eval(file_gt, file_predictions):
    """Perform evaluation."""

    # Load ground truth file and predictions file
    data_gt = load_file(file_gt)
    data_pred = load_file(file_predictions)

    correct = 0
    incorrect = 0
    total = len(data_gt)

    if total == 0:
        print "Error: Empty ground truth file"
        return -1

    for id, label in data_gt.iteritems():
        if id not in data_pred:
            print "Error: Missing prediction for Id=" + id
            return -1

        if data_pred[id] == label:
            correct += 1
        else:
            incorrect += 1

    print "Accuracy:   ", str(correct / total)[:6]  # max 3 digits
    print "Error rate: ", str(incorrect / total)[:6]  # max 3 digits
    return 0


def print_usage():
    print "Usage: python eval.py file_ground_truth file_predictions"
    sys.exit()


def main(argv):
    if len(argv) < 2:
        print_usage()

    eval(argv[0], argv[1])

if __name__ == '__main__':
    main(sys.argv[1:])
