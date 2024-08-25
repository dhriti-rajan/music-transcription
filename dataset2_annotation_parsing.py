import os
import xml.etree.ElementTree as et

DATASET_PATH = "IDMT-SMT-Guitar_V2/dataset2/"

# For each file in annotation folder, extract the necessary information.
# - Fields for each event: onsetSec, pitch, offsetSec, excitationStyle,
#   expressionStyle, fretNumber, stringNumber, modulationFrequency,
#   modulationFrequencyRange

def generate_test_file(folder_path: str, filename: str):
    input_file = folder_path + "annotation/" + filename + ".xml"
    output_file = folder_path + "data/" + filename + ".txt"
    
    tree = et.parse(input_file)
    root = tree.getroot()
    out = open(output_file, 'w')
    out.write("pitch,onset_sec,offset_sec,fret_number,string_number,"
              "excitation_style,expression_style,modulation_frequency,"
              "modulation_frequency_range")
    
    for event in root.iter('event'):
        pitch = event.find('pitch').text
        onset_sec = event.find('onsetSec').text
        offset_sec = event.find('offsetSec').text
        fret_number = event.find('fretNumber').text
        string_number = event.find('stringNumber').text
        excitation_style = event.find('excitationStyle').text
        expression_style = event.find('expressionStyle').text
        modulation_frequency = event.find('modulationFrequency').text
        modulation_frequency_range = event.find('modulationFrequencyRange').text
        
        out.write(pitch + "," + onset_sec + "," + offset_sec + "," + 
                  fret_number + "," + string_number + "," + excitation_style + 
                  "," + expression_style + "," + modulation_frequency + "," +
                  modulation_frequency_range + "\n")
        
    out.close()
    
# Iterate through all folders within the dataset and create test files for each
# of them.
def generate_all_tests():
    # os.mkdir(DATASET_PATH + "data/")
    files = [x.split('.')[0] for x in os.listdir(DATASET_PATH + "annotation/")]
    for file in files:
        generate_test_file(DATASET_PATH + "/", file)
        
def main():
    generate_all_tests()

main()
