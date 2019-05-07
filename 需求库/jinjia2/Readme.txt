# ��򵥵�
from jinja2 import Environment, PackageLoader
env = Environment(loader=PackageLoader('yourapplication', 'templates'))  # ��package��path��
template = env.get_template('mytemplate.html')
print template.render(the='variables', go='here')


# ���ø���·���ļ��ط���
loader = FileSystemLoader('/path/to/templates')
loader = FileSystemLoader(['/path/to/templates', '/other/path'])

# ���ø���ģ��ļ��ط���
loader = PackageLoader('mypackage', 'views')

# ���ø���dict�ֵ�ļ��ط���
loader = DictLoader({'index.html': 'source here'})

# ����ǰ׺���أ�
class jinja2.PrefixLoader(mapping, delimiter='/')  # Ĭ��Ϊ'/',   'app1/index.html'
loader = PrefixLoader({
    'app1':     PackageLoader('mypackage.app1'),
    'app2':     PackageLoader('mypackage.app2')
})




# �ֽ��뻺��
from os import path
class MyCache(BytecodeCache):
    def __init__(self, directory):
        self.directory = directory
    def load_bytecode(self, bucket):
        filename = path.join(self.directory, bucket.key)
        if path.exists(filename):
            with open(filename, 'rb') as f:
                bucket.load_bytecode(f)
    def dump_bytecode(self, bucket):
        filename = path.join(self.directory, bucket.key)
        with open(filename, 'wb') as f:
            bucket.write_bytecode(f)


# ��������
���������ַָ���: {% ... %} �� {{ ... }} ��
ǰ������ִ������ for ѭ�� ��ֵ����䣬���߰ѱ��ʽ�Ľ����ӡ��ģ���ϡ�

{{ foo.bar }}  # ͨ��.���ʱ��������ԣ�����ͨ���±�Ҳ����
{{ foo['bar'] }}


# ������
������������ùܵ����ţ� | ���ָһ��������������ᱻ��Ϊ ��һ�������������롣
{{ name|striptags|title }}  ���Ƴ� name �е����� HTML ��ǩ���Ҹ�д Ϊ������ʽ�Ĵ�Сд��ʽ��
�����ӻ� ��һ���б��ö�����������: {{ list|join(', ') }} 

