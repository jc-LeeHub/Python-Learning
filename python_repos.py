import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS


#执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars' #返回的项目按星级进行排序
r=requests.get(url)

#返回结果存入变量
response_dict = r.json()    

#仓库数目
print("Total repositories:", response_dict['total_count'])  

#仓库信息,每个字典存储一个仓库的信息
repo_dicts = response_dict['items']     
print("Repositories returned:", len(repo_dicts))

#数据存入列表
names, plot_dicts = [],[]
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])

    #将星级、对应的描述已经超链接存入字典
    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': repo_dict['description'],
        'xlink': repo_dict['html_url'],
        }
    plot_dicts.append(plot_dict)

#可视化
my_style = LS('#333366', base_style=LCS)

#修改my_config的属性，来定制图表的外观
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15       #最长显示15个字符
my_config.show_y_guides = False     #隐藏水平线
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Python Project on Github'
chart.x_labels = names

chart.add('', plot_dicts)   #添加数值及描述
chart.render_to_file('python_repos.svg')






