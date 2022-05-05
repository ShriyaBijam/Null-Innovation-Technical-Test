import re

def extract(in_file):
    """
    Function to open and read a file and extract data from it using open function
    
    Parameters:
    argument1 (str): Location of the input file

    Returns:
    str: Returns the content of the given file
    """
    try:
        f = open(in_file, 'r')
        data = f.read()
        f.close()
        return data
    except Exception as e:
        print("File not found!!! Please check file name and try again", str(e))
        exit(0)

def transformation_1(data):
    """
    Function to apply transformation of capitalizing given data using inbuilt upper function
    
    Parameters:
    argument1 (str): String on which transformation is to be applied

    Returns:
    str: Resultant string with all letters capitalized
    """
    result = data.upper()
    return result

def transformation_2(data):
    """
    Function to apply transformation of calculating count of unique words in given string (case-insensitive).
    Uses regular expression to remove punctuation and dictionary to save counts
    
    Parameters:
    argument1 (str): String on which transformation is to be applied

    Returns:
    dict: Returns the dictionary containing counts of unique words
    """
    count = {}
    for word in re.compile('\w+').findall(data):
        if word.lower() in count:
            count[word.lower()]+=1
        else:
            count[word.lower()]=1
    return count

def load(data, out_file):
    """
    Function to write given data to given file using open and write functions
    
    Parameters:
    argument1 (str): Data to be written in the file
    argument2 (str): Location of the output file

    Returns:
    str: Returns the content of the given file
    """
    f = open(out_file, 'w')
    f.write(str(data))
    f.close()


def main():
    """
    Main Function to test ETL Process
    """
    in_file = input("Enter location of input file: ")
    transformation = input("Enter Transformation number: 1 or 2: ")
    out_file= input("Enter location of output file: ")
    
    data = extract(in_file)
    if  transformation=='1':
        result = transformation_1(data) 
    elif transformation=='2':
        result = transformation_2(data)
    else: 
        print("Invalid transformation")
        exit(0)
    load(result, out_file)


if __name__=="__main__":
    main()