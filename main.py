import csv
import os


FILENAME = ['referensi_data.csv', 'data_yg_divalidasi.csv']

def read_data(filename):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    with open('{}/{}'.format(base_dir, filename)) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        data = {}
        for row in csv_reader:
            data[row[1]] = row[0]
            if line_count == 0:
                print 'Column names are {}'.format(row)
                line_count += 1
            else:
                line_count += 1
        print 'Processed {} lines.'.format(line_count)
        return data

def write_data_to_csv(data):
    print "Your data inserted to new file"
    with open('result.csv', 'w') as f:
        for key in data.keys():
            f.write('"{}",{}\n'.format(data[key],key))
    print "done :)"

def generate_unique_data(ref_data, data_to_be_validated):
    #Remove same data on ref_data and data_validated
    for k, v in ref_data.items():
        if k in data_to_be_validated:
            data_to_be_validated.pop(k)
    return data_to_be_validated

def check_data_already_unique(ref_data, data_to_be_validated):
    #check if data_to_be_validated already unique
    for k in ref_data.keys():
        try:
            if data_to_be_validated[k]:
                print "Data not unique"
                return False
        except:
            pass
    print "Data already unique"
    return True

def main():
    #FILENAME[0] => refrence data
    #FILENAME[1] => data to be validated
    ref_data = read_data(FILENAME[0])
    data_to_be_validated = read_data(FILENAME[1])
    print "Data reference without duplicate are {} lines".format(len(ref_data))

    unique_data = generate_unique_data(ref_data, data_to_be_validated)
    data_already_unique = check_data_already_unique(ref_data, unique_data)

    if data_already_unique:
        write_data_to_csv(unique_data)

main()