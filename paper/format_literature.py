from pathlib import Path
import re

from docx import Document
from docx.shared import Inches, Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_CELL_VERTICAL_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn


# --------------------------------------------------
# FILE PATHS
# --------------------------------------------------

BASE = Path(__file__).resolve().parent

SOURCE = BASE / "literature_review.md"
OUTPUT = BASE / "literature_review_final_v2.docx"


# --------------------------------------------------
# FORMATTING FUNCTIONS
# --------------------------------------------------

def format_run(run, size=10, bold=False):
    run.font.name = "Times New Roman"
    run.font.size = Pt(size)
    run.bold = bold


def set_cell_shading(cell, fill="D9EAF7"):
    shading = OxmlElement("w:shd")
    shading.set(qn("w:fill"), fill)
    cell._tc.get_or_add_tcPr().append(shading)


def set_cell_margins(cell):
    tc = cell._tc
    tc_pr = tc.get_or_add_tcPr()

    margins = OxmlElement("w:tcMar")

    for margin in ("top", "start", "bottom", "end"):
        node = OxmlElement(f"w:{margin}")
        node.set(qn("w:w"), "80")
        node.set(qn("w:type"), "dxa")
        margins.append(node)

    tc_pr.append(margins)


# --------------------------------------------------
# TABLE FUNCTION
# --------------------------------------------------

def add_table(doc, rows):

    if not rows:
        return

    column_count = max(len(row) for row in rows)

    table = doc.add_table(
        rows=1,
        cols=column_count
    )

    table.style = "Table Grid"
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = True

    for row_index, row in enumerate(rows):

        if row_index == 0:
            cells = table.rows[0].cells
        else:
            cells = table.add_row().cells

        for col_index in range(column_count):

            value = row[col_index] if col_index < len(row) else ""

            cell = cells[col_index]
            cell.text = value
            cell.vertical_alignment = (
                WD_CELL_VERTICAL_ALIGNMENT.CENTER
            )

            set_cell_margins(cell)

            if row_index == 0:
                set_cell_shading(cell)

            for paragraph in cell.paragraphs:

                paragraph.alignment = WD_ALIGN_PARAGRAPH.LEFT

                for run in paragraph.runs:
                    format_run(
                        run,
                        size=8,
                        bold=(row_index == 0)
                    )

    doc.add_paragraph()


# --------------------------------------------------
# MAIN DOCUMENT GENERATOR
# --------------------------------------------------

def main():

    if not SOURCE.exists():
        raise FileNotFoundError(
            f"Markdown file not found: {SOURCE}"
        )

    text = SOURCE.read_text(encoding="utf-8-sig")

    doc = Document()

    # Page setup
    section = doc.sections[0]

    section.top_margin = Inches(0.7)
    section.bottom_margin = Inches(0.7)
    section.left_margin = Inches(0.65)
    section.right_margin = Inches(0.65)

    # Default font
    normal = doc.styles["Normal"]
    normal.font.name = "Times New Roman"
    normal.font.size = Pt(10)

    normal.paragraph_format.space_after = Pt(6)

    lines = text.splitlines()

    i = 0

    while i < len(lines):

        line = lines[i].strip()

        if not line:
            i += 1
            continue

        # ------------------------------------------
        # MARKDOWN TABLE
        # ------------------------------------------

        if line.startswith("|"):

            rows = []

            while (
                i < len(lines)
                and lines[i].strip().startswith("|")
            ):

                cells = [
                    cell.strip()
                    for cell in lines[i].strip().strip("|").split("|")
                ]

                # Skip Markdown separator rows
                if not all(
                    re.fullmatch(r":?-{3,}:?", cell)
                    for cell in cells
                ):
                    rows.append(cells)

                i += 1

            add_table(doc, rows)
            continue

        # ------------------------------------------
        # MAIN HEADING
        # ------------------------------------------

        if line.startswith("# "):

            p = doc.add_heading(
                line[2:].strip(),
                level=1
            )

            p.alignment = WD_ALIGN_PARAGRAPH.CENTER

        # ------------------------------------------
        # SECOND LEVEL HEADING
        # ------------------------------------------

        elif line.startswith("## "):

            heading_text = line[3:].strip()

            p = doc.add_heading(
                heading_text,
                level=2
            )

        # ------------------------------------------
        # THIRD LEVEL HEADING
        # ------------------------------------------

        elif line.startswith("### "):

            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER

            run = p.add_run(line[4:].strip())
            format_run(run, size=12, bold=True)

        # ------------------------------------------
        # BULLET LIST
        # ------------------------------------------

        elif line.startswith("- "):

            p = doc.add_paragraph(
                style="List Bullet"
            )

            run = p.add_run(line[2:].strip())
            format_run(run)

        # ------------------------------------------
        # NUMBERED LIST
        # Preserve original Markdown numbering
        # ------------------------------------------

        elif re.match(r"^\d+\.\s+", line):

            p = doc.add_paragraph()

            p.paragraph_format.left_indent = Inches(0.2)
            p.paragraph_format.first_line_indent = Inches(-0.2)
            p.paragraph_format.space_after = Pt(6)

            run = p.add_run(line)
            format_run(run, size=10)

        # ------------------------------------------
        # NORMAL PARAGRAPH
        # ------------------------------------------

        else:

            p = doc.add_paragraph()

            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            p.paragraph_format.space_after = Pt(6)

            run = p.add_run(line)
            format_run(run)

        i += 1

    # ----------------------------------------------
    # SAVE DOCUMENT
    # ----------------------------------------------

    doc.save(OUTPUT)

    print("\nWord document created successfully!")
    print(f"Output file: {OUTPUT}")


# --------------------------------------------------
# RUN PROGRAM
# --------------------------------------------------

if __name__ == "__main__":
    main()