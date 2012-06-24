# -*- coding: utf-8 -*-
from django.db import models
#from mysite.autoslug import AutoSlugField
#from pytils.translit import slugify

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name=u'Название категории')
    description = models.TextField(verbose_name=u'Описание')
    #slug = AutoSlugField(populate_from='title')

    slug = models.CharField(max_length=50, verbose_name=u'seo')

    def save(self, force_insert=False, force_update=False, using=None):
        trans = Trans()
        self.slug = trans.trans(self.name)
        super(Category, self).save()

    def __unicode__(self):
        return '%s ' % (self.name)


class SubCategory(models.Model):
    name = models.CharField(max_length=200, verbose_name=u'Название под категории')
    description = models.TextField(verbose_name=u'Описание')
    sel_cat = models.ForeignKey(Category, verbose_name=u'Выбрать категорию')
    #slug = AutoSlugField(populate_from='title')
    slug = models.CharField(max_length=50, verbose_name=u'seo')

    def save(self, force_insert=False, force_update=False, using=None):
        trans = Trans()
        self.slug = trans.trans(self.name)
        super(SubCategory, self).save()


    def __unicode__(self):
        return '%s ' % (self.name)


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name=u'Название продукта')
    description = models.TextField(verbose_name=u'Описание')
    sel_subcat = models.ForeignKey(SubCategory, verbose_name=u'Выбрать под категорию')
    #slug = AutoSlugField(populate_from='title')
    slug = models.CharField(max_length=50, verbose_name=u'seo')

    def save(self, force_insert=False, force_update=False, using=None):
        trans = Trans()
        self.slug = trans.trans(self.name)
        super(Product, self).save()

    def __unicode__(self):
        return '%s ' % (self.name)


class Trans(models.Model):
    def trans(self, s):

        TRANS = {
            u'а':'a',
            u'б' : 'b',
            u'в' : 'v',
            u'г' : 'g',
            u'д' : 'd',
            u'е' : 'e',
            u'ё' : 'yo',
            u'ж' : 'zh',
            u'з' : 'z',
            u'и' : 'i',
            u'й' : 'j',
            u'к' : 'k',
            u'л' : 'l',
            u'м' : 'm',
            u'н' : 'n',
            u'о' : 'o',
            u'п' : 'p',
            u'р' : 'r',
            u'с' : 's',
            u'т' : 't',
            u'у' : 'u',
            u'ф' : 'f',
            u'х' : 'kh',
            u'ц' : 'ts',
            u'ч' : 'ch',
            u'ш' : 'sh',
            u'щ' : 'shh',
            u'ъ' : '',
            u'ы' : 'y',
            u'ь' : '',
            u'э' : 'e',
            u'ю' : 'yu',
            u'я' : 'ya',
            u'№' : '#',
            u' ' : '-'
        }
        s = s.lower()
        r = u''
        for i in s:
            if i in TRANS:
                r += TRANS[i]
            else:
                r += i
        return r


    class Meta:
        abstract = True