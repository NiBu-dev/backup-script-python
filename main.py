import shutil
import os
import datetime

class Backup:

    def __init__(self):
        print 'Start backup process!'
        self.user_in()

    def user_in(self):
        source_folder = raw_input('Please input the source directory: ')
        destination_folder = raw_input('Pleas input the destination directory: ') + '/md_backup{0}'
        new_backup_dir_name = self.check_backup_in_dest_dir(destination_folder)
        self.copy_files(source_folder, new_backup_dir_name)

    def check_backup_in_dest_dir(self, base_directory):
        date = str(datetime.datetime.now())[:16]
        date = date.replace(' ', '_').replace(':', '')
        return base_directory.format(date)

    def copy_files(self, src, dst):
        try:
            shutil.copytree(src, dst)
        except shutil.Error as exc:
            # handle any exception that might occur
            print("Got exception {} while copying {} to {}".format(exc, src, dst))

Backup()