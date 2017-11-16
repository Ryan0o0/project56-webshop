from django.core.mail import send_mail
from django.template.loader import render_to_string


msg_plain = render_to_string('templates/frames/Email2.txt', {'some_params': some_params})
msg_html = render_to_string('templates/frames/Email2.html', {'some_params': some_params})

send_mail(
    'Contact message',
    msg_plain,
    'noreply@comicfire.com',
    ['admin@comicfire.com'],
    headers = {'Reply-to': contact_email}
)