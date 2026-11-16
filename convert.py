import json


def read_chunks(path):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    chunks = []
    for part in content.split("###"):
        part = part.strip()
        if part:
            chunks.append(part)
    return chunks


def parse_article(chunk):
    lines = chunk.split("\n")
    url = lines[0]
    title = lines[1] if len(lines) > 1 else ""
    content = "\n".join(lines[2:])
    return {"url": url, "title": title, "content": content}


def write_json(articles, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(articles, f, indent=4, ensure_ascii=False)


def main():
    chunks = read_chunks("doc.txt")
    articles = []
    for chunk in chunks:
        articles.append(parse_article(chunk))
    write_json(articles, "doc.json")
    print("Text file converted to JSON successfully.")


if __name__ == "__main__":
    main()