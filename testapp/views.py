from django.template.loader import get_template
import pdfkit
from django.http import HttpResponse


def index(request):
    data = dict()
    data["name"] = "ThePythonDjango.Com"
    data["DOB"] = "Jan 10, 2015"

    template = get_template('testapp/test.html')
    html = template.render(data)
    pdf = pdfkit.from_string(html, False)

    filename = "sample_pdf.pdf"

    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="' + filename + '"'
    return response

