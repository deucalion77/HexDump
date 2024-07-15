import os
import argparse

def file_Open():

    try:
        parser = argparse.ArgumentParser(description="Read and process a file.")
        parser.add_argument('filename', type=str, help='Name of the file to read')
        file_Name = parser.parse_args()
        #file_Name = input("Enter the file: ")
        with open(file_Name.filename, "rb") as file:
            xxd = file.read()
        #print(xxd)
        return xxd
        
    except FileNotFoundError:
        print(f"\nWrong File Name")
        return None


def hex_Creation(file_Content):
    hex_File = []
    for i in range(0, len(file_Content), 8):
        #print(i)
        hex_values = " ".join(f"{byte:02x}" for byte in file_Content[i:i+8])
        hex_File.append(hex_values)
        #print(hex_File)
    return hex_File


def offset_Creation(file_Content):
    off_Set = 1000
    for i in range (len(file_Content)-1):
        off_Set += 1
       #off_Set += 1
    return off_Set


def main():
   file_Content = file_Open()
   returned_Hexs = hex_Creation(file_Content)
   off_Set = offset_Creation(file_Content)
   for i, returned_Hex in enumerate(returned_Hexs):
        strt_Index = i * 8
        end_Index = strt_Index + 8
        original_data = file_Content[strt_Index:end_Index]
        ora_Index = ''.join(chr(b) if 32 <= b < 127 else '.' for b in original_data)
        print(f"{off_Set:<8} {returned_Hex} {ora_Index:>12}")

   
main()