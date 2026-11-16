import json

from convert import parse_article, read_chunks, write_json


def test_parse_article():
    chunk = "https://example.com/a\nBike Climate\nCycling reduces CO2."
    result = parse_article(chunk)
    assert result["url"] == "https://example.com/a"
    assert result["title"] == "Bike Climate"
    assert result["content"] == "Cycling reduces CO2."


def test_parse_article_multiline_content():
    chunk = "url\ntitle\nline one\nline two"
    result = parse_article(chunk)
    assert result["content"] == "line one\nline two"


def test_parse_article_without_title():
    result = parse_article("only-url")
    assert result["url"] == "only-url"
    assert result["title"] == ""
    assert result["content"] == ""


def test_read_chunks(tmp_path):
    file = tmp_path / "doc.txt"
    file.write_text("url1\ntitle1\ntext1\n###\nurl2\ntitle2\ntext2", encoding="utf-8")
    chunks = read_chunks(str(file))
    assert len(chunks) == 2
    assert chunks[0] == "url1\ntitle1\ntext1"
    assert chunks[1] == "url2\ntitle2\ntext2"


def test_read_chunks_skips_empty_parts(tmp_path):
    file = tmp_path / "doc.txt"
    file.write_text("a\n###\n###\nb", encoding="utf-8")
    chunks = read_chunks(str(file))
    assert chunks == ["a", "b"]


def test_write_json(tmp_path):
    articles = [{"url": "u", "title": "t", "content": "c"}]
    file = tmp_path / "out.json"
    write_json(articles, str(file))
    loaded = json.loads(file.read_text(encoding="utf-8"))
    assert loaded == articles