import os
import xml.etree.ElementTree as et

DATASET_PATH = "IDMT-SMT-Guitar_V2/dataset1/"

# For each file in annotation folder, extract the necessary information
# - Fields for each event: pitch, onsetSec, offsetSec, fretNumber, stringNumber,
#   excitationStyle, expressionStyle.
# - We need to maintain the onset and offset times as separate fields because
#   in addition to needing to know how long the notes are, we need to know
#   which ones are played simultaneously to determine when we're listening to
#   a chord as opposed to a single melody line.

def generate_test_file(folder_path: str, filename: str):
    input_file = folder_path + "annotation/" + filename + ".xml"
    output_file = folder_path + "data/" + filename + ".txt"
    
    tree = et.parse(input_file)
    root = tree.getroot()
    out = open(output_file, 'w')
    out.write("pitch,onset_sec,offset_sec,fret_number,string_number,"
              "excitation_style,expression_style\n")
    
    for event in root.iter('event'):
        pitch = event.find('pitch').text
        onset_sec = event.find('onsetSec').text
        offset_sec = event.find('offsetSec').text
        fret_number = event.find('fretNumber').text
        string_number = event.find('stringNumber').text
        excitation_style = event.find('excitationStyle').text
        expression_style = event.find('expressionStyle').text
        
        out.write(pitch + "," + onset_sec + "," + offset_sec + "," + 
                  fret_number + "," + string_number + "," + excitation_style + 
                  "," + expression_style + "\n")
    
    out.close()
    

# Iterate through all folders within the dataset and create test files for each
# of them.
def generate_all_tests():
    folder_paths = [x[0] for x in os.walk(DATASET_PATH)]
    folders = set()
    
    # Get all of the folder names within the dataset
    for f in folder_paths:
        split_path = f.strip().split('/')
        
        if len(split_path) >= 3  and split_path[2] != "":
            folders.add(split_path[2])  
    
    for folder in folders:
        files = [x.split('.')[0] for x in os.listdir(DATASET_PATH + folder +
                                                      "/annotation/")]
        for file in files:
            generate_test_file(DATASET_PATH + folder + "/", file)
        
def main():
    generate_all_tests()

main()
