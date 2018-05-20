"""
Author: M Maher
Date: 20171202

v3labelmaker.py
Python module containing functions to convert CSV-formatted plant-collection database entries into JSON records, and then put these records into Mustache-formatted HTML herbarium labels to print.

To execute: python v3labelmaker.py -i <filename of CSV file, without file extension>
then open .html file in browser; print

"""

#!/usr/bin/python

import sys, getopt
import csv
import json
import pystache
from herb_label import HerbLabel

def main(argv):
    """
    Gets command-line arguments; sets name of JSON output file.
    """
    frmat = 'pretty'
    input_file = ''
    output_file = ''
    try:
        opts, args = getopt.getopt(argv,"hi:",["inputfile="])
    except getopt.GetoptError:
        print('v3labelmaker.py -i <name of input CSV file (without \'.csv\')>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('v3labelmaker.py -i <name of input CSV file (without \'.csv\')>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            input_file = arg + '.csv'
    output_file = arg + '.json'
    read_csv(input_file, output_file, frmat)
    return output_file

def read_csv(file, json_file, frmat):
    """
    Reads a CSV file and calls write_json to write the data into a JSON file.
    """
    csv_rows = []
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        title = reader.fieldnames
        # need to remove invisible/weird chars like \ufeff from start of csv file before coverting to json
        # need to remove extra empty rows from csv file before writing json
        for row in reader:
            csv_rows.extend([{title[i]:row[title[i]] for i in range(len(title))}])
        dictionary = csv_rows[:]
        write_json(dictionary, json_file, frmat)

def write_json(data, json_file, frmat):
    """
    Writes a JSON file.
    """
    with open(json_file, "w") as f:
        if frmat == "pretty":
            f.write(json.dumps(data, sort_keys=False, indent=4, separators=(',', ': '),ensure_ascii=False))
            #encoding="utf-8",
        else:
            f.write(json.dumps(data))

def mustachify(json_file):
    """
    Converts a JSON file containing herbarium specimen records into a list of Mustache-templated HTML articles.
    """
    with open(json_file) as jf:
        # load the json data into a dictionary
        labellist = json.load(jf)
        labels = []
        for l in labellist:
            label = HerbLabel(l)
            labels.append(HerbLabel(l))
    return labels

def write_html(json_file, outfile):
    """
    Makes list of Mustache-templated HTML articles, then iterates over list to generate complete HTML code containing all of the articles.
    """
    count = 0
    labels = mustachify(json_file)
    renderer = pystache.Renderer()
    with open(outfile, 'w') as fh:
        fh.write("<!DOCTYPE html><html><head><link rel=\"stylesheet\" href=\"v3labelformat.css\"/></head><body>")
        fh.write("<div class=\"item-wrapper\">")
        for l in labels:
            count += 1
            labeltext = renderer.render(l)
            fh.write(labeltext)
            if count%6 == 0:
                fh.write("</div><div class=\"item-wrapper\">")
        fh.write("</div></body></html>")

if __name__ == "__main__":
   json_file = main(sys.argv[1:])
   html_file = (sys.argv[2]) + '.html'
   write_html(json_file, html_file)
