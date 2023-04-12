# Learning to parse URLs (walkthrough with Stephen)

def parse_url(url: str):
    parsed_url = {
        "protocol": "",
        "host": "",
        "port": "",
        "path": "",
        "query": "",
        "fragment": "",
        "raw": url,
    }

    for part in [
        (":", "protocol"),
        (":", "host", "/"),
        ("/", "port"),
        ("?", "path"),
        ("#", "query"),
    ]:
        if len(part) == 2:
            url = parse_url_part(url, part[0], parsed_url, part[1])
        else:
            url = parse_url_part(url, part[0], parsed_url, part[1], part[2])

    parsed_url["fragment"] = url

    return parsed_url


def parse_url_part(
    url: str, split_char: str, parsed: dict, key: str, strip_char: str = ""
):
    url_parts = url.split(split_char, 1)
    parsed[key] = url_parts[0].strip(strip_char)

    return url_parts[1]


print(parse_url("http://www.example.com:80/articles?page=1#title"))
