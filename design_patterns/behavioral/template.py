def get_text():
    return "plain_text"


def get_xml():
    return "xml"


def get_pdf():
    return "pdf"


def get_csv():
    return "csv"


def convert_to_text(data):
    print("[CONVERT]")
    return "{} as text".format(data)


def saver():
    print("[SAVE]")


def template_function(getter, converter=False, to_save=False):
    data = getter()

    print("Got `{}`".format(data))

    if len(data) <= 3 and converter:
        data = converter(data)
    else:
        print("Skip conversion")

    if to_save:
        saver()

    print("`{}` was processed".format(data))


""" USAGE:
template_function(get_text, to_save=True)

template_function(get_pdf, converter=convert_to_text)

template_function(get_csv, to_save=True)

template_function(get_xml, to_save=True)
"""
