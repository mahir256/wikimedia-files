# This script expects two files, a file 'items.txt' which has a list of items whose
# aliases are to be removed, and another file 'aliases.txt' which contains a tab-separated
# list of aliases corresponding to each item in the previous file.
import copy
import pwb
import pywikibot
# Set site and open files.
site = pywikibot.Site('wikidata', 'wikidata')
items = open('items.txt').read().splitlines()
aliases = open('aliases.txt').read().splitlines()
# Flag to indicate that aliases have already been removed from the item.
already_done = 0
for i in range(5,len(items)):
    # Retrieve item and aliases to be removed.
    item = pywikibot.ItemPage(site, items[i])
    item.get()
    cur_alias = copy.deepcopy(item.aliases)
    todealias = aliases[i].split('\t')
    # Try to remove each alias, keeping on going if not present and breaking if
    # there are no aliases to begin with.
    for j in todealias:
        try:
            cur_alias['bn'].remove(j)
        except ValueError:
            continue
        except KeyError:
            already_done = 1
            break
    # Keep going if there are no aliases at all.
    if(already_done):
        already_done = 0
        #print("Already done")
        continue
    # Keep going if there are aliases, but they've been removed already.
    if(cur_alias['bn'] == item.aliases['bn']):
        #print(cur_alias['bn'])
        #print(item.aliases['bn'])
        #print("All removed already")
        continue
    # The fix Matej Suchanek suggested if all the aliases had to be removed.
    if(cur_alias.get('bn', []) == []):
        removed = {}
        removed['aliases'] = {}
        removed['aliases']['bn'] = list(map(lambda al: {'language': 'bn', 'value': al, 'remove': ''}, item.aliases['bn']))
        #print("The fix in action")
        item.editEntity(removed, summary=u'removed non-Bengali aliases')
    else:
        #print("Not the fix in action")
        item.editAliases(cur_alias, summary=u'removed non-Bengali aliases')