import os

#====================INPUT====================================================================
file_extension = ".001"
param_1 = 'LotID'
param_1_val = ''
param_2 = 'StepID'
param_2_val = ''
param_3 = 'WaferID'
param_3_val = ''


# ###############################################################################################
for root, dirs, files in os.walk("./"):
    for file in files:
        if file.endswith(file_extension):
            # print(file)     # print the file name with extension

            # open file & read required parameters
            with open(file, 'r') as fp:
                lines = fp.read().splitlines()
                for l in lines:
                    if param_1 in l or param_2 in l or param_3 in l:
                        print(l)

                        # TODO: extract withing quotes


            # Output: Filename
            output_filename = param_1_val + '_' + param_2_val + '_WF' + param_3_val
            print(output_filename)



