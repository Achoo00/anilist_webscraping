from docx import Document
import os
import sys

os.chdir("C:\\Users\\amaha\\PycharmProjects\\manga_novel_scraper\\manga_pdf\\")
for file_name in os.listdir("C:\\Users\\amaha\\PycharmProjects\\manga_novel_scraper\\manga_pdf\\"):
    if file_name.endswith('.pdf'):
        os.remove(path + file_name)


