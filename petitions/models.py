from django.db import models
from openelections.constants import ENROLLMENT_STATUSES
from openelections.issues.models import Issue

class Signature(models.Model):
    name = models.CharField(max_length=100)
    sunetid = models.CharField(max_length=8)
    studentid = models.CharField(max_length=8)
    enrollment_status = models.CharField(max_length=1, choices=ENROLLMENT_STATUSES)    
    issue = models.ForeignKey(Issue, related_name='signatures')
    signed_at = models.DateTimeField()
    ip_address = models.CharField(max_length=15)
    
    def __unicode__(self):
        return u'%s for %s' % (self.sunetid, self.issue.display_title())

# TODOsqs: test signed_by_sunetid
def signed_by_sunetid(issue, sunetid):
    return Signature.objects.filter(sunetid=sunetid, issue=issue)
Issue.signed_by_sunetid = signed_by_sunetid