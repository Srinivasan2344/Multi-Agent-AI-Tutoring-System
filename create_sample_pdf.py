"""Create a sample PDF file for testing."""
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Create a simple PDF
output_path = "data/sample.pdf"
c = canvas.Canvas(output_path, pagesize=letter)
width, height = letter

# Add title
c.setFont("Helvetica-Bold", 16)
c.drawString(50, height - 50, "Sample Educational Document")

# Add some content
c.setFont("Helvetica", 12)
y = height - 100

content = [
    "Introduction to Machine Learning",
    "",
    "Machine learning is a subset of artificial intelligence (AI) that provides systems",
    "the ability to automatically learn and improve from experience without being",
    "explicitly programmed.",
    "",
    "Key Concepts:",
    "- Supervised Learning: Learning with labeled data",
    "- Unsupervised Learning: Learning with unlabeled data",
    "- Reinforcement Learning: Learning through interaction and feedback",
    "",
    "Applications:",
    "- Image recognition and computer vision",
    "- Natural language processing",
    "- Recommendation systems",
    "- Autonomous vehicles",
    "",
    "Conclusion:",
    "Machine learning continues to revolutionize various industries and is becoming",
    "increasingly important in modern technology solutions."
]

line_height = 15
for line in content:
    if y < 50:  # Start new page if needed
        c.showPage()
        c.setFont("Helvetica", 12)
        y = height - 50
    c.drawString(50, y, line)
    y -= line_height

c.save()
print(f"Sample PDF created at {output_path}")
