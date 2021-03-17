import os


class LatexPaper:
    """This base class is used to export exam in tex and pdf file"""
    def get_latex_string(self) -> str:
        pass

    def export_tex_file(self, file_dir: str):
        """Export to .tex file"""
        file = open(f"{file_dir}.tex", "w")
        file.write(self.get_latex_string())
        file.close()

    def export_pdf_file(self, file_dir: str):
        """Export to pdf file"""
        self.export_tex_file(file_dir)
        os.system(f"pdflatex {file_dir}.tex")
