import json

def jsonFile2dict(jsonFilePath: str):
    
    # Open the JSON file in read mode
    with open(jsonFilePath, 'r') as json_file:
        # Load the JSON data into a dictionary
        data_dict = json.load(json_file)

    return data_dict


def dict2jsonFile(inputDict: dict, outputJsonFilePath: str):

    # Open the JSON file in write mode
    with open(outputJsonFilePath, 'w') as json_file:
        # Write the dictionary to the JSON file
        json.dump(inputDict, json_file)


def loadConfig(fileName='config.json'):
    return jsonFile2dict(fileName)