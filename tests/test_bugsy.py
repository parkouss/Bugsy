import bugzilla
from bugzilla import Bugsy, BugsyException, LoginException
try:
    from unittest.mock import MagicMock, patch
except:
    from mock import MagicMock, patch
import requests

example_return = {u'faults': [], u'bugs': [{u'cf_tracking_firefox29': u'---', u'classification': u'Other', u'creator': u'jgriffin@mozilla.com', u'cf_status_firefox30':
u'---', u'depends_on': [], u'cf_status_firefox32': u'---', u'creation_time': u'2014-05-28T23:57:58Z', u'product': u'Release Engineering', u'cf_user_story': u'', u'dupe_of': None, u'cf_tracking_firefox_relnote': u'---', u'keywords': [], u'cf_tracking_b2g18': u'---', u'summary': u'Schedule Mn tests on o\
pt Linux builds on cedar', u'id': 1017315, u'assigned_to_detail': {u'id': 347295, u'email': u'jgriffin@mozilla.com', u'name': u'jgriffin@mozilla.com',
u'real_name': u'Jonathan Griffin (:jgriffin)'}, u'severity': u'normal', u'is_confirmed': True, u'is_creator_accessible': True, u'cf_status_b2g_1_1_hd':
 u'---', u'qa_contact_detail': {u'id': 20203, u'email': u'catlee@mozilla.com', u'name': u'catlee@mozilla.com', u'real_name': u'Chris AtLee [:catlee]'},
 u'priority': u'--', u'platform': u'All', u'cf_crash_signature': u'', u'version': u'unspecified', u'cf_qa_whiteboard': u'', u'cf_status_b2g_1_3t': u'--\
-', u'cf_status_firefox31': u'---', u'is_open': False, u'cf_blocking_fx': u'---', u'status': u'RESOLVED', u'cf_tracking_relnote_b2g': u'---', u'cf_stat\
us_firefox29': u'---', u'blocks': [], u'qa_contact': u'catlee@mozilla.com', u'see_also': [], u'component': u'General Automation', u'cf_tracking_firefox\
32': u'---', u'cf_tracking_firefox31': u'---', u'cf_tracking_firefox30': u'---', u'op_sys': u'All', u'groups': [], u'cf_blocking_b2g': u'---', u'target\
_milestone': u'---', u'is_cc_accessible': True, u'cf_tracking_firefox_esr24': u'---', u'cf_status_b2g_1_2': u'---', u'cf_status_b2g_1_3': u'---', u'cf_\
status_b2g18': u'---', u'cf_status_b2g_1_4': u'---', u'url': u'', u'creator_detail': {u'id': 347295, u'email': u'jgriffin@mozilla.com', u'name': u'jgri\
ffin@mozilla.com', u'real_name': u'Jonathan Griffin (:jgriffin)'}, u'whiteboard': u'', u'cf_status_b2g_2_0': u'---', u'cc_detail': [{u'id': 30066, u'em\
ail': u'coop@mozilla.com', u'name': u'coop@mozilla.com', u'real_name': u'Chris Cooper [:coop]'}, {u'id': 397261, u'email': u'dburns@mozilla.com', u'nam\
e': u'dburns@mozilla.com', u'real_name': u'David Burns :automatedtester'}, {u'id': 438921, u'email': u'jlund@mozilla.com', u'name': u'jlund@mozilla.com ', u'real_name': u'Jordan Lund (:jlund)'}, {u'id': 418814, u'email': u'mdas@mozilla.com', u'name': u'mdas@mozilla.com', u'real_name': u'Malini Das [:md\
as]'}], u'alias': None, u'cf_tracking_b2g_v1_2': u'---', u'cf_tracking_b2g_v1_3': u'---', u'flags': [], u'assigned_to': u'jgriffin@mozilla.com', u'cf_s\
tatus_firefox_esr24': u'---', u'resolution': u'FIXED', u'last_change_time': u'2014-05-30T21:20:17Z', u'cc': [u'coop@mozilla.com', u'dburns@mozilla.com'
, u'jlund@mozilla.com', u'mdas@mozilla.com'], u'cf_blocking_fennec': u'---'}]}

def test_we_cant_post_without_a_username_or_password():
    bugzilla = Bugsy()
    try:
        bugzilla.put("foo")
        assert 1 == 0, "Should have thrown when calling put"
    except BugsyException as e:
        assert str(e) == "Message: Unfortunately you can't put bugs in Bugzilla without credentials"

def test_we_get_a_login_exception_when_details_are_wrong():
    try:
        Bugsy("foo", "bar")
        assert 1 == 0, "Should have thrown an error"
    except LoginException as e:
        assert str(e) == "Message: The username or password you entered is not valid."

def _test_we_cant_post_without_passing_a_bug_object():
    bugzilla = Bugsy("foo", "bar")
    try:
        bugzilla.put("foo")
        assert 1 == 0, "Should have thrown an error about type when calling put"
    except BugsyException as e:
        assert str(e) == "Message: Please pass in a Bug object when posting to Bugzilla"

def test_we_can_get_a_bug():
    bugzilla = Bugsy()
    bug = bugzilla.get(1017315)
    assert bug.id == 1017315
    assert bug.status == 'RESOLVED'
    assert bug.summary == 'Schedule Mn tests on opt Linux builds on cedar'

