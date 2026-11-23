import os
import logging
from collections import Counter


from text_ops import read_text,analyze_text
from report import write_csv ,write_report
folder = "data"
output_csv = "result.csv"
report_md = "report.md"

all_counts = {}
file_rows=[]
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger("docstats")


def main():
    if not os.path.isdir(folder):
        logger.error("数据文件不存在:%s",folder)
        return
    for filename in os.listdir(folder):
        if not filename.endswith(".txt"):
            continue
        path = os.path.join(folder, filename)
        try:
            text = read_text(path)
        except UnicodeDecodeError:
            logger.error("编码错误，跳过：%s",filename)
            continue
        count,sentences,words=analyze_text(text)
        all_counts[filename]=count
        
        file_rows.append((filename, len(sentences), len(words)))
        logger.info("%s 句数=%d 词数=%d", filename, len(sentences), len(words))
    total = Counter()
    for c in all_counts.values():
        total.update(c)

    print("总计 TOP10:")
    for w, n in total.most_common(10):
        print(w, n)

    write_csv(output_csv,total)

    write_report(report_md,total,file_rows)

    print("完成，结果写入", output_csv, "和", report_md)

if __name__=="__main__":
    main()
