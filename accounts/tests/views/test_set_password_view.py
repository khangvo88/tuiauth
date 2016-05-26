from django.core.urlresolvers import reverse

from common.tests.core import SimpleTestCase


class SetPasswordTestCase(SimpleTestCase):
    allow_database_queries = True

    def test_visit_password_change_view(self):
        self.login_user()
        self.visit(reverse('accounts:set_user_password'))

        self.response.status_code.should.equal(302)
        self.response['location'].should.contain(reverse('password_change'))
