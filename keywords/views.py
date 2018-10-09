from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import NewUrlForm
from .website_analyse import website_analyse_obj as wa
from .website_analyse import tags_types as tt

def home(request, url=None):
    if request.method == 'POST':
        errors = []
        form = NewUrlForm(request.POST)
        if form.is_valid():
            url = form.save(commit=False)
            validation = wa.UrlValidation(url.url)
            if validation:
                http_url = validation.http_url
                web_bytes = wa.WebBytes(http_url, use_user_agent=True)
                try:
                    web_bytes.open_url()
                except Exception as e:
                    errors.append(
                        f"Unable to get URL. Please make sure it's valid and try again.\n{e}"
                    )
                    return render(request, 'home.html', {'form': form, 'errors': errors})
                sauce = web_bytes.sauce
                soup = wa.get_soup(sauce)
                kw_data = tt.TagData(soup, tt.KeywordsTag)
                p_data = tt.TagData(soup, tt.PTag)
                common_items = wa.get_common_items(p_data.data, kw_data.data)
                res = [(keyword, common_items[keyword]) for keyword in kw_data.data]
                url.keywords = kw_data.data
                try:
                    url.save()
                except Exception as e:
                    errors.append(f'Unable to add item to database; {e}')

                # return redirect('results', {'data':'abc'})         #TODO some clever redirection
                return render(request, 'home.html', {'form': form, 'errors': errors,'res':res})
            else:
                errors.append(
                    "Unable to get URL. Please make sure it's valid and try again.2"
                )
                return render(request, 'home.html', {'form': form, 'errors': errors})
    else:
        form = NewUrlForm()

    return render(request, 'home.html', {'form': form})


def results(request, data='No data'):
    data = data
    return render(request, 'results.html', {'data': data})
