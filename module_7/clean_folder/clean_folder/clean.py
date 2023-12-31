from pathlib import Path
import sys
import shutil

script_directory = Path(__file__).resolve().parent
sys.path.append(str(script_directory))

import file_parser as parser
from normalize import normalize


def handle_media(filename: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(target_folder / normalize(filename.name))


def handle_other(filename: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(target_folder / normalize(filename.name))


def handle_archive(filename: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    folder_for_file = target_folder / normalize(filename.name.replace(filename.suffix, ''))
    folder_for_file.mkdir(exist_ok=True, parents=True)
    try:
        shutil.unpack_archive(str(filename.resolve()), str(folder_for_file.resolve()))
    except shutil.ReadError:
        folder_for_file.rmdir()
        return None
    filename.unlink()


def handle_folder(folder: Path):
    try:
        folder.rmdir()
    except OSError:
        print(f'Не удалось удалить папку {folder.resolve()}')


def main(folder: Path):
    parser.scan(folder)

    for file in parser.IMAGES:
        handle_media(file, folder / 'images')

    for file in parser.VIDEO:
        handle_media(file, folder / 'video')

    for file in parser.AUDIO:
        handle_media(file, folder / 'audio')

    for file in parser.DOCUMENTS:
        handle_media(file, folder / 'documents')

    for file in parser.OTHER:
        handle_other(file, folder / 'OTHER')

    for file in parser.ARCHIVES:
        handle_archive(file, folder / 'archives')

    for folder in parser.FOLDERS[::-1]:
        handle_folder(folder)


def start():
    try:
        if len(sys.argv) == 2:
            folder_for_scan = Path(sys.argv[1])
            print(f'Start in folder {folder_for_scan.resolve()}')
            main(folder_for_scan)
        else:
            print(f"Usage: {Path(__file__).name} indir")
    except IndexError:
        print(f"Usage: {Path(__file__).name} indir")


if __name__ == "__main__":
    start()