# ע��
 {# ... #} 
{# note: disabled template because we no longer use this
    {% for user in users %}
        ...
    {% endfor %}
#}


# ������-�����ȥ���հ�
{% for item in seq -%}
    {{ item }}
{%- endfor %}   # ��ǩ�ͼ���֮�䲻���пհס�



# �����, ʹ��#����{}
<ul>
# for item in seq
    <li>{{ item }}</li>
# endfor
</ul>

<ul>
{% for item in seq %}
    <li>{{ item }}</li>
{% endfor %}
</ul>


# ����ģ�� ���е� block ��ǩ ����ģ������ ��ģ����Ը���ģ���е���Щ����
{% block %}    # {% block sidebar %} ������ע��
# ��ģ��  {% extend %} ��ǩ������Ĺؼ���������ģ���������ģ�塰�̳С���һ��ģ��
# �� {% extends "layout/default.html" %}
{% extends "base.html" %}
{% block title %}Index{% endblock %}
{% block head %}
    {{ super() }}
    <style type="text/css">
        .important { color: #336699; }
    </style>
{% endblock %}
{% block content %}
    <h1>Index</h1>
    <p class="important">
      Welcome on my awesome homepage.
    </p>
{% endblock %}


# Super ��   ���Ե��� super ����Ⱦ����������ݡ���᷵�ظ�����Ľ��:
{% block sidebar %}
    <h3>Table Of Contents</h3>
    ...
    {{ super() }}
{% endblock %}


# ��һ�� for ѭ����������Է�����Щ����ı���:
loop.index	��ǰѭ�������Ĵ������� 1 ��ʼ��
loop.index0	��ǰѭ�������Ĵ������� 0 ��ʼ��
loop.revindex	��ѭ��������Ҫ�����Ĵ������� 1 ��ʼ��
loop.revindex0	��ѭ��������Ҫ�����Ĵ������� 0 ��ʼ��
loop.first	����ǵ�һ�ε�����Ϊ True ��
loop.last	��������һ�ε�����Ϊ True ��
loop.length	�����е���Ŀ����
loop.cycle	��һ�����м���ȡֵ�ĸ���������������Ľ��͡�



Ҫ�ݹ�� ʹ��ѭ������ֻ��Ҫ��ѭ�������м��� recursive ���Σ���������ʹ�õݹ�ĵ� �����Կɵ��������� loop ������
<ul class="sitemap">
{%- for item in sitemap recursive %}
    <li><a href="{{ item.href|e }}">{{ item.title }}</a>
    {%- if item.children -%}
        <ul class="submenu">{{ loop(item.children) }}</ul>
    {%- endif %}</li>
{%- endfor %}
</ul>



# ��
{% macro input(name, value='', type='text', size=20) -%}
    <input type="{{ type }}" name="{{ name }}" value="{{
        value|e }}" size="{{ size }}">
{%- endmacro %}
�������ռ��У���֮���������һ������:
<p>{{ input('username') }}</p>
<p>{{ input('password', type='password') }}</p>

������ڲ�ͬ��ģ���ж��壬����Ҫ����ʹ�� import ��
�ں��ڲ�������Է�����������ı���:

# ����
��ĳЩ����£���Ҫ��һ���괫�ݵ���һ���ꡣΪ�ˣ�����ʹ������� call ��    �ú����õ��ù���:
{% macro render_dialog(title, class='dialog') -%}
    <div class="{{ class }}">
        <h2>{{ title }}</h2>
        <div class="contents">
            {{ caller() }}
        </div>
    </div>
{%- endmacro %}
�ܶ���֮�����ÿ�Ĺ����� ʽ���������ͬ��ֻ�ǵ��ÿ�û�����ơ�
{% call render_dialog('Hello World') %}
    This is a simple dialog rendered by using a macro and
    a call block.
{% endcall %}



# ��ֵ
��ֵʹ�� set ��ǩ�����ҿ���Ϊ���������ֵ:
{% set navigation = [('index.html', 'Index'), ('about.html', 'About')] %}
{% set key, value = call_something() %}


# ����
include ������ڰ���һ��ģ�壬���ڵ�ǰ�����ռ��з����Ǹ��ļ��������� Ⱦ���:
{% include 'header.html' %}
    Body
{% include 'footer.html' %}

�� ���ģ�岻���ڣ�Jinja �����������䡣�� with �� without context �������ʹ��ʱ�������뱻���������Ŀɼ������ ֮ǰ ��
{% include "sidebar.html" ignore missing %}
{% include "sidebar.html" ignore missing with context %}
{% include "sidebar.html" ignore missing without context %}
��Ҳ�����ṩһ��ģ���б������ڰ���ǰ������Ƿ���ڡ�
{% include ['page_detailed.html', 'page.html'] %}
{% include ['special_sidebar.html', 'sidebar.html'] ignore missing %}


# ����
{% macro input(name, value='', type='text') -%}
    <input type="{{ type }}" value="{{ value|e }}" name="{{ name }}">
{%- endmacro %}

{%- macro textarea(name, value='', rows=10, cols=40) -%}
    <textarea name="{{ name }}" rows="{{ rows }}" cols="{{ cols
        }}">{{ value|e }}</textarea>
{%- endmacro %}
------------------������ķ�ʽ�ǰ�����ģ�鵼��Ϊһ����������������Է�������:
{% import 'forms.html' as forms %}
<dl>
    <dt>Username</dt>
    <dd>{{ forms.input('username') }}</dd>
    <dt>Password</dt>
    <dd>{{ forms.input('password', type='password') }}</dd>
</dl>
<p>{{ forms.textarea('comment') }}</p>
------------------������Ҳ���Դ�ģ���е������Ƶ���ǰ�������ռ�:
{% from 'forms.html' import input as input_field, textarea %}
<dl>
    <dt>Username</dt>
    <dd>{{ input_field('username') }}</dd>
    <dt>Password</dt>
    <dd>{{ input_field('password', type='password') }}</dd>
</dl>
<p>{{ textarea('comment') }}</p>


# ������������Ϊ  render_box.html ���� ���� box 
{% for box in boxes %}
    {% include "render_box.html" %}
{% endfor %}

# �б����ڴ洢�͵������л������ݡ����� ��������׵��� for ѭ�������б��Ԫ�鴴��һ�����ӵ��б�:
<ul>
{% for href, caption in [('index.html', 'Index'), ('about.html', 'About'),
                         ('downloads.html', 'Downloads')] %}
    <li><a href="{{ href }}">{{ caption }}</a></li>
{% endfor %}
</ul>



