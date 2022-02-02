import django_filters

from documents.models import Document

class DocumentFilter(django_filters.FilterSet):
	class Meta:
		model = Document