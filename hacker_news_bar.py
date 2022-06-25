import requests
from operator import itemgetter
from pygal.style import  LightColorizedStyle as LCS,LightenStyle as LS
import pygal
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print('Status Code: ',r.status_code)
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    url = ('https://hacker-news.firebaseio.com/v0/item/'+str(submission_id)+'.json')
    submission_r=requests.get(url)
    print(submission_r.status_code)
    response_dict=submission_r.json()
    submission_dict={'title':response_dict['title'],
        'link':"http://news.ycombinator.com/item?id="+str(submission_id),
        'comments':response_dict.get('descendants',0)
        }
    submission_dicts.append(submission_dict)
submission_dicts = sorted(submission_dicts,key=itemgetter('comments'),reverse= True)

titles,plot_dicts=[],[]
for submission_dict in submission_dicts: 
    title = submission_dict['title']
    titles.append(title)
    plot_dict = {
        'value':submission_dict['comments'],
        'label':submission_dict['title'],
        'xlink':submission_dict['link']
    }
    plot_dicts.append(plot_dict)

my_style = LS('#333366',base_style = LCS)
my_config =pygal.Config()
my_config.x_label_rotation=45
my_config.show_legend = False
my_config.truncate_label = 15
chart = pygal.Bar(my_config,style=my_style)
chart.title='Most commented stories in hacker-news.com'
chart.x_labels = titles
chart.add('',plot_dicts)
chart.render_to_file('Most_commented_hacker_news.svg')
