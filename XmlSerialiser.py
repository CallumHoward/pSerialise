import xml.etree.ElementTree as ET
from Serialiser import Serialiser


class XmlSerialiser(Serialiser):
    """
    XmlSerialiser, XML implementation of Serialiser
    """

    @staticmethod
    def serialise(data):
        try:
            serialised = xml_dumps([element.__dict__ for element in data])

        except TypeError:
            raise

        except:
            raise

        return serialised


    @staticmethod
    def deserialise(serialised, dataContainer):
        try:
            raw_data = xml_loads(serialised)  # load as a list of dictionaries
            data = [dataContainer(**element) for element in raw_data]

        except TypeError:
            raise Serialiser.DeserialiseError(
                    "Failed to restore python object. Could not deserialise target data")

        except:  # propagate unexpected exceptions
            raise

        return data


def xml_dumps(data_list):
    xml_header = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>"

    root_tag_open = "<Data xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"" + \
            " xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\">"
    root_tag_close = "</Data>"

    entry_tag_open = "<Entry>"
    entry_tag_close = "</Entry>"

    # construct xml
    output_xml = xml_header + "\n" + root_tag_open + "\n"

    for element in data_list:
        output_xml += entry_tag_open + "\n"

        for key, value in element.items():
            tag_open = "<" + key + ">"
            tag_close = "</" + key + ">"
            output_xml += tag_open + str(value) + tag_close + "\n"

        output_xml += entry_tag_close + "\n"

    output_xml += root_tag_close

    return output_xml


def xml_loads(serialised):
    output_list = []
    root = ET.fromstring(serialised)

    for entry_node in root:
        entry = {info.tag: info.text for info in entry_node}
        output_list.append(entry)

    return output_list
