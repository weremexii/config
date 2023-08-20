import os
import shutil
import re

input_folder_list = [
    '/Users/mexii/Development/my-repo/dotfile/subconverter',
    '/Users/mexii/Development/my-repo/dotfile_private/subconverter'
]

output_folder = '/Users/mexii/Development/executable/subconverter'

def dry_run_wrapper(dry_run: bool):
    def decorator(func):
        if not dry_run:
            return func
        else:
            def do_nothing(*args, **kwargs):
                return
            return do_nothing
    return decorator


def inject(dry_run: bool, skip_exist: bool):
    makedirs = dry_run_wrapper(dry_run)(os.makedirs)
    copy = dry_run_wrapper(dry_run)(shutil.copy)
    copy2 = dry_run_wrapper(dry_run)(shutil.copy2)
    for input_folder in input_folder_list:
        print(f"For input {input_folder}")
        for dirpath, dirname, filename in os.walk(input_folder):
            # set direction
            target_dirpath = str(dirpath).replace(input_folder, output_folder, 1)
            print(f"At {target_dirpath}")
            # dir create
            for d in dirname:
                if not os.path.exists(os.path.join(target_dirpath, d)):
                    print('\t' + f"mkdir - {os.path.basename(os.path.join(target_dirpath, d))}")
                makedirs(os.path.join(target_dirpath, d), exist_ok=True)
            # file copy
            for f in filename:
                will_overwrite = os.path.exists(os.path.join(target_dirpath, f))
                if not skip_exist or not will_overwrite:
                    append_warning = "(OVERWRITE)" if will_overwrite else ""
                    print('\t' + append_warning + f"copy - {os.path.basename(os.path.join(dirpath, f))}")
                if skip_exist and not will_overwrite:
                    copy(os.path.join(dirpath, f), target_dirpath)
                else:
                    copy2(os.path.join(dirpath, f), target_dirpath)
if __name__ == '__main__':
    inject(False, False)
