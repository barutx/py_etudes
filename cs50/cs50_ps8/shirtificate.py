from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("helvetica", "B", 16)
pdf.cell(40, 10, "Serhat")
pdf.ln()
pdf.cell(60,10,"Seleeem")
pdf.output("deneme1.pdf")

# class PDF(FPDF):
#     def header(self):
#         self.image("/Users/barut/Desktop/output.jpg",10,8,200,50)
#         self.set_font("helvetica", "B", 15)
#         self.cell(80)
#         self.cell(30,10, "Title", border = 1, align="C")
#         self.ln(50)
    
#     def footer(self):
#         self.set_y(-15)
#         self.set_font("helvetica", "I", 8)
#         self.cell(0,10,f"Page {self.page_no()}/{{nb}}", align="C")

# pdf = PDF()
# pdf.add_page()
# pdf.set_font("Times", size=12)
# for i in range(1,41):
#     pdf.cell(0, 10, f"Printing line number {i}", new_x="LMARGIN", new_y="NEXT")
# pdf.output("new-deneme2.pdf")
        
    
# class PDF(FPDF):
#     def header(self):
#         self.set_font("helvetica", "B", 15)
#         width = self.get_string_width(self.title) + 6
#         self.set_x((210-width))
