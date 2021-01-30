from high_order_framework_requests_python import utils_class

list_valid_chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
def is_string_valid(chuoi):
    for c in chuoi:
        if c not in list_valid_chars:
            return False
    return True

list_lines = utils_class.File_Interact("100k.txt").read_file_list()
list_lines = [line.lower() for line in list_lines if line[0]!='#' and is_string_valid(line)]
list_lines = list(dict.fromkeys(list_lines))

utils_class.File_Interact("output_70k.txt").write_file_from_list(list_lines)