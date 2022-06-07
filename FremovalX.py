from pathlib import Path

def FremovalX(path,file_name):
    for folder in path.iterdir():
        if folder.is_dir():
            FremovalX(folder,file_name)
            file_to_remove=folder / file_name
            file_to_remove.unlink()

p=input("enter parent folder path : ")
path=Path(rf"{p}")
removeF=input("enter file to remove ( ex texts.txt ): ")
FremovalX(path,removeF)
