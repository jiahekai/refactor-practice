import re
import logging
from collections import Counter

logger=logging.getLogger("docstats")

#读一个文件，返回文本
def read_text(path):
    with open(path,encoding="utf-8")as f:
        return f.read()
#清洗+分句+统计词频，返回结果
def analyze_text(text):
    text = re.sub(r"[^\u4e00-\u9fa5a-zA-Z0-9\s]", "", text)
    sentences = re.split(r"[。！？\n]+", text)
    sentences = [s.strip() for s in sentences if s.strip()]
    words = []
    for s in sentences:
        words.extend(re.findall(r"[a-zA-Z\u4e00-\u9fa5]+", s))
    count = Counter(words)
    return count,sentences,words