from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import NewUrlForm
from .website_analyse import website_analyse_obj as wa
from .website_analyse import tags_types as tt

def home(request, url=None):
    if request.method == 'POST':
        form = NewUrlForm(request.POST)
        if form.is_valid():
            input_url = form.save()
            validation = wa.UrlValidation(input_url.url)
            if validation:
                http_url = validation.http_url
                web_bytes = wa.WebBytes(http_url)
                web_bytes.open_url()
                sauce = web_bytes.sauce
                soup = wa.get_soup(sauce)
                kw_data = tt.TagData(soup, tt.KeywordsTag)
                p_data = tt.TagData(soup, tt.PTag)
                common_items = wa.get_common_items(p_data.data, kw_data.data)
                res = [(keyword, common_items[keyword]) for keyword in kw_data.data]
                # return redirect('results', {'data':'abc'})         #TODO some clever redirection
                return render(request, 'home.html', {'form': form, 'res':res})
            else:
                return render(request, 'home.html', {'form': form})
    else:
        form = NewUrlForm()

    return render(request, 'home.html', {'form': form})


def results(request, data='No data'):
    data = data
    return render(request, 'results.html', {'data': data})
