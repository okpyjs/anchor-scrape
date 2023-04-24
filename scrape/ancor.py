import re

from scrape import helper


def get_ancor(url):
    internal_links = []
    anchor_text_counts = {}
    soup = helper.get_soup(url)

    # Extract all the links and anchor text on the page
    for link in soup.find_all("a"):
        href: str = " ".join(
            re.findall(
                r".+", link.get("href"), re.MULTILINE | re.IGNORECASE | re.UNICODE
            )
        )
        text: str = " ".join(
            re.findall(
                r".+", link.text.strip(), re.MULTILINE | re.IGNORECASE | re.UNICODE
            )
        )
        text = text.replace("\xa0", " ")
        href = href.split("?")[0]

        if href.startswith(url):
            href = href.replace(url, "")
            if not href:
                continue
            if not href[0] == "/":
                href = "/" + href

        if (
            href
            and href.startswith("/")
            and not text.strip() == ""
            and not href.strip() == "/"
        ):
            internal_links.append({"url": href, "anchor_text": text})

            if text in anchor_text_counts:
                anchor_text_counts[text] += 1
            else:
                anchor_text_counts[text] = 1
    anchor_text_counts = dict(
        sorted(anchor_text_counts.items(), key=lambda item: item[1], reverse=True)
    )

    # Count the number of internal links that point to the URL provided by the user
    num_internal_links = len(internal_links)

    resp_data = {
        "total_link": num_internal_links,
        "anchor_text_distribution": anchor_text_counts,
        "links": internal_links,
    }

    return resp_data
