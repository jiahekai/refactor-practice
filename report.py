import csv

#把词频写成csv
def write_csv(output_csv,total):
    with open(output_csv, "w", newline="",encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["word", "count"])
        for w, n in total.most_common():
            writer.writerow([w, n])
#把报告写成markdown
def write_report(report_md,total,file_rows):
    with open(report_md, "w",encoding="utf-8") as f:
        f.write("# 文本统计报告\n\n")
        f.write("| 文件 | 句数 | 词数 |\n")
        f.write("| --- | --- | --- |\n")
        for row in file_rows:
            f.write("| %s | %d | %d |\n" % row)
        f.write("\n## TOP10\n\n")
        for w, n in total.most_common(10):
            f.write("- %s: %d\n" % (w, n))
