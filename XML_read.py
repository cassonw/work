import xml.etree.ElementTree as ET
import os
import sys

def getSubDirs(path = os.path.join(os.getcwd(), "XML Files")):
    """This method returns a list of the directories within the specified directory.  Defaults to the current working directory."""
    paths= []
    for item in os.listdir(path): 
        if os.path.isdir(os.path.join(path, item)):
            paths.append(os.path.join(path, item))
    return paths

def getXMLPaths(path):
    """This method returns a list of paths for each xml file found in the provided directory."""
    xml_paths = []
    for item in os.listdir(path):
        if item[-4:] == ".xml":
           xml_paths.append(os.path.join(path, item))
    return xml_paths

def getXMLPathsFromPathList(paths):
    """This method takes a list of paths and returns a list of paths to each XML file found in each path in the given list."""
    xml_paths = []
    for path in paths:
        xml_paths.extend(getXMLPaths(path))
    return xml_paths

def createTree(path):
    """This method takes a path to am XML file and returns an ElementTree."""
    return ET.parse(path)
def main():
    packages = getSubDirs()
    xml_paths = getXMLPathsFromPathList(packages)
    trees = []
    for path in xml_paths:
        trees.append(createTree(path))
    for tree in trees:
        print tree.getroot()

if __name__ == "__main__":
    main()
