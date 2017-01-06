from django.contrib.auth.backends import ModelBackend


class SiteBackend(ModelBackend):
    def authenticate(self, **credentials):
        # THIS RETURN THE AUTHENTICATED USER OR NONE IF NOT ALLOWED
        user_or_none = super(SiteBackend, self).authenticate(**credentials)

        # THEN WE CHECK IF USER IS ALLOWED TO ACCESS THE CURRENT SITE
        # if user_or_none and user_or_none.get_profile().sites.filter(id=Site.objects.get_current().id).count() < 1:
        # if user_or_none# and user_or_none.auth_user_profile.projects.filter(id_project=int(id_project)).count() < 1:
        #    user_or_none = None

        return user_or_none
