thonimport json

def convert_format(data, output_format):
    if output_format == "json":
        return json.dumps(data)
    elif output_format == "vtt":
        return data.get("vtt", "")
    else:
        raise Exception(f"Unsupported format: {output_format}")