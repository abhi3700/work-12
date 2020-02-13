import os   # for managing the file directory
import re   # for extracting text within quotes

#====================INPUT====================================================================
# dir_src = "I:\\github_repos\\work-12\\coding\\data"
dir_src = "./data/"
dir_des = "{deviceid_val}/{lotid_val}/{stepid_val}/YEDI1/"

file_ext = ".001"

lotid = 'LotID'
lotid_val = ''
lotid_lineno = 0

stepid = 'StepID'
stepid_val = ''

resultsid = 'ResultsID'
resultsid_val = ''
resultsid_lineno = 0

waferid = 'WaferID'
waferid_val = ''

deviceid = 'DeviceID'
deviceid_val = ''

output_filename = ''
#====================REPLACE function definition====================================================================
def replace_line(file_name, line_num_lotid, text_lotid, line_num_resultsid, text_resultsid):
    lines = open(file_name, 'r').readlines()
    lines[line_num_lotid] = text_lotid
    lines[line_num_resultsid] = text_resultsid
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()



# ###############################################################################################
for root, dirs, files in os.walk(dir_src):
    """Just use in case of DEBUG"""
    # print(root)
    # print(dirs)
    # print(files)
    """List comprehension for printing the message if there are no files with .001 file extension"""
    if len([x for x in files if file_ext in x]) > 0:
        for file in files:
            if file.endswith(file_ext):
                # file = dir_src + '/' + file     # append the directory to current file names, otherwise it will give the error: NoFileFound
                file = dir_src + file     # append the directory to current file names, otherwise it will give the error: NoFileFound
                # print(file)     # print the file name with extension
                # ------------------------------------------------------------------------------------
                """open file & read required parameters"""
                with open(file, 'r') as fp:
                    lines = fp.read().splitlines()
                    for l in lines:
                        if lotid in l:
                            lotid_lineno = lines.index(l)
                            lotid_val = re.findall('"([^"]*)"', l)[0]       # extract within quotes
                        if resultsid in l:
                            resultsid_lineno = lines.index(l)
                            resultsid_val = re.findall('"([^"]*)"', l)[0]       # extract within quotes
                        if stepid in l:
                            # stepid_lineno = lines.index(l)
                            stepid_val = re.findall('"([^"]*)"', l)[0]      # extract within quotes
                        if waferid in l:
                            # waferid_lineno = lines.index(l)
                            waferid_val = re.findall('"([^"]*)"', l)[0]     # extract within quotes
                        if deviceid in l:
                            deviceid_val = re.findall('"([^"]*)"', l)[0]    # extract within quotes

                # print(lotid_lineno, resultsid_lineno, stepid_lineno, waferid_lineno)      # e.g. --> 5 9 15
                # print(lotid_val, resultsid_val, stepid_val, waferid_val)       # e.g. --> F19310002.F1 POLY 01

                # ------------------------------------------------------------------------------------
                """Replace modified text in respective params"""
                replace_line(
                    file_name= file,
                    line_num_lotid= lotid_lineno,
                    text_lotid= lotid + ' \"' + lotid_val + stepid_val + '\"\n',
                    line_num_resultsid= resultsid_lineno,
                    text_resultsid= resultsid + ' \"' + resultsid_val + stepid_val + '\"\n',
                    )

                # ------------------------------------------------------------------------------------
                """ Change the Filename"""
                output_filename = lotid_val + '_' + stepid_val + '_WF' + waferid_val + '.001'
                # print(output_filename)              # e.g. --> F19310002.F1_POLY_WF01

                dir_des = dir_des.format(deviceid_val= deviceid_val,
                                                lotid_val= lotid_val,
                                                stepid_val= stepid_val,
                                                output_filename= output_filename
                                                )
                # ------------------------------------------------------------------------------------
                # """Check if the desired folder exists"""
                # # print(dir_des)
                if not os.path.exists(dir_des):     # if the desired path doesn't exist
                    os.makedirs(dir_des)

                # ------------------------------------------------------------------------------------
                """Rename & Move the files from source to destination folder"""
                try:
                    os.rename(file, dir_des + output_filename)
                except FileExistsError:
                    os.remove(file)     # delete the file when this exception is caught.
                    print('File already exists. Not to be moved. So, deleted the file')

    else:
        print("SORRY! There are no files found with extension -- .001 in the given directory")

