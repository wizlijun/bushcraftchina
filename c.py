from pdf2docx import Converter

# PDF 输入路径 & DOCX 输出路径
pdf_file = 's.pdf'
docx_file = 's.docx'

# 创建转换器对象
cv = Converter(pdf_file)
cv.convert(docx_file, start=0, end=None)  # 可指定页码范围
cv.close()


