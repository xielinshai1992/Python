import django
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'website.settings'
django.setup()

if __name__ == '__main__':
    from django.core.mail import send_mail

    send_mail(
        '来自xls的测试邮件',
        'Here is the message.',
        'xielinshai1992@sina.cn',
        ['195929666@qq.com'],
    )