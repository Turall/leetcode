# import re


# def simplify_path(path):
#     if "/./" == path or path == "/../" or path == "/":
#         return "/"
#     if not bool(re.search('[a-zA-Z]', path)):
#         return "/"

#     path = re.sub("//", "/", path)
#     path = re.sub("(\.\./)", "", path)
#     path = re.sub("(/\./)$", "", path)
#     path = re.sub("(/\./)$|(/\../)$", "/", path)
#     if path == "/":
#         return path
#     if path[-1] == "/" and path[-2] != ".":
#         path = re.sub("/$", "", path)
#     path = re.sub("/[a-z]/\.{1,2}/[a-z]?/[\.\./]?[a-z]", "/c", path)
#     path = re.sub("/[a-z]/[a-z]/[a-z]", "/c", path)

#     return path


def simplify_path(path):
    path = path.split("/")
    temp = ['']
    for i in path:
        if i:
            if i not in ('.', '..'):
                if len(temp) == 0:
                    temp.append('')
                temp.append(i)
            elif i == '..' and len(temp) > 0:
                temp.pop()
    if len(temp) < 2:
        return "/"
    else:
        return "/".join(temp)



# "/../"
# /a/../../b/../c//.//
print(simplify_path("/a/../../b/../c//.//"))
