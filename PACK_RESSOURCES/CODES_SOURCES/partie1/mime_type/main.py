


def extract_file_extension(fname):
    s = fname.split(".")
    if len(s) == 1:
        return None
    return s[-1]

print(extract_file_extension("doc.important"))

# "test.html" => "html"
# "noextension" => None
# "portrait.png" => "png"
# "doc.TXT" => "TXT"
# "doc.important.TXT" => "TXT"
