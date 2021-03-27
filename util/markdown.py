import panflute
import pypandoc
import logging
import pathlib
import io

TAG2MAPPING = {
    "links": {"panflute_cls": panflute.Link,
              "panflute2json": {"url": "url"}},
    "headers": {"panflute_cls": panflute.Header,
                "panflute2json": {"level": "level", "name": "identifier"}}}


def __init__(self, tag):
  if tag == "links":
    self.tag = panflute.Link
    self.structure = {"url": "url"}
  elif tag == "headers":
    self.tag = panflute.Header
    self.structure = {"level": "level", "name": "identifier"}


def filter(elem, pandoc_doc):
  for tag, mapping in TAG2MAPPING.items():
    if not hasattr(pandoc_doc, tag):
      setattr(pandoc_doc, tag, [])
    if isinstance(elem, mapping["panflute_cls"]):
      doc = {}
      for mapped_key, panflute_key in mapping["panflute2json"].items():
        doc[mapped_key] = getattr(elem, panflute_key)
      getattr(pandoc_doc, tag).append(doc)


def extract(markdown_path, tag):
  logging.debug(f"extract({markdown_path}, {tag})")
  assert tag in TAG2MAPPING, f"Tag Error : {tag} is not supported"
  assert pathlib.Path(markdown_path).is_file(), f"Wrong Markdown Path : {markdown_path}"

  raw_doc = pypandoc.convert_file(str(markdown_path), 'json')
  pandoc_doc = panflute.load(io.StringIO(raw_doc))
  filtered_pandoc_doc = panflute.run_filter(filter, doc=pandoc_doc)

  return getattr(filtered_pandoc_doc, tag)
