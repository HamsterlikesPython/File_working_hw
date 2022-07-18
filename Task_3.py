files_list = ['1.txt', '2.txt', '3.txt']
files_dict = {}
sorted_files_dict = {}
def file_sort(files_list):
    for file_name in files_list:
        with open(file_name, 'r', encoding='utf-8') as file:
            list_str = file.readlines()
            list_str_strip = []
            for str_ in list_str:
                str_ = str_.strip()
                list_str_strip.append(str_)
            files_dict[file_name] = (len(list_str), list_str_strip)
    sorted_files_list = sorted(files_dict.values())
    #print(len(files_dict))
    for element in sorted_files_list:
        for key in files_dict:
            if element[0] == files_dict[key][0]:
                sorted_files_dict[key] = (files_dict[key][0], files_dict[key][1])
    #print(sorted_files_dict)
    return sorted_files_dict
file_sort(files_list)

def files_result(files_list):
    file_sort(files_list)
    for file_name in sorted_files_dict:
        with open('result_task-3.txt', 'a', encoding='utf-8') as result_file:
            result_file.write(f"{file_name}\n {sorted_files_dict[file_name][0]}\n {sorted_files_dict[file_name][1]}\n")
files_result(files_list)
