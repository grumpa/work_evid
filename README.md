Work Evidence
=========

Attention :-) : My learning application in Django.

Keep a record of work you do for your customers. You can filter records by months/years and see
summary of money by customer. Good as source for your invoices.

Application contains simple TODO.

You can:
* maintain list of customers
* maintain evidence of work done for customers
* display records with some filtering (year/month/customer) and two styles: timeline and by the customers.

Application use I18n and is translatable. Views and templates use i18n posibilities of Django.

Requirements
------------
* Python, tested on 3.4. Support for Python-2 has stopped.
* Django, tested on 1.7 and 1.8 (1.9 testing in progres and seems OK)
* [django-markdown-deux](https://github.com/trentm/django-markdown-deux)

Current status
--------------

Application is in usable state. It would be probably difficult to incorporate it
in your project due to templates and authentification which are somehow egocentric.
Use it as standalone project/app.


Expected audience
-----------------

If you are more experienced then me, or you are enthuisiastic student of Django and you want to collaborate, welcome to my club. I want to learn how to paricipate in collaborative work too. :-)


Changelog
========
2016-01-05
- Model Firm has new field "show_in_list" with default=True. If you have a firm you don't work for
  it anymore, change value to False and this firm will not be offered in pulldown menu in forms for Work an Todo.
- Rewritten for Python-3.4
