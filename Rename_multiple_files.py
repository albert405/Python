import os
File_list= os.listdir('for_test/')


for file in File_list:
    file_name, file_ext = os.path.splitext(file)


    f_title, f_course, f_num = file_name.split('-')

    f_title = f_title.strip()
    f_course = f_course.strip()
    f_num = f_num.strip()[1:].zfill(2)

    new_name = '{}-{}{}'.format(f_num, f_title, file_ext)

    os.rename(file, new_name)


