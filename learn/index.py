import algoliasearch_django as algoliasearch
from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register

from learn.models import Learn
#from algoliasearch_django import raw_search

#params = { "hitsPerPage": 5 }
#response = raw_search(Learn, "jim", params)
#@register(Learn)
class LearnIndex(AlgoliaIndex):
    fields = ('name', 'description')
    # geo_field = 'location'
    settings = {'searchableAttributes': ['name']}
    index_name = 'Learn'

	
algoliasearch.register(Learn,LearnIndex)