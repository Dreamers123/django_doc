from django.shortcuts import  render
from .models import Meal
import requests
from github import Github, GithubException
from .forms import DictionaryForm


def get_meals(request):
    all_meals = {}
    if 'name' in request.GET:
        name = request.GET['name']
        url = 'https://www.themealdb.com/api/json/v1/1/search.php?s=%s'%name
        response = requests.get(url)
        data = response.json()
        meals = data['meals']

        for i in meals:
            meal_data = Meal(
                name = i['strMeal'],
                category = i['strCategory'],
                instructions = i['strInstructions'],
                region = i['strArea'],
                slug = i['idMeal'],
                image_url = i['strMealThumb']
            )
            meal_data.save()
            all_meals = Meal.objects.all().order_by('-id')

    return render (request, 'meal.html', { "all_meals":
    all_meals} )
def meal_detail(request, id):
    meal = Meal.objects.get(id = id)
    print(meal)
    return render (
        request,
        'meal_detail.html',
        {'meal': meal}
    )
def get_ip(request):
    is_cached = ('geodata' in request.session)

    if not is_cached:
        ip_address = request.META.get('HTTP_X_FORWARDED_FOR', '')
        response = requests.get('https://freegeoip.app/json/%s' % ip_address)
        request.session['geodata'] = response.json()

    geodata = request.session['geodata']
    return render(request, 'geo/home.html', {
            'ip': geodata['ip'],
            'country': geodata['country_name'],
            'latitude': geodata['latitude'],
            'longitude': geodata['longitude'],
            'api_key': 'AIzaSyC1UpCQp9zHokhNOBK07AvZTiO09icwD8I',
            'is_cached': is_cached
        })
def get_github(request):
    search_result = {}
    if 'username' in request.GET:
        username = request.GET['username']
        url = 'https://api.github.com/users/%s' % username
        response = requests.get(url)
        search_was_successful = (response.status_code == 200)  # 200 = SUCCESS
        search_result = response.json()
        search_result['success'] = search_was_successful
        search_result['rate'] = {
            'limit': response.headers['X-RateLimit-Limit'],
            'remaining': response.headers['X-RateLimit-Remaining'],
        }
    return render(request, 'core/github.html', {'search_result': search_result})

def get_oxford(request):
    search_result = {}
    if 'word' in request.GET:
        form = DictionaryForm(request.GET)
        if form.is_valid():
            search_result = form.search()
    else:
        form = DictionaryForm()
    return render(request, 'core/oxford.html', {'form': form, 'search_result': search_result})

def github_client(request):
    search_result = {}
    if 'username' in request.GET:
        username = request.GET['username']
        client = Github()

        try:
            user = client.get_user(username)
            search_result['name'] = user.name
            search_result['login'] = user.login
            search_result['public_repos'] = user.public_repos
            search_result['success'] = True
        except GithubException as ge:
            search_result['message'] = ge.data['message']
            search_result['success'] = False

        rate_limit = client.get_rate_limit()
        search_result['rate'] = {
            'limit': rate_limit.rate.limit,
            'remaining': rate_limit.rate.remaining,
        }

    return render(request, 'core/github.html', {'search_result': search_result})
