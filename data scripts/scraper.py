import pyexcel as px
import openpyxl as ox
import pickle
CASE_AMOUNT = 5
SUB_FOLDER_FILE_AMOUNT = 5
ENERGY_CELL = 'C17'
GEOMETRY_CELL = 'Z1'
TOP_FILE_PATH_NAME = 'ML_Model_Training_Data'


def get_geomtry_vector_array():

    final_arr_trainingX = []
    final_arr_trainingY = []
    for i in range(CASE_AMOUNT):
        temp_energy_list = []
        for j in range(SUB_FOLDER_FILE_AMOUNT):
            file_path = 'BuildingSimulation' + \
                str(i+1) + '\\UseCase' + \
                str(j) + 'tbl.csv'
            curr_sheet = px.get_sheet(
                file_name=TOP_FILE_PATH_NAME + '\\'+file_path)
            if(j+1 == 1):
                x = curr_sheet[GEOMETRY_CELL].split(", ")
                if x[1] == '0':
                    x[0] = '0'
                elif x[0] == '0':
                    x[0] = '0.33'
                elif x[0] == '1':
                    x[0] = '0.66'
                elif x[0] == '2':
                    x[0] == '0.99'
                else:
                    raise ValueError('Window size value not between 0,2')
                for m in range(len(x)):
                    x[m] = float(x[m])
                final_arr_trainingX.append(x)
            temp_energy_list.append(float(curr_sheet[ENERGY_CELL]))
        final_arr_trainingY.append(temp_energy_list)
    print(final_arr_trainingX)
    print(final_arr_trainingY)
    pickle.dump(final_arr_trainingX, open("trainingX.p", "wb"))
    pickle.dump(final_arr_trainingY, open("trainingY.p", "wb"))


get_geomtry_vector_array()
