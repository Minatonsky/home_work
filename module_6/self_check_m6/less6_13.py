import shutil
def create_backup(path, file_name, employee_residence):
    with open(f"{path}/{file_name}", "wb") as file_withlist:
        for employee, residence in employee_residence.items():
            line = f"{employee} {residence}\n"
            file_withlist.write(line.encode())
    archive = shutil.make_archive("backup_folder", 'zip', path)
    return archive