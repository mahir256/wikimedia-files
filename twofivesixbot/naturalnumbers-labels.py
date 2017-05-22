#!/usr/bin/python
# -*- coding: utf-8 -*-
import string
import pwb
import pywikibot

# Before running this script, make sure "naturalnumbers.txt" is
# in the same directory as this script.

trans_deva = dict(zip(map(ord, u"0123456789"), map(ord, u"०१२३४५६७८९")))
trans_deva.update((ord(c),None) for c in "")
trans_ben = dict(zip(map(ord, u"0123456789"), map(ord, u"০১২৩৪৫৬৭৮৯")))
trans_ben.update((ord(c),None) for c in "")
trans_shn = dict(zip(map(ord, u"0123456789"), map(ord, u"႐႑႒႓႔႕႖႗႘႙")))
trans_shn.update((ord(c),None) for c in "")
trans_tib = dict(zip(map(ord, u"0123456789"), map(ord, u"༠༡༢༣༤༥༦༧༨༩")))
trans_tib.update((ord(c),None) for c in "")
trans_kn = dict(zip(map(ord, u"0123456789"), map(ord, u"೦೧೨೩೪೫೬೭೮೯")))
trans_kn.update((ord(c),None) for c in "")

site = pywikibot.Site('wikidata', 'wikidata')
items = open('naturalnumbers.txt').read().splitlines()

for curnum in range(1,10001):
	item = pywikibot.ItemPage(site, items[curnum-1])
	item.get()
	unum = unicode(curnum)
	curdeva = unum.translate(trans_deva)
	curben = unum.translate(trans_ben)
	curshn = unum.translate(trans_shn)
	curtib = unum.translate(trans_tib)
	curkn = unum.translate(trans_kn)
	data = {'labels':
	{
	'anp': curdeva,
	'awa': curdeva,
	'ks-deva': curdeva,
	'gom-deva': curdeva,
	'dty': curdeva,
	'new': curdeva,
	'ne': curdeva,
	'pi': curdeva,
	'bho': curdeva,
	'mr': curdeva,
	'rwr': curdeva,
	'mai': curdeva,
	'sa': curdeva,
	'as': curben,
	'bpy': curben,
	'shn': curshn,
	'dz': curtib,
	'tcy': curkn}}
	item.editEntity(data, summary=u'added labels in different Asian languages')