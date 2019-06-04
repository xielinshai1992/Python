from django.shortcuts import render,get_object_or_404,redirect
from .import models
import markdown
import pygments
from django.db.models import Q
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django_comments.models import Comment
from django_comments import models as comment_models
from .import forms
from django.contrib.auth import authenticate,login,logout


def make_paginator(objects, page, num = 5):
    '''
    生成分页器函数
    :param objects:
    :param page:
    :param num:
    :return:
    '''
    paginator = Paginator(objects ,num)
    try:
        object_list = paginator.page(page)
    except PageNotAnInteger:
        object_list = paginator.page(1)
    except EmptyPage:
        object_list = paginator.page(paginator.num_pages)
    return object_list,paginator


def pagination_data(paginator ,page):
    '''
    用于自定义展示分页页码的方法
    :param paginator: Paginator类的对象
    :param page: 当前请求的页码
    :return: 一个包含所有页码和符号的字典
    '''
    if paginator.num_pages == 1:
        return {}
    left = []
    right = []
    left_has_more = False
    right_has_more = False
    first = False
    last = False
    #获得用户当前请求的页码号
    try:
        page_number = int(page)
    except ValueError:
        page_number = 1
    except:
        page_number = 1

    total_pages = paginator.num_pages
    page_range = paginator.page_range

    if page_number ==1:
        right =page_range[page_number:page_number+4]

        if right[-1]< total_pages-1:
            right_has_more=True
        if right[-1]<total_pages:
            last =True
    elif page_number == total_pages:
        left = page_range[(page_number-3) if(page_number-3)>0 else 0:page_number-1]
        if left[0]>2:
            left_has_more=True
        if left[0]>1:
            first = True
    else:
        left = page_range[(page_number-3)if (page_number - 3)>0 else 0:page_number-1]
        right = page_range[page_number:page_number+2]

        if right[-1]<total_pages-1:
            right_has_more=True
        if right[-1]<total_pages:
            last = True
        if left[0]>2:
            left_has_more =True
        if left[0]>1:
            first = True
    data = {
        'left':left,
        'right':right,
        'left_has_more':left_has_more,
        'right_has_more':right_has_more,
        'first':first,
        'last':last,
    }
    return data

def index(request):
    entries = models.Entry.objects.all()
    page = request.GET.get('page',1)
    entry_list,paginator = make_paginator(entries, page)
    page_data = pagination_data(paginator, page)

    return render(request, 'blog/index.html',locals())

def detail(request,blog_id):
    #entry = models.Entry.objects.get(id = blog_id )
    entry = get_object_or_404(models.Entry, id=blog_id)
    md = markdown.Markdown(extensions=['markdown.extensions.extra',
                                       'markdown.extensions.codehilite',
                                       'markdown.extensions.toc'
                                       ])
    entry.body = md.convert(entry.body)
    entry.toc = md.toc #目录信息
    entry.increase_visiting()

    comment_list = list()

    def get_comment_list(comments):
        for comment in comments:
            comment_list.append(comment)
            children = comment.child_comment.all()
            if len(children)>0:
                get_comment_list(children)

    top_comments = Comment.objects.filter(object_pk= blog_id , parent_comment=None ,content_type__app_label='blog').order_by('-submit_date')
    get_comment_list(top_comments)
    return render(request, 'blog/detail.html',locals())

def category(request, category_id):
    #c = models.Category.objects.get( id=category_id )
    c = get_object_or_404(models.Category, id = category_id)
    entries = models.Entry.objects.filter(category = c)
    page = request.GET.get('page',1)
    entry_list, paginator = make_paginator(entries,page)
    page_data = pagination_data(paginator,page)
    return render(request,'blog/index.html',locals())

def tag(request,tag_id):
    # t = models.Tag.objects.get(id=tag_id)
    t = get_object_or_404(models.Tag, id=tag_id)
    if t.name =="全部":
        entries = models.Entry.objects.all()
    else:
        entries = models.Entry.objects.filter(tags=t)
    page = request.GET.get('page', 1)
    entry_list, paginator = make_paginator(entries, page)
    page_data = pagination_data(paginator, page)
    return render(request, 'blog/index.html', locals())

def search(request):
    '''
    关键词搜索
    :param request:
    :return:
    '''

    keyword = request.GET.get('keyword',None)
    if not keyword:
        error_msg = "请输入关键字"
        return render(request,'/blog/index.html',locals())

    entries = models.Entry.objects.filter(Q(title__icontains=keyword)
                                         |Q(body__icontains=keyword)
                                         |Q(abstract__icontains=keyword))
    page = request.GET.get('page', 1)
    entry_list, paginator = make_paginator(entries, page)
    page_data = pagination_data(paginator, page)
    return render(request, 'blog/index.html', locals())

def archives(request, year, month):
    entries = models.Entry.objects.filter(created_time__year=year,created_time__month=month)
    page = request.GET.get('page', 1)
    entry_list, paginator = make_paginator(entries, page)
    page_data = pagination_data(paginator, page)
    return render(request, 'blog/index.html', locals())

def permission_denied(request):
    return render(request , 'blog/403.html',locals())

def page_not_found(request):
    return render(request, 'blog/404.html', locals())

def page_error(request):
    return render(request, 'blog/500.html', locals())

def reply(request,comment_id):
    if not request.session.get('login',None) and not request.user.is_authenticated():
        return redirect('/')
    parent_comment = get_object_or_404(comment_models.Comment, id = comment_id)
    return  render(request ,'blog/reply.html',locals())

def blog_login(request):
    #避免重复登录
    if request.session.get('is_login',None):
        return redirect("blog:blog_index")

    if request.method == "GET":
        #记录登录请求来源的url,如果没有设置为首页
        request.session['login_from'] = request.META.get('HTTP_REFERER','/')
        login_form = forms.UserForm()
        return render(request, 'blog/login.html',locals())

    if request.method == "POST":
        login_form = forms.UserForm(request.POST)
        message = '请检查填写的内容！'
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            auth_user = authenticate(username= username,password=password)
            if auth_user is not None:
                # 首先验证django认证系统的用户
                login(request, auth_user)
                request.session['is_login'] = True
                request.session['user_name'] = username
                return redirect(request.session['login_from']) #登录成功 重定向到登录请求url
            #其次验证models.User模型数据
            try:
                user = models.User.objects.get(name=username)
                if user.password == password:
                    request.session['is_login'] = True
                    request.session['user_name'] = user.name
                    return redirect(request.session['login_from'])  # 登录成功 重定向到登录请求url
                else:
                    message = "密码不正确！"
            except:
                    message = "认证用户密码错误或用户不存在！"
            return render(request,'blog/login.html',locals())

    login_form = forms.UserForm
    return render(request, 'blog/login.html',locals())

def blog_logout(request):
    if request.user.is_authenticated:
        logout(request)
    else:
        request.session.flush()
    return redirect("blog:blog_index")

def register(request):
    if request.session.get('is_login',None):
        #登录状态无法注册
        return redirect("blog:blog_index")

    if request.method =="POST":
        register_form = forms.RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            sex = register_form.cleaned_data['sex']
            if password1 != password2:
                message = "两次输入的密码不同！"
                return render(request, 'blog/register.html',locals())
            else:
                same_name_user = models.User.objects.filter(name= username)
                if same_name_user: #用户名唯一
                    message = '用户名已经存在，请重新选择用户名！'
                    return render(request, 'blog/register.html',locals())
                same_email_user = models.User.objects.filter(email=email)
                if same_email_user:  # 邮箱地址唯一
                    message = '该邮箱地址已被注册，请使用别的邮箱！'
                    return render(request, 'blog/register.html', locals())

                # 当一切都OK的情况下，创建新用户
                new_user = models.User()
                new_user.name = username
                new_user.password = password1
                new_user.email = email
                new_user.sex = sex
                new_user.save()
                return redirect('/login/')  # 注册成功！自动跳转到登录页面

    register_form =forms.RegisterForm()
    return render(request, 'blog/register.html',locals())

# def login(request):
#     import requests
#     import json
#     from django.conf import settings
#     code = request.GET.get('code', None)
#     if code is None:
#         return redirect('/')
#
#     access_token_url = 'https://api.weibo.com/oauth2/authorize?client_id=%s&client_secret=%s&grant_type=authorization_code&redirect_uri=http://www.yoursite.com/login&code=%s'\
#                         %(settings.CLIENT_ID, settings.APP_SECRET, code)
#
#     ret = requests.post(access_token_url)
#     data = ret.text
#     data_dict = json.loads(data)
#     token = data_dict['access_token']
#     uid = data_dict['uid']
#
#     request.session['token'] = token
#     request.session['uid'] = uid
#     request.session['login'] = True
#
#     user_info_url = 'https://api.weibo.com/2/users/show.json?access_token=%s&uid=%s'%(token ,uid)
#     user_info = requests.get(user_info_url)
#     user_info_dict = json.loads(user_info.text)
#
#     request.session['screen_name'] = user_info_dict['screen_name']
#     request.session['profile_image_url'] = user_info_dict['profile_image_url']
#
#     return redirect(request.GET.get('next', '/'))
#
# def logout(request):
#     if request.session['login']:
#         del request.session['login']
#         del request.session['uid']
#         del request.session['token']
#         del request.session['screen_name']
#         del request.session['profile_image_url']
#         return redirect(request.GET.get('next','/'))
#     else:
#         return redirect('/')

