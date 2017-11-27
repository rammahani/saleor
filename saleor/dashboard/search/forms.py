from ...search.forms import SearchForm
from ...search.backends import picker


class DashboardSearchForm(SearchForm):
    def search(self):
        query = self.cleaned_data['q']
        search = picker.pick_dashboard_backend()
        return search(query)